import funny as fn
import weather as wt
import sport as sp
import random_news as rw
import history as hs

while True:
    print("\n\nWhat type of news do you want?")
    print("1. Funny News")
    print("2. Sports News")
    print("3. Weather News")
    print("4. Random News")
    option = input("Enter your choice: ").strip()
    
    if option == "1":
        news = "yes"
        while(news=="yes"):
            headline = fn.generate_headline(fn.funny_name, fn.funny_working, fn.funny_objects, "Funny Headlines😂",)
            print(headline)
            news = input("\nWant more headlines (Yes/No): ").lower().strip() 

            if news == "no":
                break
        
        save = input("You want to save this headline? (Yes/No): ").lower().strip()
        if save == "yes":
            hs.save_headline("Funny", headline)

        print("Good day!")
    elif option == "2":
        news = "yes"
        while(news=="yes"):
            headline = (sp.generate_headline(sp.sport_name, sp.sport_working, sp.sport_objects, "Sports Headlines🔥"))
            print(headline)
            news = input("\nWant more headlines (Yes/No): ").lower().strip() 
           
            if news == "no":
                break

        save = input("You want to save this headline? (Yes/No): ").lower().strip()
        if save == "yes":
            hs.save_headline("Sport", headline)
    
    elif option == "3":
        news = "yes"
        while(news=="yes"):
            headline = (wt.generate_headline(wt.weather_name, wt.weather_working, wt.weather_objects, "Weather Headlines🌦️"))
            print(headline)
            news = input("\nWant more headlines (Yes/No): ").lower().strip() 
            
            if news == "no":
                break

        save = input("You want to save this headline? (Yes/No): ").lower().strip()
        if save == "yes":
            hs.save_headline("Weather", headline)

    elif option == "4":
        news = "yes"
        while(news=="yes"):
            headline = (rw.generate_headline(sp.sport_name, wt.weather_working, fn.funny_objects, "Random Headlines🤞"))
            print(headline)
            news = input("\nWant more headlines (Yes/No): ").lower().strip() 
            
            if news == "no":
                break
        
        save = input("You want to save this headline? (Yes/No): ").lower().strip()
        if save == "yes":
            hs.save_headline("Random", headline)

    else:
        print("\n\nPlease enter valid choice. Try again...!")
    


