package SnakeGame;

import java.awt.*;
// Body part of snake
public class BodyPart {

    private int xCoord, yCoord, width, height;


    public BodyPart(int xCoord, int yCoord, int tileSize) {
        this.xCoord = xCoord;
        this.yCoord = yCoord;
        width = tileSize;
        height = tileSize;
    }

    public void tick() {

    }

    public void draw(Graphics g){
        g.setColor(Color.YELLOW);
        g.fillRect(xCoord*width,yCoord*height,width,height);
    }
    public void drawApple(Graphics g){
        g.setColor(Color.RED);
        g.fillOval(xCoord*width,yCoord*height,width,height);
    }

    public int getxCoord() {
        return xCoord;
    }

    public void setxCoord(int xCoord) {
        this.xCoord = xCoord;
    }

    public int getyCoord() {
        return yCoord;
    }

    public void setyCoord(int yCoord) {
        this.yCoord = yCoord;
    }
}
