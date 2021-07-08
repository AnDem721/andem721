import csv

def get_bus_dict():
    autobusy_list = []
    passengers = []
    dates = []
    with open("przewoz_osob_gdynia.csv") as csvfile:
        autobusy = csv.reader(csvfile)
        for row in autobusy:
            autobusy_list.append(row)
    autobusy_list.pop(0)
    for i in autobusy_list:
        passengers.append(float(i[0]))
        dates.append(i[1])
    passengers_dict = dict(zip(dates, passengers))
    return passengers_dict

def max_passengers(dict):
     max_passengers = max(dict, key=dict.get)
     print(f"Najwięcej pasażerów było dnia {max_passengers}")



def min_passengers(dict):
    min_passengers = min(dict, key=dict.get)
    print(f"Najmniej pasażerów było dnia {min_passengers}")

def main():
    passengers_dict = get_bus_dict()
    max_passengers(passengers_dict)
    min_passengers(passengers_dict)

main()
