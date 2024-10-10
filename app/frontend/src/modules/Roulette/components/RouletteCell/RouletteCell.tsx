import React from "react"
import style from "./rouletteCell.module.css"
import { IRouletteCell } from "./RouletteCellTypes"
import Modal from "../../../../components/UI/Modal/Modal";
import Button from "../../../../components/UI/Button/Button";

const RouletteCell: React.FC<IRouletteCell> = React.memo(({ item, isAnimate, index, getPrize }) => {
  return (
    <>

      <div className={`${style.itemWrapper} ${isAnimate && index == 19 ? style.winnerItem : ''}`}>
        {
          item.name === undefined ? 
          <div className={style.item}>{item}</div>
          : 
          <img className={style.img} src={item.img} alt="" />
        }
        
      </div>

      {isAnimate && index == 19 ?
        <Modal funcOnClose={getPrize}>
          <h1>Заберите приз!</h1>
          <h2 className={style.text}>{item.name}</h2>
          <div className={`${style.itemWrapper}`} style={{ width: "50%" }}>
            <img className={style.img} src={item.img} alt="" />
          </div>
          
          <Button onClick={getPrize} style={{ fontSize: "16px", marginTop: "10px" }}>Забрать</Button>
        </Modal> : null}
    </>
  )
})

export default RouletteCell