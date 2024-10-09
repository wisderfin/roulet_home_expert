import { create } from 'zustand';

type StateMoney = {
    money: number
}

type ActionMoney = {
    addMoney: () => void
    subMoney: (count: number) => void
    resetMoney: () => void
}

export const useMoneyStore = create<StateMoney & ActionMoney>((set) => ({
    money: 0,
    addMoney: () => set((state) => ({ money: state.money + 10 })),
    subMoney: (count: number) => set((state) => ({ money: state.money - count })),
    resetMoney: () => set(() => ({ money: 1000 })),
}));

