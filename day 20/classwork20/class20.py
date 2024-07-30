def greet():
    print( 'Hello Mariam!')
    
greet()



def add ():
    print( 10+7 )

add()


def add(num1, num2):
    print(num1-num2 )
add(3,4)
add(10,8)

def add (num1, num2, operation):
    if operation== "+": #  Tu operacia udris + daprintavs jams
        print(num1+num2)
    elif operation=="-":# tu operacia unda  minuss - mashin gamoitans sxvaobas
        print(num1-num2)
    elif operation=="*":  # tu opracia udris "*"mashin dabewdas namravls
         print(num1*num2) 
    elif operation=="/": # tu opracia udris "*"mashin dabewdas namravls
        print(num1/num2)

    add(3, 4, "+")
    add(5, 6,  "-")
    add( 10, 7, "*")
    add(2, 5, "/")
