package com;

import java.lang.reflect.Array;
import java.util.Arrays;

/**
 * Klasa rozszerzająca Figurę oraz Interfejs Obliczenia, pozwala liczyć dane z wprowadzonych punktów (2szt).
 * Klasa wykorzystuje metody toString celem wywołania danych oraz odpowiednie implementacje linia.
 *
 */

public class Linia extends Figura implements Obliczenia{

    private double a, b, c,d;

    public double getA() {
        return a;
    }

    public double getB() {
        return b;
    }

    public double getC() {
        return c;
    }

    public double getD() {
        return d;
    }



    public Linia(Punkt A, Punkt B) {
        super(A, B);
        double[] arr = sortujBoki(linia(A,B),-1,-1,-1);

        a = (double) Array.get(arr, 3);// Ponieważ index 0,1,2 jest niepotrzebną nam linnią, stworzona została uniwersalna metoda dla wszystkich figur.


    }

    public Linia(Punkt A, Punkt B, Punkt C) {
        super(A, B, C);

        double[] arr = sortujBoki(linia(A,B),linia(B,C),linia(C,A),-1);

        a = (double) Array.get(arr, 1);// Ponieważ index 0 jest niepotrzebną nam linnią, stworzona została uniwersalna metoda dla wszystkich figur.
        b = (double) Array.get(arr, 2);
        c = (double) Array.get(arr, 3);

    }

    public Linia(Punkt A, Punkt B, Punkt C, Punkt D) {
        super(A, B, C, D);

        double[] arr = sortujBoki(linia(A,B),linia(B,C),linia(C,D),linia(D,A));

        a = (double) Array.get(arr, 0);
        b = (double) Array.get(arr, 1);
        c = (double) Array.get(arr, 2);
        d = (double) Array.get(arr, 3);


    }


    public double[] sortujBoki(double z,double x,double zz,double xx){
        double[] arr = {z,x,zz,xx};
        Arrays.sort(arr);
        return arr;
    }

  /*  public static double max(double a, double b, double c, double d) {


        double max = a;

        if (b > max)
            max = b;
        if (c > max)
            max = c;
        if (d > max)
            max = d;

        return max;
    }
    public static double min(double a, double b, double c, double d) {

        double min = a;

        if (b < min)
            min = b;
        if (c < min)
            min = c;
        if (d < min)
            min = d;

        return min;
    }*/ // Metoda max min "ręcznie"

    @Override
    public double linia(Punkt A, Punkt B) {
        double pomocnicza1,pomocnicza2;

        pomocnicza1 = Math.pow((B.x - A.x),2);
        pomocnicza2 = Math.pow((B.y - A.y),2);
        double DlugoscLinii = Math.sqrt(pomocnicza1+pomocnicza2);

        return DlugoscLinii;
    }

    @Override
    public double poleTrojkat(Punkt A, Punkt B, Punkt C) {
        return 0;
    }

    @Override
    public double poleKolo(double a) {
        return 0;
    }

    @Override
    public double poleProstokat(double max, double min) {
        return 0;
    }

    @Override
    public double obwod(double  a, double  b, double  c, double  d) {
        return 0;
    }

    @Override
    public double obwodKolo(double a) {
        return 0;
    }


}
