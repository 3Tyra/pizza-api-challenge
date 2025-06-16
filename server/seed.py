import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    # Drop all and create tables again (only for dev/test, not production)
    db.drop_all()
    db.create_all()

    # Add pizzas
    pepperoni = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    margherita = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella, Basil")
    db.session.add_all([pepperoni, margherita])

    # Add restaurants
    dominos = Restaurant(name="Domino's", address="123 Pizza Street")
    kikis = Restaurant(name="Kiki's Pizza", address="456 Crust Ave")
    db.session.add_all([dominos, kikis])

    # Commit first to generate IDs
    db.session.commit()

    # Add restaurant pizzas now that IDs are generated
    rp1 = RestaurantPizza(price=10, pizza_id=pepperoni.id, restaurant_id=dominos.id)
    rp2 = RestaurantPizza(price=12, pizza_id=margherita.id, restaurant_id=kikis.id)
    db.session.add_all([rp1, rp2])
    db.session.commit()

    print("Database seeded successfully!")
