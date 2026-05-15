#include <cmath> // Include the cmath library for sin() and M_PI

int pwmPin = 26; // GPIO26

void setup() {
  ledcAttach(pwmPin, 100000, 8); // Attach GPIO26 to LEDC and configure it 100kHz
}

const int freq = 50; 
const float Tper_us = 1000000.0 / freq; 

void loop() {
  // Get the current time in microseconds within a single period
  unsigned long time_in_period = micros() % (unsigned long)Tper_us;
  
  // Convert the time to a normalized angle from 0 to 2*PI radians
  // The expression is (time_in_period / Tper_us) * (2 * M_PI)
  float angle = (float)time_in_period / Tper_us * 2.0 * M_PI;

  // Calculate the duty cycle from the sine wave
  // The value will range from 0 to 255 (for 8-bit resolution)
  int duty = (int)(127.5 * (sin(angle) + 1.0));

  ledcWrite(pwmPin, duty);
}