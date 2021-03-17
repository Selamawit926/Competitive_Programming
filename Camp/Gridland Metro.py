def gridlandMetro(n, m, k, track):
    
    tot=n*m
    visited={}
    count=0

    for i in range(k):

        if track[i][0] not in visited:

            visited[track[i][0]]= (track[i][1],track[i][2])
            count+=track[i][2]-track[i][1] + 1


        else:
            prev= visited[track[i][0]]
            if track[i][1]>prev[1] or track[i][2] < prev[0]:
                count+= track[i][2]-track[i][1] + 1
                
            else:
                if track[i][1]<prev[0]:
                    count+= (prev[0]-track[i][1])
                    visited[track[i][0]]=(track[i][1],prev[1])

                if track[i][2]>prev[1]:
                    count+= (track[i][2]-prev[1])
                    visited[track[i][0]]=(prev[0],track[i][2])


    return tot-count