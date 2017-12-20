from copy import copy

import sys
#------------------------------------------------------------------------------

#----SSTF-------
def SSTF(head_position , Request_input):
    request_queueCopy = copy(Request_input)
    head_pos = head_position
    highest = max(request_queueCopy)
    min_diff=abs(head_pos-highest)
    j=highest
    request_queueCopy.sort()
    #print request_queueCopy
    sch_list = []
    totalCost = 0
    while len(request_queueCopy) > 0:
        if min_diff == 0:
            j = max(request_queueCopy)
        for i in request_queueCopy:
            diff= abs(head_pos-i)
            if diff<min_diff:
                min_diff=diff
                j=i
        totalCost+= abs(head_pos - j)
        head_pos = j
        request_queueCopy.remove(j)
        sch_list.append(j)
        min_diff=abs(head_pos-highest)
        j=highest


    return totalCost,sch_list
#------------------------------------------------------------------------------
def main():
    request_queue = open(sys.argv[1], 'r')
    lines = request_queue.readlines()       # Read contents of txt file
    head_position = int(lines[0])
    request_queue.close()
    Request_input = lines[1].split(",")
    Request_input = [int(i) for i in Request_input]

    seektime,QueueOrder =SSTF(head_position,Request_input)
    maxWait = QueueOrder[len(QueueOrder)-1]
    totalCost = seektime

    QueueOrder = [str(i) for i in QueueOrder]
    print(", " . join(QueueOrder))
    #Seek time or the Total time to traverse all the tracks
    print totalCost
    #request waiting for the max tme and its time
    print(str(maxWait) + "," + str(totalCost))

main()
