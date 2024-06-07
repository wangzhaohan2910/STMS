from cmd import Cmd
from argparse import ArgumentParser

gData = None


class cApp(Cmd):
    prompt = "Command>"

    def do_EOF(self, line):
        """Exit the program."""
        return True


if __name__ == "__main__":
    hParser = ArgumentParser(description="The STMS.")
    hParser.add_argument("file", type=open)
    tSplited = map(
        lambda sLine: sLine.split(" "), hParser.parse_args().file.read().split("\n")
    )
    print("Welcome to the STMS.")
    cApp().cmdloop()
