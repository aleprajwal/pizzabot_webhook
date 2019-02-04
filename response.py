import random

WELCOME = [
"Hi! This is PizzaBot, Your virtual assistant to make your pizza order. Here's the menu for pizza. Please make your order",
"Welcome, I'm here to help you make your pizza order. Please make your order from the menu",
"This is PizzaBot, Make your order for pizza. Here's the menu",
"Hi! This is your Virtual Assistant speaking from webhook. Please, Make your order. I can show you menu for pizza"]


ORDER_PIZZA = [
"{number} {size} sized {pizza_topping} pizza, sure!! Would you like to have a drink?"]


UPSELL_DRINK = [
"{drink}, Would you love to have some breadsticks?"]

UPSELL_BREADSTICK = [
"{breadstick}, Breadsticks. Would you like to have a dessert too?"]

UPSELL_DESSERT = [
"{dessert} sweet!! \n\nYOUR ORDER DETAILS\n{items}\nDoes this complete your order?"]

COMPELETE_ORDER_FALLBACK =[
"YOUR BILL\n{items}\n\nDoes this complete your order?"]

ORDER_DELIVERY = [
"Thank You, Your order will be delivered at {location}.  How would you like to make your payment?"]


if __name__ == '__main__':
	print(random.choice(WELCOME))
