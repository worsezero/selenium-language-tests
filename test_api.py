import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post_status_code():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_get_post_has_correct_id():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert data["id"] == 1

def test_get_post_title_is_string():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert isinstance(data["title"], str)


def test_create_post():
    new_post = {
        "title": "My test post",
        "body": "This is a test",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    data = response.json()

    assert response.status_code == 201
    assert data["title"] == "My test post"
    assert data["id"] == 101


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")


    assert response.status_code == 200
    assert response.json() == {}



def test_get_comments_by_post():
    response = requests.get(f"{BASE_URL}/comments?postId=1")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)


def test_update_post():
    update_post = {
        "id": 1,
        "title": "My test post",
        "body": "Updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=update_post)
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "My test post"



