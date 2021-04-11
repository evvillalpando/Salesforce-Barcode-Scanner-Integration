import time
from simple_salesforce import Salesforce
import pandas as pd

passwd = ''
print('Logging into Salesforce...')

sf = Salesforce(password=passwd, username='', security_token='')

class Log:

    def __init__(self):
        self.nums = []
        self.loc = {}
        self.current = ''

    def input_num(self):
        x = str(input('Tracking No: '))

        if len(x) == 3:
            self.location_change(x)
            return True

        elif x != '':
            if len(x) > 18:
                self.nums.append(x[-12:])
            else:
                self.nums.append(x)
            return True
        else:
            self.loc[self.current] = self.nums
            return False

    def location_change(self, x):
        self.loc[self.current] = self.nums
        self.nums = []
        if x not in self.loc.keys():
            self.loc[x] = []
            self.current = x
            self.input_num()
        else:
            self.current = x
            self.input_num()

logger = Log()

x = logger.input_num()
while x is True:
    x = logger.input_num()

not_in_sf = []
for key, values in logger.loc.items():

    for value in values:
        query = sf.query_all_iter(
            "SELECT CaseNumber, Tracking_Number__c, Model_Number__c, Status, Email__c  FROM Case WHERE Tracking_Number__c = '{}'".format(value))

        list_query = list(query)

        if len(list_query) == 0:
            not_in_sf.append(value)
            continue

        else:
            if list_query[0]['Tracking_Number__c'][0] == "1":
                print(list_query[0]['CaseNumber'],'\t', 'https://www.ups.com/track?loc=null&tracknum=' + list_query[0]['Tracking_Number__c'],'\t',
                      list_query[0]['Model_Number__c'],'\t',
                      list_query[0]['Status'],'\t', key)
            else:
                print(list_query[0]['CaseNumber'], '\t',
                      'https://www.fedex.com/fedextrack/?trknbr=' + list_query[0]['Tracking_Number__c'], '\t',
                      list_query[0]['Model_Number__c'], '\t',
                      list_query[0]['Status'], '\t', key)

print("Tracking numbers not found", not_in_sf)
# print(logger.loc)
        # sf.Case.upsert('CaseNumber/' + case_number, {'Status': 'Repair in progress'})
        # print(case_number)
