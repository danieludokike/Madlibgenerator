# PYTHON MAD LIBS GENERATOR
def get_answers():
    inputs = []
    # Accepting user inputs
    noun = input("Choose a noun: ")
    inputs.append(noun)

    plural_noun = input("Choose a plural noun: ")
    inputs.append(plural_noun)

    noun2 = input("Choose a noun: ")
    inputs.append(noun2)

    place = input("Choose a place: ")
    inputs.append(place)

    adjective = input("Choose an adjective (Describe word): ")
    inputs.append(adjective)

    noun3 = input("Choose a noun: ")
    inputs.append(noun3)

    if check_input(inputs):
        return {
            "noun": noun,
            "plural_noun": plural_noun,
            "noun2": noun2,
            "place": place,
            "adjective": adjective,
            "noun3": noun3
        }
    return None


def check_input(input_val):
    # Checking if all values were provided
    for var in input_val:
        if var == "" or var is None:
            return False
        return True


def generate_mad_libs():
    return_val = get_answers()
    if return_val is None:
        print("Please fill out all inputs!")
        return
    counter = 1
    while counter < 11:
        print("------------------------------------------")
        print("Be kind to your", return_val["noun"], "- footed", return_val["plural_noun"])
        print("For a duck may be somebody's", return_val["noun2"], ",")
        print("Be kind to your", return_val["plural_noun"], "in", return_val["place"])
        print("Where the weather is always", return_val["adjective"], ".")
        print()
        print("You may think that is this the", return_val["noun3"], ",")
        print("Well it is.")
        print("------------------------------------------")

        counter += 1


if __name__ == "__main__":
    generate_mad_libs()
