ORG 0x7C00 ; Set the starting address for the code to 0x7C00, the location where the BIOS loads the boot sector.

; Initialize the Extra Segment (ES) to point to the Data Segment (DS).
mov AX, DS ; Load the value of DS into AX.
mov ES, AX ; Set ES to the value in AX (which is DS).

; Method 1: Display character 'A' using TTY mode.
mov AH, 0Eh ; Set AH to 0Eh, indicating the BIOS function to write a character in TTY mode.
mov AL, 'A' ; Load the character 'A' into AL.
int 10h    ; Call BIOS interrupt 10h to display the character.

; Move the cursor to the next row.
mov AH, 02h ; Set AH to 02h, indicating the BIOS function to set the cursor position.
mov BH, 0  ; Set page number to 0.
mov DH, 1  ; Set row number to 1.
mov DL, 0  ; Set column number to 0.
int 10h    ; Call BIOS interrupt 10h to move the cursor.

; Method 2: Display character 'B'.
mov AH, 0aH ; Set AH to 0aH, indicating the BIOS function to write a character.
mov AL, 'B' ; Load the character 'B' into AL.
int 10h    ; Call BIOS interrupt 10h to display the character.

; Move the cursor to the next row.
mov AH, 02h ; Set AH to 02h for cursor positioning.
mov BH, 0  ; Set page number to 0.
mov DH, 2  ; Set row number to 2.
mov DL, 0  ; Set column number to 0.
int 10h    ; Call BIOS interrupt 10h to move the cursor.

; Method 3: Display character 'C' with color attribute.
mov AH, 09h  ; Set AH to 09h, indicating the BIOS function to write a character with an attribute.
mov AL, 'C'  ; Load the character 'C' into AL.
mov BL, 0x07 ; Set BL to 0x07, which is the attribute for standard gray on black.
mov CX, 1    ; Set CX to 1, indicating the number of times to display the character.
int 10h      ; Call BIOS interrupt 10h to display the character.

; Move the cursor to the next row.
mov AH, 02h ; Set AH to 02h for cursor positioning.
mov BH, 0  ; Set page number to 0.
mov DH, 3  ; Set row number to 3.
mov DL, 0  ; Set column number to 0.
int 10h    ; Call BIOS interrupt 10h to move the cursor.

; Method 4: Display character 'D' with a red color attribute.
mov AH, 13h ; Set AH to 13h, indicating the BIOS function to display a string with attributes.
mov AL, 2   ; Set AL to 2, indicating the sub-function to display a character and attribute.
mov BH, 0   ; Set page number to 0.
mov BL, 0x04; Set BL to 0x04, which is the attribute for red color.
mov DH, 4   ; Set row number to 4.
mov DL, 0   ; Set column number to 0.
mov CX, 1   ; Set CX to 1, indicating the number of times to display the character.
lea BP, [MsgMethod4] ; Load the address of MsgMethod4 into BP.
int 10h     ; Call BIOS interrupt 10h to display the character.

; Method 5: Display character 'E' with a light green color attribute and update the cursor.
mov AH, 13h ; Set AH to 13h for string display with attributes.
mov AL, 3   ; Set AL to 3, indicating the sub-function to display a character, attribute, and update the cursor.
mov BH, 0   ; Set page number to 0.
mov BL, 0x0A; Set BL to 0x0A, which is the attribute for light green color.
mov DH, 5   ; Set row number to 5.
mov DL, 0   ; Set column number to 0.
mov CX, 1   ; Set CX to 1, indicating the number of times to display the character.
lea BP, [MsgMethod5] ; Load the address of MsgMethod5 into BP.
int 10h     ; Call BIOS interrupt 10h to display the character.

; Method 6: Display the character "F" with standard color.
mov AH, 13h ; Set AH to 13h for string display with attributes.
mov AL, 0   ; Set AL to 0, indicating the sub-function to display a string without updating the cursor.
mov BH, 0   ; Set page number to 0.
mov BL, 0x07; Set BL to 0x07, which is the standard color attribute.
mov DH, 6   ; Set row number to 6.
mov DL, 0   ; Set column number to 0.
lea BP, MsgMethod6 ; Load the address of MsgMethod6 into BP.
mov CX, 2   ; Set CX to 2, indicating the total number of bytes (character + attribute) in the string.
int 10h     ; Call BIOS interrupt 10h to display the character.

; Method 7: Display the character "J" with standard color and update the cursor.
mov AH, 13h ; Set AH to 13h for string display with attributes.
mov AL, 1   ; Set AL to 1, indicating the sub-function to display a string and update the cursor.
mov BH, 0   ; Set page number to 0.
mov BL, 0x07; Set BL to 0x07, which is the standard color attribute.
mov DH, 7   ; Set row number to 7.
mov DL, 0   ; Set column number to 0.
lea BP, MsgMethod7 ; Load the address of MsgMethod7 into BP.
mov CX, 2   ; Set CX to 2, indicating the total number of bytes (character + attribute) in the string.
int 10h     ; Call BIOS interrupt 10h to display the character.

; Data segment: Define the characters used in the above methods.
MsgMethod4 db 'D' ; Define a single character 'D'.
MsgMethod5 db 'E' ; Define a single character 'E'.
MsgMethod6 db 'F', 0x07 ; Define the character "F" with standard color attribute.
MsgMethod7 db 'J', 0x07 ; Define the character "J" with standard color attribute.

; End the program and return control to the operating system.
int 20h     ; Call BIOS interrupt 20h to terminate the program
