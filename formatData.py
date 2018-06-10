import codecs
# File objects

with codecs.open('cars.csv', encoding='utf-8') as rf:
    with open('cars.csv', 'a') as wf:
        size = 1
        f_contents = rf.read(size)
        while len(f_contents) > 0:
            print(f_contents)
            new = wf.write(f_contents.replace(';',','))
            print(new)
            f_contents = rf.read(size)
