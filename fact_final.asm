.data
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
	
	lw $s7,0($s4)
