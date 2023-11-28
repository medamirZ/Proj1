public class Liste {
    private static final int LMAX = 3;
    private int [] tab;
    private int longueur_liste;

    // Constructor and other methods for Liste class

    public Liste() {
        this.tab = new int[LMAX];
        this.longueur_liste = 0;
    }

    // Insertion function
    public Liste inserer(int p, int e) {
        int j;

        if (longueur_liste < LMAX) {
            if (p >= 1 && p <= longueur_liste + 1) {
                for (j = longueur_liste - 1; j >= p - 1; j--) {
                    tab[j + 1] = tab[j];
                }
                tab[p - 1] = e;
                longueur_liste++;
            } else {
                System.out.println("L'insertion est impossible, la position p est invalide.");
            }
        } else {
            System.out.println("L'insertion est impossible, la liste est saturée.");
        }

        return this;
    }
public static void main(String[] args) {
    Liste l = new Liste();
    l.inserer(1, 5);
    l.inserer(2, 5);
    l.inserer(3, 5);
    
}
    // Other methods and class definition
}
