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

def test_get_category(client):
    """
    Test get a single category by its ID
    """

    # Suppose we have an existing category in the database with ID 1
    existing_category_id = 1

    # We make a GET request to get the category by its ID
    response = client.get(f'/categories/{existing_category_id}')

    # We verify that the request has been successful (status code 200)
    assert response.status_code == 200

    assert response.headers['content-type'] == 'application/json'

    category = response.json()

    assert category['id'] == existing_category_id
    assert category['name'] == post_data['name']


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

def test_create_category_missing_name(client):
    """
    Test if an error is raised when the name is not provided while creating a category
    """

    post_data = {"image": "https://i.imgur.com/QkIa5tT.jpeg"}

    headers = {'Content-Type': 'application/json'}

    response = client.post(
        '/categories',
        json=post_data,
        headers=headers
    )

    # Verifies that the request has failed (status code 422 - Unprocessable Entity)
    assert response.status_code == 422

    print(response.json()['detail'][0]['msg'])

    # Verify that the expected error message is present in the response
    assert response.json()['detail'][0]['msg'] == 'Field required'

def test_create_category_non_unique_name(client):
    """
    Test if an error is raised when creating a category with a non-unique name
    """
    headers = {'Content-Type': 'applications/json'}

    response = client.post(
        '/categories',
        json=post_data,
        headers=headers
    )

    # Verifies that the request has failed (status code 422 - Unprocessable Entity)
    assert response.status_code == 422