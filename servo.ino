#include <Servo.h>

Servo servo;
#define SERVO 9

void setup() {
  Serial.begin(9600);
  servo.attach(SERVO);
}

void loop() {
  if(Serial.available()){
    servo.write(90);
    //add the code for the second servo too. Set pin number accordingly
    }
    else{
      servo.write(20);
      }
    
  

}
