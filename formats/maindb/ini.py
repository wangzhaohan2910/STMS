from configparser import ConfigParser


def dumper(filename, data):
    config = ConfigParser()
    config["teachers"] = {i: ",".join(list(j)) for i, j in data["teacher"].items()}
    config["pupils"] = {i: ",".join(list(j)) for i, j in data["pupil"].items()}
    with open(filename, "w") as file:
        config.write(file)
