import random
class Company:
    def __init__(self, name, company_type):
        self.name = name 
        self.company_type = company_type

    """dekoratory"""
    @classmethod
    def create_it_company(cls, name):
        return cls (
            name, 
            "it"
        )
        
    @classmethod
    def create_random_comapny(cls):
        return cls(
            f"comapny-{random.randint(1,10)}",
            "unknown"
        )
    
    @staticmethod
    def validate_name(name):
        if len(name) > 20:
            return False
        return True

    

if __name__ == '__main__': 

    intel = Company('intel', 'it')
    # apple = Company('apple', 'it')
    print(Company.validate_name("intel"))
    apple = Company.create_it_company('apple')
    amazon = Company('amazon', 'market')
    rand1 = Company.create_random_comapny()