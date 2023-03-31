function mergeSort(arr) {
    // if the array has less than 2 elements,it is already sorted
    if (arr.length < 2) {
      return arr;
    }
    
    // Split the array into two 
    const mid = Math.floor(arr.length / 2);
    const leftArr = arr.slice(0, mid);
    const rightArr = arr.slice(mid);
    
    // Recursively sort the left and right 
    const sortedLeft = mergeSort(leftArr);
    const sortedRight = mergeSort(rightArr);
    
    // Merge the sorted left and right halves
    const mergedArr = [];
    let leftIndex = 0;
    let rightIndex = 0;
    while (leftIndex < sortedLeft.length && rightIndex < sortedRight.length) {
      if (sortedLeft[leftIndex] < sortedRight[rightIndex]) {
        mergedArr.push(sortedLeft[leftIndex]);
        leftIndex++;
      } else {
        mergedArr.push(sortedRight[rightIndex]);
        rightIndex++;
      }
    }
    
    // Add any remaining elements from the left or right array
    return mergedArr.concat(sortedLeft.slice(leftIndex)).concat(sortedRight.slice(rightIndex));
  }
  const arr = [3, 5, 1, 4, 2];
  const result = mergeSort(arr);
  console.log(result); 
    