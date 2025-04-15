# Emarket API

Emarket is an e-commerce platform that provides RESTful APIs for creating, reading, updating, and deleting products, reviews, and orders.
## Installation

To install the Emarket API, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/emarket-api.git
   cd emarket-api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

Now the Emarket API should be running on `http://127.0.0.1:8000/`.

## API Endpoints

### Product Endpoints

* `GET /api/products/`: Get a list of all products.
* `GET /api/products/:id`: Get a specific product by ID.
* `POST /api/products/`: Create a new product.
* `PUT /api/products/:id`: Update a specific product by ID.
* `DELETE /api/products/:id`: Delete a specific product by ID.

### Review Endpoints

* `GET /api/reviews/`: Get a list of all reviews.
* `GET /api/reviews/:id`: Get a specific review by ID.
* `POST /api/reviews/`: Create a new review.
* `PUT /api/reviews/:id`: Update a specific review by ID.
* `DELETE /api/reviews/:id`: Delete a specific review by ID.

### Order Endpoints

* `GET /api/orders/`: Get a list of all orders.
* `GET /api/orders/:id`: Get a specific order by ID.
* `POST /api/orders/`: Create a new order.
* `PUT /api/orders/:id`: Update a specific order by ID.
* `DELETE /api/orders/:id`: Delete a specific order by ID.

## Authentication

Emarket uses JSON Web Tokens (JWT) for authentication. To obtain a JWT, send a `POST` request to the `/api/auth/login/` endpoint with your username and password.

### Example Request
