#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

bool est_blanc (char c){
	//return ((c == ' ') || (c == '\t') || (c == '\n'));
	return (c <= ' '); //Code ASCII
}

bool est_debut_sequence(char c){
	return ((c == '>') || (c == ';'));
}

bool est_nucleotide (char c){
	return ((c == 'A') || (c == 'C') || (c == 'G') || (c == 'T') || (c == 'a') || (c == 'c') || (c == 'g') || (c == 't'));
}

void lire_entete(ifstream &flux){
	string l;
	getline(flux, l);
	clog << "Nouvelle séquence détectée : '" << l << "'" << endl;
}

void traiter_nucleotide(char c ){

}

void erreur(char *nom_fich, unsigned int ligne, unsigned int colonne, const char* message){
	cerr << nom_fich << ":" << ligne << ":" << colonne << ":" << message << endl;
	exit(1);
}

void usage() {
	cerr << "Usage: lire_fichier <Fichier>" << endl;
	exit(1);
}

void lire_fichier_fasta(char* nom_fich){
		ifstream monFlux(nom_fich);  //Ouverture d'un fichier en lecture

	if(monFlux)
	{
    unsigned int ligne = 0,colonne = 0;
    char c, precedent = '\n';
    bool dans_sequence = false;
    size_t nb_nucleotides = 0;
    while(monFlux){
    	monFlux.get(c);
    	if (!est_blanc(c)){
    		if (est_debut_sequence(c)){
    			if (precedent == '\n'){
    				lire_entete(monFlux);
    				nb_nucleotides = 0;
    				dans_sequence = true;
    				}
    				else {
    					erreur(nom_fich, ligne, colonne, "Caractère invalide");
    				}
    		} else {
    				if (est_nucleotide(c)){
    					traiter_nucleotide(c);
    					++nb_nucleotides;
    					}
    					else {
    						erreur(nom_fich, ligne, colonne, "caractère invalide");
    					}
    				}
    			}
    		}
    		precedent = c;
    		    if (dans_sequence){
    	clog << "La séquence comporte " << nb_nucleotides << endl;
    }
	else
	{
    	erreur(nom_fich, 0, 0, "Impossible de lire le fichier");
	}
    	}
    	

    

}


int main(int argc, char** argv) {
	if (argc != 2){
		usage();
	}
	lire_fichier_fasta(argv[1]);

   }

