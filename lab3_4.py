def sequential_search(elements, target):
    for i in range(len(elements)):
        if elements[i] == target:
            return elements[i]  
    return -1

elements = [1, 3, 5, 8, 10, 23, 35]
target = 10
result = sequential_search(elements, target)
if result==-1:
    print(f"Element {target} not found in the list")
else:
   print(f"Element {target} found in the list at index of ",result)
