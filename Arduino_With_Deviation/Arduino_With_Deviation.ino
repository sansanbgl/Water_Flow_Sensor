#include <math.h>

#define NUM_BASELINE_READINGS 10
#define NUM_READINGS 20
int pulseCount_2_readings[NUM_READINGS];
int baselineReadings[NUM_BASELINE_READINGS];
int index = 0;

#define Z_SCORE_THRESHOLD 5

byte sensorInterrupt = 1;   // INPUT IN PIN 3   -> INTERRUPT = 1 FOR UNO
byte sensorInterrupt_2 = 0; // OUTPUT IN PIN 2  -> INTERRUPT = 0 FOR UNO

byte sensorPin = 3;
byte sensorPin_2 = 2;
int buzzerPin = 7;

// - Flow rate pulse characteristics: Frequency (Hz) = 7.5 * Flow rate (L/min)
float calibrationFactor = 7.5;
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

float calculateMean(int data[], int dataSize)
{
  float sum = 0.0;
  for (int i = 0; i < dataSize; i++)
  {
    sum += data[i];
  }
  return sum / dataSize;
}

// Function to calculate the standard deviation
float calculateStandardDeviation(int data[], int dataSize, float mean)
{
  float sum = 0.0;
  for (int i = 0; i < dataSize; i++)
  {
    sum += pow(data[i] - mean, 2);
  }
  float variance = sum / dataSize;
  return sqrt(variance);
}

void setup()
{
  Serial.begin(9600);

  pinMode(sensorPin, INPUT);
  digitalWrite(sensorPin, HIGH);
  pinMode(sensorPin_2, INPUT);
  digitalWrite(sensorPin_2, HIGH);
  pinMode(buzzerPin, OUTPUT);

  pulseCount = 0;
  flowRate = 0.0;
  flowMilliLitres = 0;
  totalMilliLitres = 0;

  pulseCount_2 = 0;
  flowRate_2 = 0.0;
  flowMilliLitres_2 = 0;
  totalMilliLitres_2 = 0;

  oldTime = 0;

  attachInterrupt(sensorInterrupt, pulseCounter, FALLING);
  attachInterrupt(sensorInterrupt_2, pulseCounter_2, FALLING);
}

bool baselineInitialized = false;
int baselineSum = 0;
int baselineCount = 0;
float baselineMean = 0;
float standardDeviation = 0;
void loop()
{
  if ((millis() - oldTime) > 1000)
  {
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

    Serial.print(millis() / 100);
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
    Serial.print(totalMilliLitres / 1000);

    int receivedValue;
    receivedValue = pulseCount_2;
    pulseCount_2_readings[index] = receivedValue;
    index = (index + 1) % NUM_READINGS;
    if (!baselineInitialized)
    {
      // Calculate baseline values from the first 10 readings
      baselineReadings[baselineCount] = receivedValue;
      baselineSum += receivedValue;
      baselineCount++;

      if (baselineCount >= NUM_BASELINE_READINGS)
      {
        baselineInitialized = true;
        baselineMean = calculateMean(baselineReadings, NUM_BASELINE_READINGS);

        
      }
    }
    else
    {
      // Check for irregularity
      standardDeviation = calculateStandardDeviation(pulseCount_2_readings, NUM_READINGS, receivedValue);

      // Serial.print("Standard Deviation: ");

      if (standardDeviation > 5 && standardDeviation < 7.5)
      {
        // Check if pulseCount still has readings
        int pulseCountReading = pulseCount;
        if (pulseCountReading > 0)
        {
          printBuzzer(buzzerPin, 2000);
          // Serial.println("Small Leak Detected!");

        }
      }
      else if (standardDeviation > 7.5)
      {
          printBuzzer(buzzerPin, 500);
      }
    }
    Serial.print(";");
    Serial.print(baselineMean);
    Serial.print(";");
    Serial.print(standardDeviation);
    Serial.print(";");
    Serial.println("00");

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

void printBuzzer(int buzzerPin, int buzzerDuration)
{
  digitalWrite(buzzerPin, HIGH);
  delay(buzzerDuration);
  digitalWrite(buzzerPin, LOW);
}