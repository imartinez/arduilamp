
int ledR = 9;           // the pin that the LED is attached to
int ledG = 10;           // the pin that the LED is attached to
int ledB = 11;           // the pin that the LED is attached to

void setup() {
	Serial.begin(9600); // set the baud rate
	Serial.println("Arduino Ready!"); // print "Ready" once connection stablished

  // declare pin 9, 10 and 11 to be an output
  pinMode(ledR, OUTPUT);
  pinMode(ledG, OUTPUT);
  pinMode(ledB, OUTPUT);
}

void loop() {
	while (Serial.available()) {
  	delay(3);  //delay to allow buffer to fill
  	if (Serial.available() >0) {
  		char c = Serial.read();  //gets one char from serial buffer
      if (c == 'R') {
        String redString;
        while (Serial.available()) {
          delay(3);  //delay to allow buffer to fill
          redString += (char)Serial.read();
        }
        analogWrite(ledR, redString.toInt());     
        Serial.println("Set R to: " + redString); //see what was received
        redString = "";     
        Serial.flush();        
      } else if (c == 'G') {
        String greenString;
        while (Serial.available()) {
          delay(3);  //delay to allow buffer to fill
          greenString += (char)Serial.read();
        }
        analogWrite(ledG, greenString.toInt());     
        Serial.println("Set G to: " + greenString); //see what was received
        greenString = "";   
        Serial.flush();  
      } else if (c == 'B') {
        String blueString;
        while (Serial.available()) {
          delay(3);  //delay to allow buffer to fill
          blueString += (char)Serial.read();
        }
        analogWrite(ledB, blueString.toInt());     
        Serial.println("Set B to: " + blueString); //see what was received
        blueString = ""; 
        Serial.flush();    
      }
	  }
	}
}
