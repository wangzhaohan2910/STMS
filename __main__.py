from pickle import dump, load
from operator import and_, or_, xor
from functools import reduce


class Teacher:
    iId = 0
    sName = ""
    setStudent = set()

    def __init__(self, sName="", setStudent=None):
        self.sName = sName
        self.setStudent = set(setStudent) if setStudent else set()


class Database:
    sFileName = ""
    STU = [""]
    TCH = [Teacher()]

    def getStudentName(self, *lId):
        return (self.STU[i] for i in lId)

    def putStudentName(self, iId, sName):
        self.STU[iId] = sName
        return True

    def getStudentTeacher(self, *lId):
        return ({i.iId for i in self.TCH if iId in i.setStudent} for iId in lId)

    def putStudentTeacher(self, iId, *lTeacher):
        for i in self.TCH:
            if i.iId not in lTeacher:
                i.setStudent.discard(iId)
            else:
                i.setStudent.add(iId)
        return True

    def getStudentCount(self):
        return len(self.STU) - 1

    def putStudent(self, iId, sName, *lTeacher):
        return self.putStudentName(iId, sName) and self.putStudentTeacher(
            iId, *lTeacher
        )

    def postStudent(self, sName, *lTeacher):
        self.STU.append("")
        self.putStudent(self.getStudentCount(), sName, *lTeacher)
        return self.getStudentCount()

    def deleteStudent(self, *lId):
        for i in lId:
            self.STU[i] = ""
            for j in self.TCH:
                j.setStudent.discard(i)
        while self.STU[-1] == "" and len(self.STU) > 1:
            self.STU.pop()
        return True

    def deleteAllStudent(self):
        for i in self.TCH:
            i.setStudent.clear()
        self.STU = [""]
        return True

    def getStudentInTeachers(self, iId, *lTeacher):
        return (iId in self.TCH[i].setStudent for i in lTeacher)

    def getStudentTeacherCount(self, *lId):
        return (len(next(self.getStudentTeacher(i))) for i in lId)

    def getStudentAnd(self, *lId):
        return {i.iId for i in self.TCH if all(j in i.setStudent for j in lId)}

    def putStudentAnd(self, iId, *lId):
        return self.putStudentTeacher(iId, *self.getStudentAnd(iId, *lId))

    def putStudentAndName(self, iId, sName, *lId):
        return self.putStudent(iId, sName, *self.getStudentAnd(iId, *lId))

    def postStudentAnd(self, sName, *lId):
        return self.postStudent(sName, *self.getStudentAnd(*lId))

    def getStudentOr(self, *lId):
        return {i.iId for i in self.TCH if any(j in i.setStudent for j in lId)}

    def putStudentOr(self, iId, *lId):
        return self.putStudentTeacher(iId, *self.getStudentOr(iId, *lId))

    def putStudentOrName(self, iId, sName, *lId):
        return self.putStudent(iId, sName, *self.getStudentOr(iId, *lId))

    def postStudentOr(self, sName, *lId):
        return self.postStudent(sName, *self.getStudentOr(*lId))

    def getStudentXor(self, *lId):
        return {i.iId for i in self.TCH if sum(j in i.setStudent for j in lId) % 2 != 0}

    def putStudentXor(self, iId, *lId):
        return self.putStudentTeacher(iId, *self.getStudentXor(iId, *lId))

    def putStudentXorName(self, iId, sName, *lId):
        return self.putStudent(iId, sName, *self.getStudentXor(iId, *lId))

    def postStudentXor(self, sName, *lId):
        return self.postStudent(sName, *self.getStudentXor(*lId))

    def getStudentAndTeacher(self, iId, *lId):
        return next(self.getStudentTeacher(iId)) & set(lId)

    def putStudentAndTeacher(self, iIdAno, iId, *lId):
        return self.putStudentTeacher(iIdAno, *self.getStudentAndTeacher(iId, *lId))

    def putSameStudentAndTeacher(self, iId, *lId):
        return self.putStudentAndTeacher(iId, iId, *lId)

    def putStudentAndTeacherName(self, iIdAno, iId, sName, *lId):
        return self.putStudent(iIdAno, sName, *self.getStudentAndTeacher(iId, *lId))

    def putSameStudentAndTeacherName(self, iId, sName, *lId):
        return self.putStudentAndTeacherName(iId, iId, sName, *lId)

    def postStudentAndTeacher(self, sName, iId, *lId):
        return self.postStudent(sName, *self.getStudentAndTeacher(iId, *lId))

    def getStudentOrTeacher(self, iId, *lId):
        return next(self.getStudentTeacher(iId)) | set(lId)

    def putStudentOrTeacher(self, iIdAno, iId, *lId):
        return self.putStudentTeacher(iIdAno, *self.getStudentOrTeacher(iId, *lId))

    def putSameStudentOrTeacher(self, iId, *lId):
        return self.putStudentOrTeacher(iId, iId, *lId)

    def putStudentOrTeacherName(self, iIdAno, iId, sName, *lId):
        return self.putStudent(iIdAno, sName, *self.getStudentOrTeacher(iId, *lId))

    def putSameStudentOrTeacherName(self, iId, sName, *lId):
        return self.putStudentOrTeacherName(iId, iId, sName, *lId)

    def postStudentOrTeacher(self, sName, iId, *lId):
        return self.postStudent(sName, *self.getStudentOrTeacher(iId, *lId))

    def getStudentXorTeacher(self, iId, *lTeacher):
        return next(self.getStudentTeacher(iId)) ^ set(lTeacher)

    def putStudentXorTeacher(self, iIdAno, iId, *lId):
        return self.putStudentTeacher(iIdAno, *self.getStudentXorTeacher(iId, *lId))

    def putSameStudentXorTeacher(self, iId, *lId):
        return self.putStudentXorTeacher(iId, iId, *lId)

    def putStudentXorTeacherName(self, iIdAno, iId, sName, *lId):
        return self.putStudent(iIdAno, sName, *self.getStudentXorTeacher(iId, *lId))

    def putSameStudentXorTeacherName(self, iId, sName, *lId):
        return self.putStudentXorTeacherName(iId, iId, sName, *lId)

    def postStudentXorTeacher(self, sName, iId, *lId):
        return self.postStudent(sName, *self.getStudentXorTeacher(iId, *lId))

    def getAllStudentName(self):
        return {i for i in self.STU if i}

    def getAllStudentTeacher(self):
        dResult = {}
        for i in self.TCH:
            for j in i.setStudent:
                if j not in dResult:
                    dResult[j] = {i.iId}
                else:
                    dResult[j].add(i.iId)
        return dResult

    def getTeacherName(self, *lId):
        return (self.TCH[i].sName for i in lId)

    def putTeacherName(self, iId, sName):
        self.TCH[iId].sName = sName
        return True

    def getTeacherStudent(self, *lId):
        return (self.TCH[i].setStudent for i in lId)

    def putTeacherStudent(self, iId, *lId):
        self.TCH[iId].setStudent = set(lId)
        return True

    def getTeacherCount(self):
        return len(self.TCH) - 1

    def putTeacher(self, iId, sName, *lId):
        return self.putTeacherName(iId, sName) and self.putTeacherStudent(iId, *lId)

    def postTeacher(self, sName, *lId):
        self.TCH.append(Teacher())
        self.TCH[-1].iId = len(self.TCH) - 1
        self.putTeacher(self.getTeacherCount(), sName, *lId)
        return len(self.TCH) - 1

    def deleteTeacher(self, *lId):
        for i in lId:
            self.TCH[i].sName = ""
            self.TCH[i].setStudent.clear()
        while self.TCH[-1].sName == "" and len(self.TCH) > 1:
            self.TCH.pop()
        return True

    def deleteAllTeacher(self):
        self.TCH = [Teacher()]
        return True

    def getTeacherInStudents(self, iId, *lId):
        return (i in self.TCH[iId].setStudent for i in lId)

    def getTeacherStudentCount(self, *lId):
        return (len(self.TCH[i].setStudent) for i in lId)

    def getTeacherAnd(self, *lId):
        return reduce(and_, (self.TCH[i].setStudent for i in lId))

    def putTeacherAnd(self, iId, *lId):
        return self.putTeacherStudent(iId, *self.getTeacherAnd(*lId))

    def putTeacherAndName(self, iId, sName, *lId):
        return self.putTeacher(iId, sName, *self.getTeacherAnd(*lId))

    def postTeacherAnd(self, sName, *lId):
        return self.postTeacher(sName, *self.getTeacherAnd(*lId))

    def getTeacherOr(self, *lId):
        return reduce(or_, (self.TCH[i].setStudent for i in lId))

    def putTeacherOr(self, iId, *lId):
        return self.putTeacherStudent(iId, *self.getTeacherOr(*lId))

    def putTeacherOrName(self, iId, sName, *lId):
        return self.putTeacher(iId, sName, *self.getTeacherOr(*lId))

    def postTeacherOr(self, sName, *lId):
        return self.postTeacher(sName, *self.getTeacherOr(*lId))

    def getTeacherXor(self, *lId):
        return reduce(xor, (self.TCH[i].setStudent for i in lId))

    def putTeacherXor(self, iId, *lId):
        return self.putTeacherStudent(iId, *self.getTeacherXor(*lId))

    def putTeacherXorName(self, iId, sName, *lId):
        return self.putTeacher(iId, sName, *self.getTeacherXor(*lId))

    def postTeacherXor(self, sName, *lId):
        return self.postTeacher(sName, *self.getTeacherXor(*lId))

    def put(self, STU, TCH):
        self.STU = STU
        self.TCH = TCH
        return True

    def delete(self):
        return self.deleteAllStudent() and self.deleteAllTeacher()

    def get(self):
        return [self.STU, self.TCH]

    def write(self):
        dump(self.get(), open(self.sFileName, "wb"))
        return True

    def __init__(self, sFileName):
        self.sFileName = sFileName
        try:
            self.put(*load(open(self.sFileName, "rb")))
        finally:
            return None

    def __del__(self):
        self.write()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self.write()
