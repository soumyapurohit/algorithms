a  = [20,10,3,5,1,6]

def min(a):

    overallmin = a[0]

    for i in a:
        issmallest = True
        for j in a:
            if i>j:
                issmallest = False
        if issmallest:

            overallmin = i

    return overallmin

print(min(a))


def newmin(a):

    overallmin = a[0]

    for i in a:
        
        if i<overallmin:
            
            overallmin = i

    return overallmin

print(newmin(a))