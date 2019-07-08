def checkID(k):
    '''

    :param d: Dictinary
    :param k: Key
    :return: if key exists returns value, if not returns none
    '''

    if k in idDict.keys():
        return True  # True if ID exists
    else: return False # False if ID is not in Dict

idDict = {}
usrInput = input('Please enter an ID and a name (-1 to exit): ')
while usrInput!='-1':

    if len(usrInput.split()) < 2: # if the user inserted only an ID
        print('Invalid input')
        usrInput = input('Please enter an ID and a name (-1 to exit): ')
        continue

    listInput = usrInput.split()

    if listInput[0].isdigit() == False: # ID is not only numbers. means user might have typed name first.
        print('Invalid ID')
        usrInput = input('Please enter an ID and a name (-1 to exit): ')
        continue

    if checkID(listInput[0]):
        print('ID already exists')
        usrInput = input('Please enter an ID and a name (-1 to exit): ')
        continue
    else: idDict[listInput[0]] = " ".join(listInput[1:])
    usrInput = input('Please enter an ID and a name (-1 to exit): ')



for k, v in idDict.items():
    print(f'ID: {k} Name: {v}')

