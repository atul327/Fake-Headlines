import random as rn

sport_name = [
    "Atul smashes",
    "Nilesh wins",
    "Darhak trained",
    "Nagpur City",
    "Massive crowd"
]

weather_working = [
    "to experience heavy rainfall",
    "expected in the evening;",
    "but chances of thunderstorms",
    "suddenly as winter",
    "continues;"
]

funny_objects = [
    "but kicks the air instead! 😂",
    "with a watermelon. 🤦‍♂️",
    "falls into a bush. 🌿😂"
]

def generate_headline(name_list, work_list, object_list, title):
    # Yaha random choice hoga
    name = rn.choice(name_list)
    work = rn.choice(work_list)
    obj = rn.choice(object_list)

    # Final headline
    headline = f"{title}\n {name} {work} {obj}"
    return headline