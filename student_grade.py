grade = int(input("Enter your grade : "))
def student_grade():
    if grade>=90:
        print("A")
    elif grade >=80:
        print("B")
    elif grade >=70 and grade <=60:
        print("c")
    else:
        print("D")
student_grade()