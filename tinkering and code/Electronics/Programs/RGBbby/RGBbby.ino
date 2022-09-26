#define BLUE 3
#define GREEN 5
#define RED 6

void setup(){
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  digitalWrite(RED, HIGH);
  digitalWrite(GREEN, LOW);
  digitalWrite(BLUE, LOW);
  }

int redValue;
int greenValue;
int blueValue;

void loop(){
 #define delayTime 10
 greenValue = 200;
 redValue = 100;
 blueValue = 50;


 for(int x=0; x<5; x+=1){
  redValue-=1;
  greenValue+=1;

  analogWrite(RED, redValue);
  analogWrite(GREEN, greenValue);
  analogWrite(BLUE, blueValue);
  delay(delayTime);
  }
  
  
  }
