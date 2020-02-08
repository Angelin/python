import csv
from typing import Dict, Any, Union

with open('week1/course1_downloads/mpg.csv') as mpgfile: ## read as row
    mpg = list(csv.DictReader(mpgfile))

avg = sum(float(datae['cty']) / len(mpg) for datae in mpg)
print("avg: " + str(avg))

model = set(datae['model'] for datae in mpg)
print("unique models: ", model)


##Grouping the cars by number of cylinder, and finding the average cty mpg for each group.
def getCyl(elt):
    return elt['cyl']


mpg.sort(key=getCyl)

grouped_by_cyl = {}
old_key = 0
for datae in mpg:
    current_key = int(datae["cyl"])
    if old_key != current_key:
        old_key = current_key
        grouped_by_cyl[old_key] = []
    grouped_by_cyl[old_key].append(datae["cty"])
print(grouped_by_cyl)

cyg_avg = []
for cyl in grouped_by_cyl:
    cyg_avg[cyl] = sum(int(d) for d in grouped_by_cyl[cyl])
print(cyg_avg)


