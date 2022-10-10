# [x] Finish task
# [ ] Save files to drive

#  Create a classes called Student and Graduate
# Student contains name, surname and a field of study
# Graduate contains name, surname, a field of study and a obtained title.
# Create a method `graduate` in class `Student` which creates a new instance of the Graduate class
# Information in the Graduate instance would originate from the student, and it would also have a parameter to determine
# which title the student get by graduation. And return the new Graduate instance.

# So lets say we have `student = Student("John", "Smith", "biology")`
# `graduated_john = student.graduate("Mgr") should result in `graduated_john` containing Graduate
# instance with correct title, name etc.

class Student:

    def __init__(self, name, surname, study_field):
        self.name = name
        self.surname = surname
        self.study_field = study_field

    def __str__(self):
        return f"{self.name} {self.surname}, {self.study_field}"

    def graduate(self, graduation_title):
        return Graduate(self.name, self.surname, self.study_field, graduation_title)

class Graduate:

    def __init__(self, name, surname, study_field, obtained_title):
        self.name = name
        self.surname = surname
        self.study_field = study_field
        self.obtained_title = obtained_title

    def __str__(self):
        return f"{self.name} {self.surname}, {self.obtained_title} in {self.study_field}"

student_john = Student("John", "Smith", "Psychology")
graduate_john = student_john.graduate("Masters")

print(student_john)
print(graduate_john)
