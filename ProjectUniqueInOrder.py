def unique_in_order(iterable):
    attributes = list(iterable)
    if not attributes:
        return "Empty!"
    else:
        newList = []
        newList.append(attributes[0])
        for attribute in attributes: 
            if attribute != newList[-1]: 
                newList.append(attribute)
        return newList
print(unique_in_order("AaABbbBBCccCABcBa"))
print(unique_in_order([1, 2, 2, 3, 3, 1]))
print(unique_in_order(""))