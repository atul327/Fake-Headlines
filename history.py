import json
from datetime import datetime

class History:
    def save_headline(self, category, data):
        __file_path = f"{category}.json"
        try:
            # coverting python daya to json string
            head_str = json.dumps(data, indent=4)

            with open(__file_path, "w")as f:
                f.write(head_str)
            print(f"Data saved to {__file_path}")
        except FileNotFoundError:
            print("File Not Found!")

    def get_data(self, category):
        __file_path = f"{category}.json"
        try:
            with open(__file_path, "r")as f:
                data = json.load(f)
            return "".join(data) if data else "No saved headlines."
        
        except FileNotFoundError:
            print("File Not Found.!")
            print("First save the headline")


class Userdata:
    def save_user_details(self, name, age, dob):
        __userfile = "userData.json"

        try:
            data = {
                "name" : name,
                "age" : age,
                "dob" : str(dob)
            }

            with open(__userfile, "w") as f:
                json.dump(data, f, indent=4)

        except FileNotFoundError:
            pass

# getting user details for the login credetials 
    def get_user_details(self):
        __userfile = "userData.json"
        try:
            with open(__userfile, "r") as f:
                data = json.load(f)
                stored_name = data.get("name")
                stored_dob  = data.get("dob")
                
                # returning data
                return stored_name, stored_dob 
        except FileNotFoundError:
            pass

    # getting the age for verification 
    def get_age(self):
        __userfile = "userData.json"

        try:
            with open(__userfile, "r") as f:
                data = json.load(f)
                age = data.get("age")

                return age

        except FileNotFoundError:
            pass
        
