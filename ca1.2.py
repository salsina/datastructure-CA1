def merge_sort(_list): 
    if len(_list) <=1:
        return
    half = len(_list)//2  
    L1 = _list[:half] 
    L2 = _list[half:]  
    merge_sort(L1) 
    merge_sort(L2) 
    x = 0
    y = 0
    z = 0
    while (x < len(L1)) and (y < len(L2)): 
        if L1[x] < L2[y]: 
            _list[z] = L1[x] 
            x+=1
        else: 
            _list[z] = L2[y] 
            y+=1
        z+=1
    
    while x < len(L1): 
        _list[z] = L1[x] 
        x+=1
        z+=1
        
    while y < len(L2): 
        _list[z] = L2[y] 
        y+=1
        z+=1

def check(list_of_temperatures):
    temperatures_min = 0
    temperatures_max = 0
    for i in range(len(list_of_temperatures)-1):
        if i%2 ==0:
            temperatures_min += list_of_temperatures[i+1] - list_of_temperatures[i]
    for i in range(int(len(list_of_temperatures)/2)):
        temperatures_max += list_of_temperatures[-i-1] - list_of_temperatures[i]
        
    return str(temperatures_min) + " " + str(temperatures_max)

lists_of_temperatures = []
a = input()
for i in range(int(a)):
    number_of_temperatures = input()
    temperatures_str = input()
    temperatures = list(map(int,temperatures_str.split()))
    merge_sort(temperatures)
    lists_of_temperatures.append(temperatures)   
for i in range(len(lists_of_temperatures)):
    print(check(lists_of_temperatures[i]))
