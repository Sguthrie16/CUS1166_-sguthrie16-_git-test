from models import Student
from math_utils import average
def main():

    x = []
    x.append(Student("Shawn",100))
    x.append(Student("Sarah",90))
    x.append(Student("Mark",95))
    x.append(Student("John",80))
    x.append(Student("Jack",87))
    x.append(Student("Mary",69))
    x.append(Student("Chris",93))
    x.append(Student("Sam",76))
    x.append(Student("Mike",75))
    x.append(Student("Ray",75))
    for i in x:
        print(i.print_student_info())

    print average(x)

if __name__ == '__main__':
    main()
