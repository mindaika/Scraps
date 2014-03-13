__author__ = 'Randall'
import math

class LexicographicPermute:
    # I used 0-9 instead of 1-10 because the join creates strings, and the string
    # "910" is considered out of lexicographic order, even though it is numerically
    # correct
    mylist = [0,1,2,3,4,5,6,7,8]
    perms = list(mylist)
    permlist = list()
    cont = False
    j = 0
    i = 0
    permlist.append( ''.join( map( str,perms ) ) )

    for x in range( ( len(mylist)-1 ), 0, -1 ):
        if ( perms[x] > perms[x-1] ):
            cont = True

    while cont == True:
        for x in range( 0, len(mylist)-1, 1 ):
            if ( perms[x] < perms[x+1] ):
                i = x

        for x in range( i+1, len( mylist ), 1 ):
            if ( perms[i] < perms[x] ):
                j = x
        perms[i], perms[j] = perms[j], perms[i]
        perms[i+1:len( mylist )] = reversed( perms[i+1:len( mylist )] )
        permlist.append( ''.join( map( str,perms ) ) )
        cont = False
        for x in range( 0, len(mylist)-1, 1 ):
            if ( perms[x] < perms[x+1] ):
                cont = True

    # Test to see if the list is in order
    if sorted( permlist ) == permlist:
        print ( "The list is in order" )
    else:
        print ( "The list is not in order" )

    # Check for length
    print ("I spy " + str(len(permlist)) + " permutations in this trial." )
    if math.factorial(len(mylist))==len(permlist):
        print ( "There are the correct number of permutations" )
    else:
        print ( "There are not the correct number of permutations" )

    # Check for duplicates
    if len(permlist)!=len(set(permlist)):
        print ( "There are duplicates" )
    else:
        print ( "There are no duplicates ")