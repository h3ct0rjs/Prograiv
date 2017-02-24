#include  <iostream>
#include  <cmath>
#include  <algorithm>

using namespace std;
double round(double number);
static string axis = "+ ";
static string punto = "k ";
static string bg =". ";

int defaultmaxh=23;
int defaultmaxw=80; 

int main(int argc, char *argv[]) {

  int size = round(defaultmaxh/2.0)
;  double paso = (1.0);
  int *data = new int[size];      //data[8]
  for(int i = 0;i< size+size+1;++i) {
    double x = (i - (size));    //x
    x = x*paso;
    double valor = x+2;
    valor = valor/paso;
    data[i] = int(round(valor));

  }
 /* cout << "TABLA:" << endl;
  for(int i = 0; i < size+size+1;++i) {
     cout << (i - (size)) << " : " << data[i] << endl;
   }
  cout << endl;*/

  for(int i = 0;i < size;++i) {
    for(int b = 0; b < size;++b) {
      if(size - i == data[b])
        cout << punto;
      else
        cout << bg;
    }
    if(size -i == data[size])
      cout << punto;
    else
      cout << axis;

    for(int b = 0; b < size;++b) {
      if(size - i == data[b+size+1])
        cout << punto;
      else
        cout << bg;
    }
    cout << endl;
  }
  for(int i = 0;i < size*2+1;++i) {
    if( 0 == data[i] )
      cout << punto;
    else
      cout << axis;
  }
  cout << endl;

  for(int i = 0;i < size;++i) {
    for(int b = 0; b < size;++b) {
      if(0-i-1 == data[b])
        cout << punto;
      else
        cout << bg;
    }
    if(0 -i-1 == data[size])
      cout << punto;
    else
      cout << axis;

    for(int b = 0; b < size;++b) {
      if(0-i-1 == data[b+size+1])
        cout << punto;
      else
        cout << bg;
    }
    cout << endl;
  }
  delete[] data;
}

double round(double number){
  return number < 0.0 ? ceil(number - 0.5) : floor(number + 0.5);
}

