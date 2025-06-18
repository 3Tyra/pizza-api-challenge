# pizza-api-challenge

--Pizza Restaurants API--
A RESTful Flask API for managing pizzas, restaurants, and their relationships, including pricing and menu management.


## Project Description

This is a Flask-based API that allows users to manage pizzas, restaurants, and their associated prices. The API uses SQLAlchemy ORM for database interactions, Flask-Migrate for schema management, and Flask Blueprints for clean modular routing. It supports full CRUD functionality with proper validations and error responses.

---

## Setup Instructions

1. Navigate into project directory:

```bash
cd pizza-api-challenge
```

2. Install dependencies using Pipenv:

```bash
pipenv install
pipenv shell
```

3. Set up the database:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

4. Seed the database:

```bash
python seed/seed.py
```

---

## Running the Application

Start the Flask development server:

```bash
flask run
```

Visit the API at:
`http://127.0.0.1:5000/`

## API Endpoints

### Restaurants

* `GET /restaurants`
  Retrieve all restaurants

* `GET /restaurants/<int:id>`
  Retrieve a specific restaurant with its pizzas

* `DELETE /restaurants/<int:id>`
  Delete a restaurant by ID

### Pizzas

 `GET /pizzas`
  Retrieve all pizzas

 `GET /pizzas/<int:id>`
  Retrieve a specific pizza

### Restaurant Pizzas

* `POST /restaurant_pizzas`
  Create a new restaurant-pizza association with a price
  **Request JSON:**

```json
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 1
}
```

 `DELETE /restaurant_pizzas/<int:id>`
  Delete a restaurant-pizza association


Validation Rules

 Price must be an integer between 1 and 30
 Pizza and Restaurant must exist before associating
 Invalid requests return HTTP 400
 Non-existent resources return HTTP 404

## Error Handling

`404 Not Found` – Resource doesn't exist
 `400 Bad Request` – Invalid input or missing data
 `500 Internal Server Error` – Server-side failure

Example error response:

```json
{
  "error": "Restaurant not found"
}
```
# Authors:
Tyra Mwai.



