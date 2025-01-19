# python will first check the clas of objects before checking superclasses

class Teacher:
    def teach_class(self):
        print("TEaching")

    def grab_lunch(self):
        print("Eat")

    def grade_tests(self):
        print("F F F")

class CollegeProfessor(Teacher):
    def publish_book(self):
        print("Hooray")

    def grade_tests(self):
        print("A A A")

teacher = Teacher()
professor = CollegeProfessor()

teacher.grade_tests()
professor.grade_tests()