#include<bits/stdc++.h>
using namespace std;

int main(){
	int n;
	cout<<"enter the total number of goal"<<endl;
	cin>>n;
	int a,suma=0,sumb=0;
	char b;
	cout<<endl<<"enter the distance between ball and basket, the team that score(a or b)";
	cout<<endl<<"e.g."<<endl<<"7 a"<<endl<<"3 b"<<endl<<"5 a";
	for(int i=1;i<=n;i++)
	{
		cin>>a>>b;
		if(b=='a')
		{
			if(a>=7)
			{
				suma+=3;
			}
			else
			{
				suma+=1;
			}
		}
		else
		{
			if(a>=7)
			{
				sumb+=3;
			}
			else
			{
				sumb+=1;
			}
		}
		
	}
	cout<<"a="<<suma<<endl<<"b="<<sumb<<endl;
	if(suma>sumb)
	{
		cout<<"team a win";
	}
	else if(suma<sumb)
	{
		cout<<"team b win";
	}
	else
	{
		cout<<"tie";
	}
	return 0;
}

/*
--- priority_queue<Type,Container, greater/less<type> > name;
1. name.push() ----add a thing
2. name.size() ----output the size of it
3. name.pop() -----delete the lowest thing
4. name.empty() ---detect weither it is or isn't empty
5. name.top() -----output the heighest thing in it

--- struct{type virable;}virable;

---queue<type>name;
1. back(name) ----return the last thing in queue
2. front(name)----return the first thing in queue
3. pop(name)------delete the first thing in queue
4. push(name)-----add a thing in queue
5. size(name)-----return the size of the queue

---set<type>name;
1. s.insert()----add a thing in set
2. s.erase()-----delete a thing in set
3. s.count()-----find the thing in set
4. s.size()------find the size
5.s.clear()------clear the set
*/

