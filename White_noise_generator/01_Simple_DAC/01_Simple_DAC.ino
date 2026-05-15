int pwmPin = 26; // GPIO26

void setup() {
  ledcAttach(pwmPin, 100000, 8); // Attach GPIO26 to LEDC and configure it 100kHz
}

void loop() {
  for (int duty = 0; duty <= 255; duty = duty + 10) {
    ledcWrite(pwmPin, duty); // ledcWrite now takes the pin number
    delay(1);
  }
}