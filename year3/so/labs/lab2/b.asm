org 0x7c00						; Hard offset - this is where the boot sector begins

; Int 10h ax 00h - Set Video Mode
mov al, 0x3						; 80x25 text mode
mov ah, 0						; Set Video Mode
int 0x10

mov si, buffer					; SI stores the address to buffer
; Int 16h 00h: Read Next Keystroke
read_key:
	mov ah, 0
	int 0x16

	cmp ah, 0x0e				; AH = 0x0e -> BKSP pressed
	je input_bksp
	
	cmp ah, 0x1c				; AH = 0x1c -> ENTER pressed
	je input_enter
 
	cmp al, 0x20				; If ASCII < 0x20, do not try to print (Control characters)
	jge echo_char
 
	jmp read_key				; Always read for keyboard inputs


input_bksp:
	cmp si, buffer				; If buffer isn't empty...
	je read_key					; If it is, don't do anything
	dec si
	mov byte [si], 0			; Eliminate last char in buffer

;Int 10h 03h: Query Cursor Position and Size
	mov ah, 0x03
	mov bh, 0
	int 0x10

	cmp dl, 0					; If cursor is at y=0...
	jz prev_line				; Move cursor to previous line
	jmp prev_char				; Else move cursor to previous position
	
prev_char:
; Int 10h 02h: Set Cursor Position
	mov ah, 0x02
	dec dl
	int 0x10
	jmp overwrite_char

prev_line:
; Int 10h 02h: Set Cursor Position
	mov ah, 0x02
	mov dl, 79
	dec dh
	int 0x10

overwrite_char:
; Int 10h 0eH: Write Character to Cursor Location
	mov ah, 0xa					; Overwrite existing character
	mov al, 0x20				; 20h in ASCII = ' ' (Space)
	mov cx, 1					; Write only 1 space
	int 0x10
	jmp read_key				; Go back to reading input

input_enter:
;Int 10h 03h: Query Cursor Position and Size
	mov ah, 0x03
	mov bh, 0
	int 0x10					; DX will store (x,y) coordinates [DH = y, DL = x]

	sub si, buffer				; If buffer is empty, don't print anything
	jz write_newline			; Just write a new line instead
	
;Int 10h 03h: Query Cursor Position and Size
	mov ah, 0x03				; DL, DH store cursor (x,y) positions
	mov bh, 0
	int 0x10
	
	cmp dh, 24
	jl print_echo
	
;Int 10h 06h: Scroll Up / Clear Screen Rectangle
	mov ah, 0x06				; Scroll down once to make space for the string
	mov al, 1
	mov bh, 0x07				; Draw new line as White on Black
	mov cx, 0					; (0,0): Top-left corner of the screen
	mov dx, 0x184f				; (79,24): Bottom-right corner of the screen
	int 0x10
	mov dh, 0x17				; Move cursor 1 line above target
	
; Int 10h 13001H: Display String & Update Cursor
print_echo:
	mov bh, 0 					; Video page number.
	mov ax, 0
	mov es, ax 					; ES:BP is the pointer to the buffer
	mov bp, buffer

	mov bl, 0x70				; Attribute: Black on White
	mov cx, si					; String length
	inc dh						; y coordinate
	mov dl, 0					; x coordinate

	mov ax, 0x1301				; Write mode: character only, cursor moved
	int 0x10

write_newline:
	cmp dh, 24					; If at the last line of the terminal...
	je scroll_down				; Scroll screen down 1 line

;Int 10h 03h: Query Cursor Position and Size
	mov ah, 0x03				; DL, DH store cursor (x,y) positions
	mov bh, 0
	int 0x10

	jmp move_down				; Else, just move cursor downwards

;Int 10h 06h: Scroll Up / Clear Screen Rectangle
scroll_down:
	mov ah, 0x06
	mov al, 1
	mov bh, 0x07				; Draw new line as White on Black
	mov cx, 0					; (0,0): Top-left corner of the screen
	mov dx, 0x184f				; (79,24): Bottom-right corner of the screen
	int 0x10
	mov dh, 0x17				; Move cursor 1 line above target

; Int 10h 02h: Set Cursor Position
move_down:
	mov ah, 0x02				; Move the cursor at the start of the line below this one
	mov bh, 0
	inc dh
	mov dl, 0
	int 0x10
	
	add si, buffer
clear_buffer:
	mov byte [si], 0			; Replace every non 0 byte to 0 in the buffer
	inc si
	cmp si, 0
	jne clear_buffer
	mov si, buffer
	jmp read_key

echo_char:
	cmp al, 0x7f				; Don't try to print [DEL]
	jge read_key

	cmp si, buffer + 256		; If buffer is at max size (256), ignore further inputs
	je read_key
	mov [si], al
	inc si
	
; Int 10h 0eH: Write character as TTY
	mov ah, 0xe					; Echo any valid characters to screen
	int 10h
	jmp read_key

buffer: times 256 db 0x0		; Empty 256 char buffer for our code