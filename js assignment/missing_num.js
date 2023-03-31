function findMissingNumber(arr) {
    const n = arr.length;
    
    // Calculate the sum of integers 
    const expectedSum = (n+1) * (n+2) / 2;
    
    // Calculate the actual sum 
    const actualSum = arr.reduce((sum, num) => sum + num);
    
    const missingNumber = expectedSum - actualSum;
    
    return missingNumber;
  }
  const arr = [1, 3, 4, 5, 6];
const result = findMissingNumber(arr);
console.log(result); 

  