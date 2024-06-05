#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <file_to_compile.mnl>"
    exit 1
fi

FILENAME=$(basename -- "$1")
BASENAME="${FILENAME%.*}"

python3 main.py "$1"
cd asm_out/
nasm -f elf -o "${BASENAME}.o" "${BASENAME}.asm"
gcc -m32 -no-pie -o "${BASENAME}" "${BASENAME}.o"

echo "Compiled successfully to ${BASENAME}"
echo "Run ./asm_out/${BASENAME} to execute"