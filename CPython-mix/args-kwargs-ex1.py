def binary_search(*args, **kwargs):
    item = kwargs
    item_list = args
    first = 0
    last = len(item_list) - 1
    isfound = False
    while (first <= last and not isfound):
        mid = (first + last) // 2
        
        if item_list[mid] == item:
            isfound = True
        else:
            if item < item_list[mid]:
                last = mid - 1 
            else:
                first = mid + 1
    return isfound

''' print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5)) '''
                    
print(binary_search())
                    
                          