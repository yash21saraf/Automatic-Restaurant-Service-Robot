#include "XBee.h"
#include "queue.h"
#include <SoftwareSerial.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(6, 7, 8, 9, 10, 11); //replace 0,1 by 6,7
/////////////////////////////////////////////////////////
XBee xbee;
Queue RxQ;
SoftwareSerial sserial(12,13);
//RX = 2,TX = 3
////////////////////////////////////////////////////////
#define MR1 4 //IN4
#define MR2 2 //IN3 orignally 2
#define MRP 5 //ENB
#define ML1 2 //IN2
#define ML2 1 //IN1 orignally 1
#define MLP 3 //ENA
////////////////////////////////////////////////////////////
int LFSensor[5] ;
int S ;
int lspeed = 0 ;
int rspeed = 0 ;
double rad,error=0.0,output=0.0,P,I,D,preverror=0,consKp=35,consKi=0.0,consKd=0;
unsigned int sm;
unsigned char M;
int cutoff=500 ;
char control = '#' ;
//////////////////////////////////////////////////////////
void motorsetup(){
    pinMode(MR1, OUTPUT);
    pinMode(MR2, OUTPUT);
    pinMode(MRP, OUTPUT);
    pinMode(ML1, OUTPUT);
    pinMode(ML2, OUTPUT);
    pinMode(MLP, OUTPUT);  
}

void sensorsetup(){
    pinMode(A0, INPUT);
    pinMode(A1, INPUT);
    pinMode(A2, INPUT);
    pinMode(A3, INPUT);
    pinMode(A4, INPUT);
    pinMode(A5, INPUT); 
}

void setup(){
  sserial.begin(9600);
  motorsetup() ;
  sensorsetup() ;
  lcd.begin(16, 2);
}

void motor(int l_speed,int r_speed)
{
  unsigned char M=0;
    if (l_speed >= 0) 
  {
      M|=0b00000100;
      M&=0b11111101;     
    }
    else 
  {
      M|=0b00000010;
      M&=0b11111011;
      l_speed*=-1;
    }
   if (r_speed >= 0) 
   {
      M|=0b00010000;
      M&=0b11111110;
   }
   else
    {
      M|=0b00000001;
      M&=0b11101111;

      r_speed*=-1;
    } 
  PORTD = M&0b00010111 ;
  analogWrite(MLP,l_speed) ;
  analogWrite(MRP,r_speed) ;
}
void read_sensor()
{
  if(analogRead(A0)>cutoff) LFSensor[0]=1;
  else  LFSensor[0]=0 ;
  if(analogRead(A1)>cutoff) LFSensor[1]=1;
  else  LFSensor[1]=0 ;
  if(analogRead(A2)>cutoff) LFSensor[2]=1;
  else  LFSensor[2]=0 ;
  if(analogRead(A3)>cutoff) LFSensor[3]=1;
  else  LFSensor[3]=0 ;
  if(analogRead(A4)>cutoff) LFSensor[4]=1;
  else  LFSensor[4]=0 ;

}
void line_follow()
{      
 
          if((     LFSensor[0]== 0 )&&(LFSensor[1]== 0 )&&(LFSensor[2]== 0 )&&(LFSensor[3]== 0 )&&(LFSensor[4]== 1 ))  {error = 4;}
  else if((LFSensor[0]== 0 )&&(LFSensor[1]== 0 )&&(LFSensor[2]== 0 )&&(LFSensor[3]== 1 )&&(LFSensor[4]== 1 ))  {error = 3;}
  else if((LFSensor[0]== 0 )&&(LFSensor[1]== 0 )&&(LFSensor[2]== 0 )&&(LFSensor[3]== 1 )&&(LFSensor[4]== 0 ))  {error = 2;}
  else if((LFSensor[0]== 0 )&&(LFSensor[1]== 0 )&&(LFSensor[2]== 1 )&&(LFSensor[3]== 1 )&&(LFSensor[4]== 0 ))  {error = 1;}
  else if((LFSensor[0]== 0 )&&(LFSensor[1]== 0 )&&(LFSensor[2]== 1 )&&(LFSensor[3]== 0 )&&(LFSensor[4]== 0 ))  {error = 0;}
  else if((LFSensor[0]== 0 )&&(LFSensor[1]== 1 )&&(LFSensor[2]== 1 )&&(LFSensor[3]== 0 )&&(LFSensor[4]== 0 ))  {error =- 1;}
  else if((LFSensor[0]== 0 )&&(LFSensor[1]== 1 )&&(LFSensor[2]== 0 )&&(LFSensor[3]== 0 )&&(LFSensor[4]== 0 ))  {error = -2;}
  else if((LFSensor[0]== 1 )&&(LFSensor[1]== 1 )&&(LFSensor[2]== 0 )&&(LFSensor[3]== 0 )&&(LFSensor[4]== 0 ))  {error = -3;}
  else if((LFSensor[0]== 1 )&&(LFSensor[1]== 0 )&&(LFSensor[2]== 0 )&&(LFSensor[3]== 0 )&&(LFSensor[4]== 0 ))  {error = -4;}
  //else if((LFSensor[0]== 1 )&&(LFSensor[1]== 1 )&&(LFSensor[2]== 1 )&&(LFSensor[3]== 1 )&&(LFSensor[4]== 1 ))  {mode = STOPPED; error = 0;}
 // else if((LFSensor[0]== 0 )&&(LFSensor[1]== 0 )&&(LFSensor[2]== 0 )&&(LFSensor[3]== 0 )&&(LFSensor[4]== 0 ))  {mode = NO_LINE; error = 0;}

        P = consKp * error;
        I += consKi * error;
        D = consKd * (error - preverror);
        preverror = error;
        output = P + I + D;
        rad = abs(output);

        if (output >= 0)
        {
             sm=170-rad ;
             motor(sm,220);
         }
         else
         {
              sm=220-rad ;
              motor(180,sm) ;
              
          }  
}
void loop() { 

 xbee_fun() ;
 if( control == '+') 
 {
  read_sensor() ;
  S = LFSensor[0] + LFSensor[1] + LFSensor[2] + LFSensor[3]+ LFSensor[4] ;
  while(S < 3)
  {
     read_sensor() ;
     S = LFSensor[0] + LFSensor[1] + LFSensor[2] + LFSensor[3]+ LFSensor[4] ;
     if(S==0)  motor(0,0) ;        
     line_follow() ;
  }
  motor(0,0) ;
  control = '#' ;
 }
 if(control == '-') 
 {
  motor(150,-170) ;
  delay(1200) ;
  motor(0,0) ;
  delay(1000) ;
  read_sensor() ;
  S = LFSensor[0] + LFSensor[1] + LFSensor[2] + LFSensor[3]+ LFSensor[4] ;
  while(S < 3)
  {
     read_sensor() ;
     S = LFSensor[0] + LFSensor[1] + LFSensor[2] + LFSensor[3]+ LFSensor[4] ;
     if(S==0)  motor(0,0) ;        
     line_follow() ;
  }
  motor(0,0) ;
  control = '#' ;
 }
}

void xbee_fun()
{
    delay(5);
    int queueLen = 0;
    int delPos = 0;

    while (sserial.available() > 0){
        unsigned char in = (unsigned char)sserial.read();
        if (!RxQ.Enqueue(in)){
            break;
        }
    }
    queueLen = RxQ.Size();
    for (int i=0;i<queueLen;i++){
        if (RxQ.Peek(i) == 0x7E){
            unsigned char checkBuff[Q_SIZE];
            unsigned char msgBuff[Q_SIZE];
            int checkLen = 0;
            int msgLen = 0;

            checkLen = RxQ.Copy(checkBuff, i);
            msgLen = xbee.Receive(checkBuff, checkLen, msgBuff);
 
            if (msgLen > 0){
                                
                unsigned char outMsg[Q_SIZE];
                unsigned char outFrame[Q_SIZE];
                int frameLen = 0;
                int addr = ((int )msgBuff[4] << 8) + (int)msgBuff[5];
                

                // 10 is length of "you sent: "
                memcpy(outMsg, "you sent: ", 10);
                // len - (9 bytes of frame not in message content)
                memcpy(&outMsg[10], &msgBuff[8], msgLen-9);
                control = *&outMsg[10] ;
                lcd.clear() ;
                for(int i = 10; i< msgLen+1 ; i++)
                {
                lcd.setCursor(i-10,1);
                lcd.print(char(*&outMsg[i]));
                }
                // 10 + (-9) = 1 more byte in new content than in previous message
                frameLen = xbee.Send(outMsg, msgLen+1, outFrame, addr);
                sserial.write(outFrame, frameLen);
                i += msgLen;
                delPos = i;    
            }else{
                if (i>0){
                    delPos = i-1;
                }
            }
        }
    }

    RxQ.Clear(delPos);
}

