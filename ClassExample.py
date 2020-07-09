class student:
    rollno=1
    CLASS=1
    name="xyz"
    age=1
    marks=1
    def percentage(self):
        return student.marks/5
    def INPUT(self):
        student.rollno=int(input("Enter your roll no.:"))
        student.CLASS=int(input("Enter your class:"))
        student.name=input("Enter your name:")
        student.age=int(input("Enter your age:"))
        student.marks=int(input("Enter your marks:"))
    def output(self):
        print("Hello!",student.name)
        print("Yours details...:")
        print("\n\nCLASS:\t\t",student.CLASS)
        print("\nrollno:\t",student.rollno)
        print("\nage:\t\t",student.age)
        print("\nmarks:\t\t",student.marks)
        print("\n\nYour percentage is:",student.percentage(self))
s1=student()
s1.INPUT()
s1.output()
