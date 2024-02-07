// Include the standard input-output library for general I/O operations
#include <stdio.h>

// Prevent multiple inclusions of this header file
#ifndef KEYPADCONTROL_H
#define KEYPADCONTROL_H

// Include the Keypad library for keypad interfacing
#include <Keypad.h>

// Define Arduino pins connected to the keypad rows
#define ROW_PIN_1 8
#define ROW_PIN_2 7
#define ROW_PIN_3 6
#define ROW_PIN_4 5

// Define Arduino pins connected to the keypad columns
#define COL_PIN_1 4
#define COL_PIN_2 3
#define COL_PIN_3 2
#define COL_PIN_4 1

// Define the number of rows and columns on the keypad
const byte numRows = 4; // The keypad has 4 rows
const byte numCols = 4; // The keypad has 4 columns

// Define the correct password and calculate its length
const char correctPassword[] = "4567"; // Set the correct password
const byte passwordLength = sizeof(correctPassword) - 1; // Calculate the length of the correct password excluding the null terminator

// Define the layout of the keypad
// Each character represents a button on the keypad
char keys[numRows][numCols] = {
  {'1', '2', '3', 'A'}, // First row of buttons
  {'4', '5', '6', 'B'}, // Second row
  {'7', '8', '9', 'C'}, // Third row
  {'*', '0', '#', 'D'}  // Fourth row
};

// Specify the Arduino pins connected to the keypad rows
byte rowPins[numRows] = {ROW_PIN_1, ROW_PIN_2, ROW_PIN_3, ROW_PIN_4}; // Connect keypad rows to these pins on Arduino

// Specify the Arduino pins connected to the keypad columns
byte colPins[numCols] = {COL_PIN_1, COL_PIN_2, COL_PIN_3, COL_PIN_4}; // Connect keypad columns to these pins on Arduino

// Initialize the keypad by passing the keymap, row pins, column pins, and the number of rows and columns
// This creates a Keypad object that can be used to detect key presses
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, numRows, numCols);

// End of the condition to prevent multiple inclusions
#endif
