__author__ = 'fbueti'
import csv
from collections import Counter

def top5byFreq(keywords,candidate):
        path =  candidate + '.csv'
        category = []
        expenses = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        total = 0.0
        words = keywords.split(" ")

        with open(path) as csvfile:
            all_expenses = csv.DictReader(csvfile)
            for expense in all_expenses:
                if any(word in expense['disb_desc'].lower() for word in words):
                    category.append(expense['recipient_nm'])
                    total += float(expense['disb_amt'])
            top5 = Counter(category).most_common(6)
            for i in range(0,6): top5[i] = top5[i][0]
            csvfile.seek(0)
            all_expenses = csv.DictReader(csvfile)
            for expense in all_expenses:
                if(expense['recipient_nm'] in top5):
                    expenses[(top5.index(expense['recipient_nm']))] += float(expense['disb_amt'])

        print ("Total spent on " + words[0] + ": $" + (str(round(total,2))))
        for i in range(0,6):
            print("<li>" + str(i+1)+ ". " + top5[i].title() +", $" +str('{0:,}'.format(round(expenses[i],2))) + "</li>")

# top5byFreq('air', 'trump')
top5byFreq('food cater meal', 'bernie')
# top5byFreq('travel ', 'hillary')
