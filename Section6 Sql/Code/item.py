import sqlite3

from flask_restful import Resource,reqparse

from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    @jwt_required()
    def get(self, name):
        # return {'item': next(filter(lambda x: x['name'] == name, items), None)}
        # connection=sqlite3.connect('data.db')
        # cursor=connection.cursor()
        # query="SELECT * FROM items WHERE name=?"
        # result=cursor.execute(query,(name,))
        # row=result.fetchone()
        # connection.close()
        # if row:
        #     return {'item':{'name':row[0],'price':row[1]}}
        # return {'message':'Item not found'},400
        item=self.find_by_name(name)
        if item:
            return item
        return {'message':'Item not found'},400
    @classmethod
    def find_by_name(cls,name):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="SELECT * FROM items WHERE name=?"
        result=cursor.execute(query,(name,))
        row=result.fetchone()
        connection.close()
        if row:
            return {'item':{'name':row[0],'price':row[1]}}
        

    def post(self, name):
        # if next(filter(lambda x: x['name'] == name, items), None) is not None: done in 85th video
        if self.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)},400
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        # items.append(item) 85th video
        # we cannot append we have to enter into the dadtbase
        try:
            self.insert_item(item)
        except:
            return {"message":"An internal errror occrued"},500
        return item
    @classmethod
    def insert_item(cls,item):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="INSERT INTO items VALUES(?,?)"
        cursor.execute(query,(item['name'],item['price']))
        connection.commit()
        connection.close()
    @jwt_required()
    def delete(self, name):
        # global items
        # items = list(filter(lambda x: x['name'] != name, items)) in 86th video
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="DELETE FROM items WHERE name=?"
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        return {'message': 'Item deleted'},202

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        # global items
        # Once again, print something not in the args to verify everything works
        # item = next(filter(lambda x: x['name'] == name, items), None) in 88th video
        item=self.find_by_name(name)
        update_item = {'name': name, 'price': data['price']}
        if item is None:
            try:
                Item.insert_item(update_item)
            except:
                return {"message":"An error occured"},500
            # items.append(item) above lines are same as append
        else:
            try:
                Item.update(update_item)
            except:
                return {"message":"An error occured"},500
            # item.update(data) above lines will replace the update function
        return update_item
    @classmethod
    def update(cls,item):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="UPDATE items SET price=? WHERE name=?"
        cursor.execute(query,(item['price'], item['name']))
        connection.commit()
        connection.close()

class ItemList(Resource):
    def get(self):
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="SELECT * FROM items"
        result=cursor.execute(query)
        items=[]
        for row in result:
            items.append({'name':row[0],'price':row[1]})
        
        connection.close()
        return {'items': items}