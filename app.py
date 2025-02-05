from flask import Flask, request

app = Flask(__name__)

products = [{
    "id": 1,
    "title": 'Product 1',
    "price": 150
},
{
    "id": 2,
    "title": 'Product 2',
    "price": 400
}]

@app.route('/')
def hello():
    return '<h1> Hello world!</h1>'

@app.route('/second')
def another_route():
    return('<h2> This is the second </h2>')

@app.route('/products')
def all_products():
    return products

# Get product with id
@app.route('/products/<int:id>')
def one_product(id):
    filtered_products = list(filter(lambda p: p['id'] == id, products))
    print(filtered_products)
    return filtered_products

@app.route('/can-vote')
def canvote():
    age = int(request.args.get('age'))
    if age >= 18:
        return {"message": "You can vote", "can_vote" : True}
    return {"message": "You cannot vote", "can_vote" : False}
