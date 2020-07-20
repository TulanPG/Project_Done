package SnakeGame;

import javax.swing.*;

public class Main {
//Press enter for replay

    public Main(int hardLevelSet) {
        JFrame frame = new JFrame();
        GamePanel gamePanel =new GamePanel();
        gamePanel.setHardLevel(hardLevelSet);
        frame.add(gamePanel);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("SnakeGame_ByTulan");
        frame.pack();
        frame.setVisible(true);
        frame.setLocationRelativeTo(null);
        frame.setResizable(false); // Window can't be Resizable
    }





    public static void main(String[] args) {

        new OpenPanel();

    }

}
