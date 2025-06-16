from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import models to register tables with SQLAlchemy
from server.models import restaurant, pizza, restaurant_pizza

# Import and register route blueprints
from server.controllers import register_routes
register_routes(app)


if __name__ == '__main__':
    app.run(debug=True)
