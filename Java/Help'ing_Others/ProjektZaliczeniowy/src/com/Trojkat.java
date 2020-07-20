package com;

/**
 * Klasa rozszerzająca Figurę oraz Interfejs Obliczenia, pozwala liczyć dane z wprowadzonych punktów (3szt).
 * Klasa wykorzystuje metody toString celem wywołania danych oraz odpowiednie implementacje pola i obwodu.
 *
 */
public class Trojkat extends Figura implements Obliczenia{
    private double pole, obwod, bokA, bokB, bokC, bokD;



    public Trojkat(Punkt A, Punkt B, Punkt C) {
        super(A, B, C);
        Figura pomocniczy = new Linia(A,B,C);
        setBokA(((Linia) pomocniczy).getA());
        setBokB(((Linia) pomocniczy).getB());
        setBokC(((Linia) pomocniczy).getC());
        setBokD(0);
        setObwod(obwod(getBokA(),getBokB(),getBokC(),getBokD()));
        setPole(poleTrojkat(A,B,C));
    }




    @Override
    public String toString() {
        return "Trojkat{" +
                "pole=" + pole +
                ", obwod=" + obwod +
                '}';
    }

    public void setPole(double pole) {
        this.pole = pole;
    }

    public double getPole() {
        return pole;
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


    @Override
    public double linia(Punkt A, Punkt B) {
        return 0;
    }

    @Override
    public double poleTrojkat(Punkt A, Punkt B, Punkt C) {
        double area = (A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y)) / 2.0;
        return Math.abs(area);
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
        double obwod = a+b+c+d;
        return obwod;
    }

    @Override
    public double obwodKolo(double a) {
        return 0;
    }


}
