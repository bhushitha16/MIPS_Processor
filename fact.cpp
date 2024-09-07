#include<bits/stdc++.h>
using namespace std;
int fact(int n){ //factorial function
	if(n==0)  //base condition
		return 1;
	else{
		int result=1;
		for(int i=1;i<=n;i++){
			result=result*i;
		}
		return result;
	}
}
int main(){
	int n;
	cin>>n;
	cout<<fact(n)<<endl;

	return 0;
}
