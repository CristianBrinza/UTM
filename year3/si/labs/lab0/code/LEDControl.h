// LEDControl.h - Header file for controlling an LED.

#ifndef LEDControl_h
#define LEDControl_h

#include <Arduino.h>

#define LED_PIN 8 // Define the LED pin number

byte ledState = LOW; // Variable to store the current state of the LED

// Function to initialize the LED pin
void setupLED() {
  pinMode(LED_PIN, OUTPUT); // Set the LED pin as an output
}

// Function to toggle the LED state
void toggleLED() {
  ledState = !ledState; // Toggle the state
  digitalWrite(LED_PIN, ledState); // Apply the new state to the LED
}

#endif
