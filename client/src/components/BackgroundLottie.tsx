// BackgroundLottie.tsx
import React from 'react';
import Lottie from 'react-lottie';
import animationData from '../../public/bg_lottie.json'; 

const BackgroundLottie: React.FC = () => {
  const defaultOptions = {
    loop: true,
    autoplay: true,
    animationData: animationData,
    rendererSettings: {
      preserveAspectRatio: 'xMidYMid slice'
    }
  };

  return (
    <div className="background-lottie">
      <Lottie options={defaultOptions} height="100%" width="100%" />
    </div>
  );
};

export default BackgroundLottie;
