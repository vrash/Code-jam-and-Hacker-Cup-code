int a[N] // This is the input
int products[N];

// Get the products below the current index
p=1;
for(int i=0;i<N;++i) {
  products[i]=p;
  p*=a[i];
}

// Get the products above the curent index
p=1;
for(int i=N-1;i>=0;--i) {
  products[i]*=p;
  p*=a[i];
}