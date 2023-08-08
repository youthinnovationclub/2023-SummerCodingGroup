void setup() { //made using processing js
  size(800, 400); //border
}

int x = 900;
int y = 200;

void draw() {
  background(0, 175, 250); // background
  
  noStroke();
  fill(0, 0, 255);
  rect(0, 200, 800, 200); //water
  
  fill(255, 255, 0);
  ellipse (x, y, 100, 70); //head
  
  fill(165, 42, 42);
  ellipse(x-35, y, 30, 70); //hair
  rect(x-35, y-35, 30, 70);
  fill(255, 255, 0);
  ellipse(x-5, y+20, 20, 100);
  fill(0, 0, 255);
  rect(0, y+35, 800, 800);
  
  fill(0);
  ellipse(x, y+20, 10, 10); //eye
  fill(0, 0, 0, 100);
  
  stroke(0);
  strokeWeight(5);
  ellipse(x, y+20, 20, 30); //goggles
  line(x, y+1, x, y-37);
  
  fill(200, 0, 0);
  noStroke();
  rect(x+20, y+15, 10, 20); //mouth
  
  fill(255, 255, 0);
  rect(x+25, y-12.5, 40, 25); //neck
  
  fill(0, 200, 255);
  ellipse(x+125, y, 150, 75); //shirt
  
  fill(0, 100, 255);
  rect(x+175, y-30, 75, 60); //shorts

  fill(255, 255, 0);
  rect(x+250, y-20, 75, 40); //legs
  ellipse(x+325, y+15, 25, 75);
  
  rect(x-75, y-10, 150, 20); //arm
  ellipse(x-75, y, 80, 20);
  
  stroke(0);
  strokeWeight(2);
  fill(0, 200, 255);
  rect(x+70, y-15, 20, 30); //sleeve
  
  fill(0, 0, 255);
  noStroke();
  ellipse(random(x+325, x+550), y, 20, 20); 
  ellipse(random(x+325, x+550), random(y-10, y), 20, 20); //splashes
  ellipse(random(x+325, x+550), random(y-20, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-30, y), 20, 20);
  ellipse(random(x+325, x+550), random(y-40, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-50, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-60, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-70, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-80, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-90, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-100, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-110, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-120, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-130, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-140, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-150, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-150, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-150, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-150, y), 20, 20); 
  ellipse(random(x+325, x+550), random(y-150, y), 20, 20); 
  
  x = x - 5; //movement
  
  textSize(50);
  fill(0, 0, 0);
  text("swimmer doing streamline", 175, 100); //text
}
  