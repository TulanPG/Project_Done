package com;

import java.awt.*;


public interface WypelnienieKolorem {
    /**
     * Interfejs pozwalający na wybranie koloru do wypełnienia figury
     * @param R wartość R
     * @param G wartość G
     * @param B wartość B
     * @return Odpowiedni kolor
     */
    Color kolor(int R, int G, int B);

}
