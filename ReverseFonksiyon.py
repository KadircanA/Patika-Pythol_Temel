def reserve_list(list) :
     list=list[::-1]
     reserved_list=[]
     for i in range(len(list)):
            reserved_list.append(list[i][::-1])
     return reserved_list

givenlist=[[1, 2], [3, 4], [5, 6, 7, 8]]
print (f"Listenin her elemanın tersi alındığında:{reserve_list(givenlist)}")