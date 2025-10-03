# MLAgent

## Deployment on Render

This project is configured to use Python 3.11.8. The following files ensure proper deployment:
- `runtime.txt` - Specifies Python 3.11.8
- `render.yaml` - Render-specific configuration
- `setup.py` - Python package configuration

### Requirements
- Python 3.11.8
- Dependencies listed in `requirements.txt`

### Local Development
```bash
# Create and activate virtual environment
python3.11 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload
```

### Deployment to Render
1. Push these changes to your GitHub repository
2. Connect your GitHub repository to Render
3. The `render.yaml` file will automatically configure the deployment with Python 3.11.8

