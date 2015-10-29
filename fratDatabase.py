import pandas as pd

df = pd.read_csv('course_histories.csv')

name_list = [x for x in df.columns if 'Unnamed' not in x]

i = 1
while i < 17:
    for name in name_list:
        df[name] = df[name].dropna() + ' : ' + df['Unnamed: %s' % (i)].dropna()
        i += 2

for name in df.columns:
    if 'Unnamed' in name:
        del df[name]

def search():
    term = str(input("What subject are you looking for?")).upper()
    counter = 0
    for item in df:
        for course in df[item]:
            if term in str(course):
                print(item, course)
                counter += 1
    print(counter, "People Have Taken This Class")
                
search()