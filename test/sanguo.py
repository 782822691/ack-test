import re

def hero_nums(hero):
    with open('./geekbangpython/txt/sanguo.txt','r',encoding='GB18030') as f:
        data = f.read().replace('\n','')
        name_num = len(re.findall(hero,data))
        return name_num
n = hero_nums('諸葛亮')
dic01 = {}
with open('./geekbangpython/txt/name.txt','r') as f :
    print(f,type(f))
    for line in f:
        name = line.split('|')
        print(name)
        for n in name:
            n_num = hero_nums(n)
            dic01[n]=n_num
            print(dic01[n])
            # print("%s出现了%s次" %(n,n_num[n]))
