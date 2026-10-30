#include <iostream>
#include <cstdlib>
using namespace std;

int a[] = {8,3,1,7,0,10,2};
int b[] = {8,3,1,7,0,10,2};

void quickSort(int arr[], int low, int high, bool random) {

    if(low >= high) return;

    if(random) swap(arr[low + rand() % (high - low + 1)], arr[high]);
    //if (random) swap(arr[rand() % 7], arr[high]);

    int pivot = arr[high];
    int i = low - 1;

    for(int j = low; j < high; j++)
        if(arr[j] <= pivot)
            swap(arr[++i], arr[j]);

    swap(arr[i + 1], arr[high]);

    int pivotPos = i + 1;

    quickSort(arr, low, pivotPos - 1, random);
    quickSort(arr, pivotPos + 1, high, random);
}

int main() {

    quickSort(a, 0, 6, false); // Deterministic
    quickSort(b, 0, 6, true);  // Randomized

    cout << "Deterministic: ";
    for(int x : a) cout << x << " ";

    cout << "\nRandomized: ";
    for(int x : b) cout << x << " ";
}
