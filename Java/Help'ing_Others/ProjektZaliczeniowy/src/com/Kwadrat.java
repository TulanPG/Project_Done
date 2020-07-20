package com;
/**
 * Klasa rozszerzająca Prostokat oraz Interfejs Obliczenia, pozwala liczyć dane z wprowadzonych punktów (4szt).
 * Klasa wykorzystuje metody toString celem wywołania danych oraz odpowiednie implementacje pola i obwodu.
 *
 */
public class Kwadrat extends Prostokat implements Obliczenia{

    private double pole, obwod;

    @Override
    public double getPole() {
        return pole;
    }

    @Override
    public void setPole(double pole) {
        this.pole = pole;
    }

    @Override
    public double getObwod() {
        return obwod;
    }

    @Override
    public void setObwod(double obwod) {
        this.obwod = obwod;
    }

    public Kwadrat(Punkt A, Punkt B, Punkt C, Punkt D) {
        super(A, B, C, D);


        pole = poleProstokat(getBokA(),getBokD());
        obwod = obwod(getBokA(),getBokB(),getBokC(),getBokD());
    }

    @Override
    public String toString() {
        return "Kwadrat{" +
                "pole=" + pole +
                ", obwod=" + obwod +
                '}';
    }
}
