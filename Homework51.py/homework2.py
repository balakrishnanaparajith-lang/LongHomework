class CourseManager:
    def __init__(self, enrolled_students, unique_courses):
        self.enrolled_students = enrolled_students
        self.unique_courses = unique_courses
    def eligibility(self):
        print("---- Certificate Eligibility Report ----")
        for name, details in self.enrolled_students.items():
            name = input("Who do you want to check")
            attendance = details["attendance"]
            score = details["score"]
            print(f"\nStudent: {name}")
            print(f"Attendance: {attendance}%")
            print(f"Score: {score}")
            if attendance < 90:
                print("Result: Attendance too low. No certificate.")
            else:
                if score > 90:
                    print("Result: Distinction")
                elif score > 70:
                    print("Result: Merit")
                elif score > 55:
                    print("Result: Pass .No certificate")
                else:
                    print("Result: Fail")
    def course_completion(self):
        for name,detail in self.enrolled_students.items():
            completion = detail["Completion"]
            print(f"{name} is {completion}% of the way through the course.")


students = {
        "Bob": {"course": "Math",
                "Completion":96,
                "attendance": 95,
                "score": 88},
        "Billy": {"course": "Science" ,
                  "Completion": 75,
                  "attendance": 80,
                  "score": 73},
        "Tim": {"course": "Math",
                "Completion":32,
                "attendance": 60,
                "score": 43}
    }
courses = {"Math", "Science"}
cor = CourseManager(students, courses)
while True:
    print("1. Check Eligibility")
    print("2. Check Course Completion")
    print("3. Exit")
    bob = int(input("Enter a choice"))
    if bob == 1:
        cor.eligibility()
    elif bob == 2:
        cor.course_completion()
    else:
        print("Thanks for checking.")
        break
