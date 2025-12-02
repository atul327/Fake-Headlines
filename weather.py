import random as rn

weather_name = [
    "Nagpur",
    "Strong winds",
    "Sunny morning",
    "Temperature drops",
    "Extreme heat wave"
]

weather_working = [
    "to experience heavy rainfall",
    "expected in the evening;",
    "but chances of thunderstorms",
    "suddenly as winter",
    "continues;"
]

weather_objects = [
    "tonight—alert issued.",
    "people advised to stay safe.",
    "after 4 PM.",
    "breeze hits the city.",
    "stay hydrated, says officials."
]

def generate_headline(name_list, work_list, object_list, title):
    # Yaha random choice hoga
    name = rn.choice(name_list)
    work = rn.choice(work_list)
    obj = rn.choice(object_list)

    # Final headline
    headline = f"{title}\n {name} {work} {obj}"
    return headline