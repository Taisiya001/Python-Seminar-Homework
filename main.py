telephone = []
data1 = str(input('Введите данные:'))
telephone.append(data1)
data = open('Telephone.txt', 'a')
data.write(f'{telephone}\n')
#data.write('LINE 1\n')
data.close()

#exit()
path = 'Telephone.txt'
data = open(path, 'r')
for line in data:
  print(line)
data.close()