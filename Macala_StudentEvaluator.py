# This function shows the program title and a separator before inputs.
def display_header():
    print("Student Performance Evaluator")
    print('-'*50)

# This function asks for the student name and three assessment scores.
def get_student_info():

    a = input("Enter Assessment 1: ")
    b = input("Enter Assessment 2: ")
    c = input("Enter Assessment 3: ")
    evaluate_performance(name,a,b,c)
    display_report(name, a, b, c)
    return name, a, b, c


# This function
def evaluate_performance(a,b,c):
    average = (a + b + c)/3
    if average >= 90 and average <= 100:
        print("Outstanding")
    if average >= 85 and average < 90:
        print("Very Satisfactory")
    if average >= 80 and average < 85:
        print("Satisfactory")
    if average >= 75 and average < 80:
        print("Fairly Satisfactory")
    if average < 75:
        print("Needs Improvement")
    display_report(average, name, a, b, c)
    return average

def display_report(average, name, a, b, c):
    print(f"Student Name: ", name)
    print(f"Assessment Scores: ", a and b and c )
    print(f"Average Score: {average:.2f}")
    if average >= 90 and average <= 100:
        print("Performance Level: Outstanding")
    if average >= 85 and average < 90:
        print("Performance Level: Very Satisfactory")
    if average >= 80 and average < 85:
        print("Performance Level: Satisfactory")
    if average >= 75 and average < 80:
        print("Performance Level: Fairly Satisfactory")
    if average < 75:
        print("Performance Level: Needs Improvement")

display_header()
name = input("Enter Student Name: ")
get_student_info()
evaluate_performance()
display_report()