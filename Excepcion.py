import sys 

def division (a, b):
    return a / b
 

def test (a, b):
        return division (a, b) + 42
try :
     print( test (55, int(sys.stdin.readline())))

except Exception as e :
    print("Error: {}".format(e))

5