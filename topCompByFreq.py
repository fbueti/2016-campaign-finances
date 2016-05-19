__author__ = 'fbueti'
import csv
from collections import Counter

def topCompByFreq(candidate):
        categories = []
        path = candidate + ".csv"
        with open(path) as csvfile:
            all_expenses = csv.DictReader(csvfile)
            for expense in all_expenses:
                    categories.append(expense['recipient_nm'])
            top5 = Counter(categories).most_common(5)
            for i in range (0,5):
                top5[i] = top5[i][0]
            expenses = [0.0] * 5
            csvfile.seek(0)
            all_expenses = csv.DictReader(csvfile)
            for expense in all_expenses:
                if expense['recipient_nm'] in top5:
                    expenses[top5.index(expense['recipient_nm'])] += float(expense['disb_amt'])
        for i in range(0,5):
            print ("<li>" + str(i+1) + ". " + top5[i].title() + ", $" + str('{0:,}'.format(round(expenses[i],2))) + "</li>")
# topCompByFreq('trump')
topCompByFreq('bernie')
# topCompByFreq('hillary')

# get top companies overall
# categories = []
# with open('trump.csv') as trump_file, open('bernie.csv') as bernie_file, open('hillary.csv') as hillary_file:
#         trump = csv.DictReader(trump_file)
#         bernie = csv.DictReader(bernie_file)
#         hillary = csv.DictReader(hillary_file)
#         for expense in trump:
#             categories.append(expense['recipient_nm'])
#         for expense in bernie:
#             categories.append(expense['recipient_nm'])
#         for expense in hillary:
#             categories.append(expense['recipient_nm'])
#         top5 = Counter(categories).most_common(5)
#         for i in range(0,5):
#             print (str(i+1) + ". " + top5[i][0])