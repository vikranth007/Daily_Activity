# def find_union(a, b):
#     union = []
#     i ,j = 0, 0


#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             if len(union) == 0 or union[-1] != a[i]:
#                 union.append(a[i])
#             i += 1
#         else:
#             if len(union) == 0 or union[-1] != b[j]:
#                 union.append(b[j])
#             j += 1
  
#     while i < len(a):
#         if union[-1] != a[i]:
#             union.append(a[i])
#         i += 1
    
#     while j < len(b):
#         if union[-1] != b[j]:
#             union.append(b[j])
#         j += 1
#     return union


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [2, 3, 4, 4, 5, 11, 12]

# union = find_union(a, b)

# print(find_union(a, b))



#User function Template for python3


    
    #Function to return a list containing the union of the two arrays.
def findUnion(a,b):
    i ,j = 0, 0
    u = []
    
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            if len(u) == 0 or u[-1] != a[i]:
                u.append(a[i])
            i += 1
        else:
            if len(u) == 0 or u[-1] != b[j]:
                u.append(b[j])
            j += 1
            
            
    while i < len(a):
        if u[-1] != a[i]:
            u.append(a[i])
        i += 1
    
    while j < len(b):
        if u[-1] !=b[j]:
            u.append(b[j])
        j += 1
    
    return u
  


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

print(findUnion(a,b))