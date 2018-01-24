import math
#Creating a function for calculating square values in a list
def sqr(list):
    return [i ** 2 for i in list]

def perimeter(Poly_X,Poly_Y,sqr): #two lists of the X and Y coordinates that form the polygon (not sorted) and the sqr function

    k = [abs((x[1] - x[0])) for x in zip(Poly_X[1:], Poly_X[:-1])]#Calculating the differences between consecutive values for X coordinates of the polygon
    m = [abs((y[1] - y[0])) for y in zip(Poly_Y[1:], Poly_Y[:-1])]#Calculating the differences between consecutive values for Y coordinates of the polygon
    lastx = abs(Poly_X[-1] - Poly_X[0])#Calculating the difference between the last and first value of the X coordinates, since the polygon has 16 line segments and the original differences are 15.
    lasty = abs(Poly_Y[-1] - Poly_Y[0])
    k.append(lastx)#Incorporating the new X difference to the list with the rest of the differences
    m.append(lasty)
    k2 = sqr(k)#Squaring the values X to fit the formula
    m2 = sqr(m)
    z = [x + y for x, y in zip(k2,m2)]
    final = [math.sqrt(i) for i in z]
    Per = sum(final)
    return Per

print "The perimeter of the polygon is: " + str(perimeter(Poly_X,Poly_Y,sqr))
