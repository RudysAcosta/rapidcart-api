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

def test_get_categories(client):
    """
    Test get all categories
    """

    response = client.get('/categories')

    # Verify that the request was successful
    assert response.status_code == 200

    # Verify that the content of the response is valid JSON
    assert response.headers['content-type'] == 'application/json'

    # Verify that the response contains category data
    categories = response.json()
    assert isinstance(categories, list)
    assert len(categories) > 0

