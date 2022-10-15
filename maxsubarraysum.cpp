#include<iostream>
using namespace std;
int main()
{
  int n;
  cin>>n;
  int arr[n];
  for(int i=0;i<n;i++)
  {
      cin>>arr[i];
  }
  int maxSum=INT_MIN;
//   Brute force method
//time complexity of this program is O(n3) because we are using three nested loops i.e. nxnxn  
//   for(int i=0;i<n;i++)
// {
//     for(int j=i;j<n;j++)
//     {
//         int sum=0;
//         for(int k=i;k<=j;k++)
//         {
//             sum+=arr[k];
//             // cout<<sum;
//         }
//         // cout<<endl;
//         maxSum=max(maxSum, sum);
//     }
// }
//Kadane's Algorithm most optimized sol for this problem with complexity O(n)
int curSum=0;
for(int i=0;i<n;i++)
{
    curSum+=arr[i];
    if(curSum<0)
    {
        curSum=0;//for negative values
    }
    maxSum=max(maxSum, curSum);
}
cout<<maxSum<<endl;
    return 0;
}
