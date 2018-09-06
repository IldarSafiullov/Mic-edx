list_of_animals = ["cat", "dog", "horse"]


def list_o_matic(string):
    if string == "":
        list_of_animals.pop()
        return list_of_animals
    elif string in list_of_animals:
        list_of_animals.remove(string)
        return list_of_animals
    else:
        list_of_animals.append(string)
        return list_of_animals

while list_of_animals:
    string = input("Eneter the animal, empty string or quit")
    if string == "quit":
        pass
    else:
        list_o_matic(string)
    print("The new list is: ", list_of_animals)
