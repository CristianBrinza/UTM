ORG 100h              ; origin, standard for .COM files

; Method 1: Write character as TTY
mov ah, 09h
mov dx, msg
int 21h
call newline

; Method 2: Write character
mov ah, 0Eh
mov al, 'a'
int 10h
call newline

; Method 3: Write character/attribute
mov ah, 09h
mov al, 'b'
mov bl, 07h          ; attribute (gray on black)
mov cx, 1
int 10h
call newline

; Method 4: Display character + attribute
mov ah, 09h
mov al, 'c'
mov bl, 0Fh          ; attribute (bright white on black)
mov cx, 1
int 10h
call newline

; Method 5: Display character + attribute & update cursor
mov ah, 09h
mov al, 'd'
mov bl, 02h          ; attribute (green on black)
mov cx, 1
int 10h
call newline

; Method 6: Display string
mov ah, 09h
mov dx, msg
int 21h
call newline

; Method 7: Display string & update cursor
mov ah, 09h
mov dx, msg
int 21h
call newline

; Method 8: Print directly to video memory
mov ax, 0B800h
mov es, ax
mov di, 10*160       ; 14th line
mov ax, 0700h | 'a'  ; attribute and character
mov [es:di], ax
call newline

; Exit
mov ah, 4Ch
int 21h

newline:
    mov ah, 02h
    mov dl, 0Ah
    int 21h
    mov dl, 0Dh
    int 21h
    ret

msg: db 'a$', 0Ah, 0Dh, '$'


