#HW3

################################################################################
#          Name:- Aaditya Sakhardande                                          #
#          ASU ID:- 1233720594                                                 #
#          Email:- asakhar3@asu.edu                                            #
#          Date:- 01/29/2025                                                   #
# Program to solve resister network with voltage and/or current sources        #
################################################################################                                                                              #


import numpy as np                     # needed for arrays
from numpy.linalg import solve         # needed for matrices
from read_netlist import read_netlist  # supplied function to read the netlist
import comp_constants as COMP          # needed for the common constants
import os
################################################################################
# How large a matrix is needed for netlist? This could have been calculated #
# at the same time as the netlist was read in but we'll do it here #
# Input: #
# netlist: list of component lists #
# Outputs: #
# node_cnt: number of nodes in the netlist #
# volt_cnt: number of voltage sources in the netlist #
################################################################################ 
def get_dimensions(netlist):           

    columns_2_and_3 = [row[2:4] for row in netlist]   
    columns_2_3_list = [item for sublist in columns_2_and_3 for item in sublist] 
    node_cnt = max(columns_2_3_list)
    z=0 #Counter

    for i in netlist:   
        if i[0]==1:    
            z+=1
        volt_cnt=z 
    return node_cnt,volt_cnt 

################################################################################
# Function to stamp the components into the netlist                            #
# Input:                                                                       #
#   y_add:    the admittance matrix                                            #
#   netlist:  list of component lists                                          #
#   currents: the matrix of currents                                           #
#   node_cnt: the number of nodes in the netlist                               #
# Outputs:                                                                     #
#   node_cnt: the number of rows in the admittance matrix                      #
################################################################################

def stamper(y_add,netlist,currents,node_cnt):
    for comp in netlist:     
        i = comp[COMP.I] - 1
        j = comp[COMP.J] - 1

        if  comp[COMP.TYPE] == COMP.R:          
            if (i >= 0):                            
                y_add[i,i] += 1.0/comp[COMP.VAL]

            if (j>=0):
                y_add[j,j] += 1.0/comp[COMP.VAL]

            if i >= 0 and j >= 0:  
                y_add[i, j] -= 1.0 / comp[COMP.VAL]  
                y_add[j, i] -= 1.0 / comp[COMP.VAL]  

        elif comp[COMP.TYPE] == COMP.VS:   #If the component Type is: Voltage Source
            if i >= 0:
                y_add[i, node_cnt] = 1   
                y_add[node_cnt, i] = 1 
            if j >= 0:
                y_add[j, node_cnt] = -1 
                y_add[node_cnt, j] = -1 

            currents[node_cnt] = comp[COMP.VAL]
            node_cnt += 1   

        elif comp[COMP.TYPE] == COMP.IS:   #If the component Type is: Current Source
            if i >= 0:
                currents[i] -= comp[COMP.VAL]  
            if j >= 0:
                currents[j] += comp[COMP.VAL]  

    return  node_cnt
################################################################################
# Start the main program now... #
################################################################################
# Read the netlist!
netlist = read_netlist()
node_cnt,volt_cnt=get_dimensions(netlist) 

print("Node Count: ", node_cnt)
print("Voltage Count: ",volt_cnt)

#Creating the Matrix/Vector 's to be populated / stamped with the corresponding values (MUTABLE OBJECTS):
matrix_y_add= np.zeros((node_cnt+volt_cnt,node_cnt+volt_cnt)) 
currents_vec=np.zeros((node_cnt+volt_cnt,1)) 
node_cnt_result = stamper(matrix_y_add, netlist, currents_vec, node_cnt) 


print("matrix_y_add: \n", matrix_y_add)
print("Rows admittance: ", node_cnt+volt_cnt)
print("Columns admittance: ", node_cnt+volt_cnt)
print("TOTAL ROWS OF ADMITTANCE MATRIX OR TOTAL NODE COUNT: ", node_cnt_result)
solution_vec = solve(matrix_y_add, currents_vec)
print("CURRENT", currents_vec)
print("Complete Voltage Vector including current from voltage sources: \n", solution_vec)
print(type(solution_vec))

if node_cnt_result>node_cnt:  
    print(solution_vec[0:node_cnt])

else:    
    print(solution_vec)











