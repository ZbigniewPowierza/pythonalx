my_list = [1, "a", "ala", "kot", 121]
print(my_list[0])

my_list2 = [1, 2, 3, my_list]
print(my_list2[3])
print(my_list2[3][2])
print(dir(my_list)) #sprawdzamy jakie metody działają na liście
print(my_list.append(10))
#   my_list.append(10)
print(my_list)

print(my_list.pop())
print(my_list.pop())
print(my_list)


#łączenie list
a = [1,2,3]
b = [3,4,5]
print(a+b)
a.extend(b)
c = a + b
print(c)

# podmiana elementu w liście
a[0] = 100
print(a)
# w tupli to nie działa
x = (1,2,3)
#x(0) = 100 # SyntaxError: can't assign to function call
y = (4,5,6)
x = x + y
print(x.index(3))
print(3 in x)
print(x)
print("y" in "abecadło")