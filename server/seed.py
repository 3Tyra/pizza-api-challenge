import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

with app.app_context():
    db.drop_all()
    db.create_all()

    
    pepperoni = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    margherita = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella, Basil")
    hawaiian = Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Cheese, Ham, Pineapple")
    veg_extravaganza = Pizza(name="Veg Extravaganza", ingredients="Dough, Tomato Sauce, Cheese, Bell Peppers, Olives, Onions, Mushrooms")
    db.session.add_all([pepperoni, margherita, hawaiian, veg_extravaganza])

    
    elaines = Restaurant(name="Elaine's Pizza", address="12 Westlands, Nairobi")
    mama_roma = Restaurant(name="Mama Roma", address="45 Kenyatta Avenue, Nairobi")
    nyama_choma = Restaurant(name="Nyama Choma Pizza", address="23 Moi Avenue, Nairobi")
    safari_slice = Restaurant(name="Safari Slice", address="78 Mombasa Road, Nairobi")
    db.session.add_all([elaines, mama_roma, nyama_choma, safari_slice])

    db.session.commit()

    
    rp1 = RestaurantPizza(price=15, pizza_id=pepperoni.id, restaurant_id=elaines.id)
    rp2 = RestaurantPizza(price=18, pizza_id=margherita.id, restaurant_id=mama_roma.id)
    rp3 = RestaurantPizza(price=20, pizza_id=hawaiian.id, restaurant_id=nyama_choma.id)
    rp4 = RestaurantPizza(price=16, pizza_id=veg_extravaganza.id, restaurant_id=safari_slice.id)
    db.session.add_all([rp1, rp2, rp3, rp4])

    db.session.commit()

    print("Database seeded successfully!")
