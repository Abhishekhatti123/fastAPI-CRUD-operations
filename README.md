# FastAPI CRUD App

This project is a simple CRUD (Create, Read, Update, Delete) application built using FastAPI.

## Features

- Create, read, update, and delete operations for managing resources.
- FastAPI framework for building APIs.
- Easy to extend and customize.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd fastapi-crud-app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

3. Access the interactive API documentation at:
   ```
   http://127.0.0.1:8000/docs
   ```
