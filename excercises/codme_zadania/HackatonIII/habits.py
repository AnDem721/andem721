from datetime import date, datetime
import json


class HabitsTracker:
    def __init__(self):
        self.habits = load_habits()
    def habits_display(self):
        for habit in self.habits:
            actual_date = datetime.isocalendar(datetime.now())
            week_view = {'Mon': '', 'Tue': '', 'Wed': '', 'Thu': '', 'Fri': '', 'Sat': '', 'Sun': ''}
            print(habit.get('name').title(), habit.get('freq'), "times a week")
            for date in habit['progress']:
                x = datetime.isocalendar(datetime.strptime(date, '%Y-%m-%d'))
                if x[1] == actual_date[1]:
                    dict_list = list(week_view)
                    dict_key = dict_list[x[2] - 1]
                    week_view[dict_key] = "X"
            for key in week_view:
                print(key, ":", week_view[key])

    def menu(self):
        while True:
            print("HabitTracker")
            usr_choice = {
                1: "Wyświetl postępy",
                2: "Dodaj kolejny nawyk do śledzenia",
                3: "Zapisz do pliku",
                4: "Dodaj postęp"
            }
            for i in usr_choice:
                print(i, usr_choice[i])
            x = int(input("=>"))
            if x == 1:
                self.habits_display()
            elif x == 2:
                self.new_habit()
            elif x == 3:
                self.save_to_file()
            elif x == 4:
                self.log_progress()


    def new_habit(self):
        habit_name = input("Podaj nazwę dla nowego nawyku: ")
        start_date = date.today()
        habit = {
            "habit_id": habit_name,
            "name": habit_name,
            "freq": "",
            "start_date": start_date,
            "progress": []
        }
        self.habits.append(habit)

    def save_to_file(self):
        with open("habits.json", "w", encoding="utf-8") as f:
            json.dump(self.habits, f)


    def log_progress(self):
        habits_list = []
        habits_choice = {}
        current_date = date.today()
        for name in self.habits:
            habits_list.append(name['name'])
        for x in range(len(habits_list)):
            habits_choice[x] = ""
        user_choice = dict(zip(habits_choice.keys(), habits_list))
        for i in user_choice:
            print(i, user_choice[i])
        prog = int(input("Którą czynność logujesz?: "))
        self.habits[prog]['progress'].append(str(current_date))





def load_habits():
    with open("habits.json", "r", encoding="utf-8") as f:
       habits_data = json.load(f)
    return habits_data



if __name__ == '__main__':
    tracker = HabitsTracker()
    tracker.menu()