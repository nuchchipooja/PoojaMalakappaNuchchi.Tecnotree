function reverseWords(str) {
    // Split the string into an array of words
    const words = str.split(" ");
    
    // Reverse the order of the words in the array
    const reversedWords = words.reverse();
    
    // Join the reversed words into a new string
    const reversedString = reversedWords.join(" ");
    
    // Return the reversed string
    return reversedString;
  }
  const str = "byee! have a great day:)";
  const result = reverseWords(str);
  console.log(result); // Output: "world! Hello"
    