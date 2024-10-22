import { IDaysProps } from "./DaysTypes"
import style from "./itemLi.module.css"

const Days:React.FC<IDaysProps> = ({ days }) => {
    
  return (
    <li className={style.item}>
        {days}
    </li>
  )
}

export default Days