dict1 = {'a': "value in a",'b': "value in b",'z': "value in z",'f': "value in f"}

def tryGetValue(d,k):
    '''

    :param d: Dictinary
    :param k: Key
    :return: if key exists returns value, if not returns none
    '''

    if k in d.keys():
        return d[k]
    else: return None

print(tryGetValue(dict1, 'a'))

def getSortedKeys(d):   # Assumes a dictionary with only string keys or only int keys
    '''

    :param d: Dictionary
    :return: list of sorted keys
    '''
    return sorted(list(d.keys()))


print(getSortedKeys(dict1))


dict2 = {1:1,2:2,3:3}

def mergeDict(d1,d2):
    '''

    :param d1: Dictionary 1 to merge
    :param d2: Dictionary 2 to merge
    :return: d3 - a new dictionary merged from both.
    '''
    d3={}
    for k,v in d1.items():
        d3[k] = v
    for k,v in d2.items():
        d3[k] = v

    return d3

dict3 = mergeDict(dict1,dict2)

print(dict3)



