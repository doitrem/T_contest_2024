def vadim(a):
    tmp_line = a.split(',')
    #print (tmp_line)
    #print (tmp_line[0])
    result_add = []
    
    for i in range(len(tmp_line)):
        if '-' in tmp_line[i]:
            split_line = tmp_line[i].split('-')
            #print(split_line[0])
            #print(split_line[1])
            
            start_from = int(split_line[0])
            fin_to = int(split_line[1])
            #print(start_from)
            #print(fin_to)
            
            tmp_i = start_from
            while tmp_i <= fin_to:
                result_add.append(tmp_i)
                tmp_i += 1
        else:
            to_int = int(tmp_line[i])
            result_add.append(to_int)
            
    for i in result_add:
        print(i, end=' ')
