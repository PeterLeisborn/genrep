#Author: Peter Leisborn
#Date: 2024-09-18

while True:
    list = []
    serie = 0
    parallell = 0

    print('Hej, välkommen till resistansberäkningen!')
    
    values = input('Ange resistansvärde: ')
    list = values.split()
        
    if list == []:
        print('Serieresistans: 0')
        print('Parallellresistans: 0')
        break

    for i in range(len(list)):
        serie = serie + int(list[i])
    print(f'Serieresistans: {serie}')  

    for i in range(len(list)):
        parallell += int(list[i])**-1
    print(f'Parallellresistans: {parallell**-1}')

    break