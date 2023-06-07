#if 0
#include <SPI.h>
#include <PN532_SPI.h>
#include <PN532.h>
#include <NfcAdapter.h>

PN532_SPI pn532spi(SPI, 10);
NfcAdapter nfc = NfcAdapter(pn532spi);
#else

#include <Wire.h>
#include <PN532_I2C.h>
#include <PN532.h>
#include <NfcAdapter.h>

#include "ArduinoJson.h"


PN532_I2C pn532_i2c(Wire);
NfcAdapter nfc = NfcAdapter(pn532_i2c);
#endif

void setup(void) {
  Serial.begin(9600);
  nfc.begin();
}

void loop(void) {
  if (nfc.tagPresent()) {
    NfcTag tag = nfc.read();

    if (tag.hasNdefMessage())  // every tag won't have a message
    {
      NdefMessage message = tag.getNdefMessage();
      if (message.getRecordCount() != 1) {
      }
      int recordCount = message.getRecordCount();
      for (int i = 0; i < recordCount; i++) {
        NdefRecord record = message.getRecord(i);
        int payloadLength = record.getPayloadLength();
        byte payload[payloadLength];
        record.getPayload(payload);
        
        // Extract the text between the brackets, including the brackets
        String payloadAsString = "";
        bool insideBrackets = false;  // Variable to track whether we are currently inside the brackets
        for (int c = 0; c < payloadLength; c++) {
          if (payload[c] == '{') {                // Search for the opening bracket
            insideBrackets = true;                // Set the insideBrackets variable to true
            payloadAsString += (char)payload[c];  // Add the opening bracket to the payload string
          } else if (payload[c] == '}') {         // Search for the closing bracket
            insideBrackets = false;               // Set the insideBrackets variable to false
            payloadAsString += (char)payload[c];  // Add the closing bracket to the payload string
            break;                                // Stop extracting characters after the closing bracket
          } else if (insideBrackets) {            // Only add characters to the payload string if we are inside the brackets
            payloadAsString += (char)payload[c];
          }
        }
        StaticJsonDocument<192> doc;
        DeserializationError error = deserializeJson(doc, payloadAsString);
        if (error) {
          return;
        }
        const char* Nombre = doc["Nombre del medicamento"];                
        int Dosis_cada_8_horas_ = doc["Frecuencia de dosificación (cada X horas)"];             
        int Fecha_de_caducidad_meses_ = doc["Vencimiento (meses)"]; 
        int Peso_de_la_dosis_g_ = doc["Peso de cada dosis (g)"];           
        Serial.println(Nombre);

        // id is probably blank and will return ""
        String uid = record.getId();
        if (uid != "") {
       //   Serial.print("  ID: ");
       //   Serial.println(uid);
        }
      }
    }
  }
  delay(3000);
}