#include <bits/stdc++.h> //didn't work in mac0S
#include <ncurses.h>
using namespace std;
#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);
#define VERSION "0.3"
#define AUTHOR "    Hector Jimenez S."
#define EMAIL  "    hfjimenez@utp.edu.co"
												//http://stackoverflow.com/questions/16223610/list-of-vectors
list<vector<int>> listofvector;					//we want to store a list of vectors, of the following form :
												//[[permutation1],[permutation2],[permutation2],[permutation3]]
list<vector<int>> Solutions;					//we want to store a list of vectors, of the following form :
void theory();
void printhelp();
void nqueens();
void version();
void printhelp(){
	
		cout<<"Usage: solvequeen [OPTION...] [NQUEENS] \n\n"<<endl
    <<"\ntheory : Show information about libraries and resource to solve this problem"<<endl
		<<"help : Print this contextual menu."	   <<endl
		<<"version: Show programm version"  <<endl
		<<"not-color: Disable color in the ncurses menu"  <<endl;}
void version(){
	cout<<"\n\t:::Nqueens Solver: Assignment 1::"<<endl
		<<"\t|\tVersion: "<<VERSION <<"\t\t|"<<endl
		<<"\t|    Computer Programming IV\t|"<<endl
		<<"\t| "<<AUTHOR<<"\t\t|"<<endl
		<<"\t|"<<EMAIL<<"\t|"<<endl
		<<"\t:::::::::::::::::::::::::::::::::"<<endl;};

void theory(){
	cout<<"Representamos las n reinas mediante un vector[1-n], teniendo en cuenta que cada índice del"<<endl
	<<"vector representa una fila y el valor una columna. Así cada reina estaría en la posición (i, v[i])"<<endl
	<<"para i = 1-8.Despues realizamos una permutacion usando el metodo next_permutation del vector anterior para"<<endl
	<<"obtener todas las posibles combinaciones de reinas en el tablero de ajedrez, estos se almacenan en una lista "<<endl
	<<"de vectores,Luego realizamos la comprobacion de si las reinas se matan entre si, por ejemplo para un  "<<endl
	<<"par de reinas Q1(i,j),Q2(k,l) estas estaran en la misma diagonal si y solo si pasa las siguientes condiciones :"<<endl
	<<endl
	<<" i-j==k-l || i+j == k+l || j-l == i-k||j-l==k-i"<<endl
	<<endl
	<<"Si el vector permutado con las posiciones de las reinas cumple la condicion anterior hemos hallado una solucion"<<endl
	<<"Por lo tanto procederemos a ir graficando las soluciones en nuestro board de ncurses. "<<endl;}

bool check(vector <int>vect){
	for(auto const&r1: vect){
		for(int j=r1+1;j<vect.size();j++){
			if( (r1-vect[r1] == j-vect[j]) || (r1+vect[r1] == j+vect[j]) || (vect[r1]-vect[j] == r1-j) || (vect[r1]-vect[j] == j-r1) ) {
				return 1;		//si hay un elemento en la diagonal, pum devuelve un 1. 
			}			
		}
	}
	return 0;					//Si termino, el vector recibido es winner.
}

void nqueens(int n){									//this will create the permutations needed
	int n2=n;
	vector<int> v(n2);
	iota(begin(v),end(v),0);							//fill the vector fast, linear time
	int sol=0;											//count the number of solutions founded
	do {
 		if(check(v)){} 
		else {
			cout<<"Combinacion Ganadora!"<<endl;
			sol++;
			for(auto const &x: v){
	    		cout <<x+1 <<" ";
	    	}
	    	cout <<endl;
		}
		cout<<endl;
		if(sol>=1) break;
 	 }while (next_permutation(v.begin(),v.end()) );		//3!:6,4!:24,5!:120,6!:720,7!:5040,8!:40320,10!:3628800
}


int main(int argc, char *argv[]){
	chrono::time_point<chrono::system_clock> start, end;
  	start = chrono::system_clock::now();
	int n=0;											//by default it takes n queen as 0.
	bool color=true;									//by default color is enable
//I was wanting to learn about argc, and argv, because there are many c/c++ programms in unix that support this feature.
//arguments
	while (argc > 1){
		if (argv[1][0] == '-' && argv[1][1] == '-'){

			if (strcmp(&argv[1][2], "theory") == 0){
				theory();return 0;
			}

			else if (strcmp(&argv[1][2], "help") == 0){
				printhelp();
			}

			else if (strcmp(&argv[1][2], "version") == 0){
				version();
			}

			else if (strcmp(&argv[1][2], "not-color") == 0){
				color=false;
				return 0;
			}

			else{
				cout<<"Wow you introduce a Bad Argument: "<<argv[1]<<"Try again"<<endl;
				exit(1);
			}
		}

		else if (argv[1][0] == '-'){
			int len = strlen(argv[1]);
			for(int i = 1; i < len; i++){
				if (argv[1][i] == 't'){
					theory();
				}

				else if (argv[1][i] == 'h'){
					printhelp();
				}

				else if (argv[1][i] == 'v'){
					version();
				}

				else if (argv[1][i] == 'c'){
					color=false;
				}

				else{
					cout<<"Bad Argument: "<<argv[1][i]<<endl;
					exit(1);
				}
			}
		}

		else n = atoi(argv[1]);	//number of nqueens to permute
		++argv;
		--argc;
	}

	/*if(n>12){
		cout<<"Sorry, unfortunately until now I'm unable to process more than 12 queens\n n>12 takes a lot of time to precompute the n permutations"<<endl;
		cout<<"I will handle this decision for you, with n=8 "<<endl;
		n=8;
	}*/
	nqueens(n);				//permutations
	end = chrono::system_clock::now();
	chrono::duration<double> elapsed_seconds = end - start;
	cout << "time: " << elapsed_seconds.count() << "s\n";
	return 0;

	}
