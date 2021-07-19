def containsCloseNums(nums, k):
    idxMap = {}
    for i, num in enumerate(nums):
        if num not in idxMap:
            idxMap[num] = [i]
        else:
            idxMap[num].append(i)

    for key in idxMap:
        if len(idxMap[key]) == 2:
            if idxMap[key][1] - idxMap[key][0] <= k:
                return True
        elif len(idxMap[key]) > 2:
            for i in range(len(idxMap[key]) - 1):
                if idxMap[key][i + 1] - idxMap[key][i] <= k:
                    return True
                
    return False