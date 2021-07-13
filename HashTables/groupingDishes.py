def groupingDishes(dishes):
    table = {}
    for dish in dishes:
        for i in dish[1:len(dish)]:
            if i not in table:
                table[i] = [dish[0]]
            else:
                table[i].append(dish[0])
                
  
    sortedKeys = sorted(table)
    sortedTable = {}
    
    for key in sortedKeys:
        if len(table[key]) > 1:
            sortedRow = sorted(table[key])
            sortedTable[key] = sortedRow
            
    ret = []
    for key in sortedTable:
        temp = [key]
        for i in sortedTable[key]:
            temp.append(i)
        ret.append(temp)
        
    return ret

    
def groupingDishes2(dishes):
    table = {}
    for dish in dishes:
        for i in dish[1:len(dish)]:
            if i not in table:
                table[i] = [dish[0]]
            else:
                table[i].append(dish[0])
                
    ret = []
    for key in sorted(table):
        if len(table[key]) > 1:
            ret.append([key] + sorted(table[key]))
        
    return ret
    
