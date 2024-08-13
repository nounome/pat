#一开始测试点3和4没过，因为id用int型存储，如果id为00000，那么用int就变成0了！！！！

n=int(input())

titles={}
authors={}
key_words={}
publishers={}
years={}

for i in range(n):
    id=input()

    title=input()
    if title in titles:
        titles[title].append(id)
    else:
        titles[title]=[id]

    author=input()
    if author in authors:
        authors[author].append(id)
    else:
        authors[author]=[id]

    key_word=input().split()
    for word in key_word:
        if word in key_words:
            key_words[word].append(id)
        else:
            key_words[word]=[id]

    publisher=input()
    if publisher in publishers:
        publishers[publisher].append(id)
    else:
        publishers[publisher]=[id]

    year=input()
    if year in years:
        years[year].append(id)
    else:
        years[year]=[id]

m=int(input())

for i in range(m):
    infomation=input()
    print(infomation)
    num,info=infomation.split(':')
    num=int(num)
    info=info.strip()

    if num==1:
        if info in titles:
            print(('\n').join([str(x) for x in sorted(titles[info])]))
        else:
            print('Not Found')
    elif num==2:
        if info in authors:print(('\n').join([str(x) for x in sorted(authors[info])]))
        else: print('Not Found')
    elif num==3:
        if info in key_words:print(('\n').join([str(x) for x in sorted(key_words[info])]))
        else: print('Not Found')   
    elif num==4:
        if info in publishers:print(('\n').join([str(x) for x in sorted(publishers[info])]))
        else: print('Not Found')
    elif num==5:
        if info in years: 
            print(('\n').join([str(x) for x in sorted(years[info])]))
        else: print('Not Found')





#ChatGPT用defaultdict 写法二：
from collections import defaultdict

n = int(input())

titles = defaultdict(list)
authors = defaultdict(list)
key_words = defaultdict(list)
publishers = defaultdict(list)
years = defaultdict(list)

for i in range(n):
    id = input().strip()

    title = input().strip()
    titles[title].append(id)

    author = input().strip()
    authors[author].append(id)

    key_word = input().strip().split()
    for word in key_word:
        key_words[word].append(id)

    publisher = input().strip()
    publishers[publisher].append(id)

    year = input().strip()
    years[year].append(id)

m = int(input())

for i in range(m):
    information = input().strip()
    print(information)
    num, info = information.split(':')
    num = int(num)
    info = info.strip()

    if num == 1:
        if info in titles:
            print('\n'.join(sorted(titles[info])))
        else:
            print('Not Found')
    elif num == 2:
        if info in authors:
            print('\n'.join(sorted(authors[info])))
        else:
            print('Not Found')
    elif num == 3:
        if info in key_words:
            print('\n'.join(sorted(key_words[info])))
        else:
            print('Not Found')
    elif num == 4:
        if info in publishers:
            print('\n'.join(sorted(publishers[info])))
        else:
            print('Not Found')
    elif num == 5:
        if info in years:
            print('\n'.join(sorted(years[info])))
        else:
            print('Not Found')
