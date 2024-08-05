def inter_bloat(Full_list):
    inter_nums =[]
    for num in Full_list:
        if num == int(num):
           inter_nums.append(num)
    return inter_nums
    Full_list = [1,2,3,4,5,6, 3.4, 6.7, 5.0]
inter_bloat(Full_list)


