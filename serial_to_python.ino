#include<string.h>
int analogPin = 5;
int data1 = 0;
int data2 = 0;
String datajson;

void setup()
{ 
  Serial.begin(9600);
}

void loop() 
{
  data1 = touchRead(T0);
  data2 = touchRead(T3);
  datajson = String("{") + String("\"data1\":") + data1 + String(",") + String("\"data2\":") + data2 + String("}");
  Serial.println(datajson);

}
