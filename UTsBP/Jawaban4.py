list1 = ['Kalimantan', 'Sumatra ', 'Sulawesi']
list2 = ['West', 'North', 'South']
  
list2_size = len(list2)
for item in list1:
    i = 0
    while(i < list2_size):
        print(item, list2[i])
        i = i+1