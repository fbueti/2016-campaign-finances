__author__ = 'fbueti'
import csv

def top5byExp(keywords,candidate):
        path =  candidate + '.csv'
        category = []
        expenses = []
        total = 0.0
        words = keywords.split(" ")

        with open(path) as csvfile:
            all_expenses = csv.DictReader(csvfile)
            for expense in all_expenses:
                if any(word in expense['disb_desc'].lower() for word in words) and not (expense['recipient_nm'] in category):
                    category.append(expense['recipient_nm'])
                    total += float(expense['disb_amt'])
            expenses = len(category)* [0.0]
            csvfile.seek(0)
            all_expenses = csv.DictReader(csvfile)
            for item in category:
                for expense in all_expenses:
                    if(expense['recipient_nm'] == item) and any(word in expense['disb_desc'].lower() for word in words):
                        expenses[category.index(item)] += float(expense['disb_amt'])
                csvfile.seek(0)
                all_expenses = csv.DictReader(csvfile)
        top5 = []
        top5exp = []
        for i in range(0,5):
            top5.append(category[expenses.index(max(expenses))])
            top5exp.append(round(expenses[expenses.index(max(expenses))],2))
            expenses[expenses.index(max(expenses))] = 0
            print(top5[i],top5exp[i])