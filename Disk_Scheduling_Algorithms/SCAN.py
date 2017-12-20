from copy import copy

import sys
#------------------------------------------------------------------------------

#------------------------SCAN--------------------------------------------------
def SCAN(head_position , Request_input):
    head_pos = head_position
    request_queueCopy = copy(Request_input)
    totalCost = 0
    Queue_Right=[]
    Queue_Left=[]
    QueueOrder=[]
    diff_Q=[]
    check_if = 1
    a = b = 0
    request_queueCopy.sort()

    for i in range(len(request_queueCopy)):
#greater than head
        if(head_pos < request_queueCopy[i]):
            Queue_Right.append(request_queueCopy[i])
#lesser than head
        elif(head_pos > request_queueCopy[i]):
            Queue_Left.append(request_queueCopy[i])

    Queue_Left.reverse()
# a and b gives the minimun distance the track has to travel to serve requests on left n right
    if len(Queue_Right)!= 0 :a = abs(head_pos-Queue_Right[0])
    else:a=0
    if len(Queue_Left)!= 0 :b = abs(head_pos-Queue_Left[0])
    else:b=0

    if  a == b :
        Queue_Left.append(0)
        QueueOrder = Queue_Left + Queue_Right
        check_if=0
    elif a == 0:
        QueueOrder =  Queue_Left
    elif b == 0:
        QueueOrder =  Queue_Right
    elif a < b:
        Queue_Right.append(199)
        QueueOrder = Queue_Right + Queue_Left
        check_if=199
    elif a > b :
        Queue_Right.append(199)
        QueueOrder = Queue_Left + Queue_Right
        check_if=199
    seektime=0
    j=0
    while j < len(QueueOrder) :
        diff=abs(head_pos-QueueOrder[j])
        diff_Q.append(diff)
        seektime=seektime+diff
        head_pos=QueueOrder[j]
        j=j+1
    if check_if==0:
        QueueOrder.remove(0)
    elif check_if==199:
        QueueOrder.remove(199)

    return seektime,QueueOrder

#-----------------------------Main-------------------------------------------------
def main():
    request_queue = open(sys.argv[1], 'r')
    lines = request_queue.readlines()       # Read contents of txt file
    head_position = int(lines[0])
    request_queue.close()
    Request_input = lines[1].split(",")
    Request_input = [int(i) for i in Request_input]


    seektime,QueueOrder = SCAN(head_position,Request_input)
    QueueOrder = [str(i) for i in QueueOrder]
    print(", " . join(QueueOrder))
    totalCost = seektime
    maxWait = QueueOrder[len(QueueOrder)-1]

    #Seek time or the Total time to traverse all the tracks
    print totalCost
    #request waiting for the max tme and its time
    print(str(maxWait) + "," + str(seektime))


main()
