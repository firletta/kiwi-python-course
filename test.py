# Implement baby eye color calculator based on the colors of its father and the mother.
#
# Implement two functions:
# - get_baby_eye_color(str, str) -> str, that takes two colors (brown, green, blue)
#     and returns a baby color based on genetic ratio (string brown, green, blue)
#       brown + brown -> 75% brown, 18.75% green, 6.25% blue
#       green + brown -> 50% brown, 37.5% green, 12.5% blue
#       blue + brown -> 50% brown, 0% green, 50% blue
#       green + green ->  1% brown, 75% green, 24% blue
#       green + blue  ->  0% brown, 50% green, 50% blue
#       blue + blue  ->  0% brown, 1% green, 99% blue
# - measure_baby_eye_color_ratio(int, str, str) -> (float, float, float),
#     that takes a number of trials (n) and an eye color of father and a mother
#     does n experiments and count the outcomes. The function should verify that your
#     get_baby_eye_color function is returning the color with the proper distribution
#
#     e.g. for measure_baby_eye_color_ratio(1000, "brown", "brown")
#     the output should be close to (0.75, 0.1875, 0.0625)
#
# -- BONUS --
# Implement the same functionality, but extend it with a grandparents.
# Implement two functions:
# - get_grand_baby_eye_color(str, str, str, str) -> str
#     takes four color (of each grandparent) and return a color of their grandbaby
#     by the same rules as previously
# - measure_grand_baby_eye_color_ratio(int, str, str, str, str) -> (float, float, float)
#     that takes a number of trials (n) and 4 eye color of grandparents
#     and experimentally measures the new ratios
#     use it to discover the new ratios of the grandchildren eye color

import random

eye_colors = ["brown", "green", "blue"]

def get_baby_eye_color(father_eyes: str, mother_eyes: str) -> str:
    """
    :param father_eyes: str (one of "brown", "green", "blue")
    :param mother_eyes: str (one of "brown", "green", "blue")

    :return: str (one of "brown", "green", "blue")
    """

    if father_eyes == mother_eyes == "brown":
        baby_eyes = baby_eyes = random.choices(eye_colors, weights=(75, 18.75, 6.25), k=1)
    elif father_eyes == mother_eyes ==  "blue":
            baby_eyes = baby_eyes = random.choices(eye_colors, weights=(0, 1, 99), k=1)
    elif father_eyes == mother_eyes ==  "green":
        baby_eyes = baby_eyes = random.choices(eye_colors, weights=(1, 75, 24), k=1)
    elif father_eyes in ["green", "brown"] and mother_eyes in ["green", "brown"]:
        baby_eyes = baby_eyes = random.choices(eye_colors, weights=(50, 37.5, 12.5), k=1)
    elif father_eyes in ["blue", "brown"] and mother_eyes in ["blue", "brown"]:
        brownbaby_eyes = baby_eyes = random.choices(eye_colors, weights=(50, 0, 50), k=1)
    elif father_eyes in ["green", "blue"] and mother_eyes in ["green", "blue"]:
        baby_eyes = baby_eyes = random.choices(eye_colors, weights=(0, 50, 50), k=1)
    return baby_eyes

def measure_baby_eye_color_ratio(n: int, father_eyes: str, mother_eyes: str) -> (float, float, float):
    """

    :param n: int, number of experiments done
    :param father_eyes: str (one of "brown", "green", "blue")
    :param mother_eyes: str (one of "brown", "green", "blue")

    :return: (float, float, float), ratios of measured occurrence of colors
        representing the three colors (brown ratio, green ratio, blue ratio)
    """
    from collections import Counter
    occurance = Counter()
    for i in range(1,n):
        occurance.update(get_baby_eye_color(father_eyes, mother_eyes))
        occurance_numbers = ((occurance["brown"]/n),(occurance["green"]/n),(occurance["blue"]/n))
    return occurance_numbers

print(get_baby_eye_color("brown", "brown"))
print(measure_baby_eye_color_ratio(1000,"brown", "brown"))