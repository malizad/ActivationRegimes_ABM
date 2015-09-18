"""
Random Activation Regime
"""
def Interact(delta,U):
    global op1, op2

    # Selecting two random agents among all agents that are immediate neighbor on the network
    #while True:
     #   node1 = random.randint(0, no_of_agents - 1)
      #  node2 = random.randint(0, no_of_agents - 1)
       # if (node1 != node2):
        #    break
            
    #random.seed(5)
    itr = [random.randint(0,999) for r in range(700000)]
    i = 0
    while i < (len(itr)):
        node1 = itr[i]
        node2 = itr[i+1]
        i += 2
    
        # Calculating new opinion based on opinion interaction rules
        
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

