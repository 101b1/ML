"""import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

n_bins = 10
x = np.random.randn(1000, 3)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()

colors = ['red', 'tan', 'lime']
ax0.hist(x, n_bins, normed=1, histtype='bar', color=colors, label=colors)
ax0.legend(prop={'size': 10})
ax0.set_title('bars with legend')

ax1.hist(x, n_bins, normed=1, histtype='bar', stacked=True)
ax1.set_title('stacked bar')

ax2.hist(x, n_bins, histtype='step', stacked=True, fill=False)
ax2.set_title('stack step (unfilled)')

# Make a multiple-histogram of data-sets with different length.
x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
ax3.hist(x_multi, n_bins, histtype='bar')
ax3.set_title('different sample sizes')

fig.tight_layout()
plt.show()"""
import csv
import matplotlib.pyplot as plt


"""def equalize(x_l, y_l):
    if len(x_l) > len(y_l):
        return len(x_l)
    else:
        return len(y_l)"""


def str_parse(itr, op_list, op_dict):
    if itr not in op_dict:
        op_dict[itr] = len(dict.items(op_dict))
    list.append(op_list, op_dict[itr])


def is_str(itr, op_list, op_dict):
    try:
        list.append(op_list, float(itr))
    except ValueError:
        str_parse(itr, op_list, op_dict)

print(float('0'))
x_i = input('Enter X column name: ')
x_j = input('Enter Y column name: ')

with open('выгрузка.csv') as fl:
    reader = csv.reader(fl, delimiter=';')
    rownum = 0
    xf_list = []
    yf_list = []
    xg_list = []
    yg_list = []
    xu_list = []
    yu_list = []
    x_dict = {}
    y_dict = {}
    for row in reader:
        if rownum == 0:
            header = row
            i = 0
            dict_header = {}
            for elem in header:
                dict_header[elem] = i
                i += 1
            rownum += 1
        elif rownum > 2000:
            break
        else:
            if row[dict_header[x_i]] == '' or row[dict_header[x_j]] == '':
                rownum += 1
                continue
            else:
                if row[dict_header['CLASS']] == 'F':
                    is_str(row[dict_header[x_i]], xf_list, x_dict)
                    is_str(row[dict_header[x_j]], yf_list, y_dict)
                elif row[dict_header['CLASS']] == 'G':
                    is_str(row[dict_header[x_i]], xg_list, x_dict)
                    is_str(row[dict_header[x_j]], yg_list, y_dict)
                elif row[dict_header['CLASS']] == 'U':
                    is_str(row[dict_header[x_i]], xu_list, x_dict)
                    is_str(row[dict_header[x_j]], yu_list, y_dict)
                else:
                    rownum += 1
                    continue
            rownum += 1
            """if row[dict_header[x_i]] == '' or row[dict_header[x_j]] == '':
                rownum += 1
                continue
            else:
                x_list.append(row[dict_header[x_i]])
                y_list.append(row[dict_header[x_j]])
            rownum += 1"""


fig = plt.figure()
plt.scatter(xg_list, yg_list, color='blue')
plt.scatter(xf_list, yf_list, color='red', alpha='0.5')
plt.scatter(xu_list, yu_list, color='yellow', alpha='0.25')
plt.xlabel(x_i)
plt.ylabel(x_j)
plt.show()
