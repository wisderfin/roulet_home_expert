import style from "./header.module.css"
import Balance from "../Balance/Balance"

export const Header = () => {
  return (
    <div className={style.header}>
        <div className={style.wrapper}>
            <Balance/>
        </div>
    </div>
  )
}

