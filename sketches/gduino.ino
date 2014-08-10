/* 
gduino.ino
Read incoming data from the serial port
Light an LED if a certain message arrives
*/

int ledPin = 8; //LED in digital pin 8
int mail   = LOW; // is there new mail?
int val    = 0; // value read from the serial port

void setup()
{
  pinMode(ledPin, OUTPUT); // set digital pin as output
  Serial.begin(9600);
  Serial.flush();
}

void loop()
{
  // read from serial port
  if (Serial.available() > 0)
  {
    val = Serial.read(); // read what was sent over Serial
    Serial.println(val);
    
    if (val == 77) // ASCII printable character 77 == M
      mail = HIGH; 
    else if (val == 78) // ASCII printable character 78 == N
      mail = LOW; 
  }
  digitalWrite(ledPin, mail); // set mail status to LED
}
