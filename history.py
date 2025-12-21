import json

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


