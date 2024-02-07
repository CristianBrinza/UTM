// LEDControl.h - Header file description indicating it's been updated to include new functionalities for LED control

#ifndef LEDControl_h // If LEDControl_h hasn't been defined yet,
#define LEDControl_h // define it now to prevent duplicate inclusion of this header file

#include <Arduino.h> // Include the main Arduino header file for access to standard types and constants

#define LED_PIN 8 // Define the LED_PIN as 8, assigning the LED to digital pin 8 on the Arduino

byte ledState = LOW; // Declare a variable to store the current state of the LED, initialized to LOW (off)

void setupLED() {
  pinMode(LED_PIN, OUTPUT); // Set the LED_PIN as an OUTPUT, configuring it to control an LED
}

void toggleLED() {
  ledState = !ledState; // Toggle the ledState between HIGH and LOW
  digitalWrite(LED_PIN, ledState); // Apply the toggled state to the LED_PIN, turning the LED on or off
  Serial.print("LED is now "); Serial.println(ledState ? "ON" : "OFF"); // Print a confirmation message indicating the new state of the LED
}

void turnOnLED() {
  ledState = HIGH; // Set the ledState to HIGH (on)
  digitalWrite(LED_PIN, ledState); // Apply the HIGH state to the LED_PIN, turning the LED on
  Serial.println("LED turned ON"); // Print a message to the Serial monitor indicating that the LED has been turned on
}

void turnOffLED() {
  ledState = LOW; // Set the ledState to LOW (off)
  digitalWrite(LED_PIN, ledState); // Apply the LOW state to the LED_PIN, turning the LED off
  Serial.println("LED turned OFF"); // Print a message to the Serial monitor indicating that the LED has been turned off
}

bool getLEDState() {
  return ledState; // Return the current state of the ledState variable (either HIGH or LOW)
}

#endif // End of the conditional preprocessor directive, concluding the definitions in this header file
