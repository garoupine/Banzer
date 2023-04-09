#include <wiringPi.h>

// Define the GPIO pins used for the LEDs
const int LED1_PIN = 17;
const int LED2_PIN = 27;
const int LED3_PIN = 22;
const int LED4_PIN = 23;

int main() {
  // Initialize the wiringPi library
  wiringPiSetupGpio();

  // Set the LED pins to output mode
  pinMode(LED1_PIN, OUTPUT);
  pinMode(LED2_PIN, OUTPUT);
  pinMode(LED3_PIN, OUTPUT);
  pinMode(LED4_PIN, OUTPUT);



for(int i=0;i<2;++i)
  // Turn on all four LEDs
 { digitalWrite(LED1_PIN, HIGH);
   delay(1000);
   digitalWrite(LED1_PIN, LOW);
  // delay(1000);
   digitalWrite(LED2_PIN, HIGH);
  delay(1000);
  digitalWrite(LED2_PIN, LOW);

   digitalWrite(LED3_PIN, HIGH);
  delay(1000);
  digitalWrite(LED3_PIN, LOW);

   digitalWrite(LED4_PIN, HIGH);
  delay(1000);
  digitalWrite(LED4_PIN, LOW);

}


//digitalWrite(LED4_PIN, LOW);
//digitalWrite(LED3_PIN, LOW);
//digitalWrite(LED4_PIN, LOW);
//digitalWrite(LED4_PIN, LOW);

  return 0;
}
