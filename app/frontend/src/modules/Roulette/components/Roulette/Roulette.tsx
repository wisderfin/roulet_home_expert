import { useEffect, useState } from "react";
import style from "./roulette.module.css";
import RouletteCell from "../RouletteCell/RouletteCell";
import { StringOrNumberArray } from "./RouletteTypes";
import PointerRoulette from "../PointerRoulette/PointerRoulette";
import { playRoulette, getTimeUser } from "../../../../services/serversUser";
import Modal from "../../../../components/UI/Modal/Modal";
import useModal from "../../../../hooks/useModal";
import Button from "../../../../components/UI/Button/Button";
import logo from "../../assets/GroupLogo.svg"


const arrayTest: StringOrNumberArray[] = ["КРУТИ", "КРУТИ", "КРУТИ"]

export const Roulette = () => {
  const [isEndAnim, setIsEndAnim] = useState<boolean>(false);
  const [click, setClick] = useState<boolean>(true);
  const [isAnimeteRoulette, setIsAnimateRoulette] = useState<boolean>(false);
  const [arrayRoulette, setArrayRoulette] = useState<StringOrNumberArray[]>(arrayTest);
  const [timeLeft, setTimeLeft] = useState<number>(0);
  const [disabled, setDisabled] = useState(true)

  const [isVisibleModal, setIsVisibleModal, textModal, setTextModal] = useModal();

  const handleError = (error: unknown) => {
    setTextModal(String(error));
    setIsVisibleModal(true);
  };

  useEffect(() => {    
    const getTime = async () => {
    try {
      const resp = await getTimeUser()      
      setTimeLeft(resp)
      
    } catch (err) {
      handleError(err)
    } 
    }
    getTime()
  }, [])


  useEffect(() => {    
    if (timeLeft <= 0) {
      setDisabled(false)
    } else {
      setDisabled(true)
    }
    const interval = setInterval(() => {
      setTimeLeft((prevTime) => (prevTime > 0 ? prevTime - 1 : 0));
    }, 1000);

    return () => {
      clearInterval(interval)
    };
  }, [timeLeft]);


  const formatTime = (seconds: number) => {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return `${hours.toString().padStart(2, '0')}:${minutes
      .toString()
      .padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const startGame = async () => {
    if (isAnimeteRoulette || !click || timeLeft > 0) return;


    setClick(false);
    try {
      const resp = await playRoulette();
      const time = await getTimeUser()
      setArrayRoulette(() => [...arrayRoulette, ...resp.slice(3, resp.lenght)]);
      
      setDisabled(true)
      setTimeLeft(time)
      setIsAnimateRoulette(true);
    } catch (err) {
      handleError(err);
    } finally {
      setClick(true);
    }
  };

  const getPrize = () => {
    console.log(arrayRoulette);
    setIsEndAnim(false);
    setIsAnimateRoulette(false);
    setArrayRoulette(arrayTest)
  };
  return (
    <div className={style.wrapperConteiner}>
      <div className={style.containerRoulette}>
        <img src={logo} alt="logo" width="64px" className={style.img}/>
        <div className={style.main}>
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
        </div>
        <Button disabled={disabled} onClick={startGame}>{timeLeft <= 0 ? "Крутить" : formatTime(timeLeft)}</Button>
      </div>
      {isVisibleModal && <Modal funcOnClose={() => setIsVisibleModal(false)}>{textModal}</Modal>}
    </div>


  );
};
