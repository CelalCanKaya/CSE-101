load R0, 48
load R1, 1
load R2, 51
load R3, 2
load R4, 50
load R5, 42
load R6, 61
load R7, 52
move RF, R4
move RF, R5
move RF, R7

Counter:

addi R0, R0, R1
addi R4, R4, R3
jmpEQ R2=R0, Final
jmp Counter

Final:

load RF, 61
move RF, R4
halt


