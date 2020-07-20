package com;

import java.awt.*;

public class Figury{

    private double a, b, c, d, pole, obwod;
    Color color;

    public Figury(){

    }

    /**
     * Zestawienie danych figury
     * @param a Bok a figury
     * @param b Bok b figury
     * @param c Bok c figury
     * @param d Bok d figury
     * @param pole Pole figury
     * @param obwod Obwód figury
     */
    public Figury(double a, double b, double c, double d, double pole, double obwod){

        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
        this.pole = pole;
        this.obwod = obwod;
    }


    //Dodany kolor rozszerza klasę pozwala łątwiej jej dodawać kolejny argument
    public Figury(double a, double b, double c, double d, double pole, double obwod, Color color){

        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
        this.pole = pole;
        this.obwod = obwod;
        this.color = color;
    }



    @Override
    public String toString() {


        if(b == 0){
            return "\n"+"Koło{" +
                    "a=" + a +
                    ", pole=" + pole +
                    ", obwod=" + obwod +
                    ", kolor=" + color +
                    '}';
        }
        if(d==0){
            return "\n"+"Trójkąt{" +
                    "a=" + a +
                    ", b=" + b +
                    ", c=" + c +
                    ", pole=" + pole +
                    ", obwod=" + obwod +
                    ", kolor=" + color +
                    '}';
        }

        if (a == b && b == c && c == d){
            return "\n"+"Kawadrat{" +
                    "a=" + a +
                    ", b=" + b +
                    ", c=" + c +
                    ", d=" + d +
                    ", pole=" + pole +
                    ", obwod=" + obwod +
                    ", kolor=" + color +
                    '}';
        }

        else {

            return "\n"+"Prostokąt{" +
                    "a=" + a +
                    ", b=" + b +
                    ", c=" + c +
                    ", d=" + d +
                    ", pole=" + pole +
                    ", obwod=" + obwod +
                    ", kolor=" + color +
                    '}';
        }
    }

    public double getA() {
        return a;
    }

    public void setA(double a) {
        this.a = a;
    }

    public double getB() {
        return b;
    }

    public void setB(double b) {
        this.b = b;
    }

    public double getC() {
        return c;
    }

    public void setC(double c) {
        this.c = c;
    }

    public double getD() {
        return d;
    }

    public void setD(double d) {
        this.d = d;
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

    public Color getColor() {
        return color;
    }

    public void setColor(Color color) {
        this.color = color;
    }


}



