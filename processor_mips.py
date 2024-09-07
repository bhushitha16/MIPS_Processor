#cube
'''.data 
.text
#program to compute sum of cube of first n=6 natural numbers
main:
	addi $s0, $zero, 6	#hardcode input of n=6 in s0
	addi $s2, $s0, 1	#storing n+1 in s2
	mul $s1, $s0, $s2	# multiplying n(n+1) and storing in s1
	srl $s1, $s1, 1		# dividing the result in s1 by 2 and storing in s1 again
	mul $s3, $s1, $s1	# squaring n(n+1)/2 using mul to get the final result
	addi $s5,$zero,268501248	#assigning memory address to s5
	sw $s3, 0($s5)		#storing the final result in address of s5
	
	lw $s6, 0($s5)'''
 
instrmem={}
 
cubemem={4194400:"00100000000100000000000000000110",
4194404:"00100010000100100000000000000001",
4194408:"00000010000100101000100000011000",
4194412:"00000000000100011000100001000010",
4194416:"00000010001100011001100000011000",
4194420:"00100000000101011011000101010000",
4194424:"10101110101100110000000000000000",
4194428:"10001110101101100000000000000000"}

#factorial
'''.data
.text
#assembly code for fnding factorial

main:
	addi $s0, $zero, 7	#storing n=7 in s0
	addi $s5, $zero, 1	
	beq  $zero, $s0, base  #checking base case for n=0
	
	addi $s6, $zero, 0

fact: 
	addi $s6, $s6, 1    
	mul $s5, $s5, $s6     
	bne $s6, $s0, fact     #keep returning to factorial function until counter s6 reaches n value
	
base:
	addi $s4,$zero,268501248	#assigning memory address to s4
	sw $s5, 0($s4)          #storing final factorial value in s4
	
	lw $s7,0($s4)'''
 
factmem={
4194432:"00100000000100000000000000000110",
4194436:"00100000000101010000000000000001",
4194440:"00010010000000000000000000000100",
4194444:"00100000000101100000000000000000",
4194448:"00100010110101100000000000000001",
4194452:"00000010101101101010100000011000",
4194456:"00010110000101101111111111111101",
4194460:"00100000000101001011000101010000",
4194464:"10101110100101010000000000000000",
4194468:"10001110100101110000000000000000"}

#fibonacci
'''.data     
.text
main:
    addi $s5,$zero,268501248
    addi $s0, $zero, 7# Fibonacci sequence up to the 7th term
    addi $s1, $zero, 0      
    addi $s2, $zero, 1      

    beq $s0, $zero, base_case    

fib:                           
    sw $s1, 0($s5)          
    add $s3, $s1, $s2       
    addi $s0, $s0, -1       
    addi $s1, $s2, 0           
    addi $s2, $s3, 0           
    bne $s0, $zero, fib        

base_case:
    addi $t0, $zero,268501248    
    sw $s1, 0($t0)
    
    lw $s4,0($t0)'''
    
fibmem={
4194472: "00100000000101011011000101010000",
4194476: "00100000000100000000000000000011",
4194480: "00100000000100010000000000000000",
4194484: "00100000000100010000000000000001",
4194488: "00010010000000000000000000000110",
4194492: "10101110101100010000000000000000",
4194496: "00000010001100101001100000100000",
4194500: "00100010000100001111111111111111",
4194504: "00100010010100010000000000000000",
4194508: "00100010011100100000000000000000",
4194512: "00010110000000001111111111111010",
4194516: "00100000000010001011000101010000",
4194520: "10101101000100010000000000000000",
4194524: "10001101000101000000000000000000"}

#data memory
datamem={45392:0}

#32 registers
reg=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#clkcycle and program counter
clk=0
pc=0


#Control Signals
memtoreg=0
memwrite=0
branch=0
aluop=00
alusrc=0
regdst=0
regwrite=0
memread=0

#instruction fields
opcode=""
rs=""
rt=""
rd=""
func=""
shamt=""
imm=""
target=""

def bintointneg(str):          #working
    temp = -(2 ** 15)
    for i in range(1, 16):
        temp += int(str[i]) * (2 ** (15 - i))
    return temp


def bintointpos(str):          #working
    dec=0
    pow=len(str)-1
    for bit in str:
        if bit=='1':
            dec+=2**pow
        pow=pow-1
    return dec


def inttobin(num):          #working
    '''if(num==0):
        return '0'
    binstr=""
    while(num>0):
        lsb=num%2
        binstr=str(lsb)+binstr
        num=num//2
    '''
    temp = bin(abs(num)).replace("0b", "")
    flag = "0"
    if(num < 0):
        flag = "1"
    while(len(temp) < 32):
        temp = flag + temp
    return temp
    
def ControlUnit(opcode):
    global memtoreg,memwrite,branch,aluop,alusrc,regdst,regwrite,memread
    if(opcode=="000000"):       #R-type
        memtoreg=0
        memwrite=0
        branch=0
        aluop=10
        alusrc=0
        regdst=1
        regwrite=1
        memread=0
    elif(opcode=="001000"):     #addi
        memtoreg=0
        memwrite=0
        branch=0
        aluop=00
        alusrc=1
        regdst=0
        regwrite=1
        memread=0       
    elif(opcode=="101011"):     #sw
        memtoreg=0
        memwrite=1
        branch=0
        aluop=00
        alusrc=1
        regdst=0
        regwrite=0
        memread=0   
    elif(opcode=="000100"):     #beq
        memtoreg=0
        memwrite=0
        branch=1
        aluop=1             #append 0 later
        alusrc=0
        regdst=0
        regwrite=0
        memread=0
    elif(opcode=="000101"):      #bne
        memtoreg=0
        memwrite=0
        branch=1
        aluop=11             #append 0 later
        alusrc=0
        regdst=0
        regwrite=0
        memread=0     
    elif(opcode=="100011"):      #lw
        memtoreg=0
        memwrite=0
        branch=0
        aluop=00           #append 0 later
        alusrc=1
        regdst=0
        regwrite=1
        memread=1   
    

def ALUControlUnit(aluop,func):
    if(aluop==00):           #lw,sw,addi
        return "010"
    elif(aluop==1):          #beq
        return "011"
    elif(aluop==11):          #bne
        return "101"            
    elif(aluop==10):         #r-type 
        if(func=="100000"):  #add
            return "010"
        elif(func=="000010"):    #srl
            return "110"
        elif(func=="011000"):     #mul
            return "111"
        
def fetch():                    #working good
    global pc,clk,instrmem
    clk=clk+1
    print("clk:",clk)
    ins=instrmem[pc]
    pc=pc+4
    return ins

def signext(str):
    if(str[0]=='1'):
        return  "1111111111111111"+ str
    else:
        return "0000000000000000"+str


    
def decode(instr):          #working good
    global opcode, rs, rt, rd, func, shamt, target, imm,clk
    opcode="0" 
    rs="0" 
    rt="0"
    rd="0"
    func="0" 
    shamt="0" 
    target="0" 
    imm="0"
    opcode=instr[0:6]
    ControlUnit(opcode)
    if(opcode=="000000"):   #r-type
        rs=instr[6:11]
        rt=instr[11:16]
        rd=instr[16:21]
        shamt=instr[21:26]
        func=instr[26:32]
    elif(opcode=="000010"):  #j-type
        target="0000"+instr[6:32]+"00"
    else:
        rs=instr[6:11]  #i type
        rt=instr[11:16]
        #imm=signext(instr[16:32])
        imm=instr[16:32]
    print("opcode: ",opcode,"rs: ", rs,"rt: ", rt,"rd: ", rd,"func: ", func,"shamt: ", shamt,"target: ", target,"imm: ", imm)
    return opcode, rs, rt, rd, func, shamt, target, imm

def ALU(reg1,operand2,operation):               #working good
    if(operation=="010"):   #lw,sw,addi,add
        #operand2=bintoint(operand2)
        print("adding:",reg1+operand2)
        return reg1+operand2
    elif(operation=="011" or operation=="101"): #beq and bne
        #operand2=bintoint(operand2)
        print("subtracting=reg1-operand2: ",reg1-operand2)
        return reg1-operand2
    elif(operation=="110"):     #srl
        #operand2=bintoint(operand2)
        reg1=inttobin(reg1)
        print("reg1: ",reg1)
        temp = "0" * operand2
        reg1= ("0"*operand2)+reg1
        print("reg1: ",reg1)
        reg1=temp + reg1[:32 - operand2+1]
        print("reg1: ",reg1)
        reg1=bintointpos(reg1)
        print("reg1: ",reg1)
        return reg1
    elif(operation=="111"):
        #operand2=bintoint(operand2)
        return reg1*operand2

        
def execute(rs, rt, rd, func, shamt, target, imm):          #working good
    global clk,pc,branch,aluop,alusrc,regdst,regwrite
    operation=ALUControlUnit(aluop,func)
    print("operation:",operation)
    reg1=reg[bintointpos(rs)]
    print("reg1:",reg1)
    if(func=="000010"):
        reg1=reg[bintointpos(rt)]
        operand2=bintointpos(shamt)
    elif(aluop==10 or aluop==1 or aluop==11): #for beq,bne,r-type
        operand2=reg[bintointpos(rt)]
    else:
        if(imm[0]=="1" and imm[1]=="1"):
            operand2=bintointneg(imm)
        else:
            operand2=bintointpos(imm)   #i-type
    print("operand2:",operand2)
    aluresult=ALU(reg1,operand2,operation)
    print("aluresult: ",aluresult)
    return aluresult

def memstg(rlt,imm,rd,opcode):
    global clk,pc,branch,memread,memwrite,memtoreg,datamem,reg
    if(branch==1 and rlt==0 and opcode=="000100"):#beq
        pc=pc+(4*bintointpos(imm))
        print("newpc:",pc)
        return 0
    elif(branch==1 and rlt!=0 and opcode=="000101"):#bne
        pc=pc+(4*bintointneg(imm))
        print("newpc:",pc)
        return 0
    else:
        if(memread==1):#lw
            print("rlt:",rlt)
            print("datamem: ",datamem[rlt])
            return datamem[rlt]
        elif(memwrite==1):  #sw
            print("rlt:",rlt)
            print(datamem[rlt])
            datamem[rlt]=reg[bintointpos(rt)]
            print("datamem: ",datamem[rlt])
        if(memtoreg==0):
            print(rlt)
            return rlt
        elif(memtoreg==1):
            print(rlt)
            return datamem[rlt]
        
def writeback(rt,rd,memoutput):
    global clk,regwrite,regdst,reg
    print("memoutput:",memoutput)
    print("bin to int rd rt:",bintointpos(rd),bintointpos(rt))
    if(regwrite==1):
        if(regdst==1):      #r-type
            reg[bintointpos(rd)]=memoutput
        else:               #i type-lw &addi
            reg[bintointpos(rt)]=memoutput
    print("wb:",reg[bintointpos(rd)],reg[bintointpos(rt)])
        

    
 
#pgm start with input
pgm=input("Enter the program('fact' or 'fib' or 'cube'): ")
if(pgm=='cube'):
    instrmem=cubemem
    pc=4194400
    while(pc<=4194428):
        print("pc:",pc)
        instr=fetch()
        opcode, rs, rt, rd, func, shamt, target, imm=decode(instr)
        aluresult=execute(rs, rt, rd, func, shamt, target, imm)
        memoutput=memstg(aluresult,imm,rd,opcode)
        writeback(rt,rd,memoutput)
        print("reg: ",reg)
        
elif(pgm=='fact'):
    instrmem=factmem
    pc=4194432
    while(pc<=4194468):
        print("pc:",pc)
        instr=fetch()
        opcode, rs, rt, rd, func, shamt, target, imm=decode(instr)
        aluresult=execute(rs, rt, rd, func, shamt, target, imm)
        memoutput=memstg(aluresult,imm,rd,opcode)
        writeback(rt,rd,memoutput)
        print("reg: ",reg)
        
        
else:
    instrmem=fibmem
    pc=4194472
    while(pc<=4194524):
        print("pc:",pc)
        instr=fetch()
        opcode, rs, rt, rd, func, shamt, target, imm=decode(instr)
        result=execute(rs, rt, rd, func, shamt, target, imm)
        memoutput=memstg(result,imm,rd,opcode)
        writeback(rt,rd,memoutput)
        print("reg: ",reg)
        
        
print("Result:",datamem[45392])


        
