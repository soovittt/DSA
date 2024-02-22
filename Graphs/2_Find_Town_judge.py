def create_adjacency_list(trust):
    adj = {}
    for trust_arr in trust:
        print(trust_arr)
        if(trust_arr[0] in adj.keys()):
            adj[trust_arr[0]].append(trust_arr[1])
        if(trust_arr[0] not in adj.keys()):
            adj[trust_arr[0]] = [trust_arr[1]]
        if(trust_arr[1] not in adj.keys()):
            adj[trust_arr[1]] = [] 

        # if(trust_arr[0] in adj.keys()):
        #     adj[trust_arr[0]].append(trust_arr[1])
        # if(trust_arr[1] not in adj.keys()):
        #     print("went uin e: ",trust_arr)
        #     adj[trust_arr[1]] = []
        # else:
        #     print("went uin : ",trust_arr)
        #     adj[trust_arr[0]] = [trust_arr[1]]
    return adj





def findJudge (n, trust):
    adj = create_adjacency_list(trust)
    print(adj)
    for key , value in adj.items():
        value_arr = value
        for val in value_arr:
            if( len(adj[val])==0 and [value for values in adj.values() for value in values].count(val)== len([key for key in adj.keys() if val != key])):
                return val
    return -1

print(findJudge(3,[[1,3],[2,3]]))
    