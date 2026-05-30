class Student:
    school_name = "DPS"
    total_students=0
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
        Student.total_students+=1
    
    def display_details(self):
        print(f"Student name: {self.name}")
        print(f"Student roll number: {self.roll}")
        print("Obtained Marks:")
        for i in self.marks:
            print(f"   {i} marks: {self.marks[i]}")
        total=sum(self.marks.values())
        print(f"Total: {total}")
        avg=total/len(self.marks)
        print(f"Average: {avg}")
        Student.calculate_grade(avg)
    
    @classmethod
    def show_total_students(cls):
        print(f"Total students: {cls.total_students}")

    @staticmethod
    def calculate_grade(avg):
        if(avg>=90):
            print("S Grade")
        elif avg>=85:
            print("A Grade")
        elif avg>=60:
            print("B Grade")
        else:
            print("C Grade")



studentList=[]

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Show Total Students")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name=input("Enter name:   ")
        roll=int(input("Enter roll number:   "))
        subjects = [
            "English",
            "Hindi",
            "Mathematics",
            "Science",
            "Social Science"
        ]
        marks={}
        for subject in subjects:
            marks[subject]=int(input(f"Enter {subject} marks :   "))
        stud=Student(name,roll,marks)
        studentList.append(stud)
        print("Student Added Successfully")

    elif choice == 2:
        if len(studentList)==0:
            print("No students found")
        else:
            for i in studentList:
                i.display_details()

    elif choice == 3:
        Student.show_total_students()

    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")    
