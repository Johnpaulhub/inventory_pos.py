from flask import Flask, request, redirect, url_for

app = Flask(__name__)

INVENTORY = [
    {"id": 1, "item": "A4 Paper Ream", "stock": 10, "price": 650.0},
    {"id": 2, "item": "Black Ink Bottle", "stock": 4, "price": 1200.0}
]

@app.route('/')
def pos_home():
    item_html = ""
    for i in INVENTORY:
        item_html += f'''
        <div style="background: #1b2230; border-radius: 8px; padding: 12px; margin-bottom: 10px; border: 1px solid #2a3447; display: flex; justify-content: space-between; align-items: center;">
            <div>
                <div style="font-size: 14px; font-weight: bold; color: #fff;">{i['item']}</div>
                <div style="font-size: 11px; color: #94a3b8; margin-top: 2px;">Stock Left: <span style="color: #38bdf8; font-weight: bold;">{i['stock']}</span></div>
            </div>
            <div style="font-size: 14px; font-weight: bold; color: #10b981;">KES {i['price']:.2f}</div>
        </div>
        '''

    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cyber POS & Inventory</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ font-family: sans-serif; background: #121824; color: #fff; margin: 0; padding: 12px; }}
            h2 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 6px; }}
            .card {{ background: #1b2230; padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #2a3447; }}
            input {{ width: 100%; padding: 10px; margin: 6px 0 12px 0; background: #121824; border: 1px solid #334155; color: #fff; border-radius: 6px; box-sizing: border-box; }}
            button {{ width: 100%; padding: 12px; background: #0284c7; color: white; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; }}
        </style>
    </head>
    <body>
        <h2>Cyber POS & Inventory</h2>
        <div class="card">
            <h3 style="margin-top:0; color:#38bdf8; font-size:15px;">Add New Stock Item</h3>
            <form action="/add_item" method="POST">
                <input type="text" name="item" placeholder="Item Name" required>
                <input type="number" name="stock" placeholder="Initial Stock Quantity" required>
                <input type="number" step="0.01" name="price" placeholder="Unit Price (KES)" required>
                <button type="submit">+ Save Item</button>
            </form>
        </div>
        <h3 style="color: #38bdf8; margin-top: 20px;">Current Inventory</h3>
        {item_html}
    </body>
    </html>
    '''

@app.route('/add_item', methods=['POST'])
def add_item():
    item = request.form.get('item')
    stock = int(request.form.get('stock', 0))
    price = float(request.form.get('price', 0))
    if item:
        INVENTORY.append({"id": len(INVENTORY) + 1, "item": item, "stock": stock, "price": price})
    return redirect(url_for('pos_home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)
