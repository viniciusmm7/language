SYS_EXIT equ 1
SYS_READ equ 3
SYS_WRITE equ 4
STDIN equ 0
STDOUT equ 1
True equ 1
False equ 0

segment .data

formatin: db "%d", 0
formatout: db "%d", 10, 0
scanint: times 4 db 0

segment .bss
res RESB 1

section .text
global main
extern scanf
extern printf
extern fflush
extern stdout

binop_je:
JE binop_true
JMP binop_false

binop_jg:
JG binop_true
JMP binop_false

binop_jl:
JL binop_true
JMP binop_false

binop_false:
MOV EAX, False  
JMP binop_exit

binop_true:
MOV EAX, True

binop_exit:
RET

main:

PUSH EBP
MOV EBP, ESP
PUSH DWORD 0
PUSH scanint
PUSH formatin
CALL scanf
ADD ESP, 8
MOV EAX, DWORD [scanint]
MOV [EBP - 4], EAX
PUSH DWORD 0
PUSH scanint
PUSH formatin
CALL scanf
ADD ESP, 8
MOV EAX, DWORD [scanint]
MOV [EBP - 8], EAX
PUSH DWORD 0
MOV EAX, [EBP - 4]
MOV [EBP - 12], EAX
PUSH DWORD 0
MOV EAX, 1
MOV [EBP - 16], EAX
LOOP_23:
MOV EAX, [EBP - 16]
PUSH EAX
MOV EAX, [EBP - 8]
MOV EBX, EAX
POP EAX
CMP EAX, EBX
CALL binop_jl
CMP EAX, False
JE EXIT_23
MOV EAX, [EBP - 12]
PUSH EAX
MOV EAX, [EBP - 4]
MOV EBX, EAX
POP EAX
IMUL EAX, EBX
MOV [EBP - 12], EAX
MOV EAX, [EBP - 16]
PUSH EAX
MOV EAX, 1
MOV EBX, EAX
POP EAX
ADD EAX, EBX
MOV [EBP - 16], EAX
JMP LOOP_23
EXIT_23:
MOV EAX, [EBP - 12]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8

PUSH DWORD [stdout]
CALL fflush
ADD ESP, 4

MOV ESP, EBP
POP EBP

MOV EAX, 1
XOR EBX, EBX
INT 0x80