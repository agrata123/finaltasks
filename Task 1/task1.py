def pizza_total_price(tuesday, pizza_number,customer_delivery,order_from_app):
    '''calculation of total price of pizza based on various conditions.
        
        parameters: Tuesday: (boolean data-type) True if it's tuesday, else false.
                    pizza_number: (Integer data-type) Total number of pizza ordered by customer.
                    customer_delivery: (boolean data-type) True if customer wants delivery, else false.
                    order_from_app: (boolean data-type) True if customer is ordering using BPP app, else false.
        
        Returns the total price of pizza after applying all the conditions. (Float data-type)            '''
    
    Pizza_cost = 12.00
    Discount_on_Tuesdays = 0.50 #(50%) 
    #(Constant values given in the question)
    
    #Applying Tuesday Discount if the day is tuesday.(50% off)
    if tuesday:
        discount_applied = Discount_on_Tuesdays
        only_discount_price= pizza_number * (Pizza_cost * (1 - Discount_on_Tuesdays))
        total_price = pizza_number * (Pizza_cost * (1 - Discount_on_Tuesdays))
    else:
        discount_applied = 0
        only_discount_price = 0
        total_price = pizza_number * Pizza_cost
    
    
    Delivery_Cost = 2.50
    #if customer orders 5 or more pizzas, there is no delivery cost. If not, £2.50 delivery cost is added.(shown below)
    # Checking for delivery conditions
    if pizza_number >= 5 and customer_delivery:
        delivery_discount_applied = 0  # No delivery charge
        total_price += 0
    elif pizza_number < 5 and not customer_delivery:
        delivery_discount_applied = 0 
        total_price += 0 # No delivery charge
    elif pizza_number >=5 and not customer_delivery:
        delivery_discount_applied = 0
        total_price +=0    
    
    else:
        delivery_discount_applied = Delivery_Cost
        total_price += Delivery_Cost
    

    Discount_using_App = 0.25 
    #if the customer orders using BPP app, 25% of total price is applied as discount.
    if order_from_app:
        app_discount_applied = Discount_using_App
        only_app_discount = total_price*Discount_using_App
        total_price -= (total_price * Discount_using_App)
    else:
        app_discount_applied = 0
        only_app_discount = 0
    

    print("---------------------------------")
    print("\n\nHere is your bill:\n\n")
    bill_heading = "==BECKETT PIZZA PLAZA=="
    print(bill_heading.center(50))
    print(f"\nNumber Of Pizza                                {pizza_number}")
    print(f"\nActual Price                                  £{pizza_number*12:.2f}")
    print(f"\nTuesday Discount:{discount_applied * 100:.2f}%                       £{only_discount_price:.2f}")
    print(f"\nDelivery cost                                 £{delivery_discount_applied:.2f}")
    print(f"\nApp Discount:{app_discount_applied * 100:.2f}%                           £{only_app_discount:.2f}\n")
    
    
    
    return total_price

text_a = "BECKETT PIZZA PLAZA"
print(text_a.center(110))
text_b= "50% OFF ON TUESDAYS!!"
print(text_b.center(110))
text_c = "BEST PRICE IN THE TOWN!! ONLY AT £12!!"
print(text_c.center(110))
text_d = "ORDER FROM OUR BPP APP AND GET 25% OFF!!"
print(text_d.center(110))
print("=======================================================================================================================================")
#welcome

print("\nGREETINGS!")
print("Our Pizzas\n--------\n1)Veg Delight Pizza\n2)Meat lovers pizza\n3)Cheese Pizza\n4)Chicken Barbeque pizza\n5)Hawaiian pizza\n6)Tandoori chicken pizza\n7)Double cheese\n8)pepperoni pizza\n9)Beckett Signature Pizza\n---------")


# Now,taking input from user
while True:
    pizza_choice = int(input("\nWhich pizza would you like to order?(1/2/3/4/5/6/7/8/9):"))
    if pizza_choice >= 0 and pizza_choice <= 9:
     break
    else:
      print("please enter the numbers between 1 and 9")
        
while True:
    try:
        pizza_number = int(input("\nNumber of pizzas you wish to order? Delivery charge not added if you order 5 or more pizzas : "))
        if pizza_number > 0:
            break 
        #if user inputs positive number, the condition is true and the loop breaks. Else,(given below)
        else:
            print("Invalid input.Please enter right numbers") #if less than zero      
    except:
        print("Invalid input type")


while True:
    tuesday = input("\nIs today our special day Tuesday:D? (y/n/yes/no): ")
    tuesday = tuesday.lower()
    if tuesday == "yes" or tuesday =="no" or tuesday=="y" or tuesday=="n":
        tuesday = (tuesday =="yes" or tuesday =="y")
        break 
    #if the user says yes or y to tuesday, the condition is true,(1 is stored in tuesday, which is true) and the loop breaks. else,(given below)
    else:
        print("Invalid input. Please enter 'yes','no','y' or 'n'.")


while True:
    customer_delivery = input("\nDo you want your order to be delivered? (yes/no/y/n): ")
    customer_delivery = customer_delivery.lower()
    if customer_delivery == "yes" or customer_delivery =="no" or customer_delivery =="y" or customer_delivery=="n":
        customer_delivery = (customer_delivery =="yes" or customer_delivery == "y")
        break
    else:
        print("Invalid input. Please enter 'yes','no','y' or 'n'.")


while True:
    order_from_app = input("\nAre you ordering using our  BPP app? (yes/no/y/n): ")
    order_from_app = order_from_app.lower()
    if order_from_app =="yes" or order_from_app == "no" or order_from_app=="y" or order_from_app=="n":
        order_from_app = (order_from_app =="yes" or order_from_app =="y")
        break
    else:
        print("Invalid input. Please enter 'yes','no','y' or 'n'.")


#calling the function to calculate the total price
total_price = pizza_total_price(tuesday, pizza_number,customer_delivery,order_from_app)

#displaying total price of the pizza.
 
print("=================================================================")
print(f"\nYour Total Price:                             £{total_price:.2f}\n\nThank You! Visit again!" ) 
#(.2f displays only 2 numbers after decimal point(in order to avoid multiple numbers after decimal which could confuse the customer)

