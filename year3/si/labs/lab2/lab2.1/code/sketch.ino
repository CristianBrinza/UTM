#include <Arduino.h>
#include <LiquidCrystal.h>

// Define constants for pin assignments to improve readability and maintenance
#define BUTTON_TOGGLE_LED_PIN 2
#define BUTTON_INCREMENT_BLINK_DURATION_PIN 3
#define BUTTON_DECREMENT_BLINK_DURATION_PIN 4
#define BUTTON_INCREASE_BRIGHTNESS_PIN 5
#define BUTTON_DECREASE_BRIGHTNESS_PIN 6
#define LED_PIN 9 // PWM capable pin for LED brightness control
#define SECOND_LED_PIN 12
#define BUZZER_PIN 8 // Buzzer pin for audible feedback
#define BUTTON_PLAY_THEME_PIN 7

// Initialize the LCD with the analog interface pins
LiquidCrystal lcd(A0, A1, A2, A3, A4, A5);

// Global variables for system state management
volatile bool ledState = false; // Tracks the on/off state of the main LED
int blinkDuration = 1000; // Duration between blinks for the second LED in milliseconds
int ledBrightness = 128; // Brightness level of the main LED (0-255)

bool isPlayingTheme = false; // Tracks whether the theme is currently being played
// Note frequencies for the Harry Potter theme, based on the notes' musical pitch
// Notes in the melody:
int melody[] = {
    392, 0, 392, 0, 392, 0, // G4
    311, 0, 466, 0, 392, 0, // Eb4, Bb4, G4
    784, 0, 784, 0, 784, 0, // G5
    698, 0, 659, 0, 622, 0, 659, 0, // F5, E5, Eb5, E5
    415, 0, 554, 0, 523, 0, 494, 0, // Ab4, C#5, C5, B4
    466, 0, 466, 0, 466, 0, // Bb4
    311, 0, 466, 0, 392 // Eb4, Bb4, G4
};

// Durations of the notes (in terms of 1/4 notes):
// For example, a quarter note would be 4, half note would be 2.
int noteDurations[] = {
    12, 12, 12, 12, 12, 12, // Corresponding to G4
    9, 9, 9, 9, 9, 9, // Corresponding to Eb4, Bb4, G4
    12, 12, 12, 12, 12, 12, // Corresponding to G5
    12, 12, 12, 12, 12, 12, 12, 12, // Corresponding to F5, E5, Eb5, E5
    9, 9, 9, 9, 9, 9, 9, 9, // Corresponding to Ab4, C#5, C5, B4
    12, 12, 12, 12, 12, 12, // Corresponding to Bb4
    9, 9, 9, 9, 9 // Corresponding to Eb4, Bb4, G4
};




void setup() {
  // Configure the digital pins as inputs or outputs
  pinMode(BUTTON_TOGGLE_LED_PIN, INPUT);
  pinMode(BUTTON_INCREMENT_BLINK_DURATION_PIN, INPUT);
  pinMode(BUTTON_DECREMENT_BLINK_DURATION_PIN, INPUT);
  pinMode(BUTTON_INCREASE_BRIGHTNESS_PIN, INPUT);
  pinMode(BUTTON_DECREASE_BRIGHTNESS_PIN, INPUT);
  pinMode(BUTTON_PLAY_THEME_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  pinMode(SECOND_LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  Serial.begin(9600); // Start serial communication at 9600 baud rate
  lcd.begin(16, 2); // Initialize the LCD (16 characters, 2 rows)
    Serial.println(F("SI 2024 FAF-212 Cristian Brinza lab2.1"));
  Serial.println(F("System Ready. Press buttons!!!"));
  Serial.println(F(" "));
  updateLcdAndSerial("Startup", "LED Off", blinkDuration, ledBrightness); // Initial LCD and Serial update
    // Print lab and system readiness information on the serial monitor

}

void loop() {
  // Continuously handle input tasks and update system state
  handleButtonLedTask();
  handleBlinkSecondLedTask();
  handleVariableIncrementDecrementTask();
  handleBrightnessControlTask();
  handlePlayThemeTask();
  // The idle task is currently not implemented but could include background monitoring
  handleIdleTask();
  
}

// Generates a beep sound using the buzzer
void beepBuzzer() {
  tone(BUZZER_PIN, 1000, 100); // Emit a 1000Hz sound for 100 milliseconds
}

// Updates the LCD display and prints a corresponding message to the serial monitor
void updateLcdAndSerial(String status, String action, int duration, int brightness) {

  // Clear the LCD and prepare to display the updated state
  lcd.clear();
  
  // Display the LED state on the first line with brightness
  lcd.print("LED:");
  lcd.print(ledState ? "On " : "Off");
  lcd.print("  Br:");
  lcd.print(ledBrightness);

  // Move to the second line to display the blink duration
  lcd.setCursor(0, 1);
  lcd.print("Blink:");
  lcd.print(duration);
  lcd.print("ms");


  // Construct and send a detailed message to the serial monitor
  Serial.println("Action: " + action + ", LED Status: " + status + ", Blink Duration: " + String(duration) + "ms, Brightness: " + String(brightness));
}

// Handles the toggling of the main LED based on button input
void handleButtonLedTask() {
  static bool lastButtonState = LOW; // Remember the last state to detect changes
  bool currentButtonState = digitalRead(BUTTON_TOGGLE_LED_PIN);

  // Check for state change to HIGH (button press)
  if (currentButtonState != lastButtonState && currentButtonState == HIGH) {
    ledState = !ledState; // Toggle the LED state
    analogWrite(LED_PIN, ledState ? ledBrightness : 0); // Update LED brightness accordingly
    beepBuzzer(); // Provide audible feedback for the action
    updateLcdAndSerial(ledState ? "On" : "Off", "Toggle LED", blinkDuration, ledBrightness); // Update displays
  }
  lastButtonState = currentButtonState; // Update the last known state
}

// Manages the blinking of a secondary LED based on the current blink duration
void handleBlinkSecondLedTask() {
  static unsigned long previousMillis = 0;
  if (!ledState && (millis() - previousMillis >= blinkDuration)) {
    previousMillis = millis();
    digitalWrite(SECOND_LED_PIN, !digitalRead(SECOND_LED_PIN)); // Toggle the LED's state
  } else if (ledState) {
    digitalWrite(SECOND_LED_PIN, LOW); // Ensure the secondary LED is off when the main LED is on
  }
}

// Adjusts the blink duration based on button inputs for incrementing/decrementing
void handleVariableIncrementDecrementTask() {
  if (digitalRead(BUTTON_INCREMENT_BLINK_DURATION_PIN) == HIGH) {
    blinkDuration = max(100, blinkDuration - 100); // Decrease duration for faster blinking
    beepBuzzer();
    updateLcdAndSerial(ledState ? "On" : "Off", "Decrement Blink", blinkDuration, ledBrightness);
    delay(200); // Debounce delay
  } else if (digitalRead(BUTTON_DECREMENT_BLINK_DURATION_PIN) == HIGH) {
    blinkDuration = min(2000, blinkDuration + 100); // Increase duration for slower blinking
    beepBuzzer();
    updateLcdAndSerial(ledState ? "On" : "Off", "Increment Blink", blinkDuration, ledBrightness);
    delay(200); // Debounce delay
  }
}

// Adjusts the main LED's brightness based on button inputs
void handleBrightnessControlTask() {
  if (digitalRead(BUTTON_INCREASE_BRIGHTNESS_PIN) == HIGH) {
    ledBrightness = min(255, ledBrightness + 15); // Increase brightness
    if (ledState) {
      analogWrite(LED_PIN, ledBrightness); // Apply only if the LED is on
    }
    beepBuzzer();
    updateLcdAndSerial(ledState ? "On" : "Off", "Increase Brightness", blinkDuration, ledBrightness);
    delay(200); // Debounce delay
  } else if (digitalRead(BUTTON_DECREASE_BRIGHTNESS_PIN) == HIGH) {
    ledBrightness = max(0, ledBrightness - 15); // Decrease brightness
    if (ledState) {
      analogWrite(LED_PIN, ledBrightness); // Apply only if the LED is on
    }
    beepBuzzer();
    updateLcdAndSerial(ledState ? "On" : "Off", "Decrease Brightness", blinkDuration, ledBrightness);
    delay(200); // Debounce delay
  }
}
void handlePlayThemeTask() {
  static bool lastButtonState = LOW;
  bool currentButtonState = digitalRead(BUTTON_PLAY_THEME_PIN);

  // Toggle the theme playback on button press
  if (lastButtonState == HIGH && currentButtonState == LOW) {
    isPlayingTheme = !isPlayingTheme;
    
    if (isPlayingTheme) {
      playTheme();
    } else {
      noTone(BUZZER_PIN); // Stop playing
    }
  }
  lastButtonState = currentButtonState;
}

void playTheme() {
  for (int thisNote = 0; thisNote < 20; thisNote++) {
    // To calculate the note duration, take one second divided by the note type.
    // e.g., quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000 / noteDurations[thisNote];
    tone(BUZZER_PIN, melody[thisNote], noteDuration);

    // To distinguish the notes, set a minimum time between them.
    // The note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    // Stop the tone playing:
    noTone(BUZZER_PIN);
    
    // Check if the theme should stop playing
    if (!isPlayingTheme) {
      break;
    }
  }
}

// An optional idle task function, currently unused but could be implemented for background tasks
void handleIdleTask() {
  // Placeholder for future implementation
}
