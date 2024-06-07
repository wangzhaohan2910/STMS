from cmd import Cmd
from argparse import ArgumentParser


class cApp(Cmd):
    prompt = "Command(? for help)>"

    def do_EOF(self, line):
        """Exit the program."""
        return True


if __name__ == "__main__":
    hParser = ArgumentParser(description="The STMS.")
    hParser.add_argument("file", type=open)
    print("Welcome to the STMS.")
    cApp().cmdloop()
