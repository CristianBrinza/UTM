PShape letter;  // The PShape object
int a=0;
void setup() {
  size(600, 600, P3D);
  // Creating a custom PShape as a square, by
  // specifying a series of vertices.
  letter = createShape();
  letter.beginShape();
  letter.fill(0);
  letter.noStroke();
  letter.vertex(0, 0);
  letter.vertex(200, 0);
  letter.vertex(200, 50);
  letter.vertex(60, 200);
  letter.vertex(200, 200);
  letter.vertex(200, 250);
  letter.vertex(0, 250);
  letter.vertex(0, 200);
  letter.vertex(140, 50);
  letter.vertex(0, 50);
  letter.endShape(CLOSE);
}
    
void draw() {
  a++;
 background(255);
  translate(300, 280);
  rotateX(radians(a));
  rotateY(radians(a));
  rotateZ(radians(a));
  translate(-100, -120);
  shape(letter); // Draw the group
}
