import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id','name'])
    writer.writerows([['0','Yamada'],['1','Sanada']])

with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
