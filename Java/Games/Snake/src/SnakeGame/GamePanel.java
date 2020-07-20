package SnakeGame;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.Random;

import javax.swing.*;

public class GamePanel extends JPanel implements Runnable, KeyListener {

    private static final long serialVersionUID = 1L;

    public static final int WIDTH = 400, HEIGHT = 400;

    private Thread thread;
    private boolean running = false;

    private BodyPart b;
    private ArrayList<BodyPart> snake;

    private Apple apple, apple2, apple3;

    private ArrayList<Apple> apples;

    private Random r;

    private int xCoor = 10, yCoor = 10;
    private int size = 5;


    public int getSizeOfSnake() {
        return size;
    }

    private int hardLevel = 650000; //Deflaut is hard, medium = 500000, easy = 1000000

    public int getHardLevel() {
        return hardLevel;
    }

    public void setHardLevel(int hardLevel) {
        this.hardLevel = hardLevel;
    }

    private boolean right = true, left = false, up = false, down =false;

    private int ticks = 0;

    public GamePanel() {

        setFocusable(true);

        addKeyListener(this);
        setPreferredSize(new Dimension(WIDTH, HEIGHT));

        r = new Random();

        snake = new ArrayList<BodyPart>();
        apples = new ArrayList<Apple>();

        start();
    }

    public void tick() {
        if (snake.size() == 0) {
            b = new BodyPart(xCoor, yCoor, 10);
            snake.add(b);

        }
        if(apples.size() == 0) {
            int xCoor = r.nextInt(39);

            apple = new Apple(r.nextInt(39), r.nextInt(39), 10);
            apple2 = new Apple(r.nextInt(39), r.nextInt(39), 10);//Extra
            apple3 = new Apple(r.nextInt(39), r.nextInt(39), 10);//Extra
            apples.add(apple);
            apples.add(apple2);//Extra
            apples.add(apple3);//Extra
        }
        //Additional apple after eat
        if(apples.size() == 2) {

            apple = new Apple(r.nextInt(39), r.nextInt(39), 10);

            apples.add(apple);


        }

        for(int i = 0; i < apples.size(); i++) {
            if(xCoor == apples.get(i).getxCoor() &&
                    yCoor == apples.get(i).getyCoor()) {
                size++;
                apples.remove(i);
                i++;
            }
        }

        for(int i =0; i < snake.size(); i++) {
            if(xCoor == snake.get(i).getxCoord() &&
                    yCoor == snake.get(i).getyCoord()) {
                if(i != snake.size() - 1) {
                    stop();
                }
            }
        }
        if(xCoor < 0 || xCoor > 39 || yCoor < 0 || yCoor > 39) {
            stop();

        }

        ticks++;

        if(ticks > getHardLevel()) {
            if(right) xCoor++;
            if(left) xCoor--;
            if(up) yCoor--;
            if(down) yCoor++;

            ticks = 0;

            b = new BodyPart(xCoor, yCoor, 10);
            snake.add(b);

            if(snake.size() > size) {
                snake.remove(0);

            }
        }
    }

    public void paint(Graphics g) {
        g.clearRect(0, 0, WIDTH, HEIGHT);
        g.setColor(Color.darkGray);
        g.fillRect(0, 0, WIDTH, HEIGHT);


        g.setColor(Color.gray);
        for (int i = 0; i < WIDTH / 10; i++) {
            g.drawLine(i * 10, 0, i * 10, HEIGHT);
        }
        for (int i = 0; i < HEIGHT / 10; i++) {
            g.drawLine(0, i * 10, WIDTH, i * 10);
        }
        //Digital Apple's eatten displayer
        g.setColor(Color.WHITE);
        g.setFont(new Font("Serif", Font.BOLD, 25));
        g.drawString(String.valueOf(getSizeOfSnake()-5),10,40);

        for (int i = 0; i < snake.size(); i++) {

                    snake.get(i).draw(g);
                    if(i>=5) snake.get(i-5).drawApple(g);


        }
        for(int i = 0; i < apples.size(); i++) {
            apples.get(i).draw(g);


        }

    }

    public void start() {
        running = true;
        thread = new Thread(this);
        thread.start();
    }

    public void stop() {

        running = false;

        try {
            thread.join();
        } catch (InterruptedException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        new OpenPanel();


    }

    public void run() {
        while (running) {
            tick();
            repaint();
        }
    }

    @Override
    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();
        if((key == KeyEvent.VK_RIGHT || key == KeyEvent.VK_D )&& !left){
            right = true;
            up = false;
            down = false;
        }
        if((key == KeyEvent.VK_LEFT || key == KeyEvent.VK_A )&& !right){
            left = true;
            up = false;
            down = false;
        }
        if((key == KeyEvent.VK_UP || key == KeyEvent.VK_W )&& !down){
            right = false;
            left = false;
            up = true;
        }
        if((key == KeyEvent.VK_DOWN || key == KeyEvent.VK_S )&& !up){
            right = false;
            left = false;
            down = true;
        }
        //After dead, replay
        if(key == KeyEvent.VK_ENTER && !running){
            new Main(getHardLevel());
        }

    }
    @Override
    public void keyReleased(KeyEvent arg0) {
    }
    public void keyTyped(KeyEvent arg0) {
    }
}

