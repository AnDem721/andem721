class Person: 
    def __init__(self, name, document_id, age):
        self.name = name 
        self.document_id = document_id
        self.age = age

    def __str__(self):
        return f"{self.name}"
    
    def say_hello(self):
        return "hello from Person"

class Student(Person):
    def __init__(self, name, document_id, age, major):
        super().__init__(name, document_id, age)
        self.major = major

    def ask_question(self, question):
        print(question)

    def say_hello(self):
        hello_above = super().say_hello()
        return f" {hello_above} and hello from student"


class Teacher(Person):
#nauczyciel
    def give_homework(self, homework):
        print(homework)

class ItStudent(Student):
    def write_program(self):
        print("..")

if __name__ == '__main__': 
    stud1 = Student("Andrzej", 1234, 35, "it")

    print(stud1)
    print(stud1.say_hello())