from modules import *
users_store = r"C:\Users\shubhendra singh\OneDrive\Desktop\python\SHUBHrestro\Database\users.json"

def view_menu():

    with open(food_store, "r") as opened_file:
        menu_list = json.load(opened_file)

    if len(menu_list) == 0:
        print("\nMenu is empty.")
        return

    # Create a list of unique categories
    categories = []

    for food in menu_list:

        found = False

        for category in categories:
            if category == food["food_category"]:
                found = True
                break

        if found == False:
            categories.append(food["food_category"])

    # Print category-wise table
    for category in categories:

        print("╔══════════════════════════════════════╗")
        print(f"║ Category : {category:<26}║")
        print("╠══════════════════════════════════════╣")
        print("║ ID    ITEM NAME             PRICE    ║")
        print("╠══════════════════════════════════════╣")

        for food in menu_list:

            if food["food_category"] == category:

                print(
                    f"║ {food['food_id']:<5}"
                    f"{food['food_name']:<23}"
                    f"₹{food['food_price']:<8}║"
                )

        print("╚══════════════════════════════════════╝\n")
       
            
def add_food():
    # food_id = uuid.uuid1().hex[:10]
    with open(food_store,"r") as opened_file :
        menu_list = json.load(opened_file)
    ton = 100
    last_id = ton + len(menu_list)
    food_id = last_id + 1
    food_name = " ".join(input("Please enter food name : ").title().strip().split())
    
    while True:
        food_price = " ".join(input("Please add suitable price : ").strip().split())
        
        if food_price.isdigit():
            food_price = int(food_price)
            break
        else:
            print("\nEnter valid food price.")
        
        
    food_category = " ".join(input("please add food category : ").capitalize().split())
    
    food_info = {
        "food_id"       :  food_id,
        "food_name"     :  food_name,
        "food_price"    :  food_price,
        "food_category" :  food_category
    }
    
    with open( food_store, "r") as opened_file :
        menu_list = json.load(opened_file)
        menu_list.append(food_info)
    with open(food_store, "w") as opened_file :
        json.dump(menu_list, opened_file, indent=4)
    print("Your dish has been succefully added to menu.")
        
    # food_json = json.dumps(food_info, indent=4)
    # file.write(food_json)
    # print(food_json)
       
                
def delete_food():
    while True:
        print("Press 1 if you want to delete by Food ID .")
        print("Press 2 if you want to delete by Food Name ")
        option = int(input("select an option : "))
        
        if option == 1 :
            with open(food_store, "r") as opened_file:
                menu_list = json.load(opened_file)
                
            while True:
                delete_byID = input("\nEnter food id or food name to delete.")
                if "".join(delete_byID.strip().split()).isdigit() and 100 < int(delete_byID) <= len(menu_list)+100:
                    delete_byID = int(delete_byID)
                    break
                else:
                    print("\nPlease enter valid food id")
            
            with open(food_store,"r") as opened_file :
                menu_list = json.load(opened_file)
                
            for food in menu_list:
                if food["food_id"] == delete_byID :
                    menu_list.remove(food)
                    
                    with open(food_store,"w") as opened_file :
                        json.dump(menu_list, opened_file, indent=4)
                    print("Deleted Successfully")
                    return
            else:
                print("This Food does not exist !")
                
        elif option == 2:
            while True:
                delete_byName = " ".join((input("Enter Food Name to Delete : ")).capitalize().strip().split())
                
                if delete_byName.replace(" ","").isdigit():
                    break
                else:
                    print("\nPlease enter valid food name.")
            
            with open (food_store,"r") as opened_file:
                menu_list = json.load(opened_file)
            for food in menu_list:
                if food["food_name"] == delete_byName:
                    menu_list.remove(food)
                    with open(food_store,"w") as opened_file:
                        json.dump(menu_list,opened_file,indent=4)
                    print("Deleted Successfully !")
                    return
            else:
                print("This food does not exist !")
                
        else:
            print("Invalid Option !")
            
                                
def update_food():
    while True:
        with open(food_store, "r") as opened_file:
            menu_list = json.load(opened_file)
            
        dish_id = None
        dish_name = None
        
        while True:
            
            dish = input("Enter Your Food ID or Food Name : ")
            
            if dish.isdigit()   and   100 < int(dish) <= len(menu_list)+100 :
                dish_id = int(dish)
                break
            elif dish.replace(" ","").isalpha():
                dish_name = " ".join(dish.title().strip().split())
                break
            else:
                print("\nEnter valid food id food name.")
            
        
        with open(food_store,"r") as opened_file :
            menu_list = json.load(opened_file)
            
        for food in menu_list:
            if food["food_id"] == dish_id or food["food_name"] == dish_name:
                
                print("="*30+"\n")
                print(f"Food ID       :  {food["food_id"]}")
                print(f"Food Name     :  {food["food_name"]}")
                print(f"Food Price    :  {food["food_price"]}")
                print(f"Food Category :  {food["food_category"]}")
                print("\n"+"="*30+"\n\n")
                
                
                while True:
                    
                    print("\nWhat do you want to update in this food ?")
                    print("1. Food Name")
                    print("2. Food Price")
                    print("3. Food Category")
                    
                    option = int(input("Select an option : "))
                    
                    if option == 1:
                        new_foodName = " ".join(input("Enter new food name.").title().strip().split())
                        food["food_name"] = new_foodName
                        with open(food_store,"w") as opened_file :
                            json.dump(menu_list,opened_file,indent=4)
                        print("Food Name has been successfully updated.")
                    
                    elif option == 2:
                        
                        while True:
                            new_foodPrice = input("Enter New Food Price : ")
                            if new_foodPrice.isdigit() and int(new_foodPrice) > 0:
                                new_foodPrice = int(new_foodPrice)
                                break
                            else:
                                print("\nEnter valid food price.")
                                
                        food["food_price"] = new_foodPrice
                        with open(food_store,"w") as opened_file :
                            json.dump(menu_list,opened_file,indent=4)
                        print("Food Price has been successfully updated.")

                        
                    elif option == 3:
                        new_foodCategory = " ".join(input("Enter New Food Category : ").title().strip().split())
                        food["food_category"] = new_foodCategory
                        with open(food_store,"w") as opened_file :
                            json.dump(menu_list,opened_file,indent=4)
                        print("Food Category has been successfully updated ! ")
                        
                
                    else:
                        print("Please Enter valid option !")
                        continue
                    # this "continue" matters a lot bcz if you dont mention this here
                    # flow will go ahead and execute upcoming below code 
                    
                    while True:
                        choice = input("Do you want to update anything else in this dish ? (yes/no) : ")
                            

                        if choice == "yes":
                            break

                        elif choice == "no":
                            return

                        else:
                            print("Please enter yes or no!")
                            continue 
                        # no need to write continue bcz there is no code 
                        # after this  else statement inside this "while loop".
                    
                    
        else:
            print("Invalid Food ID ! ")


def view_orders():
    with open(orders_store, "r") as opened_file:
        orders_list = json.load(opened_file)

    if len(orders_list) == 0:
        print("\n❌ No orders found!\n")
        return

    print("\n" + "🧾" * 21)
    print("         ADMIN - ORDER DASHBOARD")
    print("🧾" * 21 + "\n")

    for order in orders_list:

        print("┌" + "─" * 40 + "┐")
        print(f"  ORDER ID       : {order['Order_id']}")
        print(f"  TIME           : {order['Order_time']}")
        print(f"  TYPE           : {order['Order_type']}")
        print(f"  STATUS         : {order['Order_status']}")
        print(f"  PAYMENT        : {order['Payment_status']}")

        if order.get("Token_no"):
            print(f"  TOKEN NO       : {order['Token_no']}")
        else:
            print(f"  TABLE NO       : {order['Table_no']}")

        print("├" + "─" * 40 + "┤")
        print("  ITEMS ORDERED")
        print("├" + "─" * 40 + "┤")

        total_bill = 0

        print(f"  {'NAME':<15}{'QTY':<6}{'PRICE':<10}{'TOTAL'}")
        print("  " + "-" * 40)

        for item in order["Items"]:
            print(
                f"  {item['food_name']:<15}"
                f"{item['food_quantity']:<6}"
                f"{item['food_price']:<10}"
                f"{item['food_total']}"
            )
            total_bill += item["food_total"]

        print("  " + "-" * 40)
        print(f"  TOTAL BILL      : ₹{total_bill}")

        print("└" + "─" * 40 + "┘\n")


def delete_orders():
    while True:
        
        print("Do you want to delete single order, multiple orders or clear all orders ?")
        print("\n1. Single")
        print("2. Multiple")
        print("3. All clear")
        print("4. Back")
        
        option = int(input("Select an option : "))
        
        if option == 1:
            
            dish_id = None
            dish_name = None
            with open(orders_store, "r") as opened_file:
                orders_list = json.load(opened_file)
        
            while True:
              
                dish = input("Enter Your Food ID or Food Name : ")
                
                if dish.isdigit() and 100 < int(dish) <= len(orders_list)+100:
                    dish_id = int(dish)
                    break
                elif dish.replace(" ","").isalpha():
                    dish_name = " ".join(dish.title().strip().split())
                    break
                else:
                    print("\nEnter valid food id food name.")
                    
            with open(orders_store, "r") as opened_file:
                orders_list = json.load(opened_file)
            for order in orders_list:
                if order.get("Order_id") == dish_id or order.get("food_name") == dish_name :
                    orders_list.remove(order)
            with open(orders_store, "w") as opened_file:
                    json.dump(orders_list,opened_file,indent=4)
            print("Deleted successfully.")
            break
              
            
        elif option == 2:
            with open(orders_store, "r") as opened_file:
                orders_list = json.load(opened_file)
            for order in orders_list:
                if order.get("Payment_status") == "Paid":
                    orders_list.remove(order)
            with open(orders_store, "w") as opened_file:
                json.dump(orders_list,opened_file,indent=4)
            print("Deleted successfully.")
            break
          
            
        elif option == 3:
            with open(orders_store, "w") as opened_file:
                json.dump([],opened_file,indent=4)
            print("Deleted successfully.")    
            break
        
        elif option == 4:
            return 
               
        else:
            print("\nEnter valid number for option.")
 
        
def view_members():
    with open(users_store, "r") as opened_file:
        users_list = json.load(opened_file)
    role_name = input("Enter your preferred role that you wanna view.").capitalize().strip()
    role_name_count = 0

    print("\n╔═══════════════════════════════════════════════════════════════════════════════════╗")
    print("║ ID    FULL NAME           ADDRESS            PHONE         ROLE                   ║")
    print("╠═══════════════════════════════════════════════════════════════════════════════════╣")

    found = False

    for user in users_list:
        if user.get("Role") == role_name:

            found = True
            role_name_count += 1

            print(
                f"║ {user['User ID']:<5}"
                f"{user['Full Name']:<20}"
                f"{user['Address']:<19}"
                f"{user['Phone']:<14}"
                f"{user['Role']:<24}║"
            )

    if not found:
        print("║                           NO STAFF FOUND                                          ║")

    print("╚═══════════════════════════════════════════════════════════════════════════════════╝")

    print(f"\nTotal {role_name} : {role_name_count}")


def add_staff():
    with open(users_store, "r") as opened_file:
        users_list = json.load(opened_file)

    user_id = len(users_list) + 1

    while True:

        full_name = " ".join(
            input("\nEnter your full name : ").title().split()
        )

        if full_name.replace(" ", "").isalpha():
            break
        else:
            print("Enter valid name.")
            
    while True:
        age = int(input("\nEnter your age : "))
        if 18 <= age <= 100:
            break
        else:
            print("Enter valid age.")
            

    while True:
        gender = input("\nEnter your gender (male/female) : ").capitalize()

        if gender.isalpha() and (gender == "Male" or gender == "Female"):
            break
        else:
            print("Enter valid gender.")
            
            
   
    while True:

        username = input("\nEnter your Gmail : ").strip().lower()

        if username.endswith("@gmail.com") and len(username) > 10:

            found = False

            for user in users_list:

                if user["Username"] == username:
                    found = True
                    break

            if found:
                print("This Gmail is already registered.")

            else:
                break

        else:
            print("Please enter a valid Gmail address.")

    while True:

        password = maskpass.askpass(prompt="\nEnter your password : ", mask = "*")

        if 6 <= len(password) <= 15:
            break

        else:
            print("Password must contain 6 to 15 characters.")
            
            
            
    # while True:

    #     password5 = maskpass.askpass(
    #         prompt="Confirm your password : ",
    #         mask="*"
    #     )

    #     if not (6 <= len(password5) <= 15):
    #         print("Password must contain 6 to 15 characters.")
    #         continue

    #     if password5 != password:
    #         print("Passwords do not match. Please try again.")
    #         continue

    #     break
            
    while True:
        password5 = maskpass.askpass(prompt="\nConfirm your password : ", mask = "*")
        
        if 6 <= len(password5) <= 15:
            
            if password5 == password:
                break
            else:
                print("Passwords do not match. Please try again.")
                
        else:
            print("Password must contain 6 to 15 characters.")
            
            
    while True:

        address = " ".join(
            input("\nEnter your address : ").capitalize().strip().split()
        )

        if len(address) > 0:
            break

        else:
            print("Enter valid address.")

    while True:

        role = input("\nEnter your role  (Admin/Staff/Customer) : ").capitalize()
        
        if role.isalpha():
            break

        else:        
            print("Please enter Admin, Staff or Customer.")
                
        
            
    while True:

        phone = input("\nEnter your phone number : ")

        if (
            phone.isdigit()
            and len(phone) == 10
            and phone.startswith(("9", "8", "7", "6"))
        ):
            break

        else:
            print("Enter valid phone number.")

    user_dict = {
        "User ID": user_id,
        "Full Name": full_name,
        "Username": username,
        "Password": password,
        "Address": address,
        "Age" : age,
        "Role": role,
        "Gender" : gender,
        "Phone": phone
    }

    users_list.append(user_dict)

    with open(users_store, "w") as opened_file:
        json.dump(users_list, opened_file, indent=4)

    print("Account Created Successfully.")                 
             

def remove_staff():
    with open(users_store, "r") as opened_file:
        users_list = json.load(opened_file)  
    
    while True:

        username3 = input("Enter your Gmail : ").strip().lower()

        if username3.endswith("@gmail.com") and len(username3) > 10:
            break

        else:
            print("Please enter a valid email address.")
                     

                   
    for user in users_list:
        if user.get("Username") == username3 and user.get("Role") == "Staff":
            users_list.remove(user)
            with open(users_store, "w") as  opened_file:
               json.dump(users_list, opened_file, indent=4)
            print("Removed Successfully.")  
            break
    else:
        print("User not found.")
        

def view_sales_report():
    with open(orders_store, "r") as opened_file:
        orders_list = json.load(opened_file)

    now = datetime.now()
    present_date = now.strftime("%d-%m-%y")

    orders_count = 0
    total_revenue = 0
    paid_orders = 0
    unpaid_orders = 0
    dine_in_count = 0
    takeaway_count = 0
    total_items_sold = 0

    if len(orders_list) != 0:

        for order in orders_list:

            if order.get("Order_time").split()[0] == present_date:

                orders_count += 1

                if order.get("Order_type") == "Dine in":
                    dine_in_count += 1
                else:
                    takeaway_count += 1

                if order.get("Payment_status") == "Due":
                    unpaid_orders += 1
                else:
                    paid_orders += 1
                    
                    # Calculate revenue from paid orders only
                    for item in order["Items"]:
                        total_revenue += item["food_total"]

                # Count total quantity of items sold in all today's orders
                for item in order["Items"]:
                    total_items_sold += item["food_quantity"]

        if orders_count > 0:

            print("\n" + "🧾" * 40)
            print("🧾" * 40)
            print("\n        TODAY'S SALES REPORT\n")
            print("🧾" * 40)
            print("🧾" * 40)

            print(f"\nDate                : {present_date}")

            print("\n" + "-" * 40)
            print("ORDER SUMMARY")
            print("-" * 40)

            print(f"Total Orders        : {orders_count}")
            print(f"Dine In Orders      : {dine_in_count}")
            print(f"Take Away Orders    : {takeaway_count}")

            print("\n" + "-" * 40)
            print("PAYMENT SUMMARY")
            print("-" * 40)

            print(f"Paid Orders         : {paid_orders}")
            print(f"Unpaid Orders       : {unpaid_orders}")

            print("\n" + "-" * 40)
            print("SALES SUMMARY")
            print("-" * 40)

            print(f"Total Items Sold    : {total_items_sold}")
            print(f"Total Revenue       : ₹{total_revenue}")

            if paid_orders > 0:
                avg_order_value = total_revenue / paid_orders
                print(f"Average Order Value : ₹{avg_order_value:.2f}")
            else:
                print("Average Order Value : ₹0.00")

            print("\n" + "🧾" * 40)
            print("🧾" * 40 + "\n")

        else:
            print("No orders found for today.")

    else:
        print("Empty Order List!")  
                  
                
            
              
        