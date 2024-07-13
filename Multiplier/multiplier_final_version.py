#!/usr/bin/env python
# coding: utf-8

# In[2]:


def T_text(A):
    t=[]
    t.append("***************************************Carry skip multiplier********************************************** ")
    t.append("********remember this program is only applicable with ST65LIKE_cell_library_v2020_1.net")
    t.append("********so put the library inside the folder of the netlist for fast easy usage")
    t.append("*********************************import transistor model here************************** ")
    t.append(".include ST65LIKE_cell_library_v2020_1.net")
    t.append(".PARAM vthVARn=xxxxxx")
    t.append(".PARAM vthVARp=-xxxxx")
    t.append(".PARAM ndepVARn=xxxxx")
    t.append(".PARAM Lmin=xxxxxxxx")
    t.append(".PARAM Wmin=xxxxxxxx")
    t.append(".PARAM tr=xxx")
    t.append("*********************************************************************************************************")
   
    z=0
    a = 0
    for i in range(0,A):
            t.append('xand'+str(a) +'   0'+'    node1'+'    z'+str(z)+'    y'+str(i)+'    x'+'0'+'    AND2_SUB         xx=1')
            z+=1
            a += 1
    for i in range(0,A):
            t.append('xand'+str(a) +'   0'+'    node1'+'    z'+str(z)+'    y'+str(i)+'    x'+'1'+'    AND2_SUB         xx=1')
            z+=1
            a += 1
    out1 = 1
    out2 = A
    zout = 2*A-1
    f = 0
    t.append('************************* fa **************************')
    t.append('xFA'+str(f)+' 0'+'  node1'+'  nodeZ'+str(0)+'  nodeCO'+str(0)+' '+ str(0) + '  z'+str(out2)+'  z'+str(out1)+'  FA_sub  xx=1')
    f += 1
    for g in  range(A-2) :  
        t.append('xFA'+str(f)+' 0'+'  node1'+'  nodeS'+str(g)+'  nodeCO'+str(g+1)+' '+ str(0) + '  z'+str(out2+g+1)+'  z'+str(out1+g+1)+'  FA_sub  xx=1')
        f += 1
    s = g
    out2 += A
    x = 2
    c = g+2
    out1 = 0
    for i in range(A-2):
            t.append('*******************************************************')
            for i in range(0,A):
                t.append('xand' + str(a) +'   0'+'    node1'+'    z'+str(z)+'    y'+str(i)+'    x'+str(x)+'    AND2_SUB         xx=1')
                z+=1 
                a += 1
                     
            t.append('**************************  fa **************************')
            t.append('xFA'+str(f)+' 0'+'  node1'+'  nodeZ'+str(s)+'  nodeCO'+str(c)+' nodeCO'+ str(c+1-A) + '  z'+str(out2)+'  nodeS'+str(out1)+'  FA_sub  xx=1')
            c += 1
            out1 += 1
            f+=1
            for g in  range(A-3) :  
                t.append('xFA'+str(f)+' 0'+'  node1'+'  nodeS'+str(s+g+1)+'  nodeCO'+str(c)+' nodeCO'+ str(c+1-A) + '  z'+str(out2+g+1)+'  nodeS'+str(out1)+'  FA_sub  xx=1')
                c += 1
                f += 1
                out1 += 1

            t.append('xFA'+str(f)+' 0'+'  node1'+'  nodeS'+str(s+g+2)+'  nodeCO'+str(c)+' nodeCO'+ str(c+1-A) + '  z'+str(out2+g+2)+'  z'+str(zout)+'  FA_sub  xx=1') 
            zout += A
            c +=1
            out2 += A
            x +=1
            s += 1
            f += 1
    out1 += A
    t.append("**************** last fa********************")
    
    t.append('xFA'+str(f)+' 0'+'  node1'+'  nodeZ'+str(s)+                        '  nodeCO'+str(c)        +        '   0'            +'   nodeCO'+str(c+1-A)       +'  nodeS'+str(s+g)+'  FA_sub  xx=1')
    f+=1
    c += 1
    for g in  range(1,A-2) :  
                t.append('xFA'+str(f)+' 0'+'  node1'+'  nodeZ'+str(s+g)+           '  nodeCO'+str(c)       +' nodeCO'+ str(c-1)      +' nodeCO'+ str(c+1-A)         +' nodeS'+str(s+g)+'  FA_sub  xx=1')
                c+=1
                f +=1
    t.append('xFA'+str(f)+' 0'+'  node1'+'  nodeZ'+str(s+g+1)                    +'  nodeZ'+str(s+g+2)     +' nodeCO'+ str(c-1)      +' nodeCO'+ str(c+1-A)        +'  z'+str(zout)       +'  FA_sub  xx=1')
  
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
   
    
    

    
   
  
    with open("Multiplier.cir", "w") as output:
        for line in t:
            output.write(line)
            output.write('\n')
 
    return t


# In[ ]:


A = int(input("\n enter the bit lenght: "))
The_number_of_full_adders =A*(A-1)
The_number_of_and_gates =A*A

if A <2  :
    print ("please enter an amount >2" )
else:
    
    T_text(A)

