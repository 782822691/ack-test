# import re
# def parse(text):
#     text = re.sub('[^\w]',' ',text)
#     text = text.lower()
#     l = text.split(' ')
#     l = filter(None,l)
#     # print(list(l))
#     dic = {}
#     for i in l:
#         if i not in dic:
#             dic[i] = 0
#         dic[i] += 1
#     sorted_word_cnt = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)
#     print(sorted_word_cnt)
#     return sorted_word_cnt
#
# with open('./geekbangpython/txt/in.txt','r') as f:
#     for i in f.readlines():
#         tmp = parse(i)
#         for word,count in tmp:
#             with open('./geekbangpython/txt/out.txt','a') as out:
#                 out.write('{} {}\n'.format(word,count))

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

# l = []
# dic = {}
# for value in values:
#     dic = {}
#     print('dic now is:', dic)
#     for i in range(0,len(attributes)):
#         dic[attributes[i]] = value[i]
#         print(l,'index is :'+ str(i),'value is :'+value[i])
#         print('dic now is:',dic)
#     print('before append', l)
#     l.append(dic)
#     print('after append',l)



# expected output:
[{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
{'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]

tuple1 = ([1,2],[100],3)
l1 = tuple1
tuple1[0].append(3)
l2 = [1,2,3]
l3 = l2
l2.append(4)
print(l3,l2)

# d = {'mike': 10, 'lucy': 2, 'ben': 30}
# print(sorted(d.items(),key=lambda x:x[1]))
