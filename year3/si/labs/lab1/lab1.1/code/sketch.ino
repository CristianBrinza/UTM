#include "LEDControl.h" // Include the updated LED control header file for LED operations
#include "ButtonControl.h" // Include the button control header file for button operations

void setup() {
  Serial.begin(9600); // Initialize serial communication at 9600 baud rate for data exchange between the Arduino and the computer
  Serial.println("SI 2024 FAF-212 Cristian Brinza lab1.1"); // Print a custom message including session identifier to the Serial monitor
  Serial.println("Welcome to the Serial Monitor!"); // Print a welcome message to the Serial monitor
  Serial.println("---------------------------------"); // Print a separator line to the Serial monitor for better readability
  setupLED(); // Call the setupLED function to initialize the LED pin as an output
  setupButton(); // Call the setupButton function to initialize the button pin as an input
}

void loop() {
  if (Serial.available() > 0) { // Check if there is data available to read from the Serial buffer
    String command = Serial.readStringUntil('\n'); // Read the incoming data from the Serial buffer as a string until a newline character is encountered
    if (command == "ON") { // Check if the read command is "ON"
      turnOnLED(); // Call the turnOnLED function to turn the LED on
    } else if (command == "OFF") { // Check if the read command is "OFF"
      turnOffLED(); // Call the turnOffLED function to turn the LED off
    } else if (command == "TOGGLE") { // Check if the read command is "TOGGLE"
      toggleLED(); // Call the toggleLED function to toggle the LED's current state
    } else { // If the command is none of the above options
      Serial.println("Invalid command. Use ON, OFF, or TOGGLE."); // Print an error message indicating the command was not recognized
    }
  }
  
  if (checkButton()) { // Check if the button state has changed to pressed
    toggleLED(); // Call the toggleLED function to toggle the LED's state in response to the button press
  }
}
