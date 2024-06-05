#!/bin/bash

set -e

find asm_out -mindepth 1 -delete

script_dir="examples"

for script in "$script_dir"/*.mnl; do
    if [ -f "$script" ] && [ -r "$script" ]; then
        script_name=$(basename "$script" .mnl)
        echo "Running main.py for $script and outputting to asm_out/$script_name.asm"
        python3 main.py "$script"
    else
        echo "Error: $script is not a readable file or does not exist"
    fi
done

echo "Compiling assembly files to executables"

cd asm_out/

for assembly in *.asm; do
    if [ -f "$assembly" ] && [ -r "$assembly" ]; then
        name="${assembly%.*}"
        echo "Compiling $assembly to $name"
        nasm -f elf -o "$name".o "$assembly"
        gcc -m32 -no-pie -o "$name" "$name".o

        echo "Running $name"
        ./"$name"
        echo
    else
        echo "Error: $assembly is not a readable file or does not exist"
    fi
done