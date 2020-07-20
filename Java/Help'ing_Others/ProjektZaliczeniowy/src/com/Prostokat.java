package com;
/**
 * Klasa rozszerzająca Figurę oraz Interfejs Obliczenia, pozwala liczyć dane z wprowadzonych punktów (4szt).
 * Klasa wykorzystuje metody toString celem wywołania danych oraz odpowiednie implementacje pola i obwodu.
 *
 */
public class Prostokat extends Figura implements Obliczenia{

    public double pole, obwod, min, max, bokA, bokB, bokC, bokD;


    public Prostokat(Punkt A, Punkt B, Punkt C, Punkt D) {
        super(A, B, C, D);


        Figura pomocniczy = new Linia(A,B,C,D);

        setBokA(((Linia) pomocniczy).getA());
        setBokB(((Linia) pomocniczy).getB());
        setBokC(((Linia) pomocniczy).getC());
        setBokD(((Linia) pomocniczy).getD());
        min =((Linia) pomocniczy).getA();
        max =((Linia) pomocniczy).getD();

        setObwod(obwod(getBokA(),getBokB(),getBokC(),getBokD()));
        setPole(poleProstokat(min,max));
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

    @Override
    public String toString() {
        return "Prostokat{" +
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
        return 0;
    }

    @Override
    public double poleProstokat(double max, double min) {

        double pole;
        pole = max*min;


        return pole;
    }

    @Override
    public double obwod(double a, double b, double c, double d) {

        double obwod = a+b+c+d;
        return obwod;

    }

    @Override
    public double obwodKolo(double a) {
        return 0;
    }
}
