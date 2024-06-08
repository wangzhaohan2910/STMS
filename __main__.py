from cmd import Cmd
from argparse import ArgumentParser

gData = {}


class cApp(Cmd):
    prompt = "Command>"

    def do_EOF(self, line):
        """Exit the program."""
        return True


if __name__ == "__main__":
    hParser = ArgumentParser(description="The STMS.")
    hParser.add_argument("file", type=open)
    for lPair in map(
        lambda sLine: sLine.split(" "), hParser.parse_args().file.read().split("\n")
    ):
        if len(lPair) > 1:
            sTeacherName = lPair[0]
            sStudentName = lPair[1]
            try:
                gData[sTeacherName].add(sStudentName)
            except:
                gData[sTeacherName] = {sStudentName}
    print("Welcome to the STMS.")
    cApp().cmdloop()
