package TicTacToe;

import java.awt.Color;
import java.awt.EventQueue;
import java.awt.Graphics;
import java.awt.Graphics2D;

import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Point2D;
import java.util.ArrayList;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;

public class KolkoiKrzyzyk extends JFrame {


    private int x,y;
    private int kto=1;
    int[] plansza={0,0,0,0,0,0,0,0,0};
    private ArrayList<Ellipse2D> kolo=new ArrayList<>();


    public KolkoiKrzyzyk()
    {
        setSize(500,500);

        Grafika graf= new Grafika();
        add(graf);

        Myszka mysz= new Myszka();
        addMouseListener(mysz);


    }


    public static void main(String[] args)
    {
        EventQueue.invokeLater(new Runnable() {

            @Override
            public void run()
            {
                KolkoiKrzyzyk kik= new KolkoiKrzyzyk();
                kik.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                kik.setVisible(true);
            }
        });


    }

    class Grafika extends JPanel
    {




        public void paintComponent(Graphics g)
        {
            Graphics2D g2= (Graphics2D)g;
            g2.drawLine(100, 200, 400, 200);
            g2.drawLine(100, 300, 400, 300);
            g2.drawLine(200, 100, 200, 400);
            g2.drawLine(300, 100, 300, 400);
            int i=0;
            for(Ellipse2D el:kolo)
            {
                kolor(el,i,g2);

                i++;
            }

        }

        public void kolor(Ellipse2D el,int i, Graphics2D g2)
        {
            if(i==0 || i==2||i==4||i==6||i==8)
            {
                g2.setColor(Color.red);

            }
            else
                g2.setColor(Color.green);
            g2.fill(el);
        }






    }

    class Myszka extends MouseAdapter
    {

        @Override
        public void mouseClicked(MouseEvent e)
        {
            x=e.getX();
            y=e.getY();


            if( czyDozwolonyRuch(x, y))
            {
                Myszka ruchCPU =new Myszka();
                dodajKolo( x, y);
                repaint();
                czyWygralem(x, y);
                ruchCPU.cpu();
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e1) {
                    // TODO Auto-generated catch block
                    e1.printStackTrace();
                }
                repaint();


            }

        }

        public boolean czyDozwolonyRuch(int x, int y)
        {
            if((x>108 && x<408)&&(y>131 && y<431))
            {
                if(x<208&&y<231)
                {
                    if(plansza[0]!=0)
                    {
                        return false;
                    }
                    else
                    {
                        if(kto==1)
                        {
                            plansza[0]=kto;

                            kto++;
                        }
                        else
                        {
                            plansza[0]=kto;

                            kto--;
                        }
                        return true;
                    }
                }
                else if(x>208&&x<308&&y<231)
                {
                    if(plansza[1]!=0)
                    {
                        return false;
                    }
                    else
                    {
                        if(kto==1)
                        {
                            plansza[1]=kto;

                            kto++;
                        }
                        else
                        {
                            plansza[1]=kto;

                            kto--;
                        }
                        return true;
                    }
                }
                else if(x>308&&y<231)
                {
                    if(plansza[2]!=0)
                    {
                        return false;
                    }
                    else
                    {
                        if(kto==1)
                        {
                            plansza[2]=kto;

                            kto++;
                        }
                        else
                        {
                            plansza[2]=kto;

                            kto--;
                        }
                        return true;
                    }
                }
                else if(x<208&&y<331&&y>231)
                {
                    if(plansza[3]!=0)
                    {
                        return false;
                    }
                    else
                    {
                        if(kto==1)
                        {
                            plansza[3]=kto;
                            kto++;
                        }
                        else
                        {
                            plansza[3]=kto;
                            kto--;
                        }
                        return true;
                    }

                }
                else if(x>208&&x<308&&y<331&&y>231)
                {
                    if(plansza[4]!=0)
                    {
                        return false;
                    }
                    else
                    {
                        if(kto==1)
                        {
                            plansza[4]=kto;
                            kto++;
                        }
                        else
                        {
                            plansza[4]=kto;
                            kto--;
                        }
                        return true;
                    }
                }
                else if(x>308&&y<331&&y>231)
                {
                    if(plansza[5]!=0)
                    {
                        return false;
                    }
                    else
                    {
                        if(kto==1)
                        {
                            plansza[5]=kto;
                            kto++;
                        }
                        else
                        {
                            plansza[5]=kto;
                            kto--;
                        }
                        return true;
                    }
                }
                else if(x<208&&y>331)
                {
                    if(plansza[6]!=0)
                    {
                        return false;
                    }
                    else
                    {if(kto==1)
                    {
                        plansza[6]=kto;
                        kto++;
                    }
                    else
                    {
                        plansza[6]=kto;
                        kto--;
                    }
                        return true;
                    }
                }
                else if(x>208&&x<308&& y>331)
                {
                    if(plansza[7]!=0)
                    {
                        return false;
                    }
                    else
                    {
                        if(kto==1)
                        {
                            plansza[7]=kto;
                            kto++;
                        }
                        else
                        {
                            plansza[7]=kto;
                            kto--;
                        }
                        return true;
                    }

                }
                else if(x>308&& y>331)
                {
                    if(plansza[8]!=0)
                    {
                        return false;
                    }
                    else
                    {
                        if(kto==1)
                        {
                            plansza[8]=kto;
                            kto++;
                        }
                        else
                        {
                            plansza[8]=kto;
                            kto--;
                        }
                        return true;
                    }
                }


                return true;
            }
            else
            {
                JOptionPane.showMessageDialog(null, "ruch poza obszarem gry");

                return false;
            }
        }

        public void czyWygralem(int x, int y)
        {int k;
            String gr;
            if(kto==2)
            {
                k=1;
                gr="czerwony";
            }
            else
            {
                k=2;
                gr="zielony";
            }

            if((plansza[0]==k&&plansza[1]==k&&plansza[2]==k)||
                    (plansza[3]==k&&plansza[4]==k&&plansza[5]==k)||
                    (plansza[6]==k&&plansza[7]==k&&plansza[8]==k)||
                    (plansza[0]==k&&plansza[3]==k&&plansza[6]==k)||
                    (plansza[1]==k&&plansza[4]==k&&plansza[7]==k)||
                    (plansza[2]==k&&plansza[5]==k&&plansza[8]==k)||
                    (plansza[0]==k&&plansza[4]==k&&plansza[8]==k)||
                    (plansza[6]==k&&plansza[4]==k&&plansza[2]==k) )

            {
                JOptionPane.showMessageDialog(null, "wygrał gracz "+gr);
                System.exit(0);
            }
            int remis=0;
            for(int i:plansza)
            {
                if(i==0)
                {
                    break;
                }
                else
                {
                    remis++;
                    if(remis==9)
                    {
                        JOptionPane.showMessageDialog(null, "remis ");
                        System.exit(0);
                    }

                }


            }




        }

        public void dodajKolo(int x, int y)
        {

            if(x<208&&y<231) {
                kolo.add( new Ellipse2D.Double(110, 120, 70, 70));
                System.out.println("Pozycja: 1");
            }

            else if(x>208&&x<308&&y<231) {
                kolo.add( new Ellipse2D.Double(220, 120, 70, 70));
                System.out.println("Pozycja: 2");
            }
            else if(x>308&&y<231) {
                kolo.add( new Ellipse2D.Double(320, 120, 70, 70));
                System.out.println("Pozycja: 3");
            }
            else if(x<208&&y<331&&y>231) {
                kolo.add( new Ellipse2D.Double(110, 220, 70, 70));
                System.out.println("Pozycja: 4");
            }
            else if(x>208&&x<308&&y<331&&y>231) {
                kolo.add( new Ellipse2D.Double(220, 220, 70, 70));
                System.out.println("Pozycja: 5");
            }
            else if(x>308&&y<331&&y>231) {
                kolo.add( new Ellipse2D.Double(320, 220, 70, 70));
                System.out.println("Pozycja: 6");
            }
            else if(x<208&&y>331) {
                kolo.add( new Ellipse2D.Double(110, 320, 70, 70));
                System.out.println("Pozycja: 7");
            }
            else if(x>208&&x<308&& y>331) {
                kolo.add( new Ellipse2D.Double(220, 320, 70, 70));
                System.out.println("Pozycja: 8");
            }
            else if(x>308&& y>331) {
                kolo.add( new Ellipse2D.Double(320, 320, 70, 70));
                System.out.println("Pozycja: 9");
            }
            else {
                JOptionPane.showMessageDialog(null, "ruch poza obszarem gry");
            }

        }

        //Randomowy CPU
        public void cpu() {
            Myszka ruchCPU =new Myszka();
            Random rand = new Random();
            int cpux, cpuy;
            boolean test;
            if(plansza[4]==1||plansza[4]==2){
                do {
                    cpux = rand.nextInt(299)+109;
                    cpuy =  rand.nextInt(299)+132;
                    test = ruchCPU.czyDozwolonyRuch(cpux,cpuy);

                }
                while (!(test));
                {
                    System.out.print("Komputer: ");
                    ruchCPU.dodajKolo(cpux, cpuy);
                }
            } else {
                cpux = 220;
                cpuy =  250;
                test = ruchCPU.czyDozwolonyRuch(cpux,cpuy);
                System.out.print("Komputer: ");
                ruchCPU.dodajKolo(cpux, cpuy);


            }czyWygralem(cpux, cpuy);
        }



    }



}

