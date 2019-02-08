import random

WELCOME = [
"Hi! This is PizzaBot, Your virtual assistant to make your pizza order. Here's the menu for pizza. Please make your order",
"Welcome, I'm here to help you make your pizza order. Please make your order from the menu",
"This is PizzaBot, Make your order for pizza. Here's the menu",
"Hi! This is your Virtual Assistant. Please, Make your order. You can ask me if you want to see menu."]


ORDER_PIZZA = [
"{number} {size} sized {pizza_topping} pizza, sure!! Would you like to have some breadsticks?"]

UPSELL_BREADSTICK = [
"{breadstick}, Breadsticks. Would you like to have drinks too?"]

UPSELL_DRINK = [
"{drink}, We have desserts too. Would you like to make an order?"]

UPSELL_DESSERT = [
"{dessert} sweet!! \n\nYOUR ORDER DETAILS\n{items}\nDoes this complete your order?"]

COMPELETE_ORDER_FALLBACK =[
"YOUR ORDER DETAILS\n{items}\n\nDoes this complete your order?"]

ORDER_DELIVERY = [
"Thank You, Your order will be delivered at {location}.  How would you like to make your payment?"]


if __name__ == '__main__':
	print(random.choice(WELCOME))
