
def retTheDiffrence(list1 , list2):
    if(len(list1)!=len(list2)):
        raise Exception ("The sizes of lists are not the same!")
    lista=[]
    for i in range(len(list1)):
        lista.append(float(list1[i])-float(list2[i]))
    return lista


def retThePercentage(list1, list2):
    if(len(list1)!=len(list2)):
        raise Exception ("The sizes of lists are not the same!")
    lista=[]
    for i in range(len(list1)):
        lista.append((float)((list1[i]/list2[i])*100))
    return lista

def getValueInPLN(dolarCourse, comoddityInDollars):
    return dolarCourse*comoddityInDollars

def getRealValues(lista1, lista2):
    if(len(lista1)!=len(lista2)):
        raise Exception("The sizes of lists are not the same")
    lista3=[]
    for i in range(len(lista1)):
        try:
            lista3.append(float(lista1[i])*float(lista2[i]))
        except Exception as err:
            raise Exception("Something is wrong with types in calc")
    return lista3
        


def unitTest():
    mistakes=0
    lista1=[1,2,3,4,5,6]
    lista2=[2,8,7,12,17.5,16.5]
    lista3=retTheDiffrence(lista1,lista2)
    if(lista3!=[-1, -6, -4, -8, -12.5, -10.5]):
        mistakes+=1

    lista3.clear()
    lista3=retThePercentage(lista1,lista2)
    if(lista3!=[50.0, 25.0, 42.857142857142854, 33.33333333333333, 28.57142857142857, 36.36363636363637]):
        mistakes+=1

    lista1.clear()
    lista1=[1,2]
    mistakes+=1
    try:
        retThePercentage(lista2,lista1)
    except Exception as err:
        mistakes-=1

    mistakes+=1
    try:
        retTheDiffrence(lista2,lista1)
    except Exception as err:
        mistakes-=1
    
    if(mistakes==0):
        print("unit test for calculations has been passed")
        return 1
    else:
        print("unit test for calculations has been failed")
        return 0


#unitTest()


    