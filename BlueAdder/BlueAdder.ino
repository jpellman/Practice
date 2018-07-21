  #include <Wire.h>
  #include <Adafruit_MCP23017.h>
  #include <Adafruit_RGBLCDShield.h>
  #include <math.h>
  
  Adafruit_RGBLCDShield lcd = Adafruit_RGBLCDShield();
  
  // A constant for the backlight color
  #define BLUE 0x1
  
  //Dimensions
  #define ROWS 2
  #define COLUMNS 16
  
  uint8_t nybbleA[4] = {0,0,0,0};
  uint8_t nybbleB[4] = {0,0,0,0};
  uint8_t whichNybble = 0;
  
  void setup(){
    Serial.begin(9600);
    lcd.begin(16,2);
    for (int i=0; i<4; i++){
      lcd.setCursor(i, 0);
      lcd.print(nybbleA[i]);
    }
    for (int i=0; i<4; i++){
      lcd.setCursor(i+5, 0);
      lcd.print(nybbleB[i]);
    }
  }
  
  void loop(){
    uint8_t buttons = lcd.readButtons();
    delay(50);
    if (buttons){
     if (buttons & BUTTON_SELECT){
       whichNybble = !whichNybble;
     }
        if (buttons & BUTTON_LEFT) {
        if (!whichNybble){
          nybbleA[0]=!nybbleA[0];
        } else if (whichNybble){
          nybbleB[0]=!nybbleB[0];
        }
      }
      if (buttons & BUTTON_UP) {
        if (!whichNybble){
          nybbleA[1]=!nybbleA[1];
        } else if (whichNybble){
          nybbleB[1]=!nybbleB[1];
        }
      }
      if (buttons & BUTTON_DOWN) {
        if (!whichNybble){
          nybbleA[2]=!nybbleA[2];
        } else if (whichNybble){
          nybbleB[2]=!nybbleB[2];
        }
      }
      if (buttons & BUTTON_RIGHT) {
        if (!whichNybble){
          nybbleA[3]=!nybbleA[3];
        } else if (whichNybble){
          nybbleB[3]=!nybbleB[3];
        }
      }
     //Refreshes the display.
    lcd.clear();
    for (int i=0; i<4; i++){
      lcd.setCursor(i, 0);
      lcd.print(nybbleA[i]);
    }
    for (int i=0; i<4; i++){
      lcd.setCursor(i+5, 0);
      lcd.print(nybbleB[i]);
    }
    uint8_t sum = addFunction(nybbleA, nybbleB);
    lcd.setCursor(0, 1);
    lcd.print(sum);
    }
  }
  
  int addFunction(uint8_t alpha[], uint8_t beta[]){
    int output1 = fulladderOutput(alpha, beta, 3, 0);
    int carry1 = fulladderCarry(alpha,beta, 3, 0);
    int output2 = fulladderOutput(alpha, beta, 2, carry1);
    int carry2 = fulladderCarry(alpha,beta, 2, carry1);
    int output3 = fulladderOutput(alpha, beta, 1, carry2);
    int carry3 = fulladderCarry(alpha,beta, 1, carry2);
    int output4 = fulladderOutput(alpha, beta, 0, carry3);
    int carry4 = fulladderCarry(alpha,beta, 0, carry3);
    
    //Converts the binary to an integer.
    int sum=0;
    if (carry4){
      sum=sum+pow(2, 4);
    }
    if (output4){
      sum=sum+pow(2, 3);
    }
    if (output3){
      sum=sum+pow(2, 2);
    }
    if (output2){
      sum=sum+pow(2, 1);
    }
    if (output1){
      sum=sum+pow(2, 0);
    }
    
    //Displays the outputs and carries in the Arduino IDE.
    uint8_t outputs[4] = {output1, output2, output3, output4};
    Serial.print("Outputs: ");
    for (int i=0; i<4; i++){
    Serial.print(outputs[i]);
    Serial.print(" ");
    }
    Serial.println();
    uint8_t carries[5] = {0, carry1, carry2, carry3, carry4};
    Serial.print("Carries: ");
    for (int i=0; i<5; i++){
    Serial.print(carries[i]);
    Serial.print(" ");
    }
    Serial.println();
    Serial.println();
    
    // Prints a binary representation of the sum to the lcd. 
    uint8_t binaryrep[5] = {carry4, output4, output3, output2, output1};
    for (int i=0; i<5; i++){
    lcd.setCursor(i+5,1);
    lcd.print(binaryrep[i]);
    }
    return sum;
  }
  
  int halfadderCarry(uint8_t alpha[], uint8_t beta[], uint8_t index){
    return (alpha[index] & beta[1index]);
  }
  
  int halfadderOutput(uint8_t alpha[], uint8_t beta[], uint8_t index){
     return (alpha[index] xor beta[index]);
  }
  
  //Full adder implemented using half adders.
  
  int fulladderCarry(uint8_t alpha[], uint8_t beta[], uint8_t index, uint8_t carryin){
    int output1 = halfadderOutput(alpha, beta, index);
    int carryout1 = halfadderCarry(alpha, beta, index);
    int carryout2 = output1 & carryin;
    return (carryout1 | carryout2);
  }
  
  int fulladderOutput(uint8_t alpha[], uint8_t beta[], uint8_t index, uint8_t carryin){
        int output1 = halfadderOutput(alpha, beta, index);
        return (output1 xor carryin);
  }
  
  //Full adder implemented using XOR, XNOR, AND, OR gates.
  
//  int fulladderCarry(uint8_t alpha[], uint8_t beta[], uint8_t index, uint8_t carryin){
//    return (((alpha[index] | beta[index]) & carryin) | ((alpha[index] & beta[index])  & !carryin));
//  }
//  
//  int fulladderOutput(uint8_t alpha[], uint8_t beta[], uint8_t index, uint8_t carryin){
//    return (((alpha[index] xor beta[index]) & !carryin) | ((!(alpha[index] xor beta[index]) & carryin)));
//  }
//  
