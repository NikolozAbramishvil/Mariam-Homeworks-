def add (num1, num2, operation):
    result=0
    if operation== "+":
        result=(num1+num2)
    elif operation=="-":# tu operacia unda  minuss - mashin gamoitans sxvaobas
     result= num1-num2
    elif operation=="*":  # tu opracia udris "*"mashin dabewdas namravls
         result=num1*num2 
    elif operation=="/": # tu opracia udris "*"mashin dabewdas namravls
        result=num1/num2
    else:# sxva shemtxvvevashi dabewdos errori
        result=" Error"
    
    print(add(3, 4, "+"))
    print (add(5,6,"-"))
    print(add( 10,7,"*"))
    print( add(2,5,"/"))