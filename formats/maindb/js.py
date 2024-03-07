import json
from copy import deepcopy


def loader(filename):
    fileread = json.loads(open(filename, "r").read())
    for i in fileread["teacher"].keys():
        fileread["teacher"][i] = set(fileread["teacher"][i])
    for i in fileread["pupil"].keys():
        fileread["pupil"][i] = set(fileread["pupil"][i])
    return fileread


def dumper(filename, data):
    datum = deepcopy(data)
    for i in datum["teacher"].keys():
        datum["teacher"][i] = list(datum["teacher"][i])
    for i in datum["pupil"].keys():
        datum["pupil"][i] = list(datum["pupil"][i])
    with open(filename, "w") as file:
        file.write(json.dumps(datum, indent=4))


if __name__ == "__main__":
    from pprint import pprint

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
    dumper("data.json", data)
    data2 = loader("data.json")
    print("\n\nData before changes:\n")
    pprint(data)
    print("\n\nData after loading and printing:\n")
    pprint(data2)
    print("\n\nData uncorrupted:\n")
    print(data == data2)
