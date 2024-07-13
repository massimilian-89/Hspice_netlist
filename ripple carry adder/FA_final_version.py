#!/usr/bin/env python
# coding: utf-8

# In[1]:


def decimalToBinary(num):   #for when we want to import integer not knowing how log is the bit length
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')


# In[2]:


def countTotalBits(num): 
      
     binary = int(num)[2:] 
     print(len(binary)) 


# In[12]:


def T_text(n):
    t=[]
    t.append("**********************Ripple carry adder**********************************************by MHN ")
    t.append("********remember this program is only for using with ST65LIKE_cell_library_v2020_1.net")
    t.append("********so put the library inside the folder of the netlist for fast easy using")
    t.append(".include ST65LIKE_cell_library_v2020_1.net")
    t.append(".PARAM vthVARn=xxxxxx")
    t.append(".PARAM vthVARp=-xxxxx")
    t.append(".PARAM ndepVARn=xxxxx")
    t.append(".PARAM Lmin=xxxxxxxx")
    t.append(".PARAM Wmin=xxxxxxxx")
    t.append(".PARAM tr=xxx")
    t.append("************************************************************************FA0*********************************")
    t.append('x'+'FA'+' 0'+'  node1'+'  nodeS'+'0'+'  nodeCO'+'0'+' nodecin'+ '0'+ '  nodeB'+'0'+'  nodeA'+'0'+'  FA_sub  xx=1')
    for i in range(1,n):
        t.append("***************************************************************FA"+str(i)+"*****************************")
        t.append("                                                        ")
        t.append('x'+'FA'+str(i)+' 0'+'  node1'+'  nodeS'+str(i)+'  nodeCO'+str(i)+' nodeCO'+ str(i-1) + '  nodeB'+str(i)+'  nodeA'+str(i)+'  FA_sub  xx=1')
    t.append("                       "+"\n")
    
    
    
    t.append("*******************************************************simulate**************************************************************")
    t.append("*****primary pwl ")
    
    for i in range(n):
        t.append("VnodeA"+str(i)+ "     nodeA"+str(i) +"                     0              pwl (0 0 1000p 0)")
        t.append("VnodeB"+str(i)+ "     nodeB"+str(i) +"                     0              pwl (0 0 1000p 0)")
    
    
   
    t.append("*************************supply******************************************************************************")
    t.append("VDD node1 0 dc 1v")
    
    t.append("vnodecin0 nodecin0 0 dc 0")
    

    t.append("**************************************************import the test voltages after this line*********************")
    t.append("****************************************************************************************************")
    
    
    t.append(".option filetype=ascii")
    t.append(".TRAN 0.1p 820p")
    t.append(".control")
    t.append("run ")
    t.append("plot                      ")
    t.append(".endc")
    t.append(".end")
    
   
  
    with open("ripple_carry_Adder.cir", "w") as output:
        for line in t:
            output.write(line)
            output.write('\n')
 
    return t


# In[11]:


A = int(input("\nEnter the first bit lenght: "))
#decimalToBinary(A)
B = int(input("\nEnter the second bit length: "))
#decimalToBinary(B)

#p=A.bit_length()
#q=B.bit_length()


if A<=B:
    num_fulladders=B
    print("\nnumber of full adders :",num_fulladders)
    T_text(B)


else:
        num_fulladders=A
        print("\nnumber of full adders :",num_fulladders)
        T_text(A)


        

