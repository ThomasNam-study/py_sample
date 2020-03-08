import csv

with open("sample1.csv", 'r') as f:
    reader = csv.reader(f)

    for c in reader:
        print(c)

with open("sample1.csv", 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print("-" * 20)


w = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

with open("output.csv", "w", newline="") as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)


with open("output2.csv", "w", newline="") as f:
    wt = csv.writer(f)

    wt.writerows(w)

# XSL
# openpyxl
# pandas 를 주로 사용 (openpyxl, xlrd
import pandas as pd

xlsx = pd.read_excel("sample.xlsx")
print(xlsx.head())
print(xlsx.tail())
print(xlsx.shape)

xlsx.to_excel("result.xlsx", index=False)
xlsx.to_csv("result.csv", index=False)
