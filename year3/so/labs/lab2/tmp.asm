Doubling the Character When Reading Key:
In the read_key label, right after saving the key to the buffer and before echoing it to the screen, you should add an extra instruction to print the character a second time.


read_key:
    ...
    mov [si], al               ; Move the key from AL to the buffer location pointed by SI.
    inc si                     ; Increment SI to point to the next position in the buffer.
    mov ah, 0x0E
    int 0x10                   ; Call interrupt 0x10 to display the character on screen.
    
    ; Duplicate the print instruction to echo the character a second time
    mov ah, 0x0E
    int 0x10                   ; Call interrupt 0x10 again to display the character a second time.

    jmp read_key               ; Jump back to 'read_key' to read the next key.



Doubling Each Character in the print_string Subroutine:
Within the print_string subroutine, you will have to repeat the instruction that prints each character. This will ensure that each character in the buffer is printed twice when the buffer content is displayed.


print_string:
    .print_char:
        mov al, [di]           ; Load the character from the buffer.
        or al, al
        jz .done               ; Jump to '.done' if it's the end of the string.

        mov ah, 0x0E
        int 0x10               ; Print the character.

        ; Repeat the print instruction to display the character a second time.
        mov ah, 0x0E
        int 0x10               ; Print the character again.

        inc di                 ; Move to the next character in the buffer.
        jmp .print_char        ; Repeat for the next character.

    .done:
        ret




To modify the code so that it prints the input string in the next row after pressing the Enter key, we need to adjust the handle_enter routine. Currently, it seems to print the input string immediately after the Enter key is pressed without moving to a new line first. The change involves adding a call to print_newline before printing the input string. Here's the revised handle_enter section:


handle_enter:
    mov di, si
    sub di, BUFFER_OFFSET
    test di, di                ; Test if DI is 0 (no characters input).
    jz clear_buffer            ; If DI is 0, jump to 'clear_buffer'.

    ; Move to a new line before printing the input string
    call print_newline         ; Add this line to move to the next line.

    mov di, BUFFER_OFFSET      ; Reset DI to the start of the buffer.
    call print_string          ; Call a subroutine to print the string from the buffer.
    call print_newline         ; Optionally, add another newline for spacing after printing.

    jmp clear_buffer           ; Clear the buffer after printing the string.