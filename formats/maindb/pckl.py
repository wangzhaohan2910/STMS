import pickle


def loader(filename):
    fileread = ""
    with open(filename, "rb") as file:
        fileread = file.read()
    return pickle.loads(fileread)


def dumper(filename, data):
    with open(filename, "wb") as file:
        file.write(pickle.dumps(data))


if __name__ == "__main__":
    from pprint import pprint
    from copy import deepcopy

    data = {
        "teacher": {
            "tea1": {"pup1", "pup2", "pup3"},
            "tea2": {"pup2", "pup3", "pup4"},
            "tea3": {"pup3", "pup4", "pup5"},
            "tea4": {"pup4", "pup5"},
            "tea5": {"pup1", "pup2"},
        },
        "pupil": {
            "pup1": {"tea1", "tea5"},
            "pup2": {"tea1", "tea2", "tea5"},
            "pup3": {"tea1", "tea2", "tea3"},
            "pup4": {"tea2", "tea3", "tea4"},
            "pup5": {"tea3", "tea4"},
        },
    }
    data2 = deepcopy(data)
    dumper("data.pckl", data2)
    print("data==data2 after dump?", data == data2)
    data2 = loader("data.pckl")
    print("data==data2 after load?", data == data2)
