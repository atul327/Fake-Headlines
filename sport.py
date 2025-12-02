import random as rn

sport_name = [
    "Atul smashes",
    "Nilesh wins",
    "Darhak trained",
    "Nagpur City",
    "Massive crowd"
]
sport_working = [
    "a powerful football shot",
    "the village cricket match",
    "for 2 hours nonstop",
    "FC signs a young rising player",
    "cheers as Atul scores"
]
sport_objects = [
    "in Nagpur Stadium!",
    "with a last-ball six!",
    "in the evening heat.",
    "from the local league.",
    "back-to-back goals!"
]

def generate_headline(name_list, work_list, object_list, title):
    # Yaha random choice hoga
    name = rn.choice(name_list)
    work = rn.choice(work_list)
    obj = rn.choice(object_list)

    # Final headline
    headline = f"{title}\n {name} {work} {obj}"
    return headline