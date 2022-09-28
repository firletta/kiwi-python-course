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
from collections import Counter

eye_colors = ["brown", "green", "blue"]

def get_baby_eye_color(father_eyes: str, mother_eyes: str) -> str:
    """
    :param father_eyes: str (one of "brown", "green", "blue")
    :param mother_eyes: str (one of "brown", "green", "blue")

    :return: str (one of "brown", "green", "blue")
    """
    global baby_eyes
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

<<<<<<< HEAD
=======
# TODO random.choices(num_list)
# https://www.geeksforgeeks.org/choose-elements-from-list-with-different-probability-in-python/


>>>>>>> 0267a0e89d7ad174fad235cacd5f117841e87a9d
def measure_baby_eye_color_ratio(n: int, father_eyes: str, mother_eyes: str) -> (float, float, float):
    """

    :param n: int, number of experiments done
    :param father_eyes: str (one of "brown", "green", "blue")
    :param mother_eyes: str (one of "brown", "green", "blue")

    :return: (float, float, float), ratios of measured occurrence of colors
        representing the three colors (brown ratio, green ratio, blue ratio)
    """

    occurance = Counter()
    for i in range(1,n):
        occurance.update(get_baby_eye_color(father_eyes, mother_eyes))
        occurance_numbers = ((occurance["brown"]/n),(occurance["green"]/n),(occurance["blue"]/n))
    return occurance_numbers

# -- BONUS --
def get_grand_baby_eye_color(
        grandfather_father_eyes: str,
        grandmother_father_eyes: str,
        grandfather_mother_eyes: str,
        grandmother_mother_eyes: str,
) -> str:
    """

    :param grandfather_father_eyes: str (one of "brown", "green", "blue")
    :param grandmother_father_eyes: str (one of "brown", "green", "blue")
    :param grandfather_mother_eyes: str (one of "brown", "green", "blue")
    :param grandmother_mother_eyes: str (one of "brown", "green", "blue")

    :return: str (one of "brown", "green", "blue")
    """
    father_eyes = get_baby_eye_color(grandfather_father_eyes, grandmother_father_eyes)
    mother_eyes = get_baby_eye_color(grandfather_mother_eyes, grandmother_mother_eyes)
    grandbaby_eyes = get_baby_eye_color(father_eyes, mother_eyes)

    return grandbaby_eyes


def measure_grand_baby_eye_color_ratio(
        n: int,
        grandfather_father_eyes: str,
        grandmother_father_eyes: str,
        grandfather_mother_eyes: str,
        grandmother_mother_eyes: str
) -> (float, float, float):
    """

    :param n: int, number of experiments done
    :param grandfather_father_eyes: str (one of "brown", "green", "blue")
    :param grandmother_father_eyes: str (one of "brown", "green", "blue")
    :param grandfather_mother_eyes: str (one of "brown", "green", "blue")
    :param grandmother_mother_eyes: str (one of "brown", "green", "blue")

    :return: (float, float, float), ratios of measured occurrence of colors
        representing the three colors (brown ratio, green ratio, blue ratio)
    """
    occurance = Counter()
    for i in range(1,n):
        occurance.update(get_grand_baby_eye_color(grandfather_father_eyes, grandmother_father_eyes, grandfather_mother_eyes, grandmother_mother_eyes))
    occurance_numbers = ((occurance["brown"]/n),(occurance["green"]/n),(occurance["blue"]/n))

    return occurance_numbers


father_eyes = input("Father eye color [brown, green, blue]: ")
mother_eyes = input("Mother eye color [brown, green, blue]: ")

print("Baby eyes color -", get_baby_eye_color(father_eyes, mother_eyes))
ratio = measure_baby_eye_color_ratio(1000, father_eyes, mother_eyes)
print("Measured ratio")
print(" - brown:", ratio[0])
print(" - green:", ratio[1])
print(" - blue:", ratio[2])

# -- BONUS --
grandfather_father_eyes = input("Grandfather from father eye color [brown, green, blue]: ")
grandmother_father_eyes = input("Grandmother from father eye color [brown, green, blue]: ")
grandfather_mother_eyes = input("Grandfather from mother eye color [brown, green, blue]: ")
grandmother_mother_eyes = input("Grandmother from mother eye color [brown, green, blue]: ")

print("Baby eyes color -", get_grand_baby_eye_color(
    grandfather_father_eyes,
    grandmother_father_eyes,
    grandfather_mother_eyes,
    grandmother_mother_eyes
))

ratio = measure_grand_baby_eye_color_ratio(1000, grandfather_father_eyes, grandmother_father_eyes, grandfather_mother_eyes, grandmother_mother_eyes)
print("Measured ratio")
print(" - brown:", ratio[0])
print(" - green:", ratio[1])
print(" - blue:", ratio[2])