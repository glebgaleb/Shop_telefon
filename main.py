from flask import *
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    connection = sqlite3.connect("database.slite")
    cursor = connection.cursor()
    products = cursor.execute("SELECT * FROM phones").fetchall()
    connection.close()
    return render_template('products.html', products=products)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/products')
def products():
    return render_template('products.html')

app.run(debug=True)