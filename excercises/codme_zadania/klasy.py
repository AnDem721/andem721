class Student():
    def __init__(self, imie, nazwisko, uczelnia, kierunek, id_no):
        self.imie = imie
        self.nazwisko = nazwisko
        self.uczelnia = uczelnia
        self.kierunek = kierunek
        self.id_noid_no = id_no
        self.grades = []

    def avg_grade(self):
        if len(self.avg_grade()) > 0:
            avg_grade = sum(self.avg_grade()) / len(self.avg_grade())
            return avg_grade

    @classmethod
    def create_polibudu(cls, imie, nazwisko, kierunek,  id_no):
        return cls(
            imie,
            nazwisko,
            "PG",
            kierunek,
            id_no
        )

stud1 = Student.create_polibudu("Andrzej", "Dembowski", "informatyka", "11111")
print(stud1.id_noid_no)
