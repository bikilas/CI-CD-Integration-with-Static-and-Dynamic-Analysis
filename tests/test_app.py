"""
Unit tests for the Flask Todo API application
"""
import pytest
from app import TodoApp


@pytest.fixture(name="app_instance")
def fixture_app_instance():
    """Create a new TodoApp instance for testing"""
    app = TodoApp()
    app.app.config['TESTING'] = True
    return app


@pytest.fixture(name="client")
def fixture_client(app_instance):
    """Create a test client"""
    with app_instance.app.test_client() as test_client:
        yield test_client


@pytest.fixture(name="reset_todos")
def fixture_reset_todos(app_instance):
    """Reset todos list before each test"""
    app_instance.todos.clear()
    app_instance.next_id = 1
    yield
    app_instance.todos.clear()
    app_instance.next_id = 1


def test_home_endpoint(client):  # pylint: disable=redefined-outer-name
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'version' in data


def test_health_check(client):  # pylint: disable=redefined-outer-name
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'


def test_get_empty_todos(client, reset_todos):  # pylint: disable=unused-argument,redefined-outer-name
    """Test getting todos when list is empty"""
    response = client.get('/todos')
    assert response.status_code == 200
    data = response.get_json()
    assert data['count'] == 0
    assert data['todos'] == []


def test_create_todo(client, reset_todos):  # pylint: disable=unused-argument,redefined-outer-name
    """Test creating a new todo"""
    response = client.post(
        '/todos',
        json={'title': 'Test Todo', 'description': 'Test Description'}
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Test Todo'
    assert data['description'] == 'Test Description'
    assert data['completed'] is False
    assert 'id' in data


def test_create_todo_missing_title(client, reset_todos):  # pylint: disable=unused-argument,redefined-outer-name
    """Test creating a todo without title"""
    response = client.post('/todos', json={'description': 'No title'})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data


def test_get_todo_by_id(client, reset_todos):  # pylint: disable=unused-argument,redefined-outer-name
    """Test getting a specific todo by ID"""
    create_response = client.post('/todos', json={'title': 'Find Me'})
    todo_id = create_response.get_json()['id']

    response = client.get(f'/todos/{todo_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Find Me'
    assert data['id'] == todo_id


def test_get_nonexistent_todo(client, reset_todos):  # pylint: disable=unused-argument,redefined-outer-name
    """Test getting a todo that doesn't exist"""
    response = client.get('/todos/999')
    assert response.status_code == 404
    data = response.get_json()
    assert 'error' in data


def test_update_todo(client, reset_todos):  # pylint: disable=unused-argument,redefined-outer-name
    """Test updating a todo"""
    create_response = client.post('/todos', json={'title': 'Original Title'})
    todo_id = create_response.get_json()['id']

    response = client.put(
        f'/todos/{todo_id}',
        json={'title': 'Updated Title', 'completed': True}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == 'Updated Title'
    assert data['completed'] is True


def test_delete_todo(client, reset_todos):  # pylint: disable=unused-argument,redefined-outer-name
    """Test deleting a todo"""
    create_response = client.post('/todos', json={'title': 'To Delete'})
    todo_id = create_response.get_json()['id']

    response = client.delete(f'/todos/{todo_id}')
    assert response.status_code == 200

    get_response = client.get(f'/todos/{todo_id}')
    assert get_response.status_code == 404


def test_delete_nonexistent_todo(client, reset_todos):  # pylint: disable=unused-argument,redefined-outer-name
    """Test deleting a todo that doesn't exist"""
    response = client.delete('/todos/999')
    assert response.status_code == 404
# Make sure there's an empty line here at the end of the file



