def intersection(arrays):

    dlist = []
    for i in arrays:
        dlist.append({j: 0 for j in i})
    
    result = dlist.pop()

    for j in dlist:
        result = list(result & j.keys())

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
