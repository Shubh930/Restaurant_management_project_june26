from modules import *
users_store = r"C:\Users\shubhendra singh\OneDrive\Desktop\python\SHUBHrestro\Database\users.json"


class Auth:
    
    def __init__(self):
        self.users_store = users_store

    # ================= CREATE ACCOUNT =====================
       
    def create_account(self):

        with open(users_store, "r") as opened_file:
            users_list = json.load(opened_file)

        user_id = len(users_list) + 1
        
        #Full Name
        while True:

            full_name = " ".join(
                input("\nEnter your full name : ").title().split()
            )

            if full_name.replace(" ", "").isalpha():
                break
            else:
                print("Enter valid name.")
        
        #Age       
        while True:
            age = int(input("\nEnter your age : "))
            if 18 <= age <= 100:
                break
            else:
                print("Enter valid age.")
                
        #Gender
        while True:
            gender = input("\nEnter your gender (male/female) : ").capitalize()

            if gender.isalpha() and gender in ["Male","Female"]:
                break
            else:
                print("Enter valid gender.")
                
                
    #Gmail
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
                print("Please enter a valid email address.")
                
                
        #Password
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
        
        
        #Confirm Password        
        while True:
            password5 = maskpass.askpass(prompt="\nConfirm your password : ", mask = "*")
            
            if 6 <= len(password5) <= 15:
                
                if password5 == password:
                    break
                else:
                    print("Passwords do not match. Please try again.")
                    
            else:
                print("Password must contain 6 to 15 characters.")
                
        
        #Address        
        while True:

            address = " ".join(
                input("\nEnter your address : ").capitalize().strip().split()
            )

            if len(address) > 0:
                break

            else:
                print("Enter valid address.")

        #Role
        while True:

            role = input("\nEnter your role  (Admin/Staff/Customer) : ").capitalize()
            
            if role.isalpha():
                break

            else:        
                print("Please enter Admin, Staff or Customer.")
                    
            
        #Phone Number        
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
        
        
        
    # ======================== SIGN IN ==============================

    def sign_in(self):

        with open(users_store, "r") as opened_file:
            users_list = json.load(opened_file)

        #Gmail
        while True:

            username2 = input("\nEnter your Gmail : ").strip().lower()

            if username2.endswith("@gmail.com") and len(username2) > 10:
                break

            else:
                print("Please enter a valid email address.")
                

        #Password
        while True:
            
            password2 = pwinput.pwinput(prompt = "\nEnter your password : ", mask = "*")

            if 6 <= len(password2) <= 15:
                break

            else:
                print("Password must contain 6 to 15 characters.")
                
        #Role       
        while True:

            role2 = input("\nEnter your role  (Admin/Staff/Customer) : ").capitalize()
            
            if role2.isalpha():
                break

            else:        
                print("Please enter Admin, Staff or Customer.")
                
        #Authentication
        for user in users_list:

            if (
                user["Username"] == username2
                and user["Password"] == password2
                and user["Role"] == role2
                
            ):
                print(f"\nWelcome {user["Full Name"]}")
                print("\nYou have successfully signed in.")
                return user

        print("Authentication unsuccessful. Please try again.")
        return None           