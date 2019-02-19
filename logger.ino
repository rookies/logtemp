#include <OneWire.h>
#include <DallasTemperature.h>

const byte oneWirePin = 2;

OneWire ow(oneWirePin);
DallasTemperature sensors(&ow);

void setup() {
  Serial.begin(9600);
  sensors.begin();
}

void loop() {
  sensors.requestTemperatures();
  Serial.println(sensors.getTempCByIndex(0));
  delay(1000);
}
