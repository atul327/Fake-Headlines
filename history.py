import json


def save_headline(category, data):
    file_path = f"{category}.json"
    try:
        with open(file_path, "w")as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {file_path}")
    except FileNotFoundError:
        print("File Not Found!")

def load_data(category):
    file_path = f"{category}.json"
    try:
        with open(file_path, "r")as f:
           data = f.load(f)
        return data
    except FileNotFoundError:
        print("File Not Found!")
