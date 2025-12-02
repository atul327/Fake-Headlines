import funny as fn
import weather as wt
import sport as sp
import random_news as rw
import history as hs

def headline_generater(module, title, category_name):
    news = "yes"
    headline = ""

    while news == "yes":
        headline = module.generate_headline(
            module.name_list,
            module.work_list,
            module.object_list,
            title
        )
        print(headline)
        news = input("\nWant more headlines (Yes/No): ").lower().strip()

    save = input("You want to save this headline? (Yes/No): ").lower().strip()
    if save == "yes":
        hs.save_headline(category_name, headline)

while True:
    print("\n\nWhat type of news do you want?")
    print("1. Funny News")
    print("2. Sports News")
    print("3. Weather News")
    print("4. Random News")
    option = input("Enter your choice: ").strip()
    

    if option == "1":
        headline_generater(fn, "Funny Headlines 😂", "Funny")

    elif option == "2":
        headline_generater(sp, "Sports Headlines 🔥", "Sport")

    elif option == "3":
        headline_generater(wt, "Weather Headlines 🌦️", "Weather")

    elif option == "4":
        headline_generater(rw, "Random Headlines 🤞", "Random")

    else:
        print("\nPlease enter valid choice. Try again...!")

    


