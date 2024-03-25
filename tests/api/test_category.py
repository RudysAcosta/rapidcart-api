from tests.test_main import client

post_data = {
    "name": "Clothes",
    "image": "https://i.imgur.com/QkIa5tT.jpeg"
}

def test_create_category(client):
    """
    Test create of category
    """

    headers = {'Content-Type': 'application/json'}

    response = client.post(
        '/categories',
        json=post_data,
        headers=headers
    )
    assert response.status_code == 201