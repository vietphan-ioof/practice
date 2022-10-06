#include <SoftwareSerial.h>


int isObstaclePin = 2;
int isObstaclePin2 = 3;
int right = HIGH; //HIGH MEANS NO OBSTACLE
int left = HIGH;


void setup() {
  //IR setup
  Serial.println("IR SETUP");
  pinMode(LED, OUTPUT);
  pinMode(isObstaclePin, INPUT);
  Serial.begin(9600);
    
}

void loop() {

  right = digitalRead(isObstaclePin);
  left = digitalRead(isObstaclePin);


  if(right == LOW || left == LOW){
    //simulate mouse click
  }else if(right == HIGH && left == HIGH){
    //do nothing
  }

}
