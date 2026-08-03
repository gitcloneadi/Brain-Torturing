class Solution {
  public:
    int largestPrimeFactor(int n) {
        int largest = 1;
        
        // Divide by 2 to handle even numbers
        while (n % 2 == 0) {
            largest = 2;
            n /= 2;
        }
        
        // Check odd factors from 3 to sqrt(n)
        for (int i = 3; i * i <= n; i += 2) {
            while (n % i == 0) {
                largest = i;
                n /= i;
            }
        }
        
        // If n is still greater than 2, it's a prime factor
        if (n > 2) {
            largest = n;
        }
        
        return largest;
    }
};
