export type StringOrNumberArray = (string | number);

export interface IRouletteCell {
    item: any
    isAnimate: boolean
    index: number
    getPrize: () => void
}
