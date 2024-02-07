// Include the standard input-output library for general I/O operations
#include <stdio.h>

// Use preprocessor directive to ensure the content of this file is included only once
#ifndef LCDDISPLAY_H
#define LCDDISPLAY_H

// Include the LiquidCrystal library to control LCD displays
#include <LiquidCrystal.h>

// Define constants for the LCD's pin connections to the Arduino
#define LCD_RS A0 // Define RS (Register Select) pin connected to Arduino's analog pin A0
#define LCD_EN A1 // Define EN (Enable) pin connected to Arduino's analog pin A1
#define LCD_D4 A2 // Define D4 pin connected to Arduino's analog pin A2
#define LCD_D5 A3 // Define D5 pin connected to Arduino's analog pin A3
#define LCD_D6 A4 // Define D6 pin connected to Arduino's analog pin A4
#define LCD_D7 A5 // Define D7 pin connected to Arduino's analog pin A5

// Initialize an instance of the LiquidCrystal class with the defined pins
LiquidCrystal lcd(LCD_RS, LCD_EN, LCD_D4, LCD_D5, LCD_D6, LCD_D7);

// This setup configures the LCD to use a 4-bit communication mode with the specified pins.
// Using analog pins for digital communication is a common practice in Arduino projects to
// increase the number of available digital pins, especially on boards with limited GPIO pins.

#endif // End of the preprocessor directive to prevent multiple inclusions of this file
