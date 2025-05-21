# Simple Inventory Management

## Method 1: With Docker
Pull the image and run the container
```
docker pull ghcr.io/janielee1111/kiratech_inventory:latest
docker run -p 8000:8000 ghcr.io/janielee1111/kiratech_inventory:latest
```

## Method 2: Without Docker
__Prerequisites__

Before you begin, ensure you have the following installed:

- Python 3.8+ 
- uv

Once you have clone the project, use *uv* to create the virtual environment and install all the dependencies:
```
uv sync
```

Run the project
```
uv run manage.py runserver
```
OR 

Do the old fashion way by activating the virtual environment and run the project.
```
.venv\Scripts\activate
python manage.py runserver
```


