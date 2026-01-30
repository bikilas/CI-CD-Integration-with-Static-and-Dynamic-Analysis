# Quick Setup Guide for CI/CD Assignment

## Initial Git Repository Setup

1. **Initialize Git repository** (if not already done):
   ```bash
   git init
   ```

2. **Add all files**:
   ```bash
   git add .
   ```

3. **Create initial commit**:
   ```bash
   git commit -m "Initial commit: CI/CD pipeline with static and dynamic analysis"
   ```

4. **Create a GitHub repository** and push:
   ```bash
   git remote add origin <your-github-repo-url>
   git branch -M main
   git push -u origin main
   ```

## Verify CI/CD Pipeline

Once you push to GitHub:

1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. You should see the workflow running automatically
4. The pipeline includes:
   - ✅ Build Stage
   - ✅ Test Stage
   - ✅ Static Analysis (Pylint)
   - ✅ Dynamic Analysis (Bandit)
   - ✅ Integration Tests

## Assignment Checklist

- [x] CI/CD platform (GitHub Actions)
- [x] Static analysis tool (Pylint)
- [x] Dynamic analysis tool (Bandit)
- [x] Simple application (Flask Todo API)
- [x] Git repository setup
- [x] Build stage
- [x] Test stage

## Testing Locally

Before pushing to GitHub, test everything locally:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run tests (Windows: use python -m pytest)
python -m pytest tests/ -v

# 3. Run static analysis (Windows: use python -m pylint)
python -m pylint app.py --rcfile=.pylintrc

# 4. Run security scan (Windows: use python -m bandit)
python -m bandit -r app.py

# 5. Run the application
python app.py
```

## Project Structure Summary

```
CI_CD_Integration/
├── .github/workflows/ci_cd.yml  # GitHub Actions workflow
├── app.py                        # Flask application
├── tests/test_app.py            # Unit tests
├── requirements.txt              # Dependencies
├── .pylintrc                     # Pylint config (static analysis)
├── .bandit                       # Bandit config (dynamic analysis)
├── .gitignore                    # Git ignore rules
├── README.md                     # Full documentation
└── SETUP_GUIDE.md               # This file
```

## Notes for Submission

- The pipeline runs automatically on push/PR
- Static analysis uses Pylint (code quality)
- Dynamic analysis uses Bandit (security scanning)
- All stages must pass for the pipeline to succeed
- Reports are generated as artifacts in GitHub Actions

