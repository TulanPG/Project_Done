package SnakeGame;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class OpenPanel {

    //Panel for chose difficult level

    public OpenPanel() {

        GamePanel t = new GamePanel();
        JFrame f=new JFrame("Difficult Level Chosen:");
        JButton b=new JButton("Hard");
        b.setBounds(50,100,140,30);
        JButton b2=new JButton("Medium");
        b2.setBounds(190,100,140,30);
        JButton b3=new JButton("Easy");
        b3.setBounds(50,150,140,30);
        JButton b4=new JButton("Beginner");
        b4.setBounds(190,150,140,30);

        JButton b5=new JButton("Difficult level: Easy");
        b5.setBounds(50,200,280,60);
        JButton b6=new JButton("Press for Start Game");
        b6.setBounds(50,265,280,60);

        f.add(b);f.add(b2);f.add(b3);f.add(b4);f.add(b5);f.add(b6);
        f.setSize(400,400);
        f.setLayout(null);
        f.setVisible(true);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setLocationRelativeTo(null);
        b.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                b5.setText("Difficult level:Hard");
                t.setHardLevel(450000);
            }
        });
        b2.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                b5.setText("Difficult level:Medium");
                t.setHardLevel(500000);
            }
        });
        b3.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                b5.setText("Difficult level:Easy");
                t.setHardLevel(650000);
            }
        });
        b4.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                b5.setText("Difficult level:Beginner");
                t.setHardLevel(1000000);
            }
        });
        b6.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                new Main(t.getHardLevel());
                f.setVisible(false);
            }
        });


    }
}
