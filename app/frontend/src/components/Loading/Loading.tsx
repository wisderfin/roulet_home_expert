import { useEffect, useState } from "react";
import style from "./loading.module.css"

export const Loading = () => {
    const [isVisible, setIsVisible] = useState(true);
    const [isRemoving, setIsRemoving] = useState(false);

    const randomTime = Math.floor(Math.random() * (5000 - 2000 + 1)) + 2000;

    useEffect(() => {
        const timer = setTimeout(() => {
          setIsRemoving(true);

          const removeTimer = setTimeout(() => {
            setIsVisible(false);
          }, 1000);
    
          return () => clearTimeout(removeTimer);
        }, randomTime); 
    
        return () => clearTimeout(timer);
      }, []);
    
      if (!isVisible) return null;

    return (
        <div className={style.loadPage} style={isRemoving ? {opacity: 0} : undefined}>
            <h1>Loading</h1>
            <svg className={style.spinner} width="65px" height="65px" viewBox="0 0 66 66" xmlns="http://www.w3.org/2000/svg">
                <circle className={style.path} fill="none" strokeWidth="4" strokeLinecap="round" cx="33" cy="33" r="30"></circle>
            </svg>
        </div>
    )
}