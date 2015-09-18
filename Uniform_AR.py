"""
Uniform Activation Regime
"""
def UniAct(delta,U):
    global op1, op2
    
    act_order = range(0,999)
    for itr in range(500): 
        #random.seed(itr)
        random.shuffle(act_order)
    
        i = 0
        while i < (len(act_order)-1):
            node1 = act_order[i]
            node2 = act_order[i+1]
        
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
            
            i += 2

