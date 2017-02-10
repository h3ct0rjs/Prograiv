//#include <bits/stdc++.h> //didn't work in mac0S 
#include <iostream>
#include <ncurses.h>
#include <algorithm>
using namespace std;
#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);
#define VERSION "0.2"
#define AUTHOR "Hector F. Jimenez S"
#define EMAIL  "hfjimenez@utp.edu.co"

class Board{

};


int main(int argc, char *argv[]){
	FAST;												//Macro Expansio	
	while(argc>1){
		if(argv[1][0]== '-' && argv[1][1] =='-'){ 				//Lookup for - -
			if(strcmp(&argv[1][2], "theory")==0){cout<<"Theory"<<endl;}
			else if(strcmp(&argv[1][2], "help")==0){}
			else if(strcmp(&argv[1][2], "nqueens")==0){}	
			else if(strcmp(&argv[1][2], "version")==0){}
			else if(strcmp(&argv[1][2], "not-color")==0){}
			else {cout<<"Wow you introduce a Bad Argument, Try again"<<endl;}
		  }
		else if(argv[1][0]== '-'){
			if(strcmp(&argv[1][2], "t")==0){}
			else if(strcmp(&argv[1][2], "h")==0){}
			else if(strcmp(&argv[1][2], "v")==0){}
			else if(strcmp(&argv[1][2], "nc")==0){}
			else {cout<<"Bad Argument"<<endl;	}
		}
		++argv;
		--argc;
	}//endwhile
	cout<<"Out"
	return 0;
	}

