import json
from history import History

hi = History()

class SmartHead():
    """def filehandle(self):
        categories = ["Funny", "Sport", "Weather"]
        for categorie in categories:
            try:
                with open(f"{categorie}.json", "r") as f:
                    return json.load(f), categorie
            except FileNotFoundError:
                print("File Not Found!")"""
    
    
    def contain_word(self):
        word = input("Enter word which you want in headline: ").lower()

        categories = ["Funny", "Sport", "Weather"]
        for categorie in categories:
            try:
                with open(f"{categorie}.json", "r") as f:
                    headlines = json.load(f)

                    # for headline in headlines:
                    if word in headlines.lower():
                        print(f"{categorie} : \n {headlines}")
                    else:
                        print(f"No {categorie} headline found from your search")
            except FileNotFoundError:
                print("File Not Found!")

    def start_word(self):
        word = input("Enter Starting word which you want in headline: ").lower()

        categories = ["Funny", "Sport", "Weather"]
        for categorie in categories:
            try:
                with open(f"{categorie}.json", "r") as f:
                    headlines = json.load(f)
                    headline = headlines.lower()
                    words = headline.split()
                    # print(len(words))


            except FileNotFoundError:
                print("File not found...!")

    def smart_head_generate(self):
        more_filter = "yes"
        while more_filter:
            print("\n\nChoose filter type:")
            print("1. Contains word")
            print("2. Starts with word")
            print("3. Ends with emoji")
            print("4. Length greater than N\n")
            choice =  int(input("Select your filter: "))

            match choice:
                case 1:
                    self.contain_word()
                case 2:
                    self.start_word()
                case 3:
                    pass
                case 4:
                    pass
                case _:
                    print("select valid filter (1 to 4)")

            more_filter = input("Do you want to apply another filter? (yes/no):").lower()

