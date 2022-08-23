
from flask import request,Flask
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
app=Flask(__name__)
api=Api(app)
app.secret_key='nawaz'
jwt=JWT(app,authenticate,identity)
items=[]
class Items(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',type=float,
                             required=True,
                             help="This field cant be empty")
    
    @jwt_required()
    def get(self,name):
        item=next(filter(lambda x:x['name']==name,items),None)
        return {'item':item}
    def post(self,name):
        if next(filter(lambda x:x['name']==name,items),None) is not None:
            return{'message':"the name'{}' already exits".format(name)}
        data=Items.parser.parse_args()
        # data=request.get_json()
        item={'name':name,'price':data['price']}
        items.append(item)
        return item
    def delete(self,name):
        global items
        items=list(filter(lambda x:x['name']!=name,items))
        return {'message':'got deleted'}
    def put(self,name):
        # we can use below method but in post methoad also weneed to write this so we are writting things in class only        
        # parser=reqparse.RequestParser()
        # parser.add_argument('price',type=float,
        #                     required=True,
        #                     help="This field cant be empty")
        data=Items.parser.parse_args()
        # below will help us to take input as price
        # data=request.get_json()
        item=next(filter(lambda x:x['name']==name,items),None)
        if item is None:
            item={'name':name,'price':data['price']}
            items.append(item)
        else:
            item.update(data)
            return item
class Items_list(Resource):
    def get(self):
        return {'items':items}
api.add_resource(Items,'/item/<string:name>')
api.add_resource(Items_list,'/items')
if __name__=='__main__':
    app.run(debug=True)