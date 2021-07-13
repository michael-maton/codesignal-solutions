def areFollowingPatterns(strings, patterns):
    patternMap = {}
    for i, letter in enumerate(patterns):
        if letter not in patternMap:
            if strings[i] in patternMap.values():
                return False
            patternMap[letter] = strings[i]
        
    newPattern = []
    
    for letter in patterns:
        newPattern.append(patternMap[letter])
        
    if newPattern == strings:
        return True
    return False
        
def areFollowingPatterns(strings, patterns):
    d = {}
    for i, j in zip(strings, patterns):
        if i in d and d[i] != j:
            return False
        d[i] = j
    return len(d) == len(set(d.values()))