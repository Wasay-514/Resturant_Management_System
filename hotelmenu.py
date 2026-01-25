#menu 
menu={
    'Pizza' : 40,
    'Pasta' : 50,
    'Burger' : 60,
    'Salad'  : 70,
    'Cofee' : 80,
}
print("Welcome to Restaurant Management System")
print("**************Rate List***************")
print("Pizza : Rs.40 \nPasta : Rs.50 \nBurger : Rs.60 \nSalad : Rs.70 \nCofee : Rs.80" )
order_total = 0

item1 = input("Enter the name What you want to order = ")
if item1 in menu:
    order_total += menu[item1]
    print(f"Your Item {item1} has been added to your order")
else:
    print(f"Ordered item {item1} is not avalible yet")
Another_order = input("Do you want to add Another Item? (Yes/No)")
if Another_order == "Yes":
    item2 = input("Enter the name of second item")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Your item {item2} has been added to your order")
else:
    print(f"Ordered item {item1} is not avalible yet")
print(f"the total amount you have to pay is : {order_total}")
