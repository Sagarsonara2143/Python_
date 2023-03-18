'''
Arbitrary Arguments : It is Used when user does not know numbers of argument
                     * used before parameter and result will be tuple - always used in last or second last if **arguments available
                     ** used before parameter and result will be dictionary - always used in last
'''

def fun(a,b,c,*d,**e):
    print("A:",a," B:",b," C:",c," D:",d," E:",e)

fun(1,2,3,4,5,6,7,x=11,y=12,z=13)
