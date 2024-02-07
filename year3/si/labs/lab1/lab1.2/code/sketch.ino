// Include the standard input-output library for general I/O operations
#include <stdio.h>

// Include custom header files for keypad, LCD display, and LED control functionalities
#include "KeypadControl.h"
#include "LcdDisplay.h"
#include "LEDControl.h"

// Include the Keypad library for interacting with the keypad
#include <Keypad.h>
// Include the LiquidCrystal library for controlling the LCD display
#include <LiquidCrystal.h>

// The setup function initializes the Arduino's digital and serial communication
void setup() {
  // Initialize serial communication at 9600 bits per second for debugging purposes
  Serial.begin(9600);
  
  // Initialize the LCD display with 16 columns and 2 rows for displaying information
  lcd.begin(16, 2);
  
  // Display the initial screen on the LCD with instructions
  displayScreen();
  
  // Initialize the LED indicators to show the lock's status
  initializeLed();
  
  // Print lab and system readiness information on the serial monitor
  Serial.println(F("SI 2024 FAF-212 Cristian Brinza lab1.2"));
  Serial.println(F("System Ready. Enter Password."));
}

// The loop function contains the main logic that runs continuously
void loop() {
  // Static array to hold the entered password, with an extra space for the null terminator
  static char enteredPassword[passwordLength + 1] = ""; 
  // Static variable to keep track of the position for the next digit in the password
  static byte currentIndex = 0;

  // Check if a key has been pressed on the keypad
  char key = keypad.getKey();
  if (key) { // If a key press is detected
    // Debugging line to separate key press events in the serial monitor
    Serial.println("--------------------");
    // Display the pressed key in the serial monitor for debugging
    Serial.print(F("Key Pressed: "));
    Serial.println(key);

    // Validate if the pressed key is a digit and within the password length
    if (currentIndex < passwordLength && isdigit(key)) {
      // Store the digit in the password array and increment the position
      enteredPassword[currentIndex++] = key;
      // Update the LCD display to show an asterisk for each entered digit
      lcd.setCursor(9 + currentIndex - 1, 1);
      lcd.print("*");
      // Echo the current state of entered password in the serial monitor
      Serial.print(F("Entered: "));
      Serial.print(enteredPassword);
      Serial.println();

      // Check if the password is fully entered and validate it
      if (currentIndex == passwordLength) {
        enteredPassword[currentIndex] = '\0'; // Null-terminate the password string
        // Compare the entered password with the correct password
        if (strcmp(enteredPassword, correctPassword) == 0) {
          unlockDoor(); // Unlock the door if the password matches
        } else {
          incorrectCode(); // Show error and prompt again if the password is incorrect
        }
        // Clear the entered password and reset the index for a new attempt
        for (int i = 0; i < passwordLength; i++) {
          enteredPassword[i] = ' ';
        }
        currentIndex = 0;
        displayScreen(); // Refresh the LCD display for the next password entry
      }
    } else if (key == '*' && currentIndex > 0) { // Implement backspace functionality
      currentIndex--; // Decrement the current index to "erase" the last digit
      lcd.setCursor(9 + currentIndex, 1); // Adjust the LCD cursor for the correction
      lcd.print(" "); // Replace the last asterisk with a space to show the digit removal
      Serial.println(F("Backspace")); // Indicate a backspace operation in the serial monitor
    }
  }
}

// Function to display the initial LCD screen for password entry
void displayScreen() {
  lcd.clear(); // Clear any previous text from the LCD
  lcd.setCursor(0, 0); // Set the cursor to the beginning of the first line
  lcd.print("Enter Password:"); // Prompt the user to enter the password
  lcd.setCursor(9, 1); // Set the cursor to the start of the second line for password input
  lcd.print("____"); // Display underscores as placeholders for a 4-digit password
  
  // Activate the red LED to indicate the system is locked and awaiting correct password
  digitalWrite(redPinLock, HIGH); // Set the red LED pin to HIGH (LED on)
  digitalWrite(greenPinUnlock, LOW); // Ensure the green LED is off by setting its pin to LOW
  // The digitalWrite function changes the voltage of a specified pin. Setting a pin to HIGH (usually 5V) turns the LED on, while LOW (0V) turns it off.
}

// Function to handle the unlocking process once the correct password is entered
void unlockDoor() {
  lcd.clear(); // Clear the LCD to display the access granted message
  lcd.print("Access Granted"); // Inform the user that access has been granted
  // Switch the LED statuses to indicate the door is now unlocked
  digitalWrite(redPinLock, LOW); // Turn off the red LED
  digitalWrite(greenPinUnlock, HIGH); // Turn on the green LED to indicate unlocked status
  // Print a message on the serial monitor to indicate the door is unlocked
  Serial.println("-----------------------------------");
  Serial.println(F("Door Unlocked! Enjoy your access."));
  Serial.println("-----------------------------------");
  
  delay(5000); // Keep the door unlocked for 5 seconds
  
  // After 5 seconds, re-lock the door and prompt for the password again
  digitalWrite(redPinLock, HIGH); // Reactivate the red LED to show re-locking
  digitalWrite(greenPinUnlock, LOW); // Turn off the green LED
  lcd.clear(); // Clear the LCD for the next password entry
  displayScreen(); // Display the password entry prompt again
  Serial.println(F("Door re-locked. Please enter password again."));
}

// Function to handle incorrect password attempts
void incorrectCode() {
  lcd.clear(); // Clear the LCD to show the access denied message
  lcd.print("Access Denied"); // Inform the user that the entered password is incorrect
  // Keep the red LED on to indicate the door remains locked
  digitalWrite(redPinLock, HIGH); // Ensure the red LED remains activated
  digitalWrite(greenPinUnlock, LOW); // Ensure the green LED remains off
  // Print a message on the serial monitor indicating the incorrect password attempt
  Serial.println("------------------------------");
  Serial.println("Incorrect Password! Try again.");
  Serial.println("------------------------------");
  delay(3000); // Pause to allow the user time to read the message before trying again
}
