#include <Adafruit_GFX.h>
#include <Adafruit_SSD1331.h>
#include <SPI.h>

#define sclk 13  
#define mosi 11  
#define cs   10  
#define rst  9   
#define dc   8   

Adafruit_SSD1331 display = Adafruit_SSD1331(cs, dc, mosi, sclk, rst);

const int soundSensorPin = A0; // Sound sensor connected to A0
const int buzzerPin = 3;       // Buzzer connected to D3

#define BLACK   0x0000
#define RED     0xF800
#define GREEN   0x07E0
#define WHITE   0xFFFF

// Sound Thresholds
const int fireThreshold = 120;
const int knockThreshold = 70;

// Time Tracking
unsigned long lastStateChange = 0;
const int fireDuration = 15000;  
const int knockDuration = 10000;  
const int defaultDuration = 20000;

String currentState = "default";
bool stateLocked = false; 

void setup() {
    Serial.begin(9600);
    display.begin();
  
    display.fillScreen(BLACK);
    display.setTextSize(1);
    display.setTextColor(WHITE);
    display.setCursor(0, 0);
    display.println("System Ready!");

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
            Serial.println("🔥 Fire Detected!");
            triggerAlert("🔥 Fire Alarm!", RED, 1000, fireDuration);
        }
    } 
    else if (soundValue > knockThreshold && soundValue <= fireThreshold) { 
        if (currentState != "knock") {
            currentState = "knock";
            lastStateChange = now;
            stateLocked = true;
            Serial.println("🚪 Knock Detected!");
            triggerAlert("🚪 Door Knock!", GREEN, 500, knockDuration);
        }
    } 
    else if (soundValue <= knockThreshold) {
        if (currentState != "default") {
            currentState = "default";
            lastStateChange = now;
            stateLocked = true;
            Serial.println("✅ Default State");
            display.fillScreen(BLACK);
            display.setCursor(0, 0);
            display.setTextColor(WHITE);
            display.println("Monitoring...");
            noTone(buzzerPin); 
        }
    }

    delay(100);
}

void triggerAlert(const char* message, uint16_t color, int toneFrequency, int duration) {
    display.fillScreen(color);
    display.setCursor(0, 0);
    display.setTextColor(WHITE);
    display.println(message);
    
    tone(buzzerPin, toneFrequency);
    delay(duration);
    noTone(buzzerPin);

    display.fillScreen(BLACK);
}
