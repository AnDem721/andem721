import random
def get_numbers():
    num1 = int(input('Podaj dolna granice zakresu liczb: '))
    num2 = int(input('Podaj górna granice zakresu liczb: '))
    num3 = int(input('Podaj ilosc liczb do wylosowania'))
    nums = [num1, num2, num3]
    return nums

def draw_nums(nums):
    numsList = []
    for x in range(nums[2]):
        numsList.append(random.randint(nums[0], nums[1]))
    print(numsList)
    return numsList

def main():
    draw_nums(get_numbers())

