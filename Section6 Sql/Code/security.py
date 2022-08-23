
from hmac import compare_digest
from user import User
# Below lines are not necessary because we already given in test.py file 
# users = [
#     User(1, 'user1', 'abcxyz'),
#     User(2, 'user2', 'abcxyz'),
# ]

# username_table = {u.username: u for u in users}
# userid_table = {u.id: u for u in users}

def authenticate(username, password):
    # we have written a peice of code in user to extract the user by username or id now we will use that so we re commenting the below line
    # user = username_table.get(username, None)
    user=User.find_by_username(username)
    if user and compare_digest(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    # we have written ciode in user.py file
    # return userid_table.get(user_id, None)
    return User.find_by_id(user_id)
