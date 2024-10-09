import React from "react"
import { IButtonUI } from "./ButtonTypes"
import style from "./style.module.css"

const Button: React.FC<IButtonUI> = ({ children, ...props }) => {
  return (
    <button  className={style.btn} {...props}>
        {children}
    </button>
  )
}

export default Button