

from typing_extensions import Required


def fibonacci(n):
    """
    Fibonacci is a function that is responsible for determine the value of index (n) in the Fibonacci Series.
    Fibonacci Series, in which each number is the sum of the two preceding ones.
    The series commonly starts from 0 and 1
    The resulting series looks like this: 
    {0, 1, 1, 2, 3, 5, 8, 13, ...}

    Input : 
        n : Integer.
    
    Output :
        return value of index (n) in the Fibonacci Series.
    """

    if( n == 0 ):
        return 0
    elif( n == 1 ):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):

    """
    Lucas is a function that is responsible for determine the value of index (n) in the lucas Series.
    Lucas Series, in which each number is the sum of the two preceding ones.
    The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. 
    The resulting series looks like this:
    {2, 1, 3, 4, 7, 11, 18, 29, ...}

    Input : 
        n : Integer.
    
    Output :
        return value of index (n) in the Lucas Series.
    """
    if ( n == 0 ):
        return 2
    elif ( n == 1):
        return 1
    else:
        lucasSeries = []
        for i in range(n+1):
            if( i == 0): lucasSeries.append(2)
            elif( i == 1): lucasSeries.append(1)
            else: 
                lucasSeries.append(lucasSeries[i-1]+lucasSeries[i-2])
        return lucasSeries[n]

def sum_series(n,idx_0 = 0 ,idx_1 = 1):
    """
    Sum Series is a function that is responsible for determine the value of index (n) in the Sum Series.
    Sum Series, in which each number is the sum of the two preceding ones.

    Sum Series function has one required parameter and two optional parameters.
    The required parameter (n) will determine which element in the series to print.
    The two optional parameters (idx_0,idx_1) will have default values of (idx_0 = 0) and (idx_1 = 1) and will determine the first two values for the series to be produced.
    Calling this function with no optional parameters will produce numbers from the fibonacci series.
    Calling it with the optional arguments (idx_0 = 2) and (idx_1 = 1) will produce values from the lucas numbers.
    Other values for the optional parameters will produce other series.
    
    The resulting series looks like this: 
    Fibonacci Series: {0, 1, 1, 2, 3, 5, 8, 13, ...}
    Lucas Series : {2, 1, 3, 4, 7, 11, 18, 29, ...}

    Input : 
        n : Integer. (Required)
        idx_0 : Integer. (Optional)
        idx_1 : Integer. (Optional)
    Output :
        return value of index (n) in the Fibonacci,Lucas or other Series.(depending on idx_0 and idx_1 values )
    """

    if( n == 0 ):
        return idx_0
    elif( n == 1 ):
        return idx_1
    else:
        return sum_series(n-1,idx_0,idx_1) + sum_series(n-2,idx_0,idx_1)

