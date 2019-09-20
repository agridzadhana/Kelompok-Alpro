List = [4,7,9,13,16,18,20]
target = 9
print(List)
print("Search Number ", target)

def binary_search(List, target):
    
    first = 0
    last = len(List)-1
    found = False
    while first <= last and not found:
        mid = (first+last)//2
        if target == List[mid]:
            found = True
        elif target > List[mid]:
            first = mid+1
        else:
            last = mid-1
    if found == True:
        print("The Number is Found!")
    else:
        print("The Number Is Not Found")
binary_search(List, target)