def cal_check(cart):
    price = sum(cart.values())
    if len(cart)>5:
        price *=0.9
    return price
cart = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print(f"Total Price:{cal_check(cart)}")