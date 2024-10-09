import { useState } from "react";
import style from "./roulette.module.css";
import RouletteCell from "../RouletteCell/RouletteCell";
import { StringOrNumberArray } from "./RouletteTypes";
import PointerRoulette from "../PointerRoulette/PointerRoulette";
import { playRoulette } from "../../../../services/serversUser";
import Fps from "../../../../components/fps/Fps";
import Modal from "../../../../components/UI/Modal/Modal";
import { useMoneyStore } from "../../../../store/store";
import useModal from "../../../../hooks/useModal";
import Footer from "../../../../components/Footer/Footer";
import { GameInput } from "../../../GameInput";


const arrayTest: StringOrNumberArray[] = ["КРУТИ", "КРУТИ", "КРУТИ"]

export const Roulette = () => {
  const [isEndAnim, setIsEndAnim] = useState<boolean>(false);
  const [click, setClick] = useState<boolean>(true);
  const [isAnimeteRoulette, setIsAnimateRoulette] = useState<boolean>(false);
  const [arrayRoulette, setArrayRoulette] = useState<StringOrNumberArray[]>(arrayTest);
  const [valueInput, setValueInput] = useState<string>('0'); 

  const { subMoney, money } = useMoneyStore();
  const [isVisibleModal, setIsVisibleModal, textModal, setTextModal] = useModal();

  const handleError = (error: unknown) => {
    setTextModal(String(error));
    setIsVisibleModal(true);
  };
  
  const startGame = async () => {
    const numericalValue = Number(valueInput);

    if (money < numericalValue || money <= 0) {
      return handleError("Недостаточно средств");
    }

    if (numericalValue < 50) {
      return handleError("Минимальная ставка 50");
    }

    if (isAnimeteRoulette || !click) return;

    setClick(false);
    try {
      const resp = await playRoulette(numericalValue);
      
      
      setArrayRoulette(() => [...arrayRoulette,...resp.slice(3, resp.lenght)]);
      
      setIsAnimateRoulette(true);
      subMoney(numericalValue);
    } catch (err) {
      handleError(err);
    } finally {
      setClick(true);
    }
  };

  const getPrize = () => {
    setIsEndAnim(false);
    setIsAnimateRoulette(false);
    setArrayRoulette((prevArray) => [prevArray[18], prevArray[19], prevArray[20]])    
  };
  return (
    <div className={style.main}>
      <Fps />
      <PointerRoulette>
        <div className={style.roulette}>
          <div
            className={`${style.itemList} ${isAnimeteRoulette ? style.animate : ''}`}
            onAnimationEnd={() => setIsEndAnim(true)}
          >
            {arrayRoulette?.map((item, index) => (
              <RouletteCell getPrize={getPrize} item={item} key={index} isAnimate={isEndAnim} index={index} />
            ))}
          </div>
        </div>
      </PointerRoulette>
      <GameInput 
        setValueInput={setValueInput} 
        startGame={startGame} 
        valueInput={valueInput} 
      />
      <Footer />
      {isVisibleModal && <Modal funcOnClose={() => setIsVisibleModal(false)}>{textModal}</Modal>}
    </div>
  );
};
