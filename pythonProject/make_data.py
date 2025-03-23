with open(r'D:\Desktop\data.txt','wt',encoding='utf-8') as f:
    for i in range(1,50000000):
        f.write('{0},用户{0}\n'.format(i,i))