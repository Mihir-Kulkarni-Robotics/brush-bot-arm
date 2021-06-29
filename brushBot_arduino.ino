// Code to upload on the arduino
#include<Servo.h>
#define joint_no 6

Servo joint_1,joint_2A,joint_2B,joint_3,joint_4,joint_5;
Servo joint_list[joint_no] = {joint_1,joint_2A,joint_2B,joint_3,joint_4,joint_5};
int pwm_pins[joint_no] = {4,5,6,7,8,9};

int parabola_x[13] = {120, 115, 110, 105, 100, 95, 90, 85, 80, 75, 70, 65, 60};
int parabola_y1[13] = {30, 31, 31, 33, 36, 40, 40, 40, 36, 33, 31, 31, 30};
int parabola_y2[13] = {151, 157, 157, 162, 165, 167, 167, 167, 165, 162, 157, 157, 151};

String data;

// Functions for initialising Arm
void startup(){
  //Function to setup all pin connections and set all servos to 90 degrees
  for(int i = 0; i < joint_no; i++){
    joint_list[i].attach(pwm_pins[i]);
  }
  for(int i = 0; i < joint_no; i++){
    joint_list[i].write(90);
  }
}

void set_neutral(){
  //Sets arm to beginning position
  joint_list[1].write(90);
  joint_list[2].write(90);
  joint_list[3].write(180);
  joint_list[4].write(20);
  joint_list[5].write(90);
}

void brush_mode(String mode){
  // function to set brush orientation
  if(mode == "horizontal"){
      joint_list[4].write(20);
      joint_list[5].write(90);
  }
  else if(mode == "vertical"){
      joint_list[4].write(100);
      joint_list[5].write(0);
  }
 }

void test_joints(){
 // code to test all 6 servos simultenously or whatever the fuck
  for(int i = 0; i < 13 ; i++){
    joint_list[0].write(parabola_x[i]);
  
    joint_list[1].write(180 - parabola_y1[i]);
    joint_list[2].write(parabola_y1[i]);

    joint_list[3].write(180 - parabola_y2[i]);
    
    delay(300);
  }

}

//Functions for mouse control
void mouse_move(){
  //Function to control arm by using cursor position
       while (Serial.available()){
         data = Serial.readString();
         
      }
    
    moveX(data);
    delay(15);
    moveY(data);
    delay(15);
}

void moveX(String temp){
    //
      temp.remove(temp.indexOf("Y"));
      temp.remove(temp.indexOf("X"), 1);
    //
    
    curX = (temp.toInt());
    joint_list[1].write(180-curX);
    joint_list[2].write(curX);
   
}
//Function for Y axis motor
void moveY(String temp1){
    //
      temp1.remove(0,temp1.indexOf("Y") + 1);
      
    //
    
    curY = (temp1.toInt());
    joint_list[3].write(curY);
   
}

//
void manual_move(){
  //Function to move arm on pre-planned path using arrays
  // containing joint angles.
  while (Serial.available()){
     data = Serial.readString();
    }
    if(data == "whatever the mode is"){
        brush_mode("horizontal");
        //Enter stuff for front brushing
    }
    else if(data == "whatever the second mode is"){
        brush_mode(vertical);
        //Enter code here for vertical movement
    }
}


void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  // 
  startup();
  delay(20);
  set_neutral();
  brush_mode("horizontal");
  delay(20);
  test_joints();
  
}

void loop() {
  // put your main code here, to run repeatedly:
  //test_joints();
  //mouse_move();
 
}