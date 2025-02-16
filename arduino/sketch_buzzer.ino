#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// OLED Display Configuration
#define SCREEN_WIDTH 128  
#define SCREEN_HEIGHT 64  
#define OLED_RESET    -1   
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Sound Sensor & Buzzer Configuration
const int soundSensorPin = A0; 
const int buzzerPin = 3;       

// Sound Thresholds
const int fireThreshold = 1020;
const int knockThreshold = 1000;

// Time Tracking
unsigned long lastStateChange = 0;
const int fireDuration = 15000;  
const int knockDuration = 10000;  
const int defaultDuration = 20000;

String currentState = "default";
bool stateLocked = false; 

void setup() {
    Serial.begin(9600);
    if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
        Serial.println("SSD1306 OLED failed to start");
        for (;;);
    }

    display.clearDisplay();
    display.setTextSize(2);
    display.setTextColor(SSD1306_WHITE);
    display.setCursor(10, 20);
    display.println("System Ready");
    display.display();

    pinMode(soundSensorPin, INPUT);
    pinMode(buzzerPin, OUTPUT);
    noTone(buzzerPin); 
}

void loop() {
    int soundValue = analogRead(soundSensorPin); 
    Serial.print("Sound Level: ");
    Serial.println(soundValue);

    unsigned long now = millis(); 

    if (stateLocked && now - lastStateChange < defaultDuration) {
        return; 
    }
    stateLocked = false;

    if (soundValue > fireThreshold) { 
        if (currentState != "fire") {
            currentState = "fire";
            lastStateChange = now;
            stateLocked = true;
            Serial.println("fire");  // ✅ Sends "fire" instead of "🔥 Fire Detected!"
            triggerAlert("🔥 FIRE", SSD1306_WHITE, 1000, fireDuration);
        }
    } 
    else if (soundValue > knockThreshold && soundValue <= fireThreshold) { 
        if (currentState != "knock") {
            currentState = "knock";
            lastStateChange = now;
            stateLocked = true;
            Serial.println("knock");  // ✅ Sends "knock" instead of "🚪 Knock Detected!"
            triggerAlert("🔶 KNOCK", SSD1306_WHITE, 500, knockDuration);
        }
    } 
    else if (soundValue <= knockThreshold) {
        if (currentState != "default") {
            currentState = "default";
            lastStateChange = now;
            stateLocked = true;
            Serial.println("default");  // ✅ Sends "default" instead of "✅ Default State"

            display.clearDisplay();
            display.setTextSize(2);
            display.setTextColor(SSD1306_WHITE);
            display.setCursor(10, 20);
            display.println("No Alerts");
            display.display();

            noTone(buzzerPin); 
        }
    }

    delay(100);
}

void triggerAlert(const char* message, uint16_t textColor, int toneFrequency, int duration) {
    display.clearDisplay();
    display.setTextSize(2);
    display.setTextColor(textColor);
    display.setCursor(10, 20);
    display.setTextWrap(false);
    display.println(message);
    display.display();

    tone(buzzerPin, toneFrequency);
    delay(duration);
    noTone(buzzerPin);

    display.clearDisplay();
    display.setTextSize(2);
    display.setTextColor(SSD1306_WHITE);
    display.setCursor(10, 20);
    display.println("No Alerts");
    display.display();
}
