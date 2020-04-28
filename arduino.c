//arduino
const int led= 12;
const int pump = 13;
const int moiSensor = A0;
String buff;
void setup()
{
 Serial.begin(9600); //Bật cổng Serial Baudrate 9600
 pinMode(led, OUTPUT); //Khai báo chân OUTPUT
 pinMode(pump, OUTPUT);
 pinMode(moiSensor, INPUT);
}
void loop()
{
 if (Serial.available()) //Nếu có tín hiệu từ Pi
 {
 buff = Serial.readStringUntil('\r'); //Đọc vào đến khi gặp \r (xuống
dòng)
D-1

 if (buff=="Led On") //Nếu dữ liệu = "Led On"
 {
 digitalWrite(led,HIGH); //Bật HIGH chân led
 Serial.println("Turned On"); //Trả ngược về "Turned On"
 } else

 if (buff=="Led Off") //Nếu dữ liệu = "Led Off"
 {
 digitalWrite(led,LOW); //Bật LOW chân led
 Serial.println("Turned Off"); //Trả ngược về "Turned Off"
 }
 if (buff=="Moisture") //Nếu dữ liệu = "Hello"
 {
 Serial.println(!digitalRead(moiSensor)); //Trả ngược về
"Hi"
 }
 if (buff=="Pump On") {
 digitalWrite(pump, LOW);
 Serial.println("Turned On");
 }
 if (buff=="Pump Off") {
 digitalWrite(pump, HIGH);
 Serial.println("Turned Off");
 }

 if (buff=="Stop")
 {
 digitalWrite(led, LOW);
 digitalWrite(moiSensor, LOW);
 }
 }
}