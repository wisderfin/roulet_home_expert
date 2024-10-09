import { useMoneyStore } from "../../../../store/store"
import style from "./balance.module.css"


const Balance = () => {
  const { resetMoney, money } = useMoneyStore()

  return (
    <div className={style.balanceBlock}>
      <div className={style.balance}>{money} Tk</div>
      <div className={style.deposit} onClick={() => resetMoney()}>Получить</div>
    </div>
  )
}

export default Balance