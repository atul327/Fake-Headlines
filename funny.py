import random as rn
from headline_base import HeadLineBase

class HeadlineGenerator:
    def __pick(self, data):
        try:
            return rn.choice(data)
        except IndexError:
            print("List not found!")

    def generate(self, title):
        name = self.__pick(self._name_list)
        work = self.__pick(self._work_list)
        obj = self.__pick(self._object_list)

        # Adding extra headline generate with temperature 
        temperature = self.__pick(self._temp_list)

        return f"{title}\n {name} {work} {obj}"


# for Funny
class FunnyHeadline(HeadlineGenerator, HeadLineBase): 
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
class SportHeadline(HeadlineGenerator, HeadLineBase):
    def __init__(self):
        self._name_list = [
            "Atul smashes",
            "Nilesh wins",
            "Darshak trained",
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
class WeatherHeadline(HeadlineGenerator, HeadLineBase):
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

        self._temperature = {
            (-50, -1): "Freezing cold conditions expected",
            (0, 5): "Severe cold weather today",
            (6, 10): "Cold weather likely",
            (11, 15): "Cool and breezy weather",
            (16, 20): "Mild and comfortable weather",
            (21, 25): "Pleasant weather conditions",
            (26, 30): "Warm weather expected",
            (31, 35): "Hot summer conditions",
            (36, 40): "Heatwave conditions expected",
            (41, 45): "Severe heat alert issued",
            (46, 60): "Extreme heat emergency warning"
        }

# just for testing try Except block
class RandomHeadline(HeadlineGenerator, HeadLineBase):
    def __init__(self):
        self._name_list = [

        ]

        self._work_list = [

        ]

        self._object_list = [

        ]