import style from "./month.module.css"
import Days from "../Days/Days"
import { IMonthProps } from "./MonthTypes"

const arrWeek = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

const Month:React.FC<IMonthProps> = ({ titleMonth, daysMonth }) => {
  let date = new Date()
  return (
    <div className={style.wrapperMonth}>
        <div className={style.month}>
            <div className={style.title}>{titleMonth} <span className={style.span}>{date.getFullYear()}г</span></div>
            <ul className={style.calendarNumber}>
              {
                arrWeek.map((item) => (
                  <li>{item}</li>
                ))
                
              }
              {
                daysMonth.map((items) => (
                  <Days days={items}/>
                ))
              }
            </ul>
        </div>
    </div>
  )
}

export default Month