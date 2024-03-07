from configparser import ConfigParser


def loader(filename):
    from pprint import pprint

    config = ConfigParser()
    config.read(filename)
    data = {"teacher": dict(config["teachers"]), "pupil": dict(config["pupils"])}
    for i in data["teacher"].keys():
        data["teacher"][i] = set(data["teacher"][i].split(","))
    for i in data["pupil"].keys():
        data["pupil"][i] = set(data["pupil"][i].split(","))
    return data


def dumper(filename, data):
    config = ConfigParser()
    config["teachers"] = {i: ",".join(list(j)) for i, j in data["teacher"].items()}
    config["pupils"] = {i: ",".join(list(j)) for i, j in data["pupil"].items()}
    with open(filename, "w") as file:
        config.write(file)


if __name__ == "__main__":
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
    dumper("test.ini", data2)
    print("data==data2 after dump?", data == data2)
    data2 = loader("test.ini")
    print("data==data2 after load?", data == data2)
