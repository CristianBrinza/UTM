// Include the standard input-output library for general I/O operations
#include <stdio.h>

// Prevent multiple inclusions of this header file using preprocessor directives
#ifndef LEDCONTROL_H
#define LEDCONTROL_H

// Define macro constants for the LED pins connected to the Arduino
// These constants improve code readability and maintainability
#define redPinLock 10       // Assign the pin number 10 to the red LED used for indicating the lock status
#define greenPinUnlock 11   // Assign the pin number 11 to the green LED used for indicating the unlock status

// Function to initialize the LEDs used for lock status indication
void initializeLed() {
  // Set the pin mode of the red LED to OUTPUT, allowing it to be turned on or off
  pinMode(redPinLock, OUTPUT);
  // Similarly, set the pin mode of the green LED to OUTPUT
  pinMode(greenPinUnlock, OUTPUT);
  // The pinMode function configures the specified digital I/O pin as either INPUT or OUTPUT.
  // Here, configuring the pins as OUTPUT enables the Arduino to control the LEDs by sending voltage signals,
  // turning them on (HIGH) or off (LOW) as needed to indicate the system's lock or unlock status.
}

// End of the conditional inclusion directive
#endif
