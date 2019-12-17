; Fizzbuzz Algorithm made by Paulo Elienay II
; Compile with: nasm -f elf fizzbuzz.asm
; Link with (64 bit systems require elf_i386 option): ld -m elf_i386 fizzbuzz.o -o fizzbuzz
; Run with: ./fizzbuzz
; TODO Properly exit to avoid seg. fault

SECTION .data
	msg db 'Fizzbuzz Algorithm! Made by Paulo Elienay II', 0Ah
	msg_len equ $-msg

	fizz db 'fizz'
	buzz db 'buzz'
	zz equ $-fizz
	num db 1

SECTION .text
global 	_start

_start:
	mov edx, msg_len
	mov ecx, msg
	mov ebx, 1
	mov eax, 4
	int	80h

	jmp main_loop

	mov	ebx, 0
	mov	eax, 1
	int	80h

main_loop:
	cmp word [num], 8
	je exit
	mov ecx, 3
	mov edx, 0
	div ecx
	cmp edx, 0
	jne .1
	mov edx, fizz
	mov ecx, zz
	mov ebx, 1
	mov eax, 4
	int 80h

	.1:
	mov ecx, 5
	mov edx, 0
	div ecx
	cmp edx, 0
	jne .2
	mov edx, buzz
	mov ecx, zz
	mov ebx, 1
	mov eax, 4
	int 80h

	.2:
	mov edx, 1
	mov ecx, 1
	mov ebx, 1
	mov eax, 4
	int 80h

	inc word [num]
	jmp main_loop

exit:
	mov edx, 1
	mov ecx, eax
	mov ebx, 1
	mov eax, 4
	int 80h
