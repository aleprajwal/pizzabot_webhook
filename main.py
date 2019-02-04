from flask import Flask, make_response, request, send_file
import json
import os
import logging
import random
from response import (WELCOME, ORDER_PIZZA, UPSELL_DRINK,
                      UPSELL_BREADSTICK, UPSELL_DESSERT, ORDER_DELIVERY, COMPELETE_ORDER_FALLBACK)

# initilize flask app
app = Flask(__name__)
filename = "pizza.txt"
image = {'pizza': 'pizza.jpg', 'drink': 'drink.jpg', 'breadstick': 'breadstick.jpg', 'dessert': 'dessert.jpg'}


# default route
@app.route('/', methods=['POST', 'GET'])
def webhook():
    req = request.get_json(silent=True, force=True)

    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'JSON error'

    if action == 'input.welcome':
        response = {
            "fulfillmentText": welcome(),
        }

    elif action == 'order.pizza':
        res = order_pizza(req)
        response = {"fulfillmentText": res}

    elif action == 'order.pizza.upsell.drink':
        res = upsell_drink(req)
        response = {"fulfillmentText": res}

    elif action == 'order.pizza.upsell.breadsticks':
        res = upsell_breadsticks(req)
        response = {"fulfillmentText": res}

    elif action == 'order.pizza.upsell.dessert':
        res = upsell_dessert(req)
        response = {"fulfillmentText": res}

    elif action == 'order.type.delivery':
        res = order_delivery(req)
        response = {"fulfillmentText": res}

    elif action == 'complete.order.fallback':
        response = {"fulfillmentText": complete_order_fallback()}

    # elif action == 'order.pizza.menu':
    #     response = {"fulfillmentMessage": {
    #         "image": {
    #             "imageUri": menu(image['pizza'])
    #         },
    #         "platform": "TELEGRAM"}}
    #
    # elif action == 'upsell.drink.menu':
    #     menu(image['drink'])
    #
    # elif action == 'upsell.breadstick.menu':
    #     menu(image['breadstick'])
    #
    # elif action == 'upsell.dessert.menu':
    #     menu(image['dessert'])

    else:
        logging.error("Action ERROR", exc_info=True)

    res = json.dumps(response, indent=4)
    r = make_response(res)
    return r


@app.route('/pizza_menu', methods=['GET', 'POST'])
def pizza_menu():
    try:
        image = os.path.join('image', 'pizza.jpg')
        return send_file(image, mimetype='image/gif')

    except Exception as e:
        logging.error("500 Error pizza_menu", exc_info=True)


@app.route('/drink_menu', methods=['GET', 'POST'])
def drink_menu():
    try:
        image = os.path.join('image', 'drink.jpg')
        return send_file(image, mimetype='image/gif')

    except Exception as e:
        logging.error("get_image()", exc_info=True)


@app.route('/breadstick_menu', methods=['GET', 'POST'])
def breadstick_menu():
    try:
        image = os.path.join('image', 'breadstick.jpg')
        return send_file(image, mimetype='image/gif')

    except Exception as e:
        logging.error("get_image()", exc_info=True)


@app.route('/dessert_menu', methods=['GET', 'POST'])
def dessert_menu():
    try:
        image = os.path.join('image', 'dessert.jpg')
        return send_file(image, mimetype='image/gif')

    except Exception as e:
        logging.error("get_image()", exc_info=True)


def welcome():
    return random.choice(WELCOME)


def order_pizza(req):
    params = req.get('queryResult').get('parameters')
    try:
        file = open(filename, "w")
        file.write("Pizza:")
        file.write(', '.join(str(top) for top in params['pizza_topping']))
        file.write(params['size'])
        file.close()
    except Exception as e:
        logging.error("500 error --> order_pizza(req)", exc_info=True)
    output_string = random.choice(ORDER_PIZZA)
    return output_string.format(
        number=int(params['number']),
        size=params['size'],
        pizza_topping=', '.join(str(top) for top in params['pizza_topping']))  # list to string


def upsell_drink(req):
    params = req.get('queryResult').get('parameters')
    try:
        file = open(filename, "a")
        file.write("\nDrink:")
        file.write(', '.join(str(d) for d in params['drink']))
        file.close()
    except Exception as e:
        logging.error(e, exc_info=True)
    output_string = random.choice(UPSELL_DRINK)
    return output_string.format(drink=', '.join(str(d) for d in params['drink']))


def upsell_breadsticks(req):
    params = req.get('queryResult').get('parameters')
    try:
        file = open(filename, "a")
        file.write("\nBreadsticks:")
        file.write(str(params['breadsticks']))
        file.close()
    except Exception as e:
        logging.error(e, exc_info=True)
    output_string = random.choice(UPSELL_BREADSTICK)
    return output_string.format(breadstick=params['breadsticks'])


def upsell_dessert(req):
    params = req.get('queryResult').get('parameters')
    try:
        file = open(filename, "a")
        file.write("\nDessert:")
        file.write(str(params['desserts']))
        file = open(filename, "r")
        items = file.read()
        file.close()
    except Exception as e:
        logging.error("500 error --> upsell_dessert(req)", exc_info=True)
    output_string = random.choice(UPSELL_DESSERT)
    return output_string.format(
        dessert=params['desserts'],
        items=items)


def order_delivery(req):
    params = req.get('queryResult').get('parameters')
    try:
        file = open(filename, "a")
        file.write("\nOrder_Type: Delivery ")
        file.write(params['location'])
        file.write(params['phone'])
        file.close()
    except Exception as e:
        logging.error("500 Error --> order_delivery(req)", exc_info=True)
    output_string = random.choice(ORDER_DELIVERY)
    return output_string.format(location=params['location'])


def complete_order_fallback():
    file = open(filename, 'r')
    items = file.read()
    output_string = random.choice(COMPELETE_ORDER_FALLBACK)
    return output_string.format(items=items)


# run the app
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0')
