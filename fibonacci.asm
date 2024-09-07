.data     
.text
main:

    addi $s5,$zero,268501248
    addi $s0, $zero, 7      # Fibonacci sequence up to the 7th term
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
    lw $s4,0($t0)