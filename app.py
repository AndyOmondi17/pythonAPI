from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os 
 
 #Initialize app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#create database
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initialize dbs
db = SQLAlchemy(app)

#Initialize Marshmallow
ma = Marshmallow(app)



#Product class/model
class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    description = db.Column(db.String(200)) 
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
   

    def __init__(self,name,description,price,quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        
        
#basically everything that will be dispalyed
#class product schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','name','description','price','quantity')

#Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

#Create
#Read
#Update
#Delete

                #Create A Product
#create a product(post)
@app.route('/product',methods=['POST'])
def add_product():
    
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']
    

    new_product = Product(name,description,price,quantity)
    db.session.add(new_product)
    
    return product_schema.jsonify(new_product)


                #READ A PRODUCT(S)
#Getting All Products
@app.route('/product',methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

#Getting a single product
@app.route('/product/<int:id>',methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)


                #UPDATING A PRODUCT
#Put method to update product
@app.route('/product/<int:id>',methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    product = Product.query.get(id)
    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity

    return product_schema.jsonify(product)

            #DELETING A PRODUCT
#USES THE DELETE METHOD
@app.route('/product/<int:id>',methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    return product_schema.jsonify(product)

#Run server
if __name__ == "__main__":
    app.run(debug = True)
