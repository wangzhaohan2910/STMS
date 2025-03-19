from pickle import dump, load


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

    def postStudent(self, sName, *lTeacher):
        self.STU.append(sName)
        for i in lTeacher:
            self.TCH[i].setStudent.add(len(self.STU) - 1)
        return len(self.STU) - 1

    def putStudentTeacher(self, iId, *lTeacher):
        for i in self.TCH:
            if i.iId not in lTeacher:
                i.setStudent.discard(iId)
            else:
                i.setStudent.add(iId)
        return True

    def putStudentName(self, iId, sName):
        self.STU[iId] = sName
        return True

    def putStudent(self, iId, sName, *lTeacher):
        return self.putStudentName(iId, sName) and self.putStudentTeacher(
            iId, *lTeacher
        )

    def deleteStudent(self, iId):
        self.STU[iId] = ""
        for i in self.TCH:
            i.setStudent.discard(iId)
        while self.STU[-1] == "" and len(self.STU) > 1:
            self.STU.pop()
        return True

    def deleteAllStudent(self):
        for i in self.TCH:
            i.setStudent.clear()
        self.STU = [""]
        return True

    def getStudentCount(self):
        return len(self.STU) - 1

    def getStudentName(self, iId):
        return self.STU[iId]

    def getStudentTeacher(self, iId):
        return {i.iId for i in self.TCH if iId in i.setStudent}

    def getStudentTeachers(self, iId, *lTeacher):
        return [iId in self.TCH[i].setStudent for i in lTeacher]

    def getStudentAnd(self, *lId):
        return {i.iId for i in self.TCH if all(j in i.setStudent for j in lId)}

    def getStudentOr(self, *lId):
        return {i.iId for i in self.TCH if any(j in i.setStudent for j in lId)}

    def getStudentXor(self, *lId):
        return {i.iId for i in self.TCH if sum(j in i.setStudent for j in lId) % 2 != 0}

    def getAllStudentName(self):
        return self.STU

    def getAllStudentTeacher(self):
        dResult = {}
        for i in self.TCH:
            for j in i.setStudent:
                if j not in dResult:
                    dResult[j] = {i.iId}
                else:
                    dResult[j].add(i.iId)
        return dResult

    def postTeacher(self, sName, *lStudent):
        self.TCH.append(Teacher())
        self.TCH[-1].iId = len(self.TCH) - 1
        self.TCH[-1].sName = sName
        self.TCH[-1].setStudent = set(lStudent)
        return len(self.TCH) - 1

    def putTeacherName(self, iId, sName):
        self.TCH[iId].sName = sName
        return True

    def putTeacherStudent(self, iId, *lStudent):
        self.TCH[iId].setStudent = set(lStudent)
        return True

    def putTeacher(self, iId, sName, *lStudent):
        return self.putTeacherName(iId, sName) and self.putTeacherStudent(
            iId, *lStudent
        )

    def deleteTeacher(self, iId):
        self.TCH[iId].sName = ""
        self.TCH[iId].setStudent.clear()
        while self.TCH[-1].sName == "" and len(self.TCH) > 1:
            self.TCH.pop()
        return True

    def deleteAllTeacher(self):
        self.TCH = [Teacher()]
        return True

    def getTeacherCount(self):
        return len(self.TCH) - 1

    def getTeacherName(self, iId):
        return self.TCH[iId].sName

    def getTeacherStudent(self, iId):
        return self.TCH[iId].setStudent

    def getTeacherStudents(self, iId, *lStudent):
        return [iId in self.getStudentTeacher(j) for j in lStudent]

    def getTeacherAnd(self, *lId):
        setResult = set()
        for j in range(1, len(self.STU)):
            if all(i in self.getStudentTeacher(j) for i in lId):
                setResult.add(j)
        return setResult

    def getTeacherOr(self, *lId):
        setResult = set()
        for j in range(1, len(self.STU)):
            if any(i in self.getStudentTeacher(j) for i in lId):
                setResult.add(j)
        return setResult

    def getTeacherXor(self, *lId):
        setResult = set()
        for j in range(1, len(self.STU)):
            count = sum(1 for i in lId if i in self.getStudentTeacher(j))
            if count % 2 != 0:
                setResult.add(j)
        return setResult

    def getAllTeacherName(self):
        return {i.sName for i in self.TCH}

    def getAllTeacherStudent(self):
        return {i.iId: i.setStudent for i in self.TCH}

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
