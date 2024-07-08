from cmd import Cmd


class Student:
    __Name = ""

    def GetName(self):
        return self.__Name

    def SetName(self, Name):
        self.__Name = Name


class Teacher(Student):
    __Students = {}

    def AddStudents(self, *Students):
        for EachStudent in Students:
            self.__Students.add(EachStudent)
