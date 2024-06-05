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
MOV EAX, 0
MOV [EBP - 8], EAX
MOV EAX, 1
MOV [EBP - 4], EAX
MOV EAX, [EBP - 4]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
PUSH DWORD 0
MOV EAX, 0
MOV [EBP - 12], EAX
LOOP_25:
MOV EAX, [EBP - 12]
PUSH EAX
MOV EAX, 10
MOV EBX, EAX
POP EAX
CMP EAX, EBX
CALL binop_jl
CMP EAX, False
JE EXIT_25
MOV EAX, [EBP - 12]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
MOV EAX, [EBP - 12]
PUSH EAX
MOV EAX, [EBP - 4]
MOV EBX, EAX
POP EAX
ADD EAX, EBX
MOV [EBP - 12], EAX
JMP LOOP_25
EXIT_25:
MOV EAX, [EBP - 12]
PUSH EAX
MOV EAX, [EBP - 4]
MOV EBX, EAX
POP EAX
CMP EAX, EBX
CALL binop_jg
CMP EAX, False
JE ELSE_43
PUSH DWORD 0
MOV EAX, [EBP - 12]
PUSH EAX
MOV EAX, [EBP - 4]
MOV EBX, EAX
POP EAX
AND EAX, EBX
MOV [EBP - 16], EAX
PUSH DWORD 0
MOV EAX, [EBP - 12]
PUSH EAX
MOV EAX, [EBP - 4]
MOV EBX, EAX
POP EAX
OR EAX, EBX
MOV [EBP - 20], EAX
PUSH DWORD 0
MOV EAX, [EBP - 12]
PUSH EAX
MOV EAX, [EBP - 4]
MOV EBX, EAX
POP EAX
IMUL EAX, EBX
MOV [EBP - 24], EAX
PUSH DWORD 0
MOV EAX, [EBP - 12]
PUSH EAX
MOV EAX, [EBP - 4]
MOV EBX, EAX
POP EAX
IDIV EBX
MOV [EBP - 28], EAX
MOV EAX, [EBP - 16]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
MOV EAX, [EBP - 20]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
MOV EAX, [EBP - 24]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
MOV EAX, [EBP - 28]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
MOV EAX, [EBP - 16]
MOV [EBP - 16], EAX
MOV EAX, [EBP - 20]
NEG EAX
MOV [EBP - 20], EAX
MOV EAX, [EBP - 24]
NOT EAX
MOV [EBP - 24], EAX
MOV EAX, [EBP - 28]
PUSH EAX
MOV EAX, [EBP - 12]
MOV EBX, EAX
POP EAX
CMP EAX, EBX
CALL binop_je
MOV [EBP - 28], EAX
MOV EAX, [EBP - 16]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
MOV EAX, [EBP - 20]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
MOV EAX, [EBP - 24]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
MOV EAX, [EBP - 28]
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
JMP EXIT_43
ELSE_43:
MOV EAX, 1234567890
PUSH EAX
PUSH formatout
CALL printf
ADD ESP, 8
EXIT_43:

PUSH DWORD [stdout]
CALL fflush
ADD ESP, 4

MOV ESP, EBP
POP EBP

MOV EAX, 1
XOR EBX, EBX
INT 0x80