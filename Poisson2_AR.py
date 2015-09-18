# Poisson activation regime when moderate agents have higher chance of interaction

def PoisAct2(delta,U):
    global op1, op2
    for itr in range(2000):
        abs_op1 = list()
        abs_op2 = list()
        op = list()
        l = list() # list contains lambda values for each agent
        for ag in range(len(op1)):
            abs_op1.append(abs(op1[ag]))
        for ag in range(len(op2)):
            abs_op2.append(abs(op2[ag]))
        for ag in range(len(op1)):
            op.append(abs_op1[ag] + abs_op2[ag])
        max_op = max(op)
        min_op = min(op)
        for ag in range(no_of_agents): # populating the lambda list with normalized total absolute opinions
            l.append((op[ag] - min_op)/(max_op - min_op))
            
        # computing agents' first activation time
        act_list = list()
        time_list = list()
        temp = list()
        for ag in range(len(op)):
            if l[ag] != 0:
                nextT = -1 * log(random.random()) / (1/l[ag])
                while nextT < 2.0:
                    act_list.append((nextT, ag))
                    temp.append(ag)
                    nextT = nextT + -1 * log(random.random()) / l[ag]
        
        if len(act_list) % 2 > 0:
            act_list.pop()  # Makes sure the list is even in length. I will need pairs of agents.
        act_list.sort()
        arrQ = deque(act_list)
        for i in range(250):
            if len(arrQ) < 2:   # Checking there is still one pair left.
                break
            t1, node1 = arrQ.popleft()  # Pop off the next two agents and process them.
            t2, node2 = arrQ.popleft()
            while node1 == node2:
                t2, node2 = arrQ.popleft()
                    # Calculating new opinion based on opinion interaction rules
            #pair += 1    
            op1_diff = abs (op1[node2] - op1[node1])
            op2_diff = abs (op2[node2] - op2[node1])
                        
                            
            if (op1_diff <= U) and (op2_diff <= U):
                op1[node1] = op1[node1] + mu * (op1[node2] - op1[node1])
                op2[node1] = op2[node1] + mu * (op2[node2] - op2[node1])
                op1[node2] = op1[node2] + mu * (op1[node1] - op1[node2])
                op2[node2] = op2[node2] + mu * (op2[node1] - op2[node2])
                    
            elif (op1_diff > U) and (op2_diff <= U) and (op1_diff <= (1 + delta) * U):
                op2[node1] = op2[node1] + mu * (op2[node2] - op2[node1])       
                op2[node2] = op2[node2] + mu * (op2[node1] - op2[node2]) 
                                
            elif (op1_diff <= U) and (op2_diff > U) and (op2_diff <= (1 + delta) * U):       
                op1[node1] = op1[node1] + mu * (op1[node2] - op1[node1])
                op1[node2] = op1[node2] + mu * (op1[node1] - op1[node2])
                                
            elif (op1_diff > U) and (op2_diff <= U) and (op1_diff > (1 + delta) * U):
                op2[node1] = op2[node1] - mu * psign(op2[node2] - op2[node1]) * (U - op2_diff)
                op2[node2] = op2[node2] - mu * psign(op2[node1] - op2[node2]) * (U - op2_diff)            
                    
            elif (op1_diff <= U) and (op2_diff > U) and (op2_diff > (1 + delta) * U):
                op1[node1] = op1[node1] - mu * psign(op1[node2] - op1[node1]) * (U - op1_diff)
                op1[node2] = op1[node2] - mu * psign(op1[node1] - op1[node2]) * (U - op1_diff)
        # bounding the opinions between -1 and 1
            if abs(op1[node1]) > 1: op1[node1] = psign(op1[node1])
            if abs(op1[node2]) > 1: op1[node2] = psign(op1[node2])
            if abs(op2[node1]) > 1: op2[node1] = psign(op2[node1])
            if abs(op2[node2]) > 1: op2[node2] = psign(op2[node2])

