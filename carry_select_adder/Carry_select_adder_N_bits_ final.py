#!/usr/bin/env python
# coding: utf-8

# In[13]:


def T_text(c,B,A):
    t=[]
    t.append("**********************Carry select Adder********************************************** ")
    t.append("********remember this program is only for using with ST65LIKE_cell_library_v2020_1.net")
    t.append("********so keep the library inside the folder of the netlist for fast easy using")
    t.append(".include ST65LIKE_cell_library_v2020_1.net")
    t.append(".PARAM vthVARn=xxxxxx")
    t.append(".PARAM vthVARp=-xxxxx")
    t.append(".PARAM ndepVARn=xxxxx")
    t.append(".PARAM Lmin=xxxxxxxx")
    t.append(".PARAM Wmin=xxxxxxxx")
    t.append(".PARAM tr=xxx")
    t.append(".PARAM ALIM=0.7")
    t.append("*******************************************************************************************************")
    
    
    t.append("***************************************************************Block 1*****************************")
    t.append('x'+'FA'+str(0)+' 0'+'  node1'+'  nodeS'+str(0)+'  nodeCO'+str(0)+' nodeCin'+ str(0) + '  nodeB'+str(0)+'  nodeA'+str(0)+'  FA_sub  xx=1')
    for i in range(1,B):
        t.append("                                                        ")
        t.append('x'+'FA'+str(i)+' 0'+'  node1'+'  nodeS'+str(i)+'  nodeCO'+str(i)+' nodeCO'+ str(i-1) + '  nodeB'+str(i)+'  nodeA'+str(i)+'  FA_sub  xx=1')
    t.append("                       "+"\n")
    out1 = B-1
    #         block 2
    
    for i in range(c-1):
      row = B + B*2*i
#       s = c+i*B
      s = B + B*i
      t.append("*********************  0   **************************************")
      t.append('x'+'FA'+str(row)+' 0'+'  node1'+'  nodeS'+str(s*10)+'   nodeCO'+str(s*10)+'           0'+ '     nodeB'+str(s)+'  nodeA'+str(s)+'  FA_sub  xx=1')
      for j in range(B-1):
        t.append('x'+'FA'+str(row+1+j)+' 0'+'  node1'+'  nodeS'+str(10*(s+j+1))+'  nodeCO'+str(10*(s+j+1))+'    nodeCO'+str(10*(s+j))+ '  nodeB'+str(s+j+1)+'  nodeA'+str(s+j+1)+'  FA_sub  xx=1')
      t.append("*********************  1   **************************************")
      out2 = 10*(s+B-1)
      row += B
      t.append('x'+'FA'+str(row)+' 0'+'  node1'+'  nodeS'+str((s)*10+1)+'   nodeCO'+str((s)*10+1)+'     node1'+ '   nodeB'+str(s)+'  nodeA'+str(s)+'  FA_sub  xx=1')
      for j in range(B-1):
        t.append('x'+'FA'+str(row+1+j)+' 0'+'  node1'+'  nodeS'+str(10*(s+1+j)+1)+'  nodeCO'+str(10*(s+j+1)+1)+'    nodeCO'+str(10*(s+j)+1)+ '  nodeB'+str(s+j+1)+'  nodeA'+str(s+j+1)+'  FA_sub  xx=1')
      t.append("*********************  mul   **************************************")
      m = i*B
      for j in range(B):
        t.append('xMUX_'+str(m+j)+   '            0       node1' +     '  nodez'+str(s+j)+     '  nodeS'+str(10*(s+j))+     ' nodeS'+str(10*(s+j)+1)  + ' nodeCO'+str(out1)+   '  mux21_SUB   XX=1')
      out3 = 10*(s+B-1)
      t.append("*********************  a012   **************************************")
      out4 = 2*B-1+B*i
      t.append('xAO12_' +str(i) + '          0          node1    '   'nodeCO'+str(out4 )+  ' nodeCO'+str(out1)+  ' nodeCO'+str(out3+1)+    ' nodeCO'+str(out2)+    ' AO12_SUB XX=XXX')  
      out1 = out4

    t.append("**************************************************import the test voltages after this line*********************")
    t.append("****************************************************************************************************")
    
    
    t.append(".option filetype=ascii")
    t.append(".TRAN 0.1p 820p")
    t.append(".control")
    t.append("run ")
    t.append("plot                      *****change this part for plotting*******")
    t.append(".endc")
    t.append(".end")
    
  
  
    with open("Carry_select_adder.cir", "w") as output:
        for line in t:
            output.write(line)
            output.write('\n')

    return t


# In[14]:


A = int(input("\nEnter the first bit lenght: "))

B = int(input("\nEnter any block bit length: "))

#gerd kardan
c= -(-A // B)

T_text(c,B,A)


# In[ ]:




