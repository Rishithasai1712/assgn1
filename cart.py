def cal_total(cart):
    for p in cart.values():
        if p>25000:
            total=sum(cart.values())
        if p>20000 and p<50000:
            total*=0.1
        if p>50000:
            total*=0.15
    if len(cart)>5:
        total*=0.9
    return total
cart={"a":50000,"b":52000,"c":15000,"d":5330,"e":54000}
print(f"cart items:{cart}")
print(f"total price:{cal_total(cart)}")