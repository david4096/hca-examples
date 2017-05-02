import csv, sys
rows = list(csv.reader(sys.stdin, delimiter='\t'))
writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
for col in xrange(0, len(rows[0])):
    writer.writerow([row[col] for row in rows])
