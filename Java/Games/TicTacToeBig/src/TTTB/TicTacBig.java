package TTTB;


import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.geom.Ellipse2D;
import java.util.ArrayList;
import javax.swing.JFrame;
import javax.swing.JOptionPane;


public class TicTacBig extends JFrame
{
    private final int[] pole = new int[64];

    int x;
    int y;
    int pelne;
    int stWartosc=111;
    int stPole;
    boolean czy=true;
    boolean czy2= false;
    int []abc=new int[3];
    private final ArrayList<Ellipse2D> kolo=new ArrayList<>();
    int[] plansza={ 0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0 }; // 0, 1, 2... 8,9...  /n 10, 11 ...18, 19 /n 20, 21... etc
    private int kto=2;   // Player or Player2/cpu?



    public TicTacBig()
    {
        setSize(540, 720);
        //Początkowe pola ewentualnie lub coś

        Myszka mysz= new Myszka();
        addMouseListener(mysz);

    }


    public static void main(String[] args)
    {
        TicTacBig tictacD= new TicTacBig();
        tictacD.setVisible(true);
        tictacD.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public void paint(Graphics g)
    {
        Graphics2D g2=(Graphics2D)g;
        rysujLinie(g2);
        //Tutaj tabelke z wyborem na 1 lub 2 graczy!
        int i=0;
        for(Ellipse2D el:kolo)
        {
            kolor(el,i,g2);

            i++;
        }
    }

    public void kolor(Ellipse2D el,int i, Graphics2D g2)
    {
        if(i%2 == 0)
        { //player
            g2.setColor(Color.red);

        }
        else //player2 or cpu
            g2.setColor(Color.green);
        g2.fill(el);

    }

    public void rysujLinie(Graphics2D g2)
    {

        for(int j=0; j<14; j++)
        {
            g2.setColor(Color.red);

            g2.drawLine(20+50*j, 200, 20+50*j, 700); // xx, punkt początkowy PION, xx, punkt końcowy PION (linni)
            for(int jj=2; jj<13; jj++)
            {
                g2.drawLine(20, 100+50*jj, 520, 100+50*jj);
            }}
    }

    class Myszka extends MouseAdapter
    {

        public boolean czyDozwolonyRuch(int xy)
        {
            TicTacBig test= new TicTacBig();




            if (plansza[xy] != 0)
            {
                return false;
            }else { // to do

                if(kto==2)
                { plansza[xy] = kto;
                    kto++;

                }

                else if(kto==3)
                { plansza[xy] = kto;
                    kto--;

                }return true;
            }}


        public void czyWygralem(int xy){
            int k;
            String gr;
            if(kto==2)
            {
                k=2;
                gr="czerwony";
            }
            else
            {
                k=3;
                gr="zielony";
            }
            //Klops! Jakie warunki wygranej by się nie bugowało? / /WARUNKI SĄ DLA 3 kulek!!
            for (int i = 0; i<100;i++) {


                if (i < 8 || i>9 && i<18 ||  i>19 && i<28 || i>29 && i<38 || i>39 && i<48 || i>49 && i<58 || i>59 && i<68 || i>69 && i<78 || i>79 && i<88 || i>89 && i<98)
                //horizontal rows & diagonals right (without 8, 9,... 18, 19...)
                {
                    if (	(plansza[i]==k&&plansza[i+1]==k&&plansza[i+2]==k)//max  7, 7+1, 7+2
                            ||
                            (plansza[i]==k&&plansza[i+11]==k&&plansza[i+22]==k) )


                    {
                        JOptionPane.showMessageDialog(null, "wygrał gracz "+gr +"\n(poziomo lub prawo skośnie)\n Pola wygrane i:" + i + " " + (i+1)+ " " + (i+2));
                        System.exit(0);
                    }
                }
                if (i<80) //vertical columns  (without 80, 81,... 90, 91...)
                {
                    if (	(plansza[i]==k&&plansza[i+10]==k&&plansza[i+20]==k) )


                    {
                        JOptionPane.showMessageDialog(null, "wygrał gracz "+gr+"\n(Pionowo)\n Pola wygrane i:" + i + " " + (i+10)+ " " + (i+20));
                        System.exit(0);
                    }
                }

                if (i >2 && i < 10 || i>12 && i<20 ||  i>22 && i<30 || i>32 && i<40 || i>42 && i<50 || i>52 && i<60 || i>62 && i<70 || i>72 && i<80 || i>82 && i<90 || i>92 && i<100)
                {		//diagonals left (without 0, 1, 10, 20...)

                    if (	(plansza[i]==k&&plansza[i+9]==k&&plansza[i+18]==k)
                    )

                    {
                        JOptionPane.showMessageDialog(null, "wygrał gracz "+gr+"\n(lewo skośnie )\n Pola wygrane i:" + i + " " + (i+9)+ " " + (i+18));
                        System.exit(0);
                    }
                }


            }// end warunków wygranych for (int i = 0; i<100;i++)




        /*
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


            }}*/


        }



        public void dodajKolo(int x, int y)
        {
            kolo.add( new Ellipse2D.Double(25+(x*50), 205+(y*50), 40, 40));

        }

        @Override
        public void mouseClicked(MouseEvent e) {

            x=e.getX();
            y=e.getY();

            int modX = (x-20)/50;//pozycja tabeli x
            int modY = (y-200)/50;//pozycja tabeli y

            String sx = Integer.toString(modX);
            String sy = Integer.toString(modY);
            String sxsy= sy+sx;  // Określenie pozycji w tablixy Y+X
            int xy = Integer.parseInt(sxsy);
            czyWygralem(xy);
            if(czyDozwolonyRuch(xy))
            {

                dodajKolo(modX, modY);

                // ruchCPU.cpu();
            }
            //System.out.println(Arrays.toString(plansza));
            repaint();
            czyWygralem(xy);
        }


        @Override
        public void mouseEntered(MouseEvent arg0) {
            // TODO Auto-generated method stub

        }

        @Override
        public void mouseExited(MouseEvent arg0) {
            // TODO Auto-generated method stub

        }

        @Override
        public void mousePressed(MouseEvent arg0) {
            // TODO Auto-generated method stub

        }

        @Override
        public void mouseReleased(MouseEvent arg0) {
            // TODO Auto-generated method stub

        }
    }



} // END
