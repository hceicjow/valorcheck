import csv

csvfile = open('valordata.csv', newline='')

reader = csv.reader(csvfile)
errors = []

for row in reader:
    a = row[2]
    b = a.strip()
    if not a:
        row.append('No Valor added')
    else:
        if a.isdigit():
            continue
        else:
            if a[0] == '0':
                row.append('Valor can not start with \'0\'')
            if b.isdigit() and not a.isdigit():
                row.append('Please check if there are unwanted spaces  in current valor value')
            if not a.isdigit() and not b.isdigit():
                row.append('Incorrect Valor Value')
            errors.append(row)

if errors:
    errors.pop(0)

d = open('raport.csv', 'w')

writer = csv.writer(d)
tupl1 = (['Fund Name', 'Isin', 'Valor', 'Error reason'])
writer.writerow(tupl1)

for item in errors:
    writer.writerow(item)
