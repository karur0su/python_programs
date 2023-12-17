import dataclasses

@dataclasses.dataclass
class Student:
    name: str
    age: int
    grades: list = dataclasses.field(default_factory=list)

    def add_grade(self, grade: float):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Usage example
student = Student(name='Alice', age=20)
student.add_grade(85.5)
student.add_grade(90.0)
print(f"{student.name}'s average grade: {student.average_grade()}")
