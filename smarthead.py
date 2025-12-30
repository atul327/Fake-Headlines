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
                    """
                    # BY INDEXING CAN BE SEARCH THE HEADLINE 
                    headline = headlines.lower()
                    words = headline.split()
                    # print(words)

                    for single_word in words:
                        if word == single_word:
                            word_index = words.index(word)
                            # print(word_index)
                            if words[word_index] == word:
                                print(headlines)
                            else:
                                print(f"So Sorry!!!\n I cannot find the headline from your search or Check you spelling & try again. \n Thank You!")
                    """

                    if word in headlines.lower():
                        print(f"{categorie} : \n {headlines}")
                    else:
                        print(f"So Sorry!!!\nNo {categorie} headline found from your search")
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
                    # print(words)

                    for single_word in words:
                        if word == single_word:
                            
                            # finding the index and compare the Input word with first word of headline
                            word_index = words.index(word)
                            if words[3] == word:
                                print(headlines)
                            else:
                                print(f"So Sorry!!!\n I cannot find the headline from your search or Check you spelling & try again. \n Thank You!")

            except FileNotFoundError:
                print("File not found...!")

        
    def end_with_emoji(self):
            emoji = input("Enter emoji which you want at the last: ")

            categories = ["Funny", "Sport", "Weather"]
            for categorie in categories:
                try:
                    with open(f"{categorie}.json", "r") as f:
                        headlines = json.load(f)
                        word = headlines.split()
                        
                        word_index = len(word) - 1
                        if word[word_index] == emoji:
                            print(headlines)
                            return

                except FileNotFoundError:
                    print(" Sorry!!\n File Not Found!")

            print(f"So Sorry!!!\n I cannot find the headline from your search, try again. \n Thank You!")


    def smart_head_generate(self):
        more_filter = "yes"
        while more_filter:
            print("\n\nChoose filter type:")
            print("1. Contains word")
            print("2. Starts with word")
            print("3. Ends with emoji")
            print("4. Length greater than N\n")
            try:
                choice =  int(input("Select your filter: "))

                match choice:
                    case 1:
                        self.contain_word()
                    case 2:
                        self.start_word()
                    case 3:
                        self.end_with_emoji()
                    case 4:
                        print("(Length greater)\n Feature in developing process...")
                    case _:
                        print("select valid filter (1 to 4)")
            except ValueError:
                print("Enter choice in digit only..\n")

        more_filter = input("Do you want to apply another filter? (yes/no):").lower()

# if __name__ == "__main__":
#     app = SmartHead()
#     app.smart_head_generate()