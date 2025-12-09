from funny import FunnyHeadline, SportHeadline, WeatherHeadline

import history as hs

fn = FunnyHeadline()
sp = SportHeadline()
wt = WeatherHeadline()

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


