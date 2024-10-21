import style from "./days.module.css"
import { IDaysProps } from "./DaysTypes"

const Days:React.FC<IDaysProps> = ({ days }) => {
    
  return (
    <li className={style.item}>
        {days}
    </li>
  )
}

export default Days