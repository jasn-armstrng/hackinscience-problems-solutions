# https://www.hackinscience.org/exercises/student-class:
# Student, School, and City have a name attribute, given at initialization time.
# A Student have an add_exam(grade) method, recording a new grade for him, as a float.
# A School have an add_student(student) method.
# A City have an add_school(school) method.
# Student, School, and City have a get_mean() method giving:
# For the Student, the average of its results.
# For the School, the average of the students averages.
# For the City the average of the School averages.
# School have a get_best_student() method, returning the best Student.
# Cities have a get_best_school() and a get_best_student() methods, returning respectively a School and a Student.
from typing import List

class Student:
    def __init__(self, name:str) -> None:
        """Initialize the Student with a name."""
        self.name = name
        self.grades: List[int] = []

    def add_exam(self, grade: int) -> None:
        """Record a new grade for the student."""
        self.grades.append(grade)

    def get_mean(self) -> float:
        """Return the average of the student's grades."""
        return round(sum(self.grades)/len(self.grades), 2) if self.grades else 0.0


class School:
    def __init__(self, name:str) -> None:
        """Initialize the School with a name."""
        self.name = name
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        """Add a student to the school."""
        self.students.append(student)

    def get_mean(self) -> float:
        """Return the average of the students' averages."""
        total_avg = sum(student.get_mean() for student in self.students)
        return round(total_avg/len(self.students), 2) if self.students else 0.0

    def get_best_student(self) -> str:
        """Return the student with the highest average grade."""
        if not self.students:
            return None
        best_student: Student = max(self.students, key=lambda student: student.get_mean())
        return best_student


class City:
    def __init__(self, name:str) -> None:
        """Initialize the City with a name."""
        self.name = name
        self.schools: List[School] = []

    def add_school(self, school: School) -> None:
        """Add a school to the city."""
        self.schools.append(school)

    def get_mean(self) -> float:
        """Return the average of the schools' averages."""
        total_avg = sum(school.get_mean() for school in self.schools)
        return round(total_avg/len(self.schools), 2) if self.schools else 0.0

    def get_best_school(self) -> str:
        """Return the school with the highest average grade."""
        if not self.schools:
            return None
        best_school: School = max(self.schools, key=lambda school: school.get_mean())
        return best_school

    def get_best_student(self) -> str:
        """Return the best student among all schools in the city."""
        if not self.schools:
            return None
        best_student: Student = max((student for school in self.schools for student in school.students),
                            key=lambda student: student.get_mean(), default=None)
        return best_student if best_student else None


def test_classes():
    # Test Student class
    s1 = Student("John")
    s1.add_exam(90)
    s1.add_exam(100)
    s1.add_exam(95)
    assert s1.get_mean() == 95

    s2 = Student("Jane")
    s2.add_exam(85)
    s2.add_exam(95)
    s2.add_exam(100)
    assert s2.get_mean() == 93.33

    # Test School class
    school1 = School("High School")
    school1.add_student(s1)
    school1.add_student(s2)
    assert school1.get_mean() == 94.16  # (95 + 93.33) / 2
    assert school1.get_best_student().name == "John"  # s1 has higher average

    s3 = Student("Johnathon")
    s3.add_exam(73)
    s3.add_exam(100)
    s3.add_exam(95)
    assert s3.get_mean() == 89.33

    s4 = Student("Janeka")
    s4.add_exam(85)
    s4.add_exam(95)
    s4.add_exam(96)
    assert s4.get_mean() == 92

    # Test School class
    school2 = School("High School South")
    school2.add_student(s3)
    school2.add_student(s4)
    assert school2.get_mean() == 90.66  # (95 + 93.33) / 2
    assert school2.get_best_student().name == "Janeka"  # s1 has higher average

    # Test City class
    city = City("City1")
    city.add_school(school1)
    city.add_school(school2)
    assert city.get_mean() == 92.41  # there's only one school
    assert city.get_best_school().name == "High School"  # only one school in city
    assert city.get_best_student().name == "John"  # s1 has higher average

    print("All tests passed!")


def main() -> None:
    test_classes()


if __name__ == "__main__":
    main()
