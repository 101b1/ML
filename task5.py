import pandas as pd
import numpy as np
from sklearn.metrics import roc_curve, auc
from task3 import getData

def summ(systems, i, A, B, C):

    return A*systems[0][i] + B*systems[1][i] + C*systems[2][i]


def func(systems, A, B, C):
    return [float(summ(systems, i, A, B, C)) / float(A + B + C) for i,x in enumerate(systems[0])]


data = pd.read_csv('выгрузка.csv', ';') # выгрузим данные из csv
parametrs = list()

for i in xrange(0, 3):
    parametrs.append([i for i in xrange(1, 10)])

for i,x in enumerate(parametrs):
    A = x[i]

    for j in range(0, len(x)):
        B = x[j]

        for m in range(0, len(x)):
            C = x[m]

            # функция p = (A*p1_fraud + B*p2_fraud + C*p3_fraud)/(A + B + C)
            P = func([data['p' + str(i) + '_Fraud'] for i in xrange(1, 4)], A, B, C)

            actual, predictions = getData(P, data['CLASS'])
            false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
            roc_auc = auc(false_positive_rate, true_positive_rate)

            print('A B C')
            print(A, B, C)
            print('Gini:', (roc_auc * 2) - 1)

            print('-----------------------------------')