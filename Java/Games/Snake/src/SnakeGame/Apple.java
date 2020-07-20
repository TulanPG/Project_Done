package SnakeGame;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;

public class Apple {

    private int xCoor, yCoor, width, height;

    public Apple(int xCoor, int yCoor, int tileSize) {
        this.xCoor = xCoor;
        this.yCoor = yCoor;
        width = tileSize;
        height = tileSize;
    }
    public void tick() {

    }
    public void draw(Graphics g) {
        /*int R = (int)(Math.random()*256);
        int G = (int)(Math.random()*256);
        int B= (int)(Math.random()*256);
        Color color = new Color(R, G, B);

        g.setColor(color);*/
        g.setColor(Color.RED);
        g.fillOval(xCoor * width , yCoor * height, width, height);

    }

    public int getxCoor() {
        return xCoor;
    }
    public void setxCoor(int xCoor) {
        this.xCoor = xCoor;
    }
    public int getyCoor() {
        return yCoor;
    }
    public void setyCoor(int yCoor) {
        this.yCoor = yCoor;
    }


}

