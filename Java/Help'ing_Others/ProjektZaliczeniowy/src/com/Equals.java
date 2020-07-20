package com;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

/**
 * Klasa dodatkowa, ale mogłoby to być w klasie Main, wprowadziłem ją, by zrobić projekt bardziej przejrzystym.
 *
 */
public class Equals implements WypelnienieKolorem{


    /**
     *
     * @param figuraA  Dostarczona figura w klasie "Figury" tj. boki, pole, obwód,
     * @param figuraB  Dostarczona figura w klasie "Figury" tj. boki, pole, obwód,
     * @return Równe czy nie równe (Prawda/fałsz)
     */

    public boolean Equals(Figury figuraA, Figury figuraB){
        if (figuraA == null || figuraB == null) {
            return false;
        }
            if(figuraA.getPole()==((figuraB).getPole())){
                return figuraA.getA()==((figuraB).getA()) && figuraA.getB()==((figuraB).getB()) &&
                        figuraA.getC()==((figuraB).getC()) && figuraA.getD()==((figuraB).getD()) &&
                        figuraA.getPole()==((figuraB).getPole());
            }
        return false;
    }

    /**
     * Oblicza odpowiednie figury w zależności od ilosci dostarczonych punktów, samemu dobiera co to za figura na podstawie punktów
     * @return "Figury" - Boki, pole, obwód w klasie
     */
    public Figury ObliczeniaFigur(Punkt A, Punkt B, Punkt C, Punkt D){
        Figury figuraA = new Figury();


        if (C == null && D == null) {
            Kolo aa = new Kolo(A,B);

            figuraA = new Figury(aa.getBokA(), aa.getBokB(), aa.getBokC(), aa.getBokD(), aa.getPole(), aa.getObwod());
        }

        if (C != null && D == null) {

            Trojkat aa = new Trojkat(A, B, C);
            figuraA = new Figury(aa.getBokA(), aa.getBokB(), aa.getBokC(), aa.getBokD(), aa.getPole(), aa.getObwod());
        }
        if (C != null && D != null){
            Prostokat aa = new Prostokat(A, B, C, D);
            figuraA = new Figury(aa.getBokA(), aa.getBokB(), aa.getBokC(), aa.getBokD(), aa.getPole(), aa.getObwod());
        }
        return figuraA;
    }

    /**
     * Metoda pozwalająca na dodanie koloru
     * @param R wartość R
     * @param G wartość G
     * @param B wartość B
     * @return Odpowiedni kolor w wartości RGB
     */
    @Override
    public Color kolor(int R, int G, int B) {
        Color kolor1 = new Color(R, G, B);
        return kolor1;
    }
}
