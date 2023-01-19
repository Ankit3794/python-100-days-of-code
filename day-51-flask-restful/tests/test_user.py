import json

auth_header = None


def test_create_user(client):
    response = client.post('/user', data=json.dumps({
        "username": "test",
        "password": "admin"
    }), content_type='application/json')
    assert 201 == response.status_code


def test_login(client):
    response = client.post('/login', data=json.dumps({
        "username": "test",
        "password": "admin"
    }), content_type='application/json')
    assert 200 == response.status_code
    auth = response.get_json().get("auth")
    global auth_header
    auth_header = {
        "Authorization": f"Bearer {auth}"
    }


def test_get_users(client):
    response = client.get("/user", headers=auth_header)
    assert 200 == response.status_code
    assert 'test' == response.get_json()[0]['username']


def test_update_password(client):
    response = client.put('/user', data=json.dumps({
        "username": "test",
        "password": "admin_updated"
    }), content_type='application/json')
    assert 201 == response.status_code

    response = client.post('/login', data=json.dumps({
        "username": "test",
        "password": "admin_updated"
    }), content_type='application/json')
    assert 200 == response.status_code
    auth = response.get_json().get("auth")
    global auth_header
    auth_header = {
        "Authorization": f"Bearer {auth}"
    }


def test_delete_user(client):
    response = client.delete('/user/test', headers=auth_header)
    assert 200 == response.status_code
