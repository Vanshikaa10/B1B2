## write a function that take one variable as input and return it sum , cumulative sum, average , min and maximum value.
#  implement this function using for loop.  define function documentation using docstring and show its uses
def display(list1)->None:
    total=0
    list2=[]
    for i in list1:
        total=total+i
        list2.append(total)
        
    length=len(list1)
    result = {
        'sum': total,
        'cumulative_sum': list2,
        'average': total / length if length > 0 else 0,
        'min': min(list1),
        'max': max(list1)
    }
    return result

list1=[10,18,21,8,20]
val=display(list1)
print(val)
