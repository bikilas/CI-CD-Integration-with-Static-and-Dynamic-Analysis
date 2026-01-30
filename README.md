# CI/CD Integration with Static and Dynamic Analysis Tools

This project demonstrates a complete CI/CD pipeline integrated with static and dynamic analysis tools for ensuring code quality and security.

## Project Overview

This is a simple Flask-based Todo API application that serves as a demonstration of CI/CD best practices with automated code quality checks.

## Features

- **RESTful API** for managing todos
- **Unit Tests** with pytest
- **Static Analysis** using Pylint
- **Dynamic Analysis** using Bandit (security scanning)
- **CI/CD Pipeline** with GitHub Actions

## Application Endpoints

- `GET /` - API information
- `GET /health` - Health check endpoint
- `GET /todos` - Get all todos
- `POST /todos` - Create a new todo
- `GET /todos/<id>` - Get a specific todo
- `PUT /todos/<id>` - Update a todo
- `DELETE /todos/<id>` - Delete a todo

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd CI_CD_Integration
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

   The application will be available at `http://localhost:5000`

5. **Run tests**
   ```bash
   # On Windows (if scripts not in PATH)
   python -m pytest tests/ -v
   
   # On Linux/Mac
   pytest tests/ -v
   ```

6. **Run static analysis**
   ```bash
   # On Windows (if scripts not in PATH)
   python -m pylint app.py --rcfile=.pylintrc
   
   # On Linux/Mac
   pylint app.py --rcfile=.pylintrc
   ```

7. **Run security scan**
   ```bash
   # On Windows (if scripts not in PATH)
   python -m bandit -r app.py
   
   # On Linux/Mac
   bandit -r app.py
   ```

## CI/CD Pipeline

The project includes a GitHub Actions workflow (`.github/workflows/ci_cd.yml`) that automatically runs on every push and pull request.

### Pipeline Stages

1. **Build Stage**
   - Sets up Python environment
   - Installs all dependencies
   - Verifies installation

2. **Test Stage**
   - Runs unit tests with pytest
   - Generates code coverage reports
   - Uploads coverage to Codecov

3. **Static Analysis Stage**
   - Runs Pylint for code quality checks
   - Checks for code style violations
   - Generates static analysis reports

4. **Dynamic Analysis Stage**
   - Runs Bandit for security vulnerability scanning
   - Identifies common security issues
   - Generates security reports

5. **Integration Test Stage**
   - Starts the application
   - Tests API endpoints
   - Verifies application functionality

## Tools Used

### Static Analysis Tool: Pylint
- **Purpose**: Code quality and style checking
- **Configuration**: `.pylintrc`
- **What it checks**: Code style, potential bugs, code smells, complexity

### Dynamic Analysis Tool: Bandit
- **Purpose**: Security vulnerability scanning
- **Configuration**: `.bandit`
- **What it checks**: Common security issues, insecure coding practices

## Project Structure

```
CI_CD_Integration/
├── .github/
│   └── workflows/
│       └── ci_cd.yml          # GitHub Actions workflow
├── tests/
│   └── test_app.py            # Unit tests
├── app.py                     # Main application
├── requirements.txt           # Python dependencies
├── .pylintrc                  # Pylint configuration
├── .bandit                    # Bandit configuration
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Running Analysis Tools Locally

### Pylint (Static Analysis)
```bash
# Analyze main application (Windows: use python -m pylint)
python -m pylint app.py --rcfile=.pylintrc

# Analyze tests
python -m pylint tests/ --rcfile=.pylintrc
```

### Bandit (Dynamic/Security Analysis)
```bash
# Scan application for security issues (Windows: use python -m bandit)
python -m bandit -r app.py

# Generate JSON report
python -m bandit -r app.py -f json -o bandit-report.json

# Generate text report
python -m bandit -r app.py -f txt -o bandit-report.txt
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Ensure all tests pass
4. Run static and dynamic analysis tools
5. Submit a pull request

The CI/CD pipeline will automatically validate your changes.

## License

This project is created for academic purposes.

## Author

Created as part of an academic assignment on CI/CD Integration with Static and Dynamic Analysis Tools.

