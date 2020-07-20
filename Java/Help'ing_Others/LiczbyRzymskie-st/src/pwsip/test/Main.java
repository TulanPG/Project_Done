package pwsip.test;

import pwsip.rzym.LiczbaRzymska;

public class Main {
    public static void main(String[] args) {

        //1.
        LiczbaRzymska r1 = new LiczbaRzymska("XII");
      //  LiczbaRzymska r2 = new LiczbaRzymska();

       //2.
       //System.out.println(r1);
      // System.out.print(r2);

     //3.
       System.out.println("r1 = " + r1.rzymska2arabska());

       /*     LiczbaRzymska r3 = new LiczbaRzymska("MCDXXI");
        System.out.print(r3);
        System.out.println(" = " + r3.rzymska2arabska());

       LiczbaRzymska r4 = new LiczbaRzymska("MMCMLXV");
        System.out.print(r4);
        System.out.println(" = " + r4.rzymska2arabska());

        LiczbaRzymska r5 = new LiczbaRzymska("MMCMLXVV");
       System.out.print(r5);
        System.out.println(" = " + r5.rzymska2arabska());

        //4.
        LiczbaRzymska r6;
        r6 = LiczbaRzymska.arabska2Rzymska(2020);
       System.out.print(r6);
       System.out.println(" = " + r6.rzymska2arabska());

        LiczbaRzymska r7;
        r7 = LiczbaRzymska.arabska2Rzymska(4000);
       if(r7 == null) System.out.println("Liczba spoza zakresu");

        //5.
       LiczbaRzymska r8;
        r8 = LiczbaRzymska.arabska2Rzymska(1494);
        System.out.print(r8 + " = ");
        r8.setFormat(false);
        r8.wyswietl();

       //6.
       if(r8.nastLiczbaRzymska()) {
            System.out.println("MCDXCIV + I = " + r8 + " = " + r8.rzymska2arabska());
        }

       int liczba = 3999;
       LiczbaRzymska r9 = LiczbaRzymska.arabska2Rzymska(liczba);
        if(r9.nastLiczbaRzymska()) {
            System.out.println(LiczbaRzymska.arabska2Rzymska(liczba) +
                   " + I = " + r9 + " = " + r9.rzymska2arabska());
       }
        else{
            System.out.println(liczba + " + 1 = poza zakresem");
       }

        //7.
        System.out.println("---NUMEROWANIE---");
       LiczbaRzymska start = LiczbaRzymska.arabska2Rzymska(987);
        LiczbaRzymska stop = LiczbaRzymska.arabska2Rzymska(1092);
        kolejneNumery(start, stop);
*/
       }

    //metoda do zrobienia
 
}
