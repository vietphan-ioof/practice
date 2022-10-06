#include <SoftwareSerial.h>
#include <Mouse.h>

int isObstaclePin = 2;
int isObstaclePin2 = 3;
int right = HIGH; //HIGH MEANS NO OBSTACLE
int left = HIGH;


void setup() {
  //IR setup
  Serial.begin(9600);
  Serial.println("IR SETUP");
  pinMode(isObstaclePin, INPUT);

  //mouse setup
  Mouse.begin();
  
    
}

void loop() {

  right = digitalRead(isObstaclePin);
  left = digitalRead(isObstaclePin);

  if(right == LOW || left == LOW){
    //simulate mouse click
    Mouse.click();
    Serial.println("HOLA AMIGOS");
  }
}
