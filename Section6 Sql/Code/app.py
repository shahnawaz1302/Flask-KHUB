from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from item import Item,ItemList
from security import authenticate, identity
from user import UserRegister
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
api = Api(app)
app.secret_key = 'jose'
jwt = JWT(app, authenticate, identity)





api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True