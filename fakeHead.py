from funny import FunnyHeadline, SportHeadline, WeatherHeadline

from history import History

fn = FunnyHeadline()
sp = SportHeadline()
wt = WeatherHeadline()
hs = History()

class FakeHead:
    def headline_generater(self, module, title, category_name):
        news = "yes"
        headline = ""

        while news == "yes":
            headline = module.generate(title)
            print(headline)
            news = input("\nWant more headlines (Yes/No): ").lower().strip()

        save = input("You want to save this headline? (Yes/No): ").lower().strip()
        if save == "yes":
            hs.save_headline(category_name, headline)

        saved_head = input("Want to read saved headline? (yes/no):").lower().strip()
        if saved_head == "yes" or saved_head == "y":
            print(hs.get_data(category_name))

    def showmenu(self):
        while True:
            print("\n\nWhat type of news do you want?")
            print("1. Funny News")
            print("2. Sports News")
            print("3. Weather News")
            option = input("Enter your choice: ").strip()
            

            if option == "1":
                self.headline_generater(fn, "Funny Headlines 😂", "Funny")

            elif option == "2":
                self.headline_generater(sp, "Sports Headlines 🔥", "Sport")

            elif option == "3":
                self.headline_generater(wt, "Weather Headlines 🌦️", "Weather")

            else:
                print("\nPlease enter valid choice. Try again...!")

fk = FakeHead()

fk.showmenu()


