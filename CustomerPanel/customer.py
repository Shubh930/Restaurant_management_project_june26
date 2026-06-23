from modules import *

def view_menu():

    with open(food_store, "r") as opened_file:
        menu_list = json.load(opened_file)

    categories = {
        1: "Beverage",
        2: "Junk Food",
        3: "Fast Food",
        4: "South Indian",
        5: "North Indian",
        6: "Bread",
        7: "Soup & Starters",
        8: "Chinese",
        9: "Snacks",
        10: "Dessert",
        11: "Rice",
        12: "Breakfast",
        13: "Sides"
    }

    while True:
        
        print("\n1. Beverage              8. Chinese")
        print("2. Junk Food             9. Snacks")
        print("3. Fast Food             10. Dessert")
        print("4. South Indian          11. Rice")
        print("5. North Indian          12. Breakfast")
        print("6. Bread                 13. Sides")
        print("7. Soup & Starters")

        while True:

            cat_num = input("\nSelect your category : ")

            if cat_num.isdigit() and 1 <= int(cat_num) <= 13:
                cat_num = int(cat_num)
                break

            print("Please select a valid category.")
            

        selected_category = categories[cat_num]
        

        print("=" * 40)
        print(f"      ☕ {selected_category.upper()} MENU ☕")
        print("=" * 40)

        print("\n╔══════════════════════════════════════╗")
        print("║ ID    ITEM NAME             PRICE    ║")
        print("╠══════════════════════════════════════╣")

        found = False

        for food in menu_list:

            if food["food_category"] == selected_category:

                found = True

                print(
                    f"║ {food['food_id']:<5}"
                    f"{food['food_name']:<23}"
                    f"₹{food['food_price']:<8}║"
                )

        if not found:
            print("║           MENU IS EMPTY              ║")

        print("╚══════════════════════════════════════╝")
    
        while True:
            choice = input("Do you want to view another category ? (yes/no) : ").strip().lower()
            
            if choice == "yes":
                break
            elif choice == "no":
                return    
            else:
                print("Please enter only 'yes' or 'no'. ")

   
def addto_cart():
    while True:
        
        item1 = None
        item2 = None
        
        while True:
                    
            item = input("\nEnter your food ID or food name.")
            
            if item.isdigit():
                item1 = int(item)
                break
            elif item.replace(" ", "").isalpha():
                item2 = " ".join(item.strip().title().split())
                break
            else:
                print("\nPlease enter only Food Id or Food Name."+"\n")
                
        with open(food_store, "r") as opened_file:
            menu_list = json.load(opened_file)

#The else of a for loop runs only when the loop finishes without break.
#It does not run if a break happens.
        
        for food in menu_list:

            if food["food_id"] == item1 or food["food_name"] == item2:
                
                while True:
                    quantity = input(f"\nEnter quantity of {food['food_name']} : ")

                    if quantity.isdigit() and int(quantity) > 0:
                        quantity = int(quantity)
                        break
                    else:
                        print("\nPlease enter a valid quantity.")
                    
                food["food_quantity"] = quantity
                total = food["food_price"] * quantity
                food["food_total"] = total
                
                with open(item_store, "r") as opened_file:
                    cart_list = json.load(opened_file)

                # Duplicate check
                
                for dish in cart_list:

                    if dish["food_id"] == item1 or dish["food_name"] == item2:
                        print("\nAlready added to cart!")
                        break

                else:
                    cart_list.append(food)

                    with open(item_store, "w") as opened_file:
                        json.dump(cart_list, opened_file, indent=4)

                    print("\nAdded To Cart Successfully!")
                    break
                
        else:
            print("\nFood ID Not Found!")
            print(f"Please Enter Valid Food ID (101-{len(menu_list)+100}) : "+"\n")
            
                    
        while True:
            choice = input("Do you want to add another item ? (yes/no) : ").strip().lower()
            if choice == "yes":
                break
            elif choice == "no":
                return
            else:
                print("Please enter only 'yes' or 'no'. ")

        
def view_cart():

    with open(item_store, "r") as opened_file:
        cart_list = json.load(opened_file)

    if len(cart_list) != 0:

        print("\n" + "=" * 58)
        print("                 🛒 YOUR CART 🛒")
        print("=" * 58)

        print("╔════════╦════════════════════╦══════╦════════╦══════════╗")
        print("║ ID     ║  ITEM NAME         ║ QTY  ║ PRICE  ║ TOTAL    ║")
        print("╠════════╬════════════════════╬══════╬════════╬══════════╣")

        grand_total = 0

        for item in cart_list:

            print(
                f"║ {item['food_id']:<6} "
                f"║ {item['food_name']:<18} "
                f"║ {item['food_quantity']:<4} "
                f"║ ₹{item['food_price']:<5} "
                f"║ ₹{item['food_total']:<8}║"
            )

            grand_total += item["food_total"]

        print("╠════════╩════════════════════╩══════╩════════╩══════════╣")
        print(f"║ Grand Total : ₹{grand_total:<40}║")
        print("╚════════════════════════════════════════════════════════╝\n")

    else:
        print("\n🛒 Your cart is empty!\n")
            
        
def update_cart():
    
    item1 = None
    item2 = None
        
    while True:
                    
        item = input("\nEnter your food ID or food name.")
        
        if item.isdigit():
            item1 = int(item)
            break
        elif item.replace(" ", "").isalpha():
            item2 = " ".join(item.strip().title().split())
            break
        else:
            attempts = attempts + 1
            print("\nPlease enter only Food Id or Food Name."+"\n")
            
            if attempts == 3:
                print("\nToo many invalid attempts.")
                return
     
    with open(item_store,"r") as  opened_file :
        cart_list = json.load(opened_file)
    if len(cart_list) != 0:
        for item in cart_list:
            if item["food_id"] == item1 or item["food_name"] == item2:
                while True:
                    print("\n1. Change")
                    print("2. Remove")
                    update = int(input("\nDo you want to change quantiy or remove the existing dish ? "))
                   
                    if update == 1 :
                        while True:
                            quantity = input(f"Enter quantity of {item['food_name']} : ")

                            if quantity.isdigit() and int(quantity) > 0:
                                quantity = int(quantity)
                                break
                            else:
                                print("Please enter a valid quantity.")
                                
                        item["food_quantity"] = quantity
                        total = item["food_price"] * quantity
                        item["food_total"] = total
                        with open(item_store,"w") as opened_file:
                            json.dump(cart_list,opened_file,indent=4)
                        print("\nQuantity updated successfully ! ")
                        print(f"\nItems left in cart: {len(cart_list)}")
                        return
                    
                    elif update == 2 :
                        cart_list.remove(item)
                        with open(item_store,"w") as opened_file :
                            json.dump(cart_list,opened_file,indent=4)
                        print("="*30+"\n")
                        print(f"   Food Id : {item["food_id"]}")
                        print(f"   Food Name : {item["food_name"]}")
                        print(f"   Food Price : {item["food_price"]}")
                        print(f"   Food Category : {item["food_category"]}")
                        print(f"   Food Quantity : {item["food_quantity"]}")
                        print(f"   Food Total : {item["food_total"]}")
                        print("\n"+"="*30+"\n")
                        print("\nRemoved succefully !")
                        print(f"\nItems left in cart: {len(cart_list)}")
                        return
                    
                    else:
                        print("\nPlease enter valid number ! ")
        else:
            print("Food not found in cart!")
    else:
        print("Your cart is empty ! ")
                
        
   
def place_order():
    order_id = "ORD-"+ uuid.uuid4().hex[:6].upper()
    order_time = datetime.now().strftime("%d-%m-%y  %I:%M:%S")
    
    # this is our formatted time . here all letters are sensitive 
    # %Y = 2026, %y = 26, %H = 24hr, %I = 12hr, 
    # datetime.now().date() = 12-6-2026
    # datetime.now().time() = 10:35:42.123456
    # below time is formatted 
     
    with open (item_store,"r") as opened_file:
        cart_list = json.load(opened_file) 
        
    if len(cart_list) != 0:
 
        while True:
            print("1. Dine In")
            print("2. Take Away")
            order_type = int(input("Select Order Type : "+"\n"))
            
            if order_type == 1:
                
                total = 0 
                wish_list = [] 
                
                while True:
                    
                    item1 = None
                    item2 = None
                    
                    while True:
                    
                        item = input("Enter your food ID or food name.")
                        
                        if item.isdigit():
                            item1 = int(item)
                            break
                        elif item.replace(" ", "").isalpha():
                            item2 = " ".join(item.strip().title().split())
                            break
                        else:
                            print("Please enter only Food Id or Food Name."+"\n")
                    
                    found = False
                    
                    for food in cart_list:
                        if food["food_id"] == item1 or food["food_name"] == item2:
                            wish_list.append(food)
                            cart_list.remove(food)
                            total = total + food["food_total"]
                            print(f"{food['food_name']} added to order.")
                            
                            found = True
                            
                            break
                        
                    if not found:
                        print("Item not found in cart.")
                        
                    with open (item_store,"w") as opened_file:
                        json.dump(cart_list,opened_file,indent=4)
                        
                    while True:
                            
                        choice = input("\nDo you want to order another item from your cartlist ? (yes/no) : ").strip().lower()
                        
                        if choice == "yes":
                            break
                        elif choice == "no":
                            break
                        else:
                            print("Please enter only 'yes' or 'no'. ")
                            
                    if choice == "no":
                        break        
                            
                with open(tables_store,"r") as opened_file:
                    tables_list = json.load(opened_file)
                for table in tables_list:
                    if table["status"] == "Available" :
                        print(f"Table No: {table["table_number"]} - Available")
                        
                while True:    
                    table_num = int(input("\nEnter Table Number : "))
                    with open(tables_store,"r") as opened_file:
                        tables_list = json.load(opened_file)
                    for table in tables_list:
                        if table["table_number"] == table_num and table["status"] == "Available" :
                            table["status"] = "Occupied"
                            
                            with open(tables_store, "w") as opened_file:
                                json.dump(tables_list, opened_file, indent=4) 
                      
                        
                            orders_dict = {
                                "Order_id"   : order_id,
                                "Order_time" : order_time,
                                "Order_type" : "Dine in",
                                "Order_status"  : "Confirmed",
                                "Payment_status" : "Due",
                                "Table_no" : table_num,
                                "Items" : wish_list,
                                "Total" : total
                            } 
                            
                            
                            with open(orders_store,"r") as opened_file:
                                orders_list = json.load(opened_file)
                            orders_list.append(orders_dict)
                            print(json.dumps(orders_list,indent=4))
                            with open(orders_store,"w") as opened_file:
                                json.dump(orders_list,opened_file,indent=4)
                         
                            
                            print("\n" + "="*40)
                            print("         DINE-IN ORDER CONFIRMED")
                            print("="*40)
                            print(f"Table Number  :  {table_num}")
                            print(f"Total Amount  :  ₹{total}")
                            print()
                            print("Please take your seat.")
                            print()
                            print("Your order has been successfully placed.")
                            print()
                            print("Thank you for ordering from")
                            print("THE SHUBH RESTAURANT.")
                            print("="*40)
                            
                            return
                    
                    else:
                        print("\nThis table is reserved.\n"
                              "Please enter a table number that is available.")
                            
                            
            if order_type == 2:
                
                total = 0 
                wish_list = [] 
                
                while True:
                    
                    item1 = None
                    item2 = None
                    
                    while True:
                    
                        item = input("Enter your food ID or food name.")
                        
                        if item.isdigit():
                            item1 = int(item)
                            break
                        elif item.replace(" ", "").isalpha():
                            item2 = " ".join(item.strip().title().split())
                            break
                        else:
                            print("Please enter only Food Id or Food Name.")
                    
                    found = False
                    
                    for food in cart_list:
                        if food["food_id"] == item1 or food["food_name"] == item2:
                            wish_list.append(food)
                            cart_list.remove(food)
                            total = total + food["food_total"]
                            print(f"{food['food_name']} added to order.")
                            
                            found = True
                            
                            break
                        
                    if not found:
                        print("Item not found in cart.")
                        
                    with open (item_store,"w") as opened_file:
                        json.dump(cart_list,opened_file,indent=4)
                        
                    while True:
                            
                        choice = input("\nDo you want to order another item from your cartlist ? (yes/no) : ").strip().lower()
                        
                        if choice == "yes":
                            break
                        elif choice == "no":
                            break
                        else:
                            print("Please enter only 'yes' or 'no'. ")
                            
                    if choice == "no":
                        break   
                    
                with open (orders_store,"r") as opened_file:
                    orders_list = json.load(opened_file)
                    
                token_num = 1001 + len(orders_list)
                    
              
                         
                orders_dict = {
                        "Order_id" : order_id,
                        "Order_time" : order_time,
                        "Order_type" : "Take away",
                        "Order_status"  : "Confirmed",
                        "Payment_status" : "Due",
                        "Token_no" : token_num,
                        "Items" : wish_list,
                        "Total" : total
                    }
               
                orders_list.append(orders_dict)
                print(json.dumps(orders_list,indent=4))
                with open(orders_store,"w") as opened_file:
                    json.dump(orders_list,opened_file,indent=4)       
                with open(item_store,"r") as opened_file:
                    cart_list = json.load(opened_file)
                with open(item_store,"w") as opened_file:
                    json.dump([], opened_file, indent=4) # this line is used to empty cart_list
                            
                print("\n" + "="*40)
                print("       TAKE-AWAY ORDER CONFIRMED")
                print("="*40)
                print(f"Token Number  :  {token_num}")
                print(f"Total Amount  :  ₹{total}")
                print()
                print("Please collect it from the counter")
                print("when your order number is called.")
                print()
                print("Your order has been successfully placed.")
                print()
                print("Thank you for ordering from")
                print("THE SHUBH RESTAURANT.")
                print("="*40)
                return
            
            else:
                print("\nInvalid Order Type. \nPlease Enter Valid Order Type.")
              
    else:
        print("\nYour cart is empty.")
        print("Please add at least one item to your cart before placing an order.")
                                  
                            
                               
def generateBill_npay():
    
    print("what is order type ?")
    print("1. Dine In")
    print("2. Take Away")
    
    while True:
        option = int(input("Select an option : "))
        
        if option == 1:
            
            while True:
                
                print("\nPlease select a payment method:")
                print("1. Cash")
                print("2. UPI")
                print("3. Debit/Credit Card")
                
                payment_choice = int(input("\nEnter your choice: "))
                
                if payment_choice == 1:
                    table_num = int(input("\nEnter Your Table Number : "))
                    with open(orders_store,"r") as opened_file:
                        orders_list = json.load(opened_file)
                    for order in orders_list:
                        if order.get("Table_no") == table_num:
                            order["Order_status"] = "Completed"
                            order["Payment_status"] = "Paid"
                            order["Payment_method"] = "Cash"
                            with open(orders_store,"w") as opened_file:
                                json.dump(orders_list,opened_file, indent=4)

                    with open(tables_store,"r") as opened_file:
                        tables_list = json.load(opened_file)
                    for table in tables_list:
                        if table.get("table_number") == table_num:
                            table["status"] = "Available"
                    with open(tables_store,"w") as opened_file:
                        json.dump(tables_list,opened_file,indent=4)   
                    break            
                                
                elif payment_choice == 2:
                    table_num = int(input("\nEnter Your Table Number : "))
                    with open(orders_store,"r") as opened_file:
                        orders_list = json.load(opened_file)
                    for order in orders_list:
                        if order.get("Table_no") == table_num:
                            
                            order["Order_status"] = "Completed"
                            order["Payment_status"] = "Paid"
                            order["Payment_method"] = "UPI"
                            with open(orders_store,"w") as opened_file:
                                json.dump(orders_list,opened_file, indent=4)

                    with open(tables_store,"r") as opened_file:
                        tables_list = json.load(opened_file)
                    for table in tables_list:
                        if table.get("table_number") == table_num:   # ✅ FIXED HERE
                            table["status"] = "Available"
                    with open(tables_store,"w") as opened_file:
                        json.dump(tables_list,opened_file,indent=4)
                    break
                           
                elif payment_choice == 3:
                    table_num = int(input("\nEnter Your Table Number : "))
                    with open(orders_store,"r") as opened_file:
                        orders_list = json.load(opened_file)
                    for order in orders_list:
                        if order.get("Table_no") == table_num:
                            order["Order_status"] = "Completed"
                            order["Payment_status"] = "Paid"
                            order["Payment_method"] = "Card"
                            with open(orders_store,"w") as opened_file:
                                json.dump(orders_list,opened_file, indent=4)

                    with open(tables_store,"r") as opened_file:
                        tables_list = json.load(opened_file)
                    for table in tables_list:
                        if table.get("table_number") == table_num:
                            table["status"] = "Available"
                    with open(tables_store,"w") as opened_file:
                        json.dump(tables_list,opened_file,indent=4)
                    break
                           
                else:
                    print("\nPlease enter valid payment method !")
            
            with open (orders_store,"r") as opened_file:
                orders_list = json.load(opened_file)
            for order in orders_list:
                if order.get("Table_no") == table_num:
                    
                    print("=" * 40)
                    print("         THE SHUBH RESTAURANT")
                    print("=" * 40)
                    print("              CUSTOMER BILL")
                    print("=" * 40)

                    print()
                    print(f"Order ID     : {order['Order_id']}")
                    print(f"Order Type   : {order['Order_type']}")
                    print(f"Table No.    : {order['Table_no']}")
                    print(f"Order Time   : {order['Order_time']}")

                    print()
                    print("-" * 40)
                    print(f"{'Item Name':<12}{'Qty':<7}{'Price':<10}{'Total'}")
                    print("-" * 40)

                    Subtotal = 0

                    for item in order["Items"]:
                        print(
                            f"{item['food_name']:<12}"
                            f"{item['food_quantity']:<7}"
                            f"₹{item['food_price']:<9}"
                            f"₹{item['food_total']}"
                        )

                        Subtotal += item["food_total"]

                    gst = (5 / 100) * Subtotal
                    service_charge = (5 / 100) * Subtotal
                    grand_total = Subtotal + gst + service_charge

                    print("-" * 40)

                    print()
                    print(f"Total Items          : {len(order['Items'])}")
                    print(f"Subtotal             : ₹{Subtotal:.2f}")
                    print(f"GST (5%)             : ₹{gst:.2f}")
                    print(f"Service Charge (5%)  : ₹{service_charge:.2f}")

                    print("-" * 40)
                    print(f"Grand Total          : ₹{grand_total:.2f}")

                    print()
                    print("=" * 40)
                    print("     Thank You For Dining With Us!")
                    print("            Visit Again!")
                    print("=" * 40)
            break 
    
        elif option == 2:  
            while True:
                
                print("\nPlease select a payment method:")
                print("1. Cash")
                print("2. UPI")
                print("3. Debit/Credit Card")
                
                payment_choice = int(input("\nEnter your choice: "))
                
                if payment_choice == 1:
                    token_num = int(input("\nEnter Your Token Number : "))
                    with open(orders_store,"r") as opened_file:
                        orders_list = json.load(opened_file)
                    for order in orders_list:
                        if order.get("Token_no") == token_num:
                            order["Order_status"] = "Completed"
                            order["Payment_status"] = "Paid"
                            order["Payment_method"] = "Cash"
                            with open(orders_store,"w") as opened_file:
                                json.dump(orders_list,opened_file, indent=4)
                    break            
                                
                elif payment_choice == 2:
                    token_num = int(input("\nEnter Your Token Number : "))
                    with open(orders_store,"r") as opened_file:
                        orders_list = json.load(opened_file)
                    for order in orders_list:
                        if order.get("Token_no") == token_num:
                            order["Order_status"] = "Completed"
                            order["Payment_status"] = "Paid"
                            order["Payment_method"] = "UPI"
                            with open(orders_store,"w") as opened_file:
                                json.dump(orders_list,opened_file, indent=4)
                    break
                           
                elif payment_choice == 3:
                    token_num = int(input("\nEnter Your Token Number : "))
                    with open(orders_store,"r") as opened_file:
                        orders_list = json.load(opened_file)
                    for order in orders_list:
                        if order.get("Token_no") == token_num:
                            order["Order_status"] = "Completed"
                            order["Payment_status"] = "Paid"
                            order["Payment_method"] = "Card"
                            with open(orders_store,"w") as opened_file:
                                json.dump(orders_list,opened_file, indent=4)
                    break
                           
                else:
                    print("\nPlease enter valid payment method !")
                    
            with open (orders_store,"r") as opened_file:
                orders_list = json.load(opened_file)

            for order in orders_list:
                if order.get("Token_no") == token_num:
                    
                    print("=" * 40)
                    print("         THE SHUBH RESTAURANT")
                    print("=" * 40)
                    print("              CUSTOMER BILL")
                    print("=" * 40)

                    print()
                    print(f"Order ID     : {order['Order_id']}")
                    print(f"Order Type   : {order['Order_type']}")
                    print(f"Token No.    : {order['Token_no']}")
                    print(f"Order Time   : {order['Order_time']}")

                    print()
                    print("-" * 40)
                    print(f"{'Item Name':<12}{'Qty':<7}{'Price':<10}{'Total'}")
                    print("-" * 40)

                    Subtotal = 0

                    for item in order["Items"]:
                        print(
                            f"{item['food_name']:<12}"
                            f"{item['food_quantity']:<7}"
                            f"₹{item['food_price']:<9}"
                            f"₹{item['food_total']}"
                        )

                        Subtotal += item["food_total"]

                    gst = (5 / 100) * Subtotal
                    service_charge = (5 / 100) * Subtotal
                    grand_total = Subtotal + gst + service_charge

                    print("-" * 40)

                    print()
                    print(f"Total Items          : {len(order['Items'])}")
                    print(f"Subtotal             : ₹{Subtotal:.2f}")
                    print(f"GST (5%)             : ₹{gst:.2f}")
                    print(f"Service Charge (5%)  : ₹{service_charge:.2f}")

                    print("-" * 40)
                    print(f"Grand Total          : ₹{grand_total:.2f}")

                    print()
                    print("=" * 40)
                    print("     Thank You For Dining With Us!")
                    print("            Visit Again!")
                    print("=" * 40)

            break
            
        else:
            print("Enter a valid number ! ")
                                
                       
                    
                
                
                                
                        
                        
 
        


                
                    
             
                    
                        
                
 


            
        
            

 

