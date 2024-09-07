.data 
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
	
	lw $s6, 0($s5)