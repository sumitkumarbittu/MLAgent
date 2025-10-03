# Sentiment Analysis API

A FastAPI-based sentiment analysis service that uses sentence embeddings and logistic regression to classify text as positive or negative sentiment.

## Features

- Single text prediction endpoint
- Batch prediction endpoint for multiple texts
- Built with FastAPI for high performance
- Uses `all-MiniLM-L6-v2` for sentence embeddings
- Pre-trained logistic regression classifier
- Interactive API documentation
- CORS enabled

## Prerequisites

- Python 3.11.8
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MLAgent.git
   cd MLAgent
   ```

2. Create and activate a virtual environment:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the API

```bash
uvicorn app:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### API Endpoints

#### Health Check
```http
GET /health
```

#### Single Prediction
```http
POST /predict
Content-Type: application/json

{
    "text": "I love this product!"
}
```

#### Batch Prediction
```http
POST /predict_batch
Content-Type: application/json

{
    "texts": ["I love this!", "I don't like this"]
}
```

### API Documentation

- Interactive API docs (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Alternative API docs (ReDoc): [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Deployment

### Local Development

```bash
# Start the development server with auto-reload
uvicorn app:app --reload
```

### Production Deployment

1. Ensure you have Python 3.11.8 installed
2. Install dependencies: `pip install -r requirements.txt`
3. Run with production settings:
   ```bash
   uvicorn app:app --host 0.0.0.0 --port 8000
   ```

### Deployment to Render

1. Push your code to a GitHub repository
2. Connect your GitHub repository to Render
3. The `render.yaml` file will automatically configure the deployment with Python 3.11.8

## Project Structure

- `app.py` - Main FastAPI application
- `model1.pkl` - Pre-trained logistic regression model
- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version specification
- `render.yaml` - Render deployment configuration

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


