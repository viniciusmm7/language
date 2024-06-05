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
PUSH DWORD 0
MOV EAX, 2010
MOV [EBP - 8], EAX
MOV EAX, 2025
MOV [EBP - 4], EAX
PUSH DWORD 0
PUSH scanint
PUSH formatin
CALL scanf
ADD ESP, 8
MOV EAX, DWORD [scanint]
MOV [EBP - 12], EAX
MOV EAX, [EBP - 12]
PUSH EAX
MOV EAX, [EBP - 8]
PUSH EAX
MOV EAX, [EBP - 4]
MOV EBX, EAX
POP EAX
ADD EAX, EBX
MOV EBX, EAX
POP EAX
CMP EAX, EBX
CALL binop_jg
CMP EAX, False
JE ELSE_25
MOV EAX, [EBP - 4]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
JMP EXIT_25
ELSE_25:
MOV EAX, [EBP - 8]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
EXIT_25:

PUSH DWORD [stdout]
CALL fflush
ADD ESP, 4

MOV ESP, EBP
POP EBP

MOV EAX, 1
XOR EBX, EBX
INT 0x80