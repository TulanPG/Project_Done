package com;


/**
 * Klasa rozszerzająca Figurę oraz Interfejs Obliczenia, pozwala liczyć dane z wprowadzonych punktów (2szt).
 * Klasa wykorzystuje metody toString celem wywołania danych oraz odpowiednie implementacje pola i obwodu.
 *
 */

public class Kolo extends Figura implements Obliczenia{

    final static double pi = 3.1416;
    private double pole, obwod, bokA, bokB, bokC, bokD;



    public Kolo(Punkt A, Punkt B) {
        super(A, B);
        Figura pomocniczy = new Linia(A,B);

        setBokA(((Linia) pomocniczy).getA());
        setBokB(0);
        setBokC(0);
        setBokD(0);
        setPole(poleKolo(getBokA()));
        setObwod(obwodKolo(getBokA()));
    }

    @Override
    public String toString() {
        return "Kolo{" +
                "pole=" + pole +
                ", obwod=" + obwod +
                '}';
    }

    @Override
    public double linia(Punkt A, Punkt B) {
        return 0;
    }

    @Override
    public double poleTrojkat(Punkt A, Punkt B, Punkt C) {
        return 0;
    }

    @Override
    public double poleKolo(double a) {
        double pole;
        pole = pi*a*a;

        return pole;
    }

    @Override
    public double poleProstokat(double max, double min) {
        return 0;
    }

    @Override
    public double obwod(double a, double b, double c, double d) {
        return 0;
    }

    @Override
    public double obwodKolo(double a) {
        double obwodKola;
        obwodKola = pi * a * 2;
        return obwodKola;
    }

    public double getPole() {
        return pole;
    }

    public void setPole(double pole) {
        this.pole = pole;
    }

    public double getObwod() {
        return obwod;
    }

    public void setObwod(double obwod) {
        this.obwod = obwod;
    }
    public double getBokA() {
        return bokA;
    }

    public void setBokA(double bokA) {
        this.bokA = bokA;
    }

    public double getBokB() {
        return bokB;
    }

    public void setBokB(double bokB) {
        this.bokB = bokB;
    }

    public double getBokC() {
        return bokC;
    }

    public void setBokC(double bokC) {
        this.bokC = bokC;
    }

    public double getBokD() {
        return bokD;
    }

    public void setBokD(double bokD) {
        this.bokD = bokD;
    }
}
