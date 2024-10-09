import React from 'react'
import { IPointerRoulette } from './PointerTypes'
import style from "./pointerRoulette.module.css"
import tringle from "../../assets/triangle.svg"



const PointerRoulette: React.FC<IPointerRoulette> = ({ children }) => {
  
  return (
    <>
       <div className={style.line}></div>
        <img src={tringle} alt="" className={style.triangleTop} />
            {children}
        <img src={tringle} alt="" className={style.triangleTop} style={{ transform: "rotate(0deg)" }} />
       <div className={style.line}></div>
    </>
  )
}

export default PointerRoulette