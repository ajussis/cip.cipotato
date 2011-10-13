import translitcodec, csv
csv_rows = csv.reader(open('persons.csv_OLD', 'rb'), delimiter=',', quotechar='"')
new_csv_file = open("persons.csv_NEW", "wb")
writer = csv.writer(new_csv_file, delimiter=',', quotechar='"')
for i in csv_rows:
    cell = unicode(i[0], "utf-8")
    cell = cell.encode("translit/long")
    i[0] = cell.replace(" ", "")
    writer.writerow(i)
    print i 
