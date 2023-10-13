from app import app
from app import insert_user, get_users,get_user_by_id,update_user,delete_user
from flask import json,jsonify


def test_get():
    response = app.test_client().get('/api/users')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert "Jadoueida" in str(response.data)

def test_add():
    response = app.test_client().post(
        'api/users/add',
        data=json.dumps({'name': "Jadoueida", 'email': "jadoueida",'phone':"7868",'address':"aub", 'country': "lebanose"}), content_type='application/json',
        )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    print(response.data)
    
def test_get_one():
    response = app.test_client().get('/api/users/6')
    data = json.loads(response.get_data(as_text=True))
    assert "Jadoueida" in str(response.data)    


def test_delete_one():
    response = app.test_client().delete('/api/users/delete/10')
    data = json.loads(response.get_data(as_text=True))
    assert data["status"] == "User deleted successfully"     


def test_update():
    response = app.test_client().put(
        'api/users/update',
        data=json.dumps({'user_id': 7,'name': "Mohammad", 'email': "jadoueida",'phone':"7868",'address':"aub", 'country': "lebanose"}), content_type='application/json',
        )
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    print(response.data)   

def test_insert_user():
    user =  {'name': "Jairm", 'email': "jadoueida",'phone':"7868",'address':"aub", 'country': "lebanose"}    
    response = insert_user(user)
    assert response['name'] == user['name']
    assert response['email'] == user['email']
    assert response['address'] == user['address']
    assert response['phone'] == user['phone']
    assert response['country'] == user['country']

def test_get_users():
    users = get_users()
    assert users[1]["name"] == "Jadoueida"
    assert users[2]["name"] == "Jadoueida"

def test_get_user_by_id():
    user_id = 6
    response = get_user_by_id(user_id)
    assert response["name"] == "Jadoueida"

def test_update_user():
    user =  {'user_id':1,'name': "Farhat", 'email': "jadoueida",'phone':"7868",'address':"aub", 'country': "lebanose"}    
    response = update_user(user)
    assert response['name'] == user['name']
    assert response['email'] == user['email']
    assert response['address'] == user['address']
    assert response['phone'] == user['phone']
    assert response['country'] == user['country']  

def test_delete_user():
    user_id = 11
    response = delete_user(user_id)
    assert response["status"]== "User deleted successfully"
