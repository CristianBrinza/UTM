float r, b, g, a, diam, x, y;
int ss = 0;

void setup() {
  size(480, 270);
  background(255);
}

void draw() { // Draw stuff

  // Use values to draw an ellipse

  // If the mouse is on the window is equivalent to 
  // "if mouseX is greater than 0"
  if (mouseX > 20 && mouseY > 20 && mouseX < width - 20 && mouseY < height - 20 && ss == 0) {

    for (int t = 0; t <= 5; t++) {

      // Each time through draw(), new random 
      // numbers are picked for a new ellipse.
      r = random(255);
      g = random(255);
      b = random(255);
      a = random(255);
      diam = random(90);
      //make sure there's no circles smaller than the next set diameter
      while (diam <= 20) {
        diam++;
      }
      x = random(width);
      y = random(height);

      noStroke();
      fill(r, g, b, a);
      ellipse(x, y, diam, diam);
      ss = 1;
    }

  } else if (mouseX < 20 || mouseY < 20 || mouseX > width - 20 || mouseY > height - 20) {
    fill(255);
    stroke(255);
    rect(0, 0, width, height);
    ss = 0;

  }

}
