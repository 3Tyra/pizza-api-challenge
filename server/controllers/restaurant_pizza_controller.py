from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        price = int(data.get('price'))
        pizza_id = data.get('pizza_id')
        restaurant_id = data.get('restaurant_id')

        # Validate price with model method
        RestaurantPizza.validate_price(price)

        # Validate pizza exists
        pizza = Pizza.query.get(pizza_id)
        if not pizza:
            return jsonify({"errors": ["Pizza not found"]}), 404

        # Validate restaurant exists
        restaurant = Restaurant.query.get(restaurant_id)
        if not restaurant:
            return jsonify({"errors": ["Restaurant not found"]}), 404

        # Create new RestaurantPizza
        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()

        # Assuming your model has to_dict_with_nested method
        return jsonify(rp.to_dict_with_nested()), 201

    except ValueError as e:
        # For price validation or int casting errors
        return jsonify({"errors": [str(e)]}), 400

    except Exception as e:
        # Unexpected errors - you can log e for debugging
        return jsonify({"errors": ["An unexpected error occurred."]}), 500
