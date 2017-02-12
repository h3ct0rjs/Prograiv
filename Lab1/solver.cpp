#include <bits/stdc++.h> //didn't work in mac0S 
//#include <iostream>
//#include <ncurses.h>
//#include <algorithm>
using namespace std;

#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);
#define VERSION "0.2"
#define AUTHOR "    Hector Jimenez S."
#define EMAIL  "    hfjimenez@utp.edu.co"


list<vector<int>> listofvector;					//we want to store a list of vectors, of the following form :
												//[[permutation1],[permutation2],[permutation2],[permutation3]]

void theory();
void printhelp();
void nqueens();
void version();
void ncursesflags();


void printhelp(){
		cout<<"Usage: solvequeen [OPTION...] [NQUEENS] \n\n"<<endl
	    <<"\ntheory : Show information about libraries and resource to solve this problem"<<endl
		<<"help : Print this contextual menu."	   <<endl
		<<"version: Show programm version"  <<endl
		<<"not-color: Disable color in the ncurses menu"  <<endl;
}

void version(){
	cout<<"\n\t:::Nqueens Solver: Assignment 1::"<<endl
		<<"\t|\tVersion: "<<VERSION <<"\t\t|"<<endl
		<<"\t|    Computer Programming IV\t|"<<endl
		<<"\t| "<<AUTHOR<<"\t\t|"<<endl
		<<"\t|"<<EMAIL<<"\t|"<<endl
		<<"\t:::::::::::::::::::::::::::::::::"<<endl;
};

void theory(){
	printf("Hallo World, put my theory here!");
}
void nqueens(int n){								//this will create the permutations needed
													//3!:6,4!:24,5!:120,6!:720,7!:5040,8!:40320,10!:3628800
	int n2=n;
	cout<<"We are creating a vector for you "<<endl;
	vector<int> v(n2);
	cout<<"Initializing the vector from 0 to "<<n2<<endl;
	iota(begin(v),end(v),0);						//fill the vector fast, linear time
													//http://en.cppreference.com/w/cpp/algorithm/iota
	cout<<"The size of vector after the init is: "<<v.size()<<"Is it correct ?O_o?"<<endl;
	cout<<"For Debug Porpouse your vector is : "<<endl;
	for(auto x:v)
		cout<<" "<<x;
	cout<<endl;

	cout<<"Initializing a  list of vector( form: [[permutation1],[permutation2],...,[permutationn]] )"<<endl;

	cout << "The "<<n2<<"! possible permutations with"<<n2<<" elements is:\n";		//Debuging
	do {
 		listofvector.push_back(v);
 	 }while (next_permutation(v.begin(),v.end()) );		//using iterators
	
	cout<<"Your Permutations are: "<<endl;

	for (auto &v : listofvector){
	    for (auto const &x : v)
	        cout << x << " ";
	    cout << endl;
	}
}


void ncursesflags(){
}

int main(int argc, char *argv[]){
	 chrono::time_point<chrono::system_clock> start, end;
  	start = chrono::system_clock::now();
	int n2,n=0;
	//FAST;													//Make fast input/output
	while (argc > 1)
		{
		if (argv[1][0] == '-' && argv[1][1] == '-')
			{if (strcmp(&argv[1][2], "theory") == 0){theory();return 0;}
			else if (strcmp(&argv[1][2], "help") == 0){printhelp();}
			else if (strcmp(&argv[1][2], "version") == 0){version();}
			else if (strcmp(&argv[1][2], "not-color") == 0){ncursesflags();return 0;}
			else{cout<<"Wow you introduce a Bad Argument: "<<argv[1]<<"Try again"<<endl;return 1;}
			}
		else if (argv[1][0] == '-'){
			int len = strlen(argv[1]);
			for(int i = 1; i < len; i++){
				if (argv[1][i] == 't'){	theory();}
				else if (argv[1][i] == 'h'){printhelp();}
				else if (argv[1][i] == 'v'){version();}
				else if (argv[1][i] == 'c'){ncursesflags();}
				else{cout<<"Bad Argument: "<<argv[1][i]<<endl;return 1;}
				}
			}
		else n = atoi(argv[1]);							//number of nqueens to permute
		++argv;
		--argc;
		}

	if(n>12){
		cout<<"Sorry, unfortunately until now I'm unable to process more than 12 number of queens\n n>12 takes a lot of time to precompute the n permutations"<<endl;
		cout<<"I will handle this decision for you, with n=8 "<<endl;
		n=8;
	}

	nqueens(n);				//permutations
	end = chrono::system_clock::now();
  	chrono::duration<double> elapsed_seconds = end - start;
  	cout << "time: " << elapsed_seconds.count() << "s\n";

	return 0;
	}