import random
import time
import csv
# creates random data
def create_data():
    random.seed(1)
    # random.seed(time.time)
    f=open("data.csv","w")
    headers=['type','flour','milk','sugar','butter','egg','baking powder','vanilla','salt']
    header_count=len(headers)
    type=['muffin','cupcake']
    csv.DictWriter(f,headers).writeheader()
    f.close()
    samples=200
    csvFile = open('data.csv', 'a')
    for i in range(samples):
        row = [type[random.randint(0, 1)]] + [int(random.randint(30, 60)) for i in range(header_count-1)]
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
        
  
create_data()
