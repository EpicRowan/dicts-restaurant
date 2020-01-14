
def reading_rating(opened_file):
    """Ranks the resturant scores in alphabetical order"""

    opened_file = open("scores.txt")

    resturant_rate = {}

    for line in opened_file:
        restaurant_name = opened_file[:-1]
        rating = opened_file[-1:]
        resturant_rate[restaurant_name] = rating

    return resturant_rate


    ###repl.it test code


def reading_rating(opened_file):
    """Ranks the resturant scores in alphabetical order"""

    opened_file = open("scores.txt")

    # resturant_rate = {}

    for line in opened_file:
        line = line.rstrip()
        # # line = line.split(" ")
        line = line.split(":")
        # print(line)
        for item in line:
            

        restaurant_name = line[:-1]
        rating = line[-1:]
        # print(restaurant_name)
        # print(rating)

        # resturant_rate[restaurant_name] = rating

        # resturant_rate= (sorted(resturant_rate.items()))
        # print("{} is rated at a {}".format(restaurant_name, rating))
    # return resturant_rate.keys()
(reading_rating("scores.txt"))