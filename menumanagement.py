def menu_mngmt(menu,t1,t2,t3):
    menu.append(t1)
    menu.remove(t2)
    if menu.count(t3)>1:
        return t3
menu =["Pizza", "Burger", "Pasta", "Salad"]
t1=input()
t2=input()
t3=input()
print(f"{menu}")
print(f"Availability: {t3} is available")

    
    