import Button from "../../../components/UI/Button/Button"
import style from "./header.module.css"
import iconDzen from "../assets/dzenlogo.svg"
import presents from "../assets/presents.svg"
import logoTG from "../assets/telegram.svg"

export const Header = () => {
  return (
    <div className={style.header}>
      <Button style={{ padding: "0", fontSize: "0", width: "15%"}}>
        <a href="https://t.me/klinning63">
          <img src={logoTG} alt="" width="42px" />
        </a>
      </Button>
     
      <Button style={{ padding: "0", fontSize: "0", width: "15%" }}>
        <a href="https://dzen.ru/home_expert_samara" target="_blank">
          <img src={iconDzen} alt="" className={style.img} width="32px" />
        </a>
      </Button>
      <Button style={{ padding: "0", fontSize: "0", width: "15%" }}>
        <a href="https://t.me/klinning63/272">
          <img src={presents} alt="" className={style.img} />
        </a>
      </Button>
    </div>
  )
}
