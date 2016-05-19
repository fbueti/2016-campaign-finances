__author__ = 'fbueti'
import csv
import heapq

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
full_states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def spendingPerState(candidate):
        path =  candidate + '.csv'
        expenses = 50 * [0.0]
        with open(path) as csvfile:
            all_expenses = csv.DictReader(csvfile)
            for expense in all_expenses:
                if (expense['recipient_st'] in states):
                    expenses[states.index(expense['recipient_st'])] += float(expense['disb_amt'])
        for i in range(0, 50):
            expenses[i] = round(expenses[i], 2)
        return expenses

bernie = spendingPerState('bernie')
hillary = spendingPerState('hillary')
trump = spendingPerState('trump')

# print (states)
# print (bernie)
# print (hillary)
# print (trump)

overall = [0.0] * 50
for i in range(0,50):
     overall[i] = round(bernie[i] + hillary[i] + trump[i],2)

state_codes = []
for i in range(0,50):
    if (i<10):
        state_codes.append("US0" + str(i))
    else:
        state_codes.append("US" + str(i))

def getTop5States(candidate):
    for max in heapq.nlargest(5, candidate):
        print (states[candidate.index(max)], max)

# getTop5States(bernie)
# getTop5States(trump)
# getTop5States(hillary)
# getTop5States(overall)
full_states_list = []
for state in states:
    full_states_list.append(full_states[state])
print (full_states_list)

csv_format = [states, trump]

zipped = zip(*csv_format)
with open('trump_by_state.csv', 'w') as f:
     writer = csv.writer(f)
     writer.writerows(zipped)
