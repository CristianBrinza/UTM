#include "LEDControl.h" // Include the LED control header file
#include "ButtonControl.h" // Include the button control header file

void setup() {
  setupLED(); // Initialize LED pin mode
  setupButton(); // Initialize button pin mode
}

void loop() {
  if (checkButton()) { // Check if the button was pressed
    toggleLED(); // Toggle the LED state
  }
}
