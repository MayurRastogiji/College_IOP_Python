a = int(input("enter side a  :"))
b = int(input("enter side b  :"))  
c = int(input("enter side c  :"))
def triangle(a,b,c ):
 if (a+b>c)and(b+c>a)and(a+c>b): 
    {
     print( "It is a triangle!")
    }
 
 else:
    print("It is not a triangle!")
    
    
triangle(a,b,c)