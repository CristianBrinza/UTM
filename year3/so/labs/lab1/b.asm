org 0x7c00					; Hard offset - this is where the boot sector begins

mov al, 0x3					; 80x25 text mode
mov ah, 0					; Set Video Mode
int 0x10
	
; Method 1: ah 0eH: Write character as TTY
mov si, msg1

char_m1:
	mov al, [si]			; Copy char to be printed into AL

	mov ah, 0xe				; Print the char
	int 0x10
	inc si					; Move to next char in string
	cmp byte [si], 0		; If char is null, end loop
	jne char_m1

mov si, 0

; Method 2: ah 0aH: Write character
char_m2:
	mov bh, 0				; Set Video Page to 0
	mov dx, si				; y = 0, x = SI
	mov dh, 1				; y = 1, x = SI
	mov ah, 0x2				; Move cursor to (x,y)
	int 0x10

	mov al, [msg2 + si]		; Copy char to be printed into AL
	mov bh, 0				; Set Video Page to 0
	mov cx, 1				; Repeat count = 1

	mov ah, 0xa				; Print the char
	int 0x10
	
	inc si					; Move to next char in string
	cmp byte [msg2 + si], 0	; If char is null, end loop
	jne char_m2

mov si, 0

; Method 3: ah 09H: Write character/attribute
char_m3:
	mov bh, 0				; Set Video Page to 0
	mov dx, si				; y = 0, x = SI
	mov dh, 2				; y = 2, x = SI
	mov ah, 0x2				; Move cursor to (x,y)
	int 0x10

	mov al, [msg3 + si]		; Copy char to be printed into AL
	mov bh, 0				; Video page number
	mov bl, 0x8b			; Attribute: Blinking Cyan
	mov cx, 1				; Repeat twice

	mov ah, 0x9
	int 0x10
	
	inc si					; Move to next char in string
	cmp byte [msg3 + si], 0	; If char is null, end loop
	jne char_m3

; Method 4: ax 1302H: Display Character/Attribute Cells
mov bh, 0					; Video page number
mov cx, 7					; String length 
mov dh, 3					; y coordinate
mov dl, 0					; x coordinate

mov ax, 0
mov es, ax					; ES:BP is the pointer to string
mov bp, msg4

mov ax, 0x1302
int 0x10

; Method 5: ax 1303H: Display Char/Attr Cells & Update Cursor
mov bh, 0					; Video page number
mov cx, 9					; String length
mov dh, 4					; y coordinate
mov dl, 0					; x coordinate

mov ax, 0
mov es, ax					; ES:BP is the pointer to string
mov bp, msg5

mov ax, 0x1303
int 0x10

; Method 6: ax 13000H: Display String
mov bh, 0 					; Video page number
mov ax, 0
mov es, ax 					; ES:BP is the pointer to string.
mov bp, msg6

mov bl, 0x78				; Attribute: Dim Gray on White
mov cx, 21					; String length
mov dh, 5					; y coordinate
mov dl, 0					; x coordinate

mov ax, 0x1300
int 0x10


; Method 7: ax 13001H: Display String & Update Cursor
mov bh, 0 					; Video page number.
mov ax, 0
mov es, ax 					; ES:BP is the pointer to string
mov bp, msg7

mov bl, 0x0e				; Attribute: Yellow on Black
mov cx, 30					; String length
mov dh, 6					; y coordinate
mov dl, 0					; x coordinate

mov ax, 0x1301				; Write mode: character only, cursor moved
int 0x10


; Method 8: Write to Video Memory
mov ax, 0xb800				; ES:DI Address b800:0 - Start address of video memory
mov es, ax
mov di, 0x460				; x = 0, y = 7 -> DX = A0 * 7 = 460
mov cx, 0					; CX - index in upcoming loop
mov si, msg0				; Address of text

str_loop:
	inc cx
	
	mov al, [si]			; Get char from string
	stosb					; Write AL at ES:DI in memory
	inc si					; Move to next char in string

	mov al, [attr0]			; Copy attribute to memory
	stosb

	cmp cx, 20				; String length
	jl str_loop

; Unknown bug - program may crash if memory to be written in Video memory isn't at the start
; Reason - unknown
msg0 db "Goodbye Cruel World!",0,0
attr0 db 0x40
msg1 db "something", 0
msg2 db "another", 0
msg3 db "Blinking", 0
msg4 db 'o', 0x04, 'o', 0x06, 'o', 0x0e, 'o', 0x02, 'o', 0x03, 'o', 0x01, 'o', 0x05
msg5 db 'G', 0x0c, 'r', 0x0c, 'a', 0x04, 'd', 0x04, 'i', 0x07, 'e', 0x03, 'n', 0x03, 't', 0x0b, 's', 0x0b
msg6 db "Back to Black & White"
msg7 db "Warning: You have no warnings!"