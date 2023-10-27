byte sensorInterrupt = 1;           // INPUT IN PIN 3   -> INTERRUPT = 1 FOR UNO
byte sensorInterrupt_2 = 0;         // OUTPUT IN PIN 2  -> INTERRUPT = 0 FOR UNO

byte sensorPin          = 3;
byte sensorPin_2        = 2;

// - Flow rate pulse characteristics: Frequency (Hz) = 7.5 * Flow rate (L/min)
float calibrationFactor   = 7.5;
float calibrationFactor_2 = 7.5;

volatile byte pulseCount;  
volatile byte pulseCount_2;  

float flowRate;
float flowRate_2;
unsigned int flowMilliLitres;
unsigned int flowMilliLitres_2;
unsigned long totalMilliLitres;
unsigned long totalMilliLitres_2;

unsigned long oldTime;

String dataLabel0 = "DateTime";
String dataLabel1 = "Input Pulse";
String dataLabel2 = "Output Pulse";
String dataLabel3 = "Input Flow";
String dataLabel4 = "Output Flow";
String dataLabel5 = "Total Output (mL)";
String dataLabel6 = "Total Output (L)";

bool label = true;

void setup()
{
  Serial.begin(9600);
   
  pinMode(sensorPin, INPUT);
  digitalWrite(sensorPin, HIGH);
  pinMode(sensorPin_2, INPUT);
  digitalWrite(sensorPin_2, HIGH);

  pulseCount        = 0;
  flowRate          = 0.0;
  flowMilliLitres   = 0;
  totalMilliLitres  = 0;

  pulseCount_2        = 0;
  flowRate_2          = 0.0;
  flowMilliLitres_2   = 0;
  totalMilliLitres_2  = 0;

  oldTime           = 0;

  attachInterrupt(sensorInterrupt, pulseCounter, FALLING);
  attachInterrupt(sensorInterrupt_2, pulseCounter_2, FALLING);
}

void loop()
{
  while(label) {
    Serial.print(dataLabel0);
    Serial.print(";");
    Serial.print(dataLabel1);
    Serial.print(";");
    Serial.print(dataLabel2);
    Serial.print(";");
    Serial.print(dataLabel3);
    Serial.print(";");
    Serial.print(dataLabel4);
    Serial.print(";");
    Serial.print(dataLabel5);
    Serial.print(";");
    Serial.println(dataLabel6);

    label = false;
  }
  
  if((millis() - oldTime) > 1000) { 
    detachInterrupt(sensorInterrupt);
    detachInterrupt(sensorInterrupt_2);
        
    flowRate = ((1000.0 / (millis() - oldTime)) * pulseCount) / calibrationFactor;
    flowRate_2 = ((1000.0 / (millis() - oldTime)) * pulseCount_2) / calibrationFactor_2;
    
    oldTime = millis();
    
    flowMilliLitres = (flowRate / 60) * 1000;
    flowMilliLitres_2 = (flowRate_2 / 60) * 1000;
    
    totalMilliLitres += flowMilliLitres;
    totalMilliLitres_2 += flowMilliLitres_2;
      
    unsigned int frac;
    unsigned int frac_2;
    
    Serial.print(millis());
    Serial.print(";");
    Serial.print(int(pulseCount));
    Serial.print(";");
    Serial.print(int(pulseCount_2));
    Serial.print(";");
    Serial.print(int(flowRate));
    Serial.print(";");
    Serial.print(int(flowRate_2));
    Serial.print(";");
    Serial.print(totalMilliLitres);
    Serial.print(";");
    Serial.println(totalMilliLitres / 1000);

    pulseCount = 0;
    pulseCount_2 = 0;
    
    attachInterrupt(sensorInterrupt, pulseCounter, FALLING);
    attachInterrupt(sensorInterrupt_2, pulseCounter_2, FALLING);
  }
}

void pulseCounter()
{
  pulseCount++;
}

void pulseCounter_2()
{
  pulseCount_2++;
}