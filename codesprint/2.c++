#include <bits/stdc++.h>
using namespace std;
int t = 0;
string find (int n, int c, int d, int x, int y, string q)
{
	//cout << x << " "<<y<<endl;
	t += 1;
	if (x == c && y == d)
		return q;
	if (x-2 >= 0 && x-2 < n)
	{
		if (y+1 < n)
		{//cout << x <<" "<< y <<endl;
			//q += "LR";
			find(n, c, d, x-2, y+1, q+"LR");
		}
		if (y-1 >= 0 && y-1 < n)
		{
			//q += "LL";
			find(n, c, d, x-2, y-1, q+"LL");
		}
	}
	if (t >= 2)
		return q;
	if (x+2 < n && x+2 >= 0)
	{

	
		if (y+1 < n)
		{cout << x << " "<<y << " "<<t<<endl;
			//q += "UR";
			find(n, c, d, x+2, y+1, q+"UR");
		}
		if (y-1 >= 0 && y-1 < n)
		{
			//q += "UL";
			find(n, c, d, x+2, y-1, q+"UL");
		}
	}
	if (y+2 < n)
	{
		//q += "R";
		find(n, c, d, x, y+2, q+"R");
	}
	if (y-2 >= 0 && y-2 < n)
	{
		//q += "L";
		find(n, c, d, x, y-2, q+"L");
	}
}
int main()
{
	int n;
	int a, b, c, d;
	scanf ("%d", &n);
	scanf ("%d%d%d%d", &a, &b, &c, &d);
	cout << find(n, c, d, a, b, "") << endl;
	return 0;
}
