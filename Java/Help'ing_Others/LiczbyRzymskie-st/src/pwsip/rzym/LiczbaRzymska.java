package pwsip.rzym;

import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;

public class LiczbaRzymska {

	
	private int tablicaRzymska(char litera) {

        switch (litera) {
            case 'I':  return 1;
            case 'V':  return 5;
            case 'X':  return 10;
            case 'L':  return 50;
            case 'C':  return 100;
            case 'D':  return 500;
            case 'M':  return 1000;
            default:   return -1;
        }
    }
	
	
	public int num;
	protected String rzymska;
	protected int arabska;
	
	
	public LiczbaRzymska(String rzymska) {

		this.rzymska = rzymska;
		
    }


	public LiczbaRzymska(int arabska) {
		this.arabska = arabska;
		

	}
	public LiczbaRzymska() {
		String a = "Pusta liczba";
	}

	
	public int rzymska2arabska() {
		
		if (rzymska.length() == 0)
			System.out.print("Puste pole.");

        else {

            rzymska = rzymska.toUpperCase();

            int i = 0;
            int arabska = 0;
		
            while (i < rzymska.length()) {

                char letter = rzymska.charAt(i);
                //daje mi cyfre do zamiany na litere
                

                int number = tablicaRzymska(letter);


                
                if (number < 0)

                i++;

                if (i == rzymska.length()) {

                    arabska += number;
                }
                else {

                    int nextNumber = tablicaRzymska(rzymska.charAt(i));
                    if (nextNumber > number) {

                        arabska += (nextNumber - number);
                        i++;
                    }
                    else {

                        arabska += number;
                    }
                }

            }

            if (arabska > 3999)
            	System.out.print("Roman numeral must have value 3999 or less.");

            num = arabska;
            

        }
		System.out.print("rezultat: "+ num);
		return num;
		
	}
	public void arabska2Rzymska() {
		
		
		
	}
}
