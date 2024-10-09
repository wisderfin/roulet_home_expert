import Button from "../../../../components/UI/Button/Button"
import Input from "../../../../components/UI/Input/Input"
import style from "./GameInput.module.css"
import { IGameInput } from "./GameInputTypes";


export const GameInput: React.FC<IGameInput> = ({ valueInput, setValueInput, startGame }) => {

    function onChangeInput(event: React.ChangeEvent<HTMLInputElement>) {
        const value = event.target.value;
        setValueInput(value);
    }

    const handleFocus = () => {
        if (valueInput === '0') {
            setValueInput(''); // Убираем 0 при фокусе
        }
    };

    const handleBlur = () => {
        if (valueInput === '') {
            setValueInput('0'); // Возвращаем 0, если инпут пустой
        }
    };

    function buttonValue(typeButton: string) {
        const changeValue = typeButton === 'increment' ? 50 : -50;
        setValueInput(prev => {
            const newValue = Number(prev) + changeValue;
            return newValue < 0 ? '0' : String(newValue); // Не допускаем отрицательных значений
        });
    }

    return (
        <div className={style.inputInfo}>
            <div className={style.inputBox}>
                <Input
                    value={valueInput}
                    onChange={onChangeInput}
                    onFocus={handleFocus}
                    onBlur={handleBlur}
                />
                <button onClick={() => buttonValue('increment')}>+50</button>
                <button onClick={() => buttonValue('decrement')}>-50</button>
            </div>
           

            <Button onClick={startGame}>Играть</Button>
           
        </div>

    )
}
