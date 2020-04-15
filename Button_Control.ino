// constants won't change. They're used here to set pin numbers:
//Button Group
const int bt_inj1Pin = 24;
const int bt_vac1Pin = 22; 
const int bt_inj2Pin = 46;
const int bt_vac2Pin = 28;
const int bt_inj3Pin = 30;
const int bt_vac3Pin = 32;
const int bt_inj4Pin = 34;
const int bt_vac4Pin = 36;
const int led1Pin = 26; 

//Relay Group
const int act1 = 41;
const int act2 = 43;
const int act3 = 35;
const int act4 = 33;
const int VACPin = 45;
const int AirPin = 47;

//Sensor Group
const int sensor1Pin = A0;
const int sensor2Pin = A1;
const int sensor3Pin = A2;
const int sensor4Pin = A3;


// variables will change:
int inj1_State = 0;         // variable for reading the pushbutton status
int vac1_State = 0;
int inj2_State = 0;
int vac2_State = 0;
int inj3_State = 0;
int vac3_State = 0;
int inj4_State = 0;
int vac4_State = 0;
int Threshold = 150;
int message = 0;
int count[5] = {0,0,0,0,0};


void setup() {
  // initialize the Valve pins & LEDs as outputs
  pinMode(led1Pin, OUTPUT);
  pinMode(act1, OUTPUT);
  pinMode(act2, OUTPUT);
  pinMode(act3, OUTPUT);
  pinMode(act4, OUTPUT);
  pinMode(VACPin, OUTPUT);
  pinMode(AirPin, OUTPUT);
  
  // initialize the pushbutton pin as an input:
  pinMode(bt_inj1Pin, INPUT);
  pinMode(bt_vac1Pin, INPUT);

  Serial.begin(9600);
  
}


void loop() {
  if (Serial.available() > 0){
    message = Serial.read();
  }
  inj1_State = digitalRead(bt_inj1Pin);
  vac1_State = digitalRead(bt_vac1Pin); 
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (message == 1 or inj1_State == HIGH) {
    Pressure_in(sensor1Pin,act1,0);
  }
  else if (message == 3 or vac1_State == HIGH){
    Vac(act1,0);
  }
  else if (message == 4) {
    Pressure_in(sensor2Pin,act2,1);
  }
  else if (message == 5){
    Vac(act2,1);
  }
  else if (message == 6) {
    Pressure_in(sensor3Pin,act3,2);
  }
  else if (message == 7){
    Vac(act3,2);
  }
  else if (message == 8) {
    Pressure_in(sensor4Pin,act4,3);
  }
  else if (message == 9){
    Vac(act4,3);
  }  
  else if (message == 2) {
    digitalWrite(led1Pin, LOW);
    digitalWrite(act1, HIGH);
    digitalWrite(act2, HIGH);
    digitalWrite(act3, HIGH);
    digitalWrite(act4, HIGH);
    digitalWrite(VACPin, HIGH);
    digitalWrite(AirPin,HIGH);
  }
}

void Pressure_in (int sensor_pin,int actuator_pin, int index){
  int sensorValue = 0;
  sensorValue = analogRead(sensor_pin);
  Serial.println(sensorValue);
  if (sensorValue > Threshold){
    count[index] = count[index] + 1;
  }
  if (sensorValue < Threshold and count[index] < 2){
    digitalWrite(led1Pin, HIGH);
    digitalWrite(actuator_pin, LOW);   //Open Valve
    digitalWrite(VACPin, LOW); //Close VAC
    digitalWrite(AirPin,HIGH);
  }
  else{
    digitalWrite(led1Pin, LOW);
    digitalWrite(actuator_pin, HIGH);   //Close Valve
    digitalWrite(VACPin, HIGH); //Open VAC
    digitalWrite(AirPin,HIGH);
  }
}

void Vac (int actuator_pin, int index){
  count[index] = 0;
  digitalWrite(led1Pin, HIGH);
  digitalWrite(actuator_pin, LOW);   //Open Valve
  digitalWrite(VACPin, HIGH); //Open VAC
  digitalWrite(AirPin,LOW);   //Close Compressed Air
}

