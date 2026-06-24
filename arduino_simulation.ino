void setup() {
  Serial.begin(9600); 
}

void loop() {
    // Simulating sensor stream
    float mockTemperature_livingroom = random(200, 350) / 10.0; 

    Serial.print(F("livingRoom->"));
    Serial.println(mockTemperature_livingroom);
    delay(2000); 
    // Simulating sensor stream
    float mockTemperature_bedroom = random(200, 350) / 10.0; 


    Serial.print(F("bedRoom->"));
    Serial.println(mockTemperature_bedroom);
    delay(2000); 
}