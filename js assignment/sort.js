const arr = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 },
    { name: "Charlie", age: 20 }
  ];
  
  const sortedArr = arr.sort((a, b) => a.age > b.age ? 1 : -1);
  console.log(sortedArr);