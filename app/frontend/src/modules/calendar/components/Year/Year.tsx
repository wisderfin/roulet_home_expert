import Header from '../Header/Header'
import Month from '../Month/Month'
import style from './year.module.css'

const months = [
  { titleMonth: "Январь", daysMonth: Array.from({ length: 31 }, (_, i) => i + 1) },
  { titleMonth: "Февраль", daysMonth: Array.from({ length: 28 }, (_, i) => i + 1) }, 
  { titleMonth: "Март", daysMonth: Array.from({ length: 31 }, (_, i) => i + 1) },
  { titleMonth: "Апрель", daysMonth: Array.from({ length: 30 }, (_, i) => i + 1) },
  { titleMonth: "Май", daysMonth: Array.from({ length: 31 }, (_, i) => i + 1) },
  { titleMonth: "Июнь", daysMonth: Array.from({ length: 30 }, (_, i) => i + 1) },
  { titleMonth: "Июль", daysMonth: Array.from({ length: 31 }, (_, i) => i + 1) },
  { titleMonth: "Август", daysMonth: Array.from({ length: 31 }, (_, i) => i + 1) },
  { titleMonth: "Сентябрь", daysMonth: Array.from({ length: 30 }, (_, i) => i + 1) },
  { titleMonth: "Октябрь", daysMonth: Array.from({ length: 31 }, (_, i) => i + 1) },
  { titleMonth: "Ноябрь", daysMonth: Array.from({ length: 30 }, (_, i) => i + 1) },
  { titleMonth: "Декабрь", daysMonth: Array.from({ length: 31 }, (_, i) => i + 1) }
];

export const Year = () => {
  return (
    <div className={style.wrapperYear}>
      <div className={style.year}>
        <Header/>
        {
          months.map((item) => (
            <Month titleMonth={item.titleMonth} daysMonth={item.daysMonth}/>
          ))
        }
      </div>
    </div>
  )
}
