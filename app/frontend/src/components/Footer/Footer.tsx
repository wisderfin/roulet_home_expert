import style from "./Footer.module.css"
import settingsIcon from "../../assets/settings.svg"

const Footer = () => {
  return (
    <div className={style.footerWrapper}>
      <div className={style.footer}>
        <img src={settingsIcon} alt="" className={style.image} />
      </div>
    </div>
  )
}

export default Footer