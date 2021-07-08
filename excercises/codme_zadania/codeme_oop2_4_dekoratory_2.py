class Vaccine:
    def __init__(self, company, price):
        self.company = company
        self.side_effects = []
        self.rating = []


    def rate(self, rating_no):
        self.rating.append(rating_no)

    def report_side_effect(self, side_effect):
        self.side_effects.append(side_effect)

    @property
    def avg_rating(self):
        if len(self.rating) == 0:
            raise ValueError("nie zostala oceniona")
        return sum(self.rating) / len(self.rating)

    @staticmethod
    def check_if_rating_positive(rating):
        if rating > 5:
            return True
        else:
            return False

    @classmethod
    def crate_moderna(cls, price):
        return cls(
            "moderna",
            price
        )

vac1 = Vaccine("moderna", 0.0325)
vac1.rate(7)
print(vac1.rating)
print(vac1.avg_rating)
vac1.rate(8)
print(vac1.avg_rating)
print(vac1.check_if_rating_positive(vac1.avg_rating))
print(vac1.check_if_rating_positive(5))
vac2 = Vaccine("pfizer", 0.1234)
vac2.rate(2)
vac3 = Vaccine("Astra_zeneca", 0.243)
vac3.rate(5)
vac4 = Vaccine.crate_moderna(0.2432)

