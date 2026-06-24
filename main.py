from modules import *
from auth import Auth
auth = Auth()
from AdminPanel import admin
from CustomerPanel import customer
from StaffPanel import staff

print("=" * 40)
print("          THE SHUBH RESTAURANT")
print("=" * 40)

print("=" * 40)
print("    Welcome to Food Ordering System")
print("=" * 40)

while True:

    print("\nWho would you like to proceed as?")
    print("1. Administrator")
    print("2. Customer")
    print("3. Staff")
    print("4. Exit")

    role = input("\nSelect an option : ")
    
    if not role.isdigit():
        print("Invalid Input")
        continue


    role = int(role)

    # ================= ADMIN =================

    if role == 1:
        
        while True:
            
            print("\nADMIN AUTHENTICATION")
            print("1. Sign In")
            print("2. Back")
        
            choice2 = input("\nSelect an option : ")
            
            if choice2.isdigit():
                choice2 = int(choice2)
                
                if choice2 == 1:
                    
                    
                    while True:
                        try:
                            logged_user = auth.sign_in()
                        except Exception as e:
                            print(f"Authentication Error : {e}")
                            continue
                        else:
                            print("Login successful!")
                            break

                    if logged_user and logged_user["Role"] == "Admin":
                    
                        while True:

                            print("\nWelcome To Admin Panel")
                            print("\n1. View Menu")
                            print("2. Add Food Item")
                            print("3. Update Food Item")
                            print("4. Delete Food Item")
                            print("5. View Orders")
                            print("6. Delete Orders")
                            print("7. View Members")
                            print("8. Add staff")
                            print("9. Remove staff")
                            print("10. View Sales Report")
                            print("11. Exit")

                            choice = input("\nSelect the service you want : ")

                            if choice.isdigit():

                                choice = int(choice)

                                if choice == 1:
                                    admin.view_menu()

                                elif choice == 2:
                                    admin.add_food()

                                elif choice == 3:
                                    admin.update_food()

                                elif choice == 4:
                                    admin.delete_food()
                                    
                                elif choice == 5:
                                    admin.view_orders()
                                
                                elif choice == 6:
                                    admin.delete_orders()
                                    
                                elif choice == 7:
                                    admin.view_members()

                                elif choice == 8:
                                    admin.add_staff()
                                    
                                elif choice == 9:
                                    admin.remove_staff()
                                    
                                elif choice == 10:
                                    admin.view_sales_report()
                                
                                elif choice == 11:
                                    print("Exited successfully")
                                    break
                                
                                else:
                                    print("You selected invalid service")
                                    
                            else:
                                print("You selected invalid service")
            
                    
                elif choice2 == 2:
                    break
                
                else:
                    print("\nSelect correct option.")
                    
            else:
                print("\nSelect correct option.")
              
                
            
       

    # ================= CUSTOMER =================       

    elif role == 2:
        
        while True:

            print("\nCUSTOMER AUTHENTICATION")
            print("1. Sign In")
            print("2. Create Account")
            print("3. Back")
        
            choice2 = input("\nSelect an option : ")
            
            if choice2.isdigit():
                choice2 = int(choice2)
                
                if choice2 == 1:
                    
                    while True:
                        try:
                            logged_user = auth.sign_in()
                        except Exception as e:
                            print(f"Authentication Error : {e}")
                            continue
                        else:
                            print("Login successful!")
                            break

                    if logged_user and logged_user["Role"] == "Customer":

                        while True:

                            print("\nWelcome To Customer Panel")
                            print("\n1. View Menu")
                            print("2. Add To Cart")
                            print("3. View Cart")
                            print("4. Update Cart")
                            print("5. Place Order")
                            print("6. Generate Bill & Pay")
                            print("7. Exit")
                            

                            choice = input("\nSelect the service you want : ")

                            if choice.isdigit():

                                choice = int(choice)

                                if choice == 1:
                                    customer.view_menu()

                                elif choice == 2:
                                    customer.addto_cart()

                                elif choice == 3:
                                    customer.view_cart()

                                elif choice == 4:
                                    customer.update_cart()
                                    
                                elif choice == 5:
                                    customer.place_order()
                                    
                                elif choice == 6:
                                    customer.generateBill_npay()

                                elif choice == 7:
                                    print("Exited successfully")
                                    break

                                else:
                                    print("You selected invalid service.")

                            else:
                                print("You selected invalid service.")
                            
                elif choice2 == 2:
                    
                    while True:
                        try:
                            auth.create_account()
                            print("Account has been created successfully.")
                        except FileNotFoundError:
                            print("Users file not found.")
                        except json.JSONDecodeError:
                            print("Users file contains invalid data.")
                        except Exception as e:
                            print(f"Error : {e}")
                            break
                    
                elif choice2 == 3:
                    break
                
                else:
                    print("\nSelect correct option.")
                    
            else:
                print("\nSelect correct option.")

        
                            
    
    # ================= STAFF =================
    
    elif role == 3:
        
         while True:
            
            print("\nSTAFF AUTHENTICATION")
            print("1. Sign In")
            print("2. Back")
        
            choice2 = input("\nSelect an option : ")
            
            if choice2.isdigit():
                choice2 = int(choice2)
                
                if choice2 == 1:
                    
                    
                    while True:
                        try:
                            logged_user = auth.sign_in()
                            print("Login successful!")
                            break
                        except Exception as e:
                            print(f"Authentication Error : {e}")
                            continue
                            

                    if logged_user and logged_user["Role"] == "Staff":
        
                        while True:

                            print("\nWelcome To Staff Panel")
                            print("\n1. View Orders")
                            print("2. Search Orders")
                            print("3. View Due Payments")
                            print("4. View Active Tables")
                            print("5. Exit")
                            
                            choice = input("\nSelect the service you want : ")
                            
                            if not choice.isdigit():
                                print("You selected invalid Service.")
                                continue

                            choice = int(choice)

                            if choice == 1:
                                staff.view_orders()

                            elif choice == 2:
                                staff.search_order()

                            elif choice == 3:
                                staff.View_due_payments()

                            elif choice == 4:
                                staff.view_active_tables()

                            elif choice == 5:
                                print("Exited successfully")
                                break

                            else:
                                print("You selected invalid service")
                            
                elif choice2 == 2:
                    break
                            
                else:
                    print("\nSelect correct option.")
                    
            else:
                print("\nSelect correct option.")
                
                
    # ================= EXIT =================
    
    elif role == 4:
        print("\nThank You For Visiting Us !\n")
        break
    
    else:
        print("Invalid Option")
            

    


        
 