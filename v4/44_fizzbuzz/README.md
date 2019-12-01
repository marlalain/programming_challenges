# Fizzbuzz

## How to run
This assembly code was made and tested only on a GNU/Linux enviroment (Arch Linux, x86_64 Linux 5.3.13-arch1-1), so if anything goes wrong you can [create a issue here](https://github.com/paulo-e/programming_challenges/issues).

First of all, install the requirements.
#### Arch Linux
```bash
sudo pacman -Sy nasm
```
#### Debian based (Debian, Ubuntu etc)
```bash
sudo apt-get update
sudo apt-get install nasm
```

#### Windows
[This should work](https://ccm.net/faq/1559-compiling-an-assembly-program-with-nasm#step-1-install-the-necessary-%3Cbr%20/%3Esoftware)

___

## Compiling

Now, compile and run the code (x86):

```bash
nasm -f elf fizzbuzz.asm
ld -m elf_i386 fizzbuzz.o -o fizzbuzz
./fizzbuzz
```

This should work in 32-bits systems:

```bash
nasm -f elf fizzbuzz.asm
ld fizzbuzz.o -o fizzbuzz
./fizzbuzz
```
 If this don't work, please [tell me](https://www.github.com/paulo-e)