class Student:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average(self):
        return sum(self.grades.values()) / len(self.grades)
    
    def display_card(self):
        print(f"Name: {self.name} ID Number: {self.id_number}")
        for subject, grade in self.grades.items():
            print(f"{subject} : {grade}")
        print(f"Average: {self.get_average()}")

    def grade_range(self):
        average = self.get_average()

        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return "D"
        else:
            return 'F'