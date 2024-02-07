// ButtonControl.h - Header file for button input handling without debouncing.

#ifndef ButtonControl_h
#define ButtonControl_h

#include <Arduino.h>

#define BUTTON_PIN 7 // Define the button pin number

byte lastButtonState = LOW; // Variable to store the last button state, initialized to HIGH assuming pull-up resistor

// Function to initialize the button pin
void setupButton() {
  pinMode(BUTTON_PIN, INPUT); // Set the button pin as an input
}

// Function to check the button state without debouncing
bool checkButton() {
  byte currentButtonState = digitalRead(BUTTON_PIN); // Read the current state of the button
  if (currentButtonState != lastButtonState) {
    lastButtonState = currentButtonState; // Update the last button state
    // Check if the button is pressed (assuming active low configuration)
    if (currentButtonState == LOW) {
      return true; // Button press detected
    }
  }
  return false; // No button press detected
}

#endif
