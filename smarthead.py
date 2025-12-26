from history import History

hi = History()

class SmartHead():
    def contain_word(self):
        word = input("Enter word which you want in headline: ").lower()

        categories = ["Funny", "Sport", "Weather", "Random"]
        

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
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case _:
                    print("select valid filter (1 to 4)")

            more_filter = input("Do you want to apply another filter? (yes/no):").lower()

