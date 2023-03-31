function bubbleSort(arr) {
    const n = arr.length;
    
    // Iterate through the array n-1 times
    for (let i = 0; i < n-1; i++) {
      
      // Inner loop to compare adjacent elements and swap them if necessary
      for (let j = 0; j < n-i-1; j++) {
        if (arr[j] > arr[j+1]) {
          // Swap arr[j] and arr[j+1]
          const temp = arr[j];
          arr[j] = arr[j+1];
          arr[j+1] = temp;
        }
      }
    }
    
    return arr;
  }
  const arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
  const result = bubbleSort(arr);
  console.log(result); // Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    