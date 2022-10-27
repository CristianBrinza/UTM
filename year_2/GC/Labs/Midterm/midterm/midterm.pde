//Midterm 1 Variant 2  Cristian Brinza FAF-212 (pacman eating cube)

Object[] Objects = new Object[3]; // i will add only 3 objects so they will be declared bellow

void setup() {
  size(1800, 300);  // size of the canvas
  Objects[0] = new Object(255, 255, 0, 0, 0.01);   //object 1
  Objects[1] = new Object(0, 255, 255, 350, 0.02); // objet 2
  Objects[2] = new Object(255, 0, 255, 700, 0.04); //object 3   , as i said earlier i declared 3 objects only ( the array)

}

void draw(){
  background(200, 200, 200);
  fill(60);
  rect(0,0,0,0 );
  for (int i = 0; i < 3; i++) {
    Objects[i].update();
    Objects[i].checkingFunction();
    Objects[i].display();
  }
}

class Object {
  PVector location,velocity, acceleration;// declaring the movn
  int posX,colorofobject1, colorofobject2, colorofobject3;
  
  Object (int c1, int c2, int c3, int posX, float accelerationVar) {  // the object task 2
    colorofobject1 = c1;
    colorofobject2 = c2;
    colorofobject3 = c3;
    location = new PVector(posX, 600);
    velocity = new PVector(0, 0);
    acceleration = new PVector(accelerationVar, 0);
  }
   void checkingFunction() {
    if (location.x > width) {
      location.x = -120;
    }
  }
  
  void update() { // updating the velocity and aclelerations of declared objects after leaving the space(width)
    velocity.add(acceleration);
    location.add(velocity);
  }
  
  
  
  
  void display() {
    strokeWeight(2);
    fill(colorofobject1, colorofobject2, colorofobject3);
    rect(location.x + 225, 125, 50, 50);  // square pacman tryes to eat
     fill(255, 255, 255, 255);
    arc(location.x+150, 150, 300, 300,PI/6, PI+PI/2+PI/3, PIE); // body of pacman
    fill(0, 0,0, 255);
     ellipse(location.x + 150, 90,40, 40);   //pacman eye
  }
  
  
  
 
}
