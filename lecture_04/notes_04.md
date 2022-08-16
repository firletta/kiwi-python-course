``` python
shopping_list = ["milk", "apples", "bread", "cereals", "toilet paper"]
shopping_list[0] == "milk"
shopping_list[1] == "apples"
shopping_list[2] == "bread"
shopping_list[3] == "cereals"
shopping_list[4] == "toilet paper"
```

``` python
shopping_list = ["milk", "apples", "bread", "cereals", "toilet paper"]
for i in range(5):
	print(shopping_list[i])
```

You can generate a list of integers like so:
``` python
list(range(5)) == [0, 1, 2, 3, 4]
list(range(2,8)) == [2, 3, 4, 5, 6, 7]
```

You can get numbers of elements in the list:
``` python
shopping_list = ["milk", "apples", "bread", "cereals", "toilet paper"]
len(shopping_list) == 5
```

We often use it in the conditions or in the definition of the `for` loops:
``` python
if len(shopping_list) == 0:
print("Shopping list is empty")

for i in range(len(shopping_list)):
	print(shopping_list[i]))
```

We can dynamically add and remove items from a list, using append and pop functions:
``` python
shopping_list = ["milk", "bread"]
shopping_list.append("apples")
shopping_list == ["milk", "bread", "apples"]
shopping_list.pop()
shopping_list == ["milk", "bread"]
```
Or we can easily reverse the order of the items in the list:
``` python
shopping_list.reverse()
shopping_list == ["bread", "milk"]
```

---

``` python
[expression for item in iterable if condition == True]
```