import csv
scotch_cnt = 0
with open('iowa-liquor-sample.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        for col in row:
            if "single malt scotch" in col.lower():
                #print row
                scotch_cnt += 1
                break

print scotch_cnt
