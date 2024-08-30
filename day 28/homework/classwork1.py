def well(x):
    if x.count("good")==0:
        return "fail!"
    elif x.count("good")<=2 :
        return "Publish!"
    else: 
        return "i smell a series"