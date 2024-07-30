def add(num1, num2, operation):
    if operation== "+": #  Tu operacia udris + daprintavs jams
        print(num1+num2)
    elif operation=="-":# tu operacia unda  minuss - mashin gamoitans sxvaobas
        print(num1- num2)
    elif operation=="*":  # tu opracia udris "*"mashin dabewdas namravls
         print(num1*num2) 
    elif operation=="/": # tu opracia udris "*"mashin dabewdas namravls
        print(num1/num2)
    else: # sxvva shemxtvvevashi dabewde errori
        print("Error")

    add(3,4,"+")
    add(5,6,"-")
    add( 10,7,"*")
    add(2,5,"/")
om