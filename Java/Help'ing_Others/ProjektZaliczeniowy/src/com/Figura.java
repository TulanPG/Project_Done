package com;

/**
 * Metoda abstrakcyjna jako podstawowa dla klas: Koło, Linia, Prostokąt, Trójkąt
 * Klasa Kwadrat rozszerza Prostokąt
 * W zależności od ilości podanych punktów, klasa jest rozszerzana w odpowiedniej klasie np.
 * 3 punkty daje trójkąt i tam jest imprementowana
 */
public abstract class Figura {


    public Figura(Punkt A) {
    }

    public Figura(Punkt A, Punkt B) {
    }

    public Figura(Punkt A, Punkt B, Punkt C) {
    }

    public Figura(Punkt A, Punkt B, Punkt C, Punkt D) {
    }
}


