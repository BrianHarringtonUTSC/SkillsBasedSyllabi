import random

def random_price(max_value):
    price = "$"
    price += str(random.randint(0,max_value))
    price += "."
    price += str(random.randint(0,9))
    price += str(random.randint(0,9))
    return price

def random_subset(input_list, min_num, max_num):
    list_copy = input_list[:]
    random.shuffle(list_copy)
    length = random.randint(min_num, max_num)
    return list_copy[0:length]

def create_files():
    names = ["Alice", "Bob", "Carol", "Dave", "Edith", "Frank", "Gertrude", "Hannah", "Ingrid"]
    items = ["Apple", "Banana", "Carrot", "Dragon Fruit", "Eggs", "Hamburger Buns", "Ice Pops"]
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    budget_file = open("lab8_budget.txt", "w")
    for next_name in names:
        budget_file.write(next_name + "," + random_price(100) + "\n")
    budget_file.close()

    prices_file = open("lab8_prices.txt", "w")
    for next_item in items:
        prices_file.write(next_item + "," + random_price(5) + "\n")
    prices_file.close()

    purchases_file = open("lab8_purchases.txt", "w")
    for next_day in days:
        purchases_file.write("DAY:" + next_day+ "\n")
        todays_people = random_subset(names, 2, 7)
        for next_person in todays_people:
            purchases_file.write(next_person)
            for count in range(0, random.randint(3,10),1):
                purchases_file.write("," + random.choice(items))
            purchases_file.write("\n")
    purchases_file.close()
create_files()

def price_to_float(input_string):
    amount = input_string[1:]
    return float(amount)

def build_price_dictionary(input_dict, input_file):
    for next_line in input_file:
        next_line = next_line.strip()
        items = next_line.split(",")
        input_dict[items[0]] = price_to_float(items[1])


####MAIN CODE
budget_file = open("lab8_budget.txt", "r")
budget_dict = {}
build_price_dictionary(budget_dict, budget_file)
budget_file.close()

prices_file = open("lab8_prices.txt", "r")
prices_dict = {}
build_price_dictionary(prices_dict, prices_file)
prices_file.close()

purchases_file = open("lab8_purchases.txt", "r")
day_to_total = {}
person_to_total = {}
for next_person in budget_dict:
    person_to_total[next_person] = 0

for next_line in purchases_file:
    next_line = next_line.strip()
    if(next_line.startswith("DAY")):
        current_day = next_line[4:]
        day_to_total[current_day] = 0
    else:
        items = next_line.split(",")
        person = items[0]
        for next_item in items[1:]:
            next_price = prices_dict[next_item]
            day_to_total[current_day] += next_price
            person_to_total[person] += next_price
purchases_file.close()
print(day_to_total)

import matplotlib.pyplot as plt
import numpy as np
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
day_totals = []
for next_day in days:
    day_totals.append(day_to_total[next_day])
#plt.plot(days, day_totals)

names = ["Alice", "Bob", "Carol", "Dave", "Edith", "Frank", "Gertrude", "Hannah", "Ingrid"]
budgets = []
spent = []
for next_name in names:
    budgets.append(budget_dict[next_name])
    spent.append(person_to_total[next_name])
print(budgets)
print(spent)
order = np.arange(9)
width = 0.3
plt.bar(order, budgets, 0.3, label="Amount budgeted")
plt.bar(order + width, spent, 0.3, label = "Amount spent")
plt.xticks(order + width / 2, names)
plt.legend(loc='best')
#plt.show()


###CORE COMPTENCY CODE#####
def how_many_in_line(input_line, search_item):
    input_list = input_line.split(',')
    count = 0
    for next_item in input_list:
        if(next_item == search_item):
            count += 1
    return count

purchases_file = open("lab8_purchases.txt", "r")
for next_line in purchases_file:
    next_line = next_line.strip()
    print(next_line)
    print(how_many_in_line(next_line,'Apple'))
    

purchases_file.close()