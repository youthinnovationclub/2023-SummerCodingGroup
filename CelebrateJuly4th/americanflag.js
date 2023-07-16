background(0, 0, 0); // used khan academy project to make this (JavaScript, 600x400)
noStroke();

var xPos = 15.625;
var yPos = 12.5;

var star = function(xPos,yPos) { // code for star
triangle(xPos, yPos, xPos+13.610, yPos-3, xPos+7, yPos-17);
triangle(xPos+13.750, yPos, xPos+13.875, yPos+15.658, xPos-11, yPos-4.0);
triangle(xPos-0.125, yPos+15.875, xPos+25.250, yPos-3.125, xPos,yPos-3);
};

fill (0, 0, 255); // blue box
rect(0, 0, 250, 200);

fill (255, 255, 255); // stars
star(20, 20);
star(60, 20);
star(100, 20);
star(140, 20);
star(180, 20);
star(220, 20);
star(40, 40);
star(80, 40);
star(120, 40);
star(160, 40);
star(200, 40);
star(20, 60);
star(60, 60);
star(100, 60);
star(140, 60);
star(180, 60);
star(220, 60);
star(40, 80);
star(80, 80);
star(120, 80);
star(160, 80);
star(200, 80);
star(20, 100);
star(60, 100);
star(100, 100);
star(140, 100);
star(180, 100);
star(220, 100);
star(40, 120);
star(80, 120);
star(120, 120);
star(160, 120);
star(200, 120);
star(20, 140);
star(60, 140);
star(100, 140);
star(140, 140);
star(180, 140);
star(220, 140);
star(40, 160);
star(80, 160);
star(120, 160);
star(160, 160);
star(200, 160);
star(20, 180);
star(60, 180);
star(100, 180);
star(140, 180);
star(180, 180);
star(220, 180);

fill(255, 0, 0);
rect(250, 0, 350, 28.5714286); // top stripes (red)
rect(250, 28.5714286*2, 350, 28.5714286);
rect(250, 28.5714286*4, 350, 28.5714286);
rect(250, 28.5714286*6, 350, 28.5714286);

rect(0, 228.5714286, 600, 28.5714286); // bottom stripes (red)
rect(0, 200 + 28.5714286 * 3, 600, 28.5714286);
rect(0, 200 + 28.5714286 * 5, 600, 28.5714286);

fill(255, 255, 255);
rect(250, 28.5714286, 350, 28.5714286); // top stripes (white)
rect(250, 28.5714286 * 3, 350, 28.5714286);
rect(250, 28.5714286 * 5, 350, 28.5714286);

rect(0, 28.5714286 * 7, 600, 28.5714286); // bottom stripes (white
rect(0, 28.5714286 * 9, 600, 28.5714286);
rect(0, 28.5714286 *11, 600, 28.5714286);