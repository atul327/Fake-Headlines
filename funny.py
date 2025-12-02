import random as rn

# for Funny 
funny_name = [
    "Atul tries to",
    "Nilesh goes to",
    "Darhak chases a"
]

funny_working = [
    "kick a football…",
    "buy milk and returns",
    "butterfly but"
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
