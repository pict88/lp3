#include <iostream>

using namespace std;

int partition(int a[], int low, int high, bool random) {
    if(random){
    int r = low + rand() % (high - low + 1);
    swap(a[r], a[high]);
    }  

    int pivot = a[high];
    int i = low;

    for(int j=low; j<high; j++)
        if(a[j] <= pivot)
            swap(a[i++], a[j]);

    swap(a[i], a[high]);
    return i;
}

void quickSort(int a[], int low, int high, bool random) {
    if(low < high) {
        int p = partition(a, low, high, random);
        quickSort(a, low, p-1, random);
        quickSort(a, p+1, high, random);
    }
}

int main() {
    int a[] = {8,3,1,7,0,10,2};
    int b[] = {8,3,1,7,0,10,2};

    quickSort(a, 0, 6, false); // Deterministic
    quickSort(b, 0, 6, true);  // Randomized

    cout << "Deterministic: ";
    for(int x : a) cout << x << " ";

    cout << "\nRandomized: ";
    for(int x : b) cout << x << " ";
}
