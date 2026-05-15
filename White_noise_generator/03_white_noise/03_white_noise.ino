int pwmPin = 26; // GPIO26


/////////// RANDOM FAST FUNCTION 
uint32_t seed = 123456789;
uint8_t fastRandom() {
    seed = (1664525UL * seed + 1013904223UL);
    return (seed >> 24) & 0xFF;  // returns 0–255
}
/////////////////////////////


int delay_us = 100; //2kHz of update 
void setup() {
  ledcAttach(pwmPin, 100000, 8); // Attach GPIO26 to LEDC and configure it 100kHz
}

void loop() {
  int duty = fastRandom() % 256;
    ledcWrite(pwmPin, duty); // ledcWrite now takes the pin number
    delayMicroseconds(delay_us); 
  
}