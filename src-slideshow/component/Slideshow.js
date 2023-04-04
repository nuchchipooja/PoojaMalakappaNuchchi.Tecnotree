import React, { useState, useEffect } from "react";

const Slideshow = ({ images, interval = 3000 }) => {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCurrentImageIndex((index) => (index + 1) % images.length);
    }, interval);

    return () => clearInterval(intervalId);
  }, [images, interval]);

  return (
    <div>
      <img src={images[currentImageIndex]} alt={`Image ${currentImageIndex}`} />
    </div>
  );
};

export default Slideshow;
