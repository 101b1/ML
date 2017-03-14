import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, auc
from task3 import getData
# F - fraud, G - not fraud

def es(data, p):
    '''
    Функция "переводит" решения ЭС в булево представление в соответствии с заданным порогом
    '''
    return [1 if x >= p else 0 for x in data]

def summ(systems, i):
    '''
    Суммирующая вспомогательная функция для мажритарной функции

    '''
    ans = 0
    for j in range(0, len(systems)):
        ans += systems[j][i]
    return ans

def funcMajority(systems):
    '''
    Мажоритарная функция

    '''
    return ['F' if int(0.5 + ((float(summ(systems, i)) - 0.5)/float(len(systems)))) == 1 else 'G' for i,x in enumerate(systems[0])]

def true_negativeR(data, check):
    '''
    Функция для нахождения true positive rate

    '''
    tn = len([x for i,x in enumerate(data) if (check[i] == 'F' and data[i] == 'F')]) #tn
    fp = len([x for i,x in enumerate(data) if (check[i] == 'F' and data[i] == 'G')]) #fp
    return float(tn) / float(tn+fp)

def false_positiveR (data, check):
    '''
    Функция для нахождения false negative rate
    '''
    return float(1) - true_negativeR(data, check)


data = pd.read_csv('выгрузка.csv', ';') # выгрузим данные из csv

p = 0.5 # задали решающее правило

# мажоритарная функция для всех систем
majority = funcMajority([es(data['p' + str(i) + '_Fraud'], p) for i in xrange(1, 4)])

# false positive rate для ансамбля с мажоритарной функцией
print(false_positiveR(majority, data['CLASS']))

print('----------------------')
p = 0.8 # задали решающее правило

# мажоритарная функция для всех систем
majority = funcMajority([es(data['p' + str(i) + '_Fraud'], p) for i in xrange(1, 4)])

# false positive rate для ансамбля с мажоритарной функцией
print(false_positiveR(majority, data['CLASS']))

def func(systems):
    return [float(summ(systems, i)) / float(3) for i,x in enumerate(systems[0])]


data = pd.read_csv('2016.02.20.vyygrusska.csv', ';') # выгрузим данные из csv

# функция p = (p1_fraud + p2_fraud + p3_fraud)/3
P = func([data['p' + str(i) + '_Fraud'] for i in xrange(1, 4)])

plt.figure()

actual, predictions = getData(P, data['CLASS'])
false_positive_rate, true_positive_rate, thresholds = roc_curve(actual, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)

plt.plot(false_positive_rate, true_positive_rate, label='%s ROC, AUC = %0.2f, Gini = %0.2f' % ('p_Fraud', roc_auc, (roc_auc * 2) - 1))

plt.title('Receiver Operating Characteristic')
plt.legend(loc='lower right', fontsize='small')
plt.plot([0,1],[0,1],'r--')
plt.xlim([0.0,1.0])
plt.ylim([0.0,1.0])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()