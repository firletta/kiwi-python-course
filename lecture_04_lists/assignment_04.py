shopping_list = []
while True:
    item = input("Shopping list item: ")
    if item == "stop":
        break
    else:
        shopping_list.append(item)
print(shopping_list)