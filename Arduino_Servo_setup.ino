// Test code to set up all servos on Arduino Nano
#include<Servo.h>
#define joint_no 6

Servo joint_1,joint_2A,joint_2B,joint_3,joint_4,joint_5;
Servo joint_list[joint_no] = {joint_1,joint_2A,joint_2B,joint_3,joint_4,joint_5};
int pwm_pins[joint_no] = {4,5,6,7,8,9};

void startup_Neutral(){
  //Function to setup all pin connections and set all servos to 90 degrees
  for(int i = 0; i < joint_no; i++){
    joint_list[i].attach(pwm_pins[i]);
  }
  
  for(int i = 0; i < joint_no; i++){
    joint_list[i].write(90);
  }
  
}


void test_joints(){
 // code to test all 6 servos simultenously
 joint_list[3].write(150);
 for(int pos = 60; pos < 150; pos++){
  joint_list[1].write(pos);
  joint_list[2].write(180-pos);
  delay(25);
 }
}



void setup() {
  // put your setup code here, to run once:
  startup_Neutral();
  delay(100);
  test_joints();
  delay(10);
  startup_Neutral();
}

void loop() {
  // put your main code here, to run repeatedly:

}
