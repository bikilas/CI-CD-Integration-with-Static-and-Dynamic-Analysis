"""
Simple Flask Web Application
A basic REST API for managing a todo list
"""
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
class TodoApp:
    """Main application class for the Todo API"""
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.todos = []
        self.next_id = 1
        self.setup_routes()
    def setup_routes(self):
        """Set up all the API routes"""
        @self.app.route('/')
        def home():
            """Home endpoint"""
            return jsonify({
                'message': 'Welcome to Todo API',
                'version': '1.0.0',
                'endpoints': {
                    'GET /todos': 'Get all todos',
                    'POST /todos': 'Create a new todo',
                    'GET /todos/<id>': 'Get a specific todo',
                    'PUT /todos/<id>': 'Update a todo',
                    'DELETE /todos/<id>': 'Delete a todo'
                }
            })

        @self.app.route('/todos', methods=['GET'])
        def get_todos():
            """Get all todos"""
            return jsonify({'todos': self.todos, 'count': len(self.todos)}), 200

        @self.app.route('/todos', methods=['POST'])
        def create_todo():
            """Create a new todo"""
            data = request.get_json()
            if not data or 'title' not in data:
                return jsonify({'error': 'Title is required'}), 400

            todo = {
                'id': self.next_id,
                'title': data['title'],
                'description': data.get('description', ''),
                'completed': data.get('completed', False)
            }
            self.todos.append(todo)
            self.next_id += 1
            return jsonify(todo), 201

        @self.app.route('/todos/<int:todo_id>', methods=['GET'])
        def get_todo(todo_id):
            """Get a specific todo by ID"""
            todo = next((item for item in self.todos if item['id'] == todo_id), None)
            if not todo:
                return jsonify({'error': 'Todo not found'}), 404
            return jsonify(todo), 200
        @self.app.route('/todos/<int:todo_id>', methods=['PUT'])
        def update_todo(todo_id):
            """Update a todo by ID"""
            todo = next((item for item in self.todos if item['id'] == todo_id), None)
            if not todo:
                return jsonify({'error': 'Todo not found'}), 404
            data = request.get_json()
            if 'title' in data:
                todo['title'] = data['title']
            if 'description' in data:
                todo['description'] = data['description']
            if 'completed' in data:
                todo['completed'] = data['completed']

            return jsonify(todo), 200

        @self.app.route('/todos/<int:todo_id>', methods=['DELETE'])
        def delete_todo(todo_id):
            """Delete a todo by ID"""
            todo = next((item for item in self.todos if item['id'] == todo_id), None)
            if not todo:
                return jsonify({'error': 'Todo not found'}), 404
            self.todos = [item for item in self.todos if item['id'] != todo_id]
            return jsonify({'message': 'Todo deleted successfully'}), 200
        @self.app.route('/health', methods=['GET'])
        def health_check():
            """Health check endpoint"""
            return jsonify({'status': 'healthy'}), 200
    def run(self, **kwargs):
        """Run the Flask application"""
        self.app.run(**kwargs)

if __name__ == '__main__':
    app = TodoApp()
    # Use environment variables for configuration in production
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() in ('true', '1', 't')
    host = '127.0.0.1' if debug_mode else os.environ.get('HOST', '0.0.0.0')
    app.run(
        debug=debug_mode,
        host=host,
        port=int(os.environ.get('PORT', 5000))
    )