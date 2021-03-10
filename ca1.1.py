    
def check_inversions(list_of_heights):
    num_of_inversions = 0
    min = list_of_heights[-1]
    for i in range(len(list_of_heights)):
        if list_of_heights[-i-1] <= min:
            min = list_of_heights[-i -1]
        else:
            num_of_inversions +=1
    return num_of_inversions

lists_of_heights = []
a = input()
for i in range(int(a)):
    number_of_heights = input()
    heights_str = input()
    heights = [int(i) for i in heights_str.split()]
    lists_of_heights.append(heights)   
for i in range(len(lists_of_heights)):
    print(check_inversions(lists_of_heights[i]))
        