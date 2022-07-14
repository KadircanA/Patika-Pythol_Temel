def flatten_list(x):
    for i in x:
        if isinstance(i, list):
            flatten_list(i)
        else:
            flattened_list.append(i)
    return flattened_list

flattened_list=[]
given_list=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print (f"Listenin her elemanı düzleştirildiğinde(flatten):{flatten_list(given_list)}")