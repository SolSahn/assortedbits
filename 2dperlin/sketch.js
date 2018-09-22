var speed;
var smoothness;
var detail;
var offset, initOffset = 0;
function setup() {
  createCanvas(640, 480);
  stroke(255);
  strokeWeight(3);
  noFill();
  speed = 0.015;
  smoothness = 0.015;
  detail = width/2;
}
function draw() {
  background(25, 25, 51);
  offset = initOffset
  beginShape();
  for (i = 0; i < detail; i++) {
    vertex(i * width/detail, map(noise(offset), 0, 1, height/2 - 200, height/2 + 200));
    offset += smoothness;
  }
  endShape();
  initOffset += speed;
}
