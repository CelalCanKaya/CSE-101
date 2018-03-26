load R1, 11101101b
load R2, 10101101b
load R3, 11111111b
load R5, 1b
load R7, 0
load R8, 0
load R9, 1
load RA, 10
xor R4, R2, R1
xor R4, R4, R3
Again:
load R0, 0
addi R8, R8, R9
and R6, R4, R5
addi R7, R6, R7
jmpEQ R6=R0, Finish
ror R4, 1
load R0, 8
jmpEQ R8=R0, Finish
jmp Again

Finish:
load RB, 48
addi RF, R7, RB
halt

