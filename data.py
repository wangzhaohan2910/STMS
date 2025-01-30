from log import log
from pickle import dump, load
from pprint import pformat


class Teacher:
    iId = 0
    sName = ""
    setStudent = set()

    def __init__(self, sName="", setStudent=set()):
        log("Teacher init")
        self.sName = sName
        self.setStudent = setStudent


class Database:
    sFileName = ""
    STU = [""]
    TCH = [Teacher()]

    def postStudent(self, sName, *lTeacher):
        log("PostStudent sName: " + sName + " lTeacher: " + pformat(lTeacher))
        self.STU.append(sName)
        for i in lTeacher:
            self.TCH[i].setStudent.add(len(self.STU) - 1)
        return len(self.STU) - 1

    def putStudentTeacher(self, iId, *lTeacher):
        log("PutStudentTeacher iId: " + str(iId) + " lTeacher: " + pformat(lTeacher))
        for i in self.TCH:
            if i.iId not in lTeacher:
                i.setStudent.discard(iId)
            else:
                i.setStudent.add(iId)
        return True

    def putStudentName(self, iId, sName):
        log("PutStudentName iId: " + str(iId) + " sName: " + sName)
        self.STU[iId] = sName
        return True

    def putStudent(self, iId, sName, *lTeacher):
        log(
            "PutStudent iId: "
            + str(iId)
            + " sName: "
            + sName
            + " lTeacher: "
            + pformat(lTeacher)
        )
        return self.putStudentName(iId, sName) and self.putStudentTeacher(
            iId, *lTeacher
        )

    def deleteStudent(self, iId):
        log("DeleteStudent iId: " + str(iId))
        self.STU[iId] = ""
        for i in self.TCH:
            i.setStudent.discard(iId)
        while self.STU[-1] == "" and len(self.STU) > 1:
            self.STU.pop()
        return True

    def deleteAllStudent(self):
        log("DeleteAllStudent")
        for i in self.TCH:
            i.setStudent.clear()
        self.STU = [""]
        return True

    def getStudentCount(self):
        log("GetStudentCount")
        return len(self.STU) - 1

    def getStudentName(self, iId):
        log("GetStudentName iId: " + str(iId))
        return self.STU[iId]

    def getStudentTeacher(self, iId):
        log("GetStudentTeacher iId: " + str(iId))
        setResult = {i.iId for i in self.TCH if iId in i.setStudent}
        return setResult

    def getAllStudentName(self):
        log("GetAllStudentName")
        return self.STU

    def getAllStudentTeacher(self):
        log("GetAllStudentTeacher")
        dResult = {}
        for i in self.TCH:
            for j in i.setStudent:
                if j not in dResult:
                    dResult[j] = {i.iId}
                else:
                    dResult[j].add(i.iId)
        return dResult

    def postTeacher(self, sName, *lStudent):
        log("PostTeacher sName: " + sName + " lStudent: " + pformat(lStudent))
        self.TCH.append(Teacher())
        self.TCH[-1].iId = len(self.TCH) - 1
        self.TCH[-1].sName = sName
        self.TCH[-1].setStudent = set(lStudent)
        return len(self.TCH) - 1

    def putTeacherName(self, iId, sName):
        log("PutTeacherName iId: " + str(iId) + " sName: " + sName)
        self.TCH[iId].sName = sName
        return True

    def putTeacherStudent(self, iId, *lStudent):
        log("PutTeacherStudent iId: " + str(iId) + " lStudent: " + pformat(lStudent))
        self.TCH[iId].setStudent = set(lStudent)
        return True

    def putTeacher(self, iId, sName, *lStudent):
        return self.putTeacherName(iId, sName) and self.putTeacherStudent(
            iId, *lStudent
        )

    def deleteTeacher(self, iId):
        log("DeleteTeacher iId: " + str(iId))
        self.TCH[iId].sName = ""
        self.TCH[iId].setStudent.clear()
        while self.TCH[-1].sName == "" and len(self.TCH) > 1:
            self.TCH.pop()
        return True

    def deleteAllTeacher(self):
        log("DeleteAllTeacher")
        self.TCH = [Teacher()]
        return True

    def getTeacherCount(self):
        log("GetTeacherCount")
        return len(self.TCH) - 1

    def getTeacherName(self, iId):
        log("GetTeacherName iId: " + str(iId))
        return self.TCH[iId].sName

    def getTeacherStudent(self, iId):
        log("GetTeacherStudent iId: " + str(iId))
        return self.TCH[iId].setStudent

    def getAllTeacherName(self):
        log("GetAllTeacherName")
        return {i.sName for i in self.TCH}

    def getAllTeacherStudent(self):
        log("GetAllTeacherStudent")
        return {i.iId: i.setStudent for i in self.TCH}

    def put(self, STU, TCH):
        log("Put STU: " + pformat(STU) + " TCH: " + pformat(TCH))
        self.STU = STU
        self.TCH = TCH
        return True

    def delete(self):
        log("Delete")
        return self.deleteAllStudent() and self.deleteAllTeacher()

    def get(self):
        log("Get")
        return [self.STU, self.TCH]

    def write(self):
        log("Write")
        dump(self.get(), open(self.sFileName, "wb"))
        return True

    def __init__(self, sFileName):
        log("Open " + sFileName)
        self.sFileName = sFileName
        try:
            self.put(*load(open(self.sFileName, "rb")))
        finally:
            return None

    def __del__(self):
        log("Close")
        self.write()

    def __enter__(self):
        log("Enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        log("Exit")
        return self.write()
