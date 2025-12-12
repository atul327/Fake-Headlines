import random as rn

class HeadlineGenerator:
    def __pick(self, data):
        return rn.choice(data)

    def generate(self, title):
        name = self.__pick(self._name_list)
        work = self.__pick(self._work_list)
        obj = self.__pick(self._object_list)

        return f"{title}\n {name} {work} {obj}"


# for Funny
class FunnyHeadline(HeadlineGenerator): 
    def __init__(self):
        self._name_list = [
            "Atul tries to",
            "Nilesh goes to",
            "Darhak chases a"
        ]

        self._work_list = [
            "kick a football…",
            "buy milk and returns",
            "butterfly but"
        ]

        self._object_list = [
            "but kicks the air instead! 😂",
            "with a watermelon. 🤦‍♂️",
            "falls into a bush. 🌿😂"
        ]

# for Sport
class SportHeadline(HeadlineGenerator):
    def __init__(self):
        self._name_list = [
            "Atul smashes",
            "Nilesh wins",
            "Darhak trained",
            "Nagpur City",
            "Massive crowd"
        ]
        self._work_list = [
            "a powerful football shot",
            "the village cricket match",
            "for 2 hours nonstop",
            "FC signs a young rising player",
            "cheers as Atul scores"
        ]
        self._object_list = [
            "in Nagpur Stadium!",
            "with a last-ball six!",
            "in the evening heat.",
            "from the local league.",
            "back-to-back goals!"
        ]

# for Weather
class WeatherHeadline(HeadlineGenerator):
    def __init__(self):
        self._name_list = [
        "Nagpur",
        "Strong winds",
        "Sunny morning",
        "Temperature drops",
        "Extreme heat wave"
        ]

        self._work_list = [
            "to experience heavy rainfall",
            "expected in the evening;",
            "but chances of thunderstorms",
            "suddenly as winter",
            "continues;"
        ]

        self._object_list = [
            "tonight—alert issued.",
            "people advised to stay safe.",
            "after 4 PM.",
            "breeze hits the city.",
            "stay hydrated, says officials."
        ]
