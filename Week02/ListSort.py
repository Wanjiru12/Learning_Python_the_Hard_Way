def myfunc(variance) :
    return abs(variance - 50)


marks = list((34, 87, 80, 90, 17, 59, 49))
marks.sort(key = myfunc)
print(marks)

marks.sort(reverse= True, key = myfunc)
print(marks)
