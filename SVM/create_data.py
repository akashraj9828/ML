import random
import time
import csv
# creates random data
def create_data():
    # random.seed(1)
    random.seed(time.time)
    f=open("data.csv","w")
    headers=['type','flour','milk','sugar','butter','egg','baking powder','vanilla','salt']
    header_count=len(headers)
    type=['muffin','cupcake']
    csv.DictWriter(f,headers).writeheader()
    f.close()
    samples=300
    csvFile = open('data.csv', 'a')
    for i in range(samples):
        t = random.randint(0, 1)
        row = [type[t]]
        if t==0:
            row=row + [int(random.randint(50, 100)) for i in range(header_count-1)]
        if t==1:
            row=row + [int(random.randint(0, 50)) for i in range(header_count-1)]
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()

def create_test_data():
    # random.seed(1)
    random.seed(time.time)
    f=open("test.csv","w")
    headers=['type','flour','milk']
    header_count=len(headers)
    type=['muffin','cupcake']
    csv.DictWriter(f,headers).writeheader()
    f.close()
    samples=100
    csvFile = open('test.csv', 'a')
    for i in range(samples):
        t = random.randint(0, 1)
        row = [type[t]]
        if t==0:
            row=row + [int(random.randint(50, 100)) for i in range(header_count-1)]
        if t==1:
            row=row + [int(random.randint(0, 50)) for i in range(header_count-1)]
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()

create_data()
create_test_data()
        















create_test_data()
# create_data()
