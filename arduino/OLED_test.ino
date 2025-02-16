#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 
#define SCREEN_HEIGHT 32 

#define OLED_RESET    -1 
#define SCREEN_ADDRESS 0x3C 
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() {
  // Initialize serial communication for debugging
  Serial.begin(9600);

  // Initialize the OLED display
  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;); 
  }

  display.clearDisplay();

  // Display a simple message
  display.setTextSize(1); 
  display.setTextColor(SSD1306_WHITE); 
  display.setCursor(0, 0); 
  display.println(F("Hello, Arduino Uno!"));
  display.display();
  delay(2000); // Pause for 2 seconds
}

void loop() {
  // Your main code here
}
