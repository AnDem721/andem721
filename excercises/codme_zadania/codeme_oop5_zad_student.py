class Student:
    def __init__(self, st_name, school,  major, id, grades):
        self.name = st_name
        self.school = school
        self.major = major
        self.id = id
        if self.id.isnumeric() == True:
            pass
        else: 
            raise ValueError("numer legitymacji błędny")
        self.grades = [int(i) for i in grades.split(', ')]
       
    def avg_grade(self):
        avg = sum(self.grades) / len(self.grades)
        return avg

    def check_id(self):
        pass
        
    @classmethod
    def add_polibudu(cls, st_name, id, grades):
        return cls(
            st_name,
            "pg", 
            "informatyka",
            id,
            grades
        )

    def __str__(self):
        return f"student {self.name}, school: {self.school}"

if __name__ == '__main__': 
    stud1 = Student('andrzej', 'pg', 'informatyka', '12345', "3, 3, 4, 5")
    print(stud1.grades)
    print(type(stud1.grades[0]))
    print(stud1.avg_grade())


    stud2 = Student.add_polibudu("Andrzej", "24435", '2, 2, 2, 2')

    print(stud1)
    print(stud2)