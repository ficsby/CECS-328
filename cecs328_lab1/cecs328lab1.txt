// cecs328lab1.cpp : Defines the entry point for the console application.
//

#include <iostream>
using namespace std;
#include <algorithm>
#include <vector>
#include <time.h>
#include <chrono>
#include<cstdint>

bool linear_search(vector<int>, int, int);
bool binary_search(vector<int>, int, int);
chrono::high_resolution_clock m_clock;

int main()
{
	srand(time(NULL)); //Prevents same random number generation each run
	int n = 1; // size
	cout << "Put in a positive integer" << endl;
	cin >> n;
	vector<int> arr;
	for (int i = 0; i < n; i++) {
		int randNum = rand() % 2001 - 1000;		//random number between -1000 and 1000
		arr.push_back(randNum);
	}

	sort(arr.begin(), arr.begin() + n);	//sort vector
	int key;	//random key

				//long double ;
	long double linSrchTmAvg = 0;
	long double binSrchTmAvg = 0;
	long double t;
	bool inArr;

	/*Part A
	***********************************************************************************************/
	cout << "Part A" << endl;
	int k = 500;
	for (int i = 0; i < k; i++) {
		key = rand() % n;
		//Linear Search
		clock_t clockTicks = clock();
		t = (chrono::duration_cast<chrono::nanoseconds>(m_clock.now().time_since_epoch()).count());
		inArr = linear_search(arr, key, n);
		//clockTicks = clock() - clockTicks;
		linSrchTmAvg += (chrono::duration_cast<chrono::nanoseconds>(m_clock.now().time_since_epoch()).count()) - t;

		//Binary Search
		t = (chrono::duration_cast<chrono::nanoseconds>(m_clock.now().time_since_epoch()).count());
		binary_search(arr, key, n);
		binSrchTmAvg += (chrono::duration_cast<chrono::nanoseconds>(m_clock.now().time_since_epoch()).count());

	}

	if (inArr) { cout << "Key found in array" << endl; }
	else { cout << "Key is not in array" << endl; }
	cout << "Linear Search Time Average: " << linSrchTmAvg << " nanoseconds" << endl;
	cout << "Binary Search Time Average: " << binSrchTmAvg << " nanoseconds\n" << endl;

	/*Part B
	***********************************************************************************************/
	system("pause");
	cout << "Part B" << endl;
	n = 100000;
	key = 5000;
	long double binTime = 0;
	long double linTime = 0;
	vector<int> arr2;

	for (int i = 0; i < n; i++) {
		int randNum = rand() % 2001 - 1000;		//random number between -1000 and 1000
		arr2.push_back(randNum);
	}
	sort(arr2.begin(), arr2.begin() + n);	//sort vector

											//Linear Search
	t = (chrono::duration_cast<chrono::nanoseconds>(m_clock.now().time_since_epoch()).count());
	linear_search(arr2, key, n);
	linTime = (chrono::duration_cast<chrono::nanoseconds>(m_clock.now().time_since_epoch()).count()); -t;

	//Binary Search
	t = (chrono::duration_cast<chrono::nanoseconds>(m_clock.now().time_since_epoch()).count());
	binary_search(arr2, key, n);
	binTime = (chrono::duration_cast<chrono::nanoseconds>(m_clock.now().time_since_epoch()).count()) - t;

	cout << "One time run:" << endl;
	cout << "Linear Search Time: " << linTime << " nanoseconds" << endl;
	cout << "Binary Search Time: " << binTime << " nanoseconds" << endl;
	cout << "\nOne step:" << endl;
	cout << "Linear Search Time: " << linTime / n << " nanoseconds" << endl;
	cout << "Binary Search Time: " << binTime / log(n) << " nanoseconds\n" << endl;

	/*Estimate when n = 10^7
	***********************************************************************************************/
	cout << "Time Estimates when n = 10^7: " << endl;
	long double linSrchEst = 0;
	long double binSrchEst = 0;
	n = 1000000;

	linSrchEst = n * linSrchTmAvg;
	binSrchEst = log(n) * binSrchTmAvg;
	cout << "Linear Search Time Estimate when n = 10^7: " << linSrchTmAvg << endl;
	cout << "Binary Search Time Estimate when n = 10^7: " << binSrchTmAvg << endl;

	/*When n = 10^7
	***********************************************************************************************/
	system("pause");
	cout << "When n=10^7" << endl;

	key = 5000;

	vector<int> arr3;

	for (int i = 0; i < n; i++) {
		int randNum = rand() % 2001 - 1000;		//random number between -1000 and 1000
		arr3.push_back(randNum);
	}
	sort(arr3.begin(), arr3.begin() + n);	//sort vector

											//Linear Search
	t = (chrono::duration_cast<chrono::nanoseconds>(m_clock.now().time_since_epoch()).count());
	linear_search(arr3, key, n);
	linTime = (chrono::duration_cast<chrono::nanoseconds>(m_clock.now().time_since_epoch()).count()) - t;

	//Binary Search
	t = (chrono::duration_cast<chrono::nanoseconds>(m_clock.now().time_since_epoch()).count());
	binary_search(arr3, key, n);
	binTime = (chrono::duration_cast<chrono::nanoseconds>(m_clock.now().time_since_epoch()).count() - t);

	cout << "When n = 10 ^ 7:" << endl;
	cout << "Linear Search Time: " << linTime << " nanoseconds" << endl;
	cout << "Binary Search Time " << binTime << " nanoseconds" << endl;
	//cout << "Time for one step: " << "Linear Search: " << linSrchTmAvg / n << "\tBinary Search: " << binSrchTmAvg / n << endl;

	system("pause");
	return 0;

}
/*Linear Search
***********************************************************************************************/
bool linear_search(vector<int> arr, int key, int size) {
	for (int i = 0; i < size; i++) {
		if (key == arr[i]) {
			return true;
		}
	}

	return false;
}

/*Binary Search
***********************************************************************************************/
bool binary_search(vector<int> arr, int key, int size) {
	int beg = 0;
	int end = size;
	//sort(arr, arr+size);
	while (beg < end) {
		int mid = (beg + end) / 2;
		if (key == arr[mid])
			return true;
		else if (key > arr[mid])
			beg = mid + 1;
		else
			end = mid - 1;
	}
	return false;
}
