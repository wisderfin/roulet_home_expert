import React from "react"
import style from "./rouletteCell.module.css"
import { IRouletteCell } from "./RouletteCellTypes"
import Modal from "../../../../components/UI/Modal/Modal";
import Button from "../../../../components/UI/Button/Button";

const RouletteCell: React.FC<IRouletteCell> = React.memo(({ item, isAnimate, index, getPrize }) => {

  return (
    <>

      <div className={style.itemWrapper}>
        {
          item.name === undefined ?
          <img className={style.img} src={item} alt="" />
          :
          <img className={style.img} src={"https://locback.nl.tuna.am/game/img/" + item.img} alt="" />

        }

      </div>

      {isAnimate && index == 61 ?
        <Modal funcOnClose={getPrize}>
          <h1>Заберите приз!</h1>
          <h2 className={style.text}>{item.name}</h2>
          <div className={`${style.itemWrapper}`} style={{ width: "50%" }}>
            <img className={style.img} src={"https://locback.nl.tuna.am/game/img/" + item.img} alt={item.name}/>
          </div>

          <Button onClick={getPrize} style={{ fontSize: "16px", marginTop: "10px" }}>Забрать</Button>
        </Modal> : null}
    </>
  )
})

export default RouletteCell
