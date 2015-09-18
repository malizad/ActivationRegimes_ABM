"""
Compute Number of Clusters in the Final Opinion Distribution
The algortihm is adopted from Deffuant (2006) and Huet et al (2008)
"""
def CompNoClusters():
    c_min = 5
    h = 500
    w = 1000
    cluster_array = np.zeros([h,w])
    clusters = 0
    for i in range(no_of_agents):
        if i not in cluster_array:
            clusters += 1
            current_cluster = []
            current_cluster.append(i)
            for j in range(i+1,no_of_agents):
                if j not in cluster_array:
                    delta1 = op1[i] - op1[j]
                    delta2 = op2[i] - op2[j]
                    if ((delta1**2) + (delta2**2))**0.5 < epsilon:
                        current_cluster.append(j)
            for x in range (len(current_cluster)):   
                cluster_array[clusters - 1][x] = current_cluster[x]
            
    cluster_size_list = list()
    minor = 0
    for m in range(h):
        if cluster_array[m][0] == 0:
            break
        else:
            cluster_size = 0
            for n in range (w):
                if cluster_array[m][n] > 0:
                    cluster_size += 1
            if cluster_size > c_min:
                cluster_size_list.append(cluster_size)
            else:
                minor +=1
    return cluster_size_list, minor

