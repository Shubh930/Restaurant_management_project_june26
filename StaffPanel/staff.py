from modules import *

def view_orders():
    try:
        
        with open(orders_store, "r") as opened_file:
            orders_list = json.load(opened_file)

        if len(orders_list) == 0:
            print("\n❌ No orders found!\n")
            return

        print("\n" + "🧾" * 21)
        print("         STAFF - ORDER DASHBOARD")
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
            
    except FileNotFoundError:
        print("Required file not found.")
        
    except json.JSONDecodeError:
        print("Data file is corrupted.")
        
    except KeyError as e:
        print(f"Missing key in data file : {e} ")
        
    except Exception as e:
        print(f"Unexpected error : {e}")
  
  
  
def search_order():
    
    try:
        
        print("1. Search By Order ID")
        print("2. Search By Token No")
        print("3. Search By Table No")

        option = int(input("\nSelect an option : "))

        with open(orders_store, "r") as opened_file:
            orders_list = json.load(opened_file)

        if len(orders_list) == 0:
            print("No orders found.")
            return

        if option == 1:
            search_id = input("\nEnter Order ID : ").strip().upper()

        elif option == 2:
            search_id = int(input("\nEnter Token No : "))

        elif option == 3:
            search_id = int(input("\nEnter Table No : "))

        else:
            print("Invalid option.")
            return

        for order in orders_list:

            found = False

            if option == 1 and order.get("Order_id") == search_id:
                found = True

            elif option == 2 and order.get("Token_no") == search_id:
                found = True

            elif option == 3 and order.get("Table_no") == search_id:
                found = True

            if found:

                print("\n" + "🧾" * 21)
                print("         STAFF - ORDER DASHBOARD")
                print("🧾" * 21 + "\n")

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

                return

        print("Order not found.")
    
    except FileNotFoundError:
        print("Required file not found.")
        
    except json.JSONDecodeError:
        print("Data file is corrupted.")
        
    except ValueError:
        print("Invalid input.Please enter correct data.")
        
    except KeyError as e:
        print(f"Missing key in data file : {e} ")
        
    except Exception as e:
        print(f"Unexpected error : {e}")    
    
                               
def View_due_payments():
    
    try:
        
        with open(orders_store, "r") as opened_file:
            orders_list = json.load(opened_file)
            
        for order in orders_list:
            if order["Payment_status"] == "Due":
                print("\n" + "🧾" * 21)
                print("         DUE ORDER DASHBOARD")
                print("🧾" * 21 + "\n")

            
                print("┌" + "─" * 40 + "┐")
                print(f"  ORDER ID       : {order['Order_id']}")
                print(f"  TIME           : {order['Order_time']}")
                print(f"  TYPE           : {order['Order_type']}")
                
                
                if order.get("Token_no"):
                    print(f"  TOKEN NO       : {order['Token_no']}")
                else:
                    print(f"  TABLE NO       : {order['Table_no']}")

                print("├" + "─" * 40 + "┤")
                print("  ITEMS ORDERED")
                print("├" + "─" * 40 + "┤")

                print(f"  {'NAME':<15}{'QTY':<6}{'PRICE':<10}{'TOTAL'}")
                print("  " + "-" * 40)

                for item in order["Items"]:
                    print(
                        f"  {item['food_name']:<15}"
                        f"{item['food_quantity']:<6}"
                        f"{item['food_price']:<10}"
                        f"{item['food_total']}"
                    )
                
                due_orders = 0 
                due_orders = due_orders + 1  
                print("  " + "-" * 40)
                print(f"  STATUS         : {order['Order_status']}")
                print(f"  PAYMENT        : {order['Payment_status']}")
                print(f"  DUE ORDERS        : {due_orders}")
                
                print("└" + "─" * 40 + "┘\n")
                
                return

                
        else:
            print("   All orders are paid.")
            
    except FileNotFoundError:
        print("Required file not found.")
        
    except json.JSONDecodeError:
        print("Data file is corrupted.")
        
    except KeyError as e:
        print(f"Missing key in data file : {e} ")
        
    except Exception as e:
        print(f"Unexpected error : {e}")
             
                
def view_active_tables():
    
    try:
        
        with open(tables_store, "r") as opened_file :
            tables_list = json.load(opened_file)
        
        for table in tables_list:
            if table["status"] == "Occupied":
                print("=" * 40)
                print("               TABLE INFO")
                print("=" * 40)
                
                print(f"  TABLE NO       : {table['table_number']}")
                print(f"  TABLE STATUS       : {table['status']}")
                
                print("=" * 40)
                
                return
            
        else:
            print("All table are available.")
            
    except FileNotFoundError:
        print("Required file not found.")
        
    except json.JSONDecodeError:
        print("Data file is corrupted.")
        
    except KeyError as e:
        print(f"Missing key in data file : {e} ")
        
    except Exception as e:
        print(f"Unexpected error : {e}")
       
