import pandas as pd

def esWorked(data, check, kind, p):
    '''
    ЭС сработала
    '''
    return len([x for i,x in enumerate(data) if (x >= p and (check[i] == kind))])

def esNotWorked(data, check, kind, p):
    '''
    ЭС не сработала
    '''
    return len([x for i,x in enumerate(data) if (x < p and (check[i] == kind))])

def rate (x, y):
    return float(x) / (float(x + y))

def tp (data, check, p):
    '''
    true positive
    '''
    return rate(esWorked(data, check, 'F', p), esNotWorked(data, check, 'F', p))

def tn (data, check, p):
    '''
    true negative
    '''
    return rate(esNotWorked(data, check, 'G', p), esWorked(data, check, 'G', p))

def fn (data, check, p):
    '''
    false negative
    '''
    return 1 - tp(data, check, p)

def fp (data, check, p):
    '''
    false positive
    '''
    return 1 - tn(data, check, p)

if __name__ == '__main__':
    p = 0.5  # задали решающее правило
    data = pd.read_csv('D:\\PycharmProjects\\ML\\выгрузка.csv', ';')  # выгрузим данные из csv

    # найдем tp, fp, tn, fn для ЭС 1, 2, 3
    for i in range(1, 4):
        print('p' + str(i) + '_Fraud System')

        print('true positive rate')
        print(tp(data['p' + str(i) + '_Fraud'], data['CLASS'], p))

        print('false positive rate')
        print(fp(data['p' + str(i) + '_Fraud'], data['CLASS'], p))

        print('true negative rate')
        print(tn(data['p' + str(i) + '_Fraud'], data['CLASS'], p))

        print('false negative rate')
        print(fn(data['p' + str(i) + '_Fraud'], data['CLASS'], p))

        print('-------------------------------------------')



def searchThreshold(data, check, p):
    '''
    Функция находит такой порог для решающего правила, чтобы fp <= p
    '''
    x = 0
    y = 1
    jump = 0.01
    while x < y:
        x += jump
        falsep = fp(data, check, x)
        if falsep <= p:
            return x

falsepositive = 0.2
data = pd.read_csv('выгрузка.csv', ';') # выгрузим данные из csv

for i in range(1, 4):
    print('p' + str(i) + '_Fraud System')
    print('false positive rate threshold')
    print(searchThreshold(data['p' + str(i) + '_Fraud'], data['CLASS'], falsepositive))
    print('-------------------------------------------')
