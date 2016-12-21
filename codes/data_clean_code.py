#######################################
#######################################

# Import Packages

import pandas as pd
import numpy as np
import re

#######################################
#######################################

# Read csv data

data = pd.read_csv('DY4_20161207.csv', header = None, names = ['Name','Date','Pre_Close','Open','High','Low','Close','Adj_Pre_Close','Adj_Open','Adj_High','Adj_Low','Adj_Close','Turnover_Volume','Turnover_Value','Deal_Amount','Circulation_Market_Value','Market_Value','Turnover_Rate', 'Adj_Factor','Adj_Reason'])

#######################################
#######################################

#Clean Data

# 1. Get rid of useless columns

data1 = data[['Name', 'Date', 'Adj_Pre_Close', 'Adj_Open', 'Adj_High', 'Adj_Low', 'Adj_Close', 'Turnover_Volume', 'Turnover_Value', 'Deal_Amount', 'Circulation_Market_Value', 'Market_Value', 'Turnover_Rate', 'Adj_Factor', 'Adj_Reason']]

# 2. Get rid of the stock data, which name is DY600018	

data1 = data1.iloc[:(8583871-1507)]

# 3. Fill empty cells by zeros

data1 = data1.fillna(0)

# 4. Add label column
# Our label is either 1 or -1, which depends on the difference between Adj_Pre_Close and Adj_Open. If Adj_Pre_Close is greater than Adj_Open, then label is -1; otherwise, it’s 1.

label = []
name1 = []
for i in range(len(data1['Name'])):
    if data1['Name'][i] not in name1:
        name1.append(data1['Name'][i])
        label.append(0)
        # print data1['Name'][i]
    else:
        if float(data1['Adj_Pre_Close'][i]) - float(data1['Adj_Close’][i]) >= 0:
            label.append(-1)
        else:
            label.append(1)
data1['label'] = label

# 5. Add pred1, pred2, pred3, pred4, pred5 columns
# pred1 = previous 1 day’s Adj_Close/ previous 1 day’s Adj_Pre_Close -1
# pred2 = previous 2 day’s Adj_Close/ previous 2 day’s Adj_Pre_Close -1
# pred3 = previous 3 day’s Adj_Close/ previous 3 day’s Adj_Pre_Close -1
# pred4 = previous 4 day’s Adj_Close/ previous 4 day’s Adj_Pre_Close -1
# pred5 = previous 5 day’s Adj_Close/ previous 5 day’s Adj_Pre_Close -1

pred1 = []
pred2 = []
pred3 = []
pred4 = []
pred5 = []
name2 = []
for i in range(len(data1['Name'])):
    if i in range(4571537, 4571542, 1):
        pred1.append(0)
        pred2.append(0)
        pred3.append(0)
        pred4.append(0)
        pred5.append(0)
    else:
        if data1['Name'][i] not in name2 and data1['Name'][i] != data1['Name'][i-1]:
            name2.append(data1['Name'][i])
            pred1.append(0)
            pred2.append(0)
            pred3.append(0)
            pred4.append(0)
            pred5.append(0)
            print data1['Name'][i]
        elif data1['Name'][i-1] != data1['Name'][i-2]:
            try: 
                pred1.append(float(data1['Adj_Close'][i-1])/float(data1['Adj_Pre_Close'][i-1]) - 1)
            except ZeroDivisionError:
                pred1.append(0)
            pred2.append(0)
            pred3.append(0)
            pred4.append(0)
            pred5.append(0)
        elif data1['Name'][i-2] != data1['Name'][i-3]:
            try: 
                pred1.append(float(data1['Adj_Close'][i-1])/float(data1['Adj_Pre_Close'][i-1]) - 1)
            except ZeroDivisionError:
                pred1.append(0)
            try:
                pred2.append(float(data1['Adj_Close'][i-2])/float(data1['Adj_Pre_Close'][i-2]) - 1)
            except ZeroDivisionError:
                pred2.append(0)
            pred3.append(0)
            pred4.append(0)
            pred5.append(0)
        elif data1['Name'][i-3] != data1['Name'][i-4]:
            try: 
                pred1.append(float(data1['Adj_Close'][i-1])/float(data1['Adj_Pre_Close'][i-1]) - 1)
            except ZeroDivisionError:
                pred1.append(0)
            try:
                pred2.append(float(data1['Adj_Close'][i-2])/float(data1['Adj_Pre_Close'][i-2]) - 1)
            except ZeroDivisionError:
                pred2.append(0)
            try:
                pred3.append(float(data1['Adj_Close'][i-3])/float(data1['Adj_Pre_Close'][i-3]) - 1)
            except ZeroDivisionError:
                pred3.append(0)
            pred4.append(0)
            pred5.append(0)
        elif data1['Name'][i-4] != data1['Name'][i-5]:
            try: 
                pred1.append(float(data1['Adj_Close'][i-1])/float(data1['Adj_Pre_Close'][i-1]) - 1)
            except ZeroDivisionError:
                pred1.append(0)
            try:
                pred2.append(float(data1['Adj_Close'][i-2])/float(data1['Adj_Pre_Close'][i-2]) - 1)
            except ZeroDivisionError:
                pred2.append(0)
            try:
                pred3.append(float(data1['Adj_Close'][i-3])/float(data1['Adj_Pre_Close'][i-3]) - 1)
            except ZeroDivisionError:
                pred3.append(0)
            try:
                pred4.append(float(data1['Adj_Close'][i-4])/float(data1['Adj_Pre_Close'][i-4]) - 1)
            except ZeroDivisionError:
                pred4.append(0)
            pred5.append(0)
        else:
            try: 
                pred1.append(float(data1['Adj_Close'][i-1])/float(data1['Adj_Pre_Close'][i-1]) - 1)
            except ZeroDivisionError:
                pred1.append(0)
            try:
                pred2.append(float(data1['Adj_Close'][i-2])/float(data1['Adj_Pre_Close'][i-2]) - 1)
            except ZeroDivisionError:
                pred2.append(0)
            try:
                pred3.append(float(data1['Adj_Close'][i-3])/float(data1['Adj_Pre_Close'][i-3]) - 1)
            except ZeroDivisionError:
                pred3.append(0)
            try:
                pred4.append(float(data1['Adj_Close'][i-4])/float(data1['Adj_Pre_Close'][i-4]) - 1)
            except ZeroDivisionError:
                pred4.append(0)
            try:
                pred5.append(float(data1['Adj_Close'][i-5])/float(data1['Adj_Pre_Close'][i-5]) - 1)
            except ZeroDivisionError:
                pred5.append(0)



data1[‘pred1’] = pred1
data1[‘pred2’] = pred2
data1[‘pred3’] = pred3
data1[‘pred4’] = pred4
data1[‘pred5’] = pred5


#6 Add Date_Number column
# Date_Number value is the index of date column group by each stock.

date_number = []
name = []
for i in range(len(data1['Name'])):
    if data1['Name'][i] not in name:
        a = 0
        name.append(data1['Name'][i])
        date_number.append(a)
        print data1['Name'][i]
    else:
        a += 1
        date_number.append(a)

data1['Date_Number'] = date_number

#7 Remove useless rows

name3 = []
row_index = []
for i in range(len(data1['Name'])):
    if data1['Name'][i] not in name3:
        name3.append(data1['Name'][i])
        row_index.append(i)
        row_index.append(i+1)
        row_index.append(i+2)
        row_index.append(i+3)
        row_index.append(i+4)
        #print data1['Name'][i]

data1 = data1.drop(row_index)