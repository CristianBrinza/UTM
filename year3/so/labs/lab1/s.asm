BITS 16                 ; Specify the target mode of the processor. 16-bit mode for real mode.
ORG 0x7C00              ; Set the origin. This is where the bootloader is loaded in memory by the BIOS.

start:
    cli                 ; Disable interrupts to ensure no interruptions during the bootloader execution.
    xor ax, ax          ; Set AX register to 0. XORing a register with itself is a common way to clear it.
    mov ds, ax          ; Set DS (Data Segment) register to 0.
    mov es, ax          ; Set ES (Extra Segment) register to 0.
    mov ss, ax          ; Set SS (Stack Segment) register to 0.
    mov sp, 0x7C00      ; Set SP (Stack Pointer) to 0x7C00, initializing the stack.

    call display_methods ; Call the display_methods subroutine to display the character using various methods.

    ; Infinite loop to halt the CPU after execution
    hang:
        hlt            ; Halt instruction stops the CPU execution.
        jmp hang       ; Jump to the hang label, creating an infinite loop.

display_methods:
    ; Method 1: Write character as TTY using DOS interrupt
    mov ah, 09h        ; AH=09h specifies the function to display a string.
    mov dx, msg        ; Point DX to the message string.
    int 21h            ; Call DOS interrupt 21h to display the string.
    call newline       ; Call the newline subroutine to move to the next line.

    ; Method 2: Teletype character using BIOS interrupt
    mov ah, 0Eh        ; AH=0Eh specifies the teletype function.
    mov al, 'a'        ; Load the character 'a' into AL.
    int 10h            ; Call BIOS interrupt 10h to display the character.
    call newline       ; Move to the next line.

    ; Method 3: Display character with attribute using BIOS interrupt
    mov ah, 09h        ; AH=09h specifies the function to display a character with an attribute.
    mov al, 'a'        ; Load the character 'a' into AL.
    mov bl, 07h        ; BL=07h sets the attribute (gray on black).
    mov cx, 1          ; CX specifies how many times to print the character.
    int 10h            ; Call BIOS interrupt 10h.
    call newline       ; Move to the next line.

 ; Method 4: Display character with a different attribute
    mov ah, 09h        ; AH=09h: Set the BIOS function to display a character with an attribute.
    mov al, 'a'        ; AL='a': Load the character 'a' into the AL register for display.
    mov bl, 0Fh        ; BL=0Fh: Set the attribute to bright white text on a black background.
    mov cx, 1          ; CX=1: Specify that the character should be printed only once.
    int 10h            ; Call BIOS interrupt 10h to execute the display function.
    call newline       ; Call the newline subroutine to move the cursor to the next line.

    ; Method 5: Display character, update attribute & cursor
    mov ah, 09h        ; AH=09h: Set the BIOS function to display a character with an attribute.
    mov al, 'a'        ; AL='a': Load the character 'a' into the AL register for display.
    mov bl, 02h        ; BL=02h: Set the attribute to green text on a black background.
    mov cx, 1          ; CX=1: Specify that the character should be printed only once.
    int 10h            ; Call BIOS interrupt 10h to execute the display function.
    call newline       ; Call the newline subroutine to move the cursor to the next line.

    ; Method 6: Display string using DOS interrupt
    mov ah, 09h        ; AH=09h: Set the DOS function to display a string.
    mov dx, msg        ; DX=msg: Point the DX register to the address of the msg string.
    int 21h            ; Call DOS interrupt 21h to execute the display function.
    call newline       ; Call the newline subroutine to move the cursor to the next line.

    ; Method 7: Display string and update cursor
    mov ah, 09h        ; AH=09h: Set the DOS function to display a string.
    mov dx, msg        ; DX=msg: Point the DX register to the address of the msg string.
    int 21h            ; Call DOS interrupt 21h to execute the display function.
    call newline       ; Call the newline subroutine to move the cursor to the next line.


    ; Method 8: Print directly to video memory
    mov ax, 0B800h     ; Video memory segment for color displays.
    mov es, ax         ; Set ES to point to video memory.
    mov di, 14*160     ; DI points to the 14th line on the screen.
    mov ax, 0700h | 'a'; Combine attribute (gray on black) with character 'a'.
    mov [es:di], ax    ; Write to video memory.
    call newline

    ret                ; Return from the display_methods subroutine.

newline:
    ; Print a newline character using DOS interrupt
    mov ah, 02h        ; AH=02h specifies the function to display a character.
    mov dl, 0Ah        ; ASCII for newline.
    int 21h
    mov dl, 0Dh        ; ASCII for carriage return.
    int 21h
    ret                ; Return from the newline subroutine.

msg: db 'a$', 0Ah, 0Dh, '$' ; Define the message string. '$' is a string terminator for DOS functions.

; Bootloader padding and signature
times 510-($-$$) db 0  ; Fill the remaining bytes with 0 to make the bootloader 512 bytes.
dw 0xAA55               ; Boot signature. This tells the BIOS that it's a valid bootloader.
