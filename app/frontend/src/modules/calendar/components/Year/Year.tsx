import { useState } from 'react';
import Header from '../Header/Header'
import Month from '../Month/Month'
import style from './year.module.css'

interface IMonth {
  titleMonth: string,
  daysMonth: (number | string)[]
}



const monthsArr: IMonth[] = [
  { titleMonth: "Январь", daysMonth: Array.from({ length: 31 }, (_, i) => i + 1) },
  { titleMonth: "Февраль", daysMonth: Array.from({ length: 29 }, (_, i) => i + 1) }, 
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
  const [month, setMonth] = useState<(number | string)[] | null>(null)
  const [yearArr, setYear] = useState<IMonth[]>(monthsArr)
  let currentDay = new Date()

  const getDays = (year: number) => {

    yearArr.forEach((item, index) => {
      let date = new Date(year, index, 1)
      setMonth([...item.daysMonth])



        // for (let i = 0; i < date.getDay() - 1; i++) {
        // }
      
      
    })
  }



  return (
    <div className={style.wrapperYear}>
      <div className={style.year}>
        <Header/>
        {
          yearArr.map((item) => (
            <Month titleMonth={item.titleMonth} daysMonth={item.daysMonth}/>
          ))
        }
      </div>
    </div>
  )
}
