__author__ = 'fbueti'
import csv

def noNumbers(inputString):
     return not (any(char.isdigit() for char in inputString))

with open('hillary.csv') as csvfile:
    all_possible = []
    ignore_me = ['AND' ' ' 'I' 'S']
    all_expenses = csv.DictReader(csvfile)
    for expense in all_expenses:
        categories = expense['disb_desc'].split(" ")
        for category in categories:
            if (not(category in all_possible) and not(category in ignore_me) and noNumbers(category)):
                all_possible.append(category)
    expenses = [0.0] * len(all_possible)
    csvfile.seek(0)
    all_expenses = csv.DictReader(csvfile)
    for word in all_possible:
        for expense in all_expenses:
            if (word in expense['disb_desc']):
                expenses[all_possible.index(word)] += float(expense['disb_amt'])
        csvfile.seek(0)
        all_expenses = csv.DictReader(csvfile)

top5 = []
top5exp = []
for i in range(0,40):
        top5.append(all_possible[expenses.index(max(expenses))])
        top5exp.append(round(expenses[expenses.index(max(expenses))],2))
        expenses[expenses.index(max(expenses))] = 0
        print(top5[i],top5exp[i])