from cmd import Cmd
from argparse import ArgumentParser


class cApp(Cmd):
    prompt = "Command>"


if __name__ == "__main__":
    hParser = ArgumentParser(description="The STMS.")
    hParser.add_argument("file")
    hParser.add_argument("-s", "--script", type=open)
    print(hParser.parse_args())
