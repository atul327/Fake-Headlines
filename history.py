def save_headline(category, text):
    file_path = f"{category}.txt"
    try:
        with open(file_path, "a", encoding = "utf-8") as f:
            f.write(text + "\n")
        print("Headline is saved.")
    except FileNotFoundError:
        print("File in not found")

