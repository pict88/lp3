#include <iostream>

using namespace std;

long long Recursive(int n){
    if (n<=1) return n;
    return Recursive(n-1)+Recursive(n-2); 
}

long long Iterative(int n){
    long long a=0, b=1;
    while (n-- >0){
        b+=a;
        a = b -a;
    }

    return a; 
}

int main(){
    long long n;
    cout<<"Enter number:";
    cin>>n;
    for (int i = 0; i <= n; i++) {
        cout << Recursive(i) << " ";
    }
    cout<<"\nIterative:"<<Iterative(n);
    for (int i = 0; i <= n; i++) {
        cout << Iterative(i) << " ";
    }
}
