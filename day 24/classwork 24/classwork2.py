def string_list(str_list):
    res_list= [] 
    for string in str_list:
        
        if len(string)<=4:
            res_list.append(string)
  
         
    return res_list




print(string_list(["lizi", "Tiko","Ineza", "Elene"]))