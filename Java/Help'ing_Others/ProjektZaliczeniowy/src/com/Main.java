package com;


import java.awt.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Projekt zrealizowany na 2 sposoby obliczeń (pojedyńcze obliczanie i metodą ToString wyrzucanie np.:
 * (Figura a = new Trojkat(A, B, C);),
 * Dodana jest klasa Equals, która porządkuje projekt, dodaje drugi sposób obliczeń, bardziej automatyczny
 * Dzięki niemu możemy wprowadzać dowolną ilość punktów, a program samemu dobiera sposób rozwiązywania kwestii
 * np. dając 2 punkty liczymy koło, 3 trójkąt, a 4 kwadrat/prostokąt
 */
public class Main{


    public static void main(String[] args) {
        List<Figury> figury = new ArrayList<>();

        Equals figura = new Equals();

        /*Punkt A = new Punkt(1, 2);
        Punkt B = new Punkt(1, 3);
        Punkt C = new Punkt(2, 4);
        Punkt D = new Punkt(3, 4);
        Punkt E = new Punkt(5, 4);
        Punkt Z = null;*/
        Scanner in = new Scanner(System.in);
        System.out.println("Wprowadz ilość figur: ");
        int ilosc = in.nextInt();

        for(int i = 0; i<ilosc; i++) {
            Punkt A = null,B=null,C=null,D=null,Z=null;

            System.out.println("Wprowadz ilość punktów figury "+i+": ");
            int iloscPunktow = in.nextInt();

            for(int j = 0; j<iloscPunktow; j++) {

                System.out.println("Wprowadz punkt " + (j+1) + ": \nx: ");
                int x = in.nextInt();
                System.out.println("Wprowadz punkt " + (j+1) + ": \ny: ");
                int y = in.nextInt();

                if(j==0) {
                    A = new Punkt(x, y);
                }
                if(j==1) {
                    B = new Punkt(x, y);
                }
                if(j==2) {
                    C = new Punkt(x, y);
                }
                if(j==3) {
                    D = new Punkt(x, y);
                }
            }
            figury.add(
                    figura.ObliczeniaFigur(A,B,C,D));
        }
        System.out.println(figury);


        System.out.println("Ile porównań chcesz wprowadzić: ");
        int ilosc2 = in.nextInt();
        for(int i = 0; i<ilosc2; i++) {

            System.out.println("Którą figurę chcesz porównać?\n wpisz pierwszą(kolejność wprowadzania): ");
            int figura1 = in.nextInt();
            System.out.println("Którą figurę chcesz porównać?\n wpisz druga(kolejność wprowadzania): ");
            int figura2 = in.nextInt();

            System.out.println("Figury są równe?: "+
                    figura.Equals(figury.get(figura1),figury.get(figura2)));
            System.out.println(figury.get(figura1) + " Wobec "+ figury.get(figura2));
        }

        System.out.println("Ile figur chcesz pokolorować: ");
        int ilosc3 = in.nextInt();
        for(int i = 0; i<ilosc3; i++) {

            System.out.println("Którą figurę chcesz pokolorować?\n (kolejność wprowadzania): ");
            int figura1 = in.nextInt();
            System.out.println("Jaki ma mieć kolor? (Wartość RGB)\n R : ");
            int kolorR = in.nextInt();
            int kolorG = in.nextInt();
            int kolorB = in.nextInt();

            figury.get(figura1).setColor(figura.kolor(kolorR,kolorG,kolorB));
            System.out.println(figury.get(figura1));

        }



        /*
       //Metoda krok po kroku na otrzymywanie wyników, brak konsoli dla tej metody, należy wprowadzać Punktu A,B,C...
       +Dodatkowo wykorzystanie tylko podstawowego zadania + Klasa Equals i Figury które mogły być w Main, ale zostały
       rozdzielone dla łatwiejszej pracy

        Punkt A = new Punkt(1, 2);// <--- Tutaj wprowadzamy współrzędne  za x,y
        Punkt B = new Punkt(1, 3);
        Punkt C = new Punkt(2, 2);
        Punkt D = new Punkt(3, 4);
        Punkt E = new Punkt(4, 5);
        Trojkat a = new Trojkat(A, B, C);
        Kolo b = new Kolo(A, B);
        Prostokat c = new Prostokat(A, B,C,D);
        Kwadrat d = new Kwadrat(A, B,C,E);
        Kwadrat e = new Kwadrat(E, A,B,C);
        //Figura e = new Kwadrat(E, A,B,C);
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);

        List<Figury> figury = new ArrayList<>();

        Equals figura = new Equals();

        figury.add(new Figury(a.getBokA(),a.getBokB(),a.getBokC(),a.getBokD(),a.getPole(), a.getObwod()));
        figury.add(new Figury(b.getBokA(),b.getBokB(),b.getBokC(),b.getBokD(),b.getPole(), b.getObwod()));
        figury.add(new Figury(c.getBokA(),c.getBokB(),c.getBokC(),c.getBokD(),c.getPole(), c.getObwod()));
        figury.add(new Figury(d.getBokA(),d.getBokB(),d.getBokC(),d.getBokD(),d.getPole(), d.getObwod()));
        figury.add(new Figury(e.getBokA(),e.getBokB(),e.getBokC(),e.getBokD(),e.getPole(), e.getObwod()));
        System.out.println("Czy równe: "+figura.Equals(figury.get(3),figury.get(4)));
        figury.get(1).setColor(figura.kolor(1,2,3));
        System.out.println(figury.get(1));
        */
    }

}
