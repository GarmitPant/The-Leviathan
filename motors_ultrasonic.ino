const int trigpin = 8;
const int echopin= 7;
long duration;
int distance;
const int leftForward=2;
const int leftBackward=3;
const int rightForward=4;
const int rightBackward=5;

void setup() {
  // put your setup code here, to run once:
  pinMode(trigpin,OUTPUT);
  pinMode(echopin,INPUT);
  Serial.begin(9600);
  pinMode(leftForward, OUTPUT);
  pinMode(leftBackward, OUTPUT);
  pinMode(rightForward, OUTPUT);
  pinMode(rightBackward, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigpin,HIGH);
  delayMicroseconds(1);
  digitalWrite(trigpin,LOW);
  duration=pulseIn(echopin,HIGH);
  distance = duration*0.034/2;

  while (distance < 2){
    performTask(random(4));
  }
  if (Serial.available()){
    performTask(0);
  }
  else{
    performTask(random(3));
  }

}

void moveForward(){
   digitalWrite(leftForward, HIGH);
   digitalWrite(leftBackward, LOW);
   digitalWrite(rightForward, HIGH);
   digitalWrite(rightBackward, LOW);
   delay(10000);
}

void moveRight(){
  digitalWrite(leftForward, HIGH);
   digitalWrite(leftBackward, LOW);
   digitalWrite(rightForward, LOW);
   digitalWrite(rightBackward, LOW); 
   delay(5000);
}

void moveLeft(){
  digitalWrite(leftForward, LOW);
  digitalWrite(leftBackward, LOW);
  digitalWrite(rightForward, HIGH);
  digitalWrite(rightBackward, LOW);
  delay(5000); 
}

void moveReverse(){
  digitalWrite(leftForward, LOW);
  digitalWrite(leftBackward, HIGH);
  digitalWrite(rightForward, LOW);
  digitalWrite(rightBackward, HIGH);
  delay(5000);
  }

void performTask(int a){
  switch (a) {
  case 0:
    moveForward();
    break;
  case 1:
   moveRight();
    break;
  case 2:
    moveLeft();
    break;
  case 3:
    moveReverse();
    break;  
  }
}
