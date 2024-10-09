import React from 'react'
import style from "./input.module.css"

interface IInput extends React.DetailedHTMLProps<React.InputHTMLAttributes<HTMLInputElement>, HTMLInputElement> {}

const Input:React.FC<IInput> = ({ ...props }) => {
  return (
    <input className={style.input} type="number" min="0" autoComplete="off" {...props}/>
  )
}

export default Input