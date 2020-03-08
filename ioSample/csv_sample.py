import csv

with open("test.csv", 'w', newline='') as f:
    w = csv.writer(f)

    w.writerow(['test1', 'test2', 'test3'])
    w.writerows([['test1', 'test2', 'test3'], ['test1', 'test2', 'test3']])
