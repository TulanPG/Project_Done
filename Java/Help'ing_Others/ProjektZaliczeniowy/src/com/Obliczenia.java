package com;

public interface Obliczenia {

    /**
     * linia - Kod pozwalający obliczyć długość odcinka
     * @param A Dostarczony punkt 1
     * @param B Dostarczony punkt 2
     * @return Dlugość linni
     */
    double linia(Punkt A, Punkt B);

    /**
     * poleTrojkat - Kod pozwalający obliczyć pole trójkąta
     * @param A Dostarczony punkt 1
     * @param B Dostarczony punkt 2
     * @param C Dostarczony punkt 3
     * @return Pole
     */
    double poleTrojkat(Punkt A, Punkt B, Punkt C);

    /**
     * poteKolo - Kod pozwalający obliczyć pole koła
     * @param a Długość promienia powstałego z |AB|
     * @return Pole
     */
    double poleKolo(double a);

    /**
     * poleProstokat- Kodpozwalający obliczyć pole z prostokąta/kwadratu
     * @param max Maksymalna długość odcinka
     * @param min
     * @return
     */
    double poleProstokat(double max, double min);

    /**
     * obwod - Kod pozwalający obliczyć obwód figur
     * @param a długość odcinka a
     * @param b długość odcinka b
     * @param c długość odcinka c
     * @param d długość odcinka d
     * @return obwód
     */
    double obwod(double a,double b,double c,double d);

    /**
     * obwod - Kod pozwalający obliczyć obwód figur
     * @param a długość odcinka a/ Promień
     * @return obwódKoła
     */
    double obwodKolo(double a);

}
