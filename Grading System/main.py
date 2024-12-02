from student import Student

def main():
    student = Student('Alice', 10)
    student.add_grade('Math', 90)
    student.add_grade('Science',90)
    student.add_grade('English', 85)

    student.display_card()


if __name__ == '__main__':
    main()