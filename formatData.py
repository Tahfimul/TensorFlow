import codecs
# File objects

with codecs.open('cereal.csv', encoding='utf-8') as rf:
    with open('cereal.csv', 'a') as wf:
        size = 1
        f_contents = rf.read()
        #a = wf.write(f_contents.replace('A','0'))
        #g = wf.write(f_contents.replace('G','1'))
        #k = wf.write(f_contents.replace('K','2'))
        #n = wf.write(f_contents.replace('N','3'))
        #p = wf.write(f_contents.replace('P','4'))
        #q = wf.write(f_contents.replace('Q','5'))
        h = wf.write(f_contents.replace('H,',''))
        # while len(f_contents) > 0:
        #     print(f_contents)
        #     new = wf.write(f_contents.replace(';',','))
        #     print(new)
        #     f_contents = rf.read(size)
