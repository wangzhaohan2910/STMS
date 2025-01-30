import unittest
from io import StringIO
from data import Database, Teacher

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # 创建一个测试数据库实例
        self.db = Database("test.db")

    def tearDown(self):
        # 清理测试数据库文件
        self.db.delete()

    def test_constructor(self):
        # 测试构造函数是否正确初始化数据库
        self.assertEqual(self.db.sFileName, "test.db")
        self.assertEqual(self.db.STU, [""])
        self.assertEqual(len(self.db.TCH), 1)
        self.assertIsInstance(self.db.TCH[0], Teacher)

    def test_post_student(self):
        # 测试添加学生
        student_id = self.db.postStudent("学生1", 0)
        self.assertEqual(student_id, 1)
        self.assertEqual(self.db.STU[1], "学生1")
        self.assertEqual(self.db.TCH[0].setStudent, {1})

    def test_put_student_name(self):
        # 测试更新学生姓名
        self.db.postStudent("学生1", 0)
        self.assertTrue(self.db.putStudentName(1, "学生2"))
        self.assertEqual(self.db.STU[1], "学生2")

    def test_put_student_teacher(self):
        # 测试更新学生的教师
        self.db.postStudent("学生1", 0)
        self.assertTrue(self.db.putStudentTeacher(1, 0))
        self.assertEqual(self.db.TCH[0].setStudent, {1})

    def test_put_student(self):
        # 测试更新学生信息
        self.db.postStudent("学生1", 0)
        self.assertTrue(self.db.putStudent(1, "学生2", 0))
        self.assertEqual(self.db.STU[1], "学生2")
        self.assertEqual(self.db.TCH[0].setStudent, {1})

    def test_delete_student(self):
        # 测试删除学生
        self.db.postStudent("学生1", 0)
        self.assertTrue(self.db.deleteStudent(1))
        self.assertEqual(len(self.db.STU), 1)
        self.assertEqual(self.db.TCH[0].setStudent, set())

    def test_delete_all_student(self):
        # 测试删除所有学生
        self.db.postStudent("学生1", 0)
        self.assertTrue(self.db.deleteAllStudent())
        self.assertEqual(self.db.STU, [""])
        self.assertEqual(self.db.TCH[0].setStudent, set())

    def test_get_student_count(self):
        # 测试获取学生数量
        self.db.postStudent("学生1", 0)
        self.assertEqual(self.db.getStudentCount(), 1)

    def test_get_student_name(self):
        # 测试获取学生姓名
        self.db.postStudent("学生1", 0)
        self.assertEqual(self.db.getStudentName(1), "学生1")

    def test_get_student_teacher(self):
        # 测试获取学生的教师
        self.db.postStudent("学生1", 0)
        self.assertEqual(self.db.getStudentTeacher(1), {0})

    def test_get_all_student_name(self):
        # 测试获取所有学生姓名
        self.db.postStudent("学生1", 0)
        self.assertEqual(self.db.getAllStudentName(), ["", "学生1"])

    def test_get_all_student_teacher(self):
        # 测试获取所有学生的教师
        self.db.postStudent("学生1", 0)
        self.assertEqual(self.db.getAllStudentTeacher(), {1: {0}})

    def test_post_teacher(self):
        # 测试添加教师
        teacher_id = self.db.postTeacher("教师1", 0)
        self.assertEqual(teacher_id, 1)
        self.assertEqual(self.db.TCH[1].sName, "教师1")
        self.assertEqual(self.db.TCH[1].setStudent, {0})

    def test_put_teacher_name(self):
        # 测试更新教师姓名
        self.db.postTeacher("教师1", 0)
        self.assertTrue(self.db.putTeacherName(1, "教师2"))
        self.assertEqual(self.db.TCH[1].sName, "教师2")

    def test_put_teacher_student(self):
        # 测试更新教师的学生
        self.db.postTeacher("教师1", 0)
        self.assertTrue(self.db.putTeacherStudent(1, 0))
        self.assertEqual(self.db.TCH[1].setStudent, {0})

    def test_put_teacher(self):
        # 测试更新教师信息
        self.db.postTeacher("教师1", 0)
        self.assertTrue(self.db.putTeacher(1, "教师2", 0))
        self.assertEqual(self.db.TCH[1].sName, "教师2")
        self.assertEqual(self.db.TCH[1].setStudent, {0})

    def test_delete_teacher(self):
        # 测试删除教师
        self.db.postTeacher("教师1", 0)
        self.assertTrue(self.db.deleteTeacher(1))
        self.assertEqual(len(self.db.TCH), 1)
        self.assertEqual(self.db.TCH[0].sName, "")
        self.assertEqual(self.db.TCH[0].setStudent, set())

    def test_delete_all_teacher(self):
        # 测试删除所有教师
        self.db.postTeacher("教师1", 0)
        self.assertTrue(self.db.deleteAllTeacher())
        self.assertEqual(len(self.db.TCH), 1)
        self.assertEqual(self.db.TCH[0].sName, "")
        self.assertEqual(self.db.TCH[0].setStudent, set())

    def test_get_teacher_count(self):
        # 测试获取教师数量
        self.db.postTeacher("教师1", 0)
        self.assertEqual(self.db.getTeacherCount(), 1)

    def test_get_teacher_name(self):
        # 测试获取教师姓名
        self.db.postTeacher("教师1", 0)
        self.assertEqual(self.db.getTeacherName(1), "教师1")

    def test_get_teacher_student(self):
        # 测试获取教师的学生
        self.db.postTeacher("教师1", 0)
        self.assertEqual(self.db.getTeacherStudent(1), {0})

    def test_get_all_teacher_name(self):
        # 测试获取所有教师姓名
        self.db.postTeacher("教师1", 0)
        self.assertEqual(self.db.getAllTeacherName(), {"", "教师1"})

    def test_get_all_teacher_student(self):
        # 测试获取所有教师的学生
        self.db.postTeacher("教师1", 0)
        self.assertEqual(self.db.getAllTeacherStudent(), {0: set(), 1: {0}})

    def test_put(self):
        # 测试批量更新数据
        data = ["学生1", "学生2"]
        teachers = [Teacher("教师1", {0}), Teacher("教师2", {1})]
        self.assertTrue(self.db.put(data, teachers))
        self.assertEqual(self.db.STU, data)
        self.assertEqual(self.db.TCH, teachers)

    def test_delete(self):
        # 测试删除所有数据
        self.db.postStudent("学生1", 0)
        self.db.postTeacher("教师1", 0)
        self.assertTrue(self.db.delete())
        self.assertEqual(self.db.STU, [""])
        self.assertEqual(len(self.db.TCH), 1)
        self.assertIsInstance(self.db.TCH[0], Teacher)
        self.assertEqual(self.db.TCH[0].sName, "")
        self.assertEqual(self.db.TCH[0].setStudent, set())
        self.assertEqual(self.db.TCH[0].iId, 0)

    def test_get(self):
        # 测试获取所有数据
        self.db.postStudent("学生1", 0)
        self.db.postTeacher("教师1", 0)
        data, teachers = self.db.get()
        self.assertEqual(data, ["", "学生1"])
        self.assertEqual(len(teachers), 2)
        self.assertEqual(teachers[1].sName, "教师1")
        self.assertEqual(teachers[1].setStudent, {0})
if __name__ == "__main__":
    unittest.main()