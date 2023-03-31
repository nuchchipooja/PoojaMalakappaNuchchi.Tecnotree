function findFirstNonRepeatingChar(str) {
    const n = str.length;
    const charCount = {};
    
    // Count the frequency of each character in the string
    for (let i = 0; i < n; i++) {
      const char = str[i];
      if (charCount[char] === undefined) {
        charCount[char] = 1;
      } else {
        charCount[char]++;
      }
    }
    
    // Find the first character with frequency of 1
    for (let i = 0; i < n; i++) {
      const char = str[i];
      if (charCount[char] === 1) {
        return char;
      }
    }
    
    // If no non-repeating character is found, return null
    return null;
  }
  const str = "hi hello";
  const result = findFirstNonRepeatingChar(str);
  console.log(result); // Output: "h"
    