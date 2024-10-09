export type StringOrNumberArray = (string | number);

export interface IRouletteCell {
    item: StringOrNumberArray
    isAnimate: boolean
    index: number
    getPrize: () => void
}
