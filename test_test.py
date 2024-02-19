import unittest
from main import StudentsInMLOps

class TestStudentsInMLOps(unittest.TestCase):
    def setUp(self):
        self.students = StudentsInMLOps()

    def test_enrollStudents(self):
        self.students.enrollStudents(5)
        self.assertEqual(self.students.getTotalStrength(), 5)

    def test_dropStudents(self):
        self.students.enrollStudents(10)
        self.students.dropStudents(3)
        self.assertEqual(self.students.getTotalStrength(), 7)

    def test_getTotalStrength(self):
        self.students.enrollStudents(8)
        self.assertEqual(self.students.getTotalStrength(), 8)

    def test_getClassName(self):
        self.assertEqual(self.students.getClassName(), "StudentsInMLOps")

if __name__ == '__main__':
    unittest.main()