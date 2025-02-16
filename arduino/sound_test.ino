const int soundSensorPin = A0; 
const int ledPin = 2; 

void setup() {
  pinMode(soundSensorPin, INPUT); 
  pinMode(ledPin, OUTPUT); //optional light 
  Serial.begin(9600); 
}

void loop() {
  int soundValue = analogRead(soundSensorPin);

  // Display the sound sensor value on the Serial Monitor
  Serial.print("Sound Level: ");
  Serial.println(soundValue);

  int threshold = 400;

  if (soundValue > threshold) {
   //write to sound and to dectect
    digitalWrite(ledPin, HIGH);
    print('hello')
  } else {
    // No sound detected, turn off the LED
    digitalWrite(ledPin, LOW);
    print('low')
  }
  //delay the system so it won't cause rapidly
  delay(100); 
}
