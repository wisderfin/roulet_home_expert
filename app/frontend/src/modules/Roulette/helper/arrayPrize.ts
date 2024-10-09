const arrayPrize = [
    {name: "common", chance: 50},
    {name: "rare", chance: 30},
    {name: "epic", chance: 15},
    {name: "legendary", chance: 4.5},
    {name: "myfik", chance: 0.5},
]




function getRandomNumber() {
    const min = 0.01;
    const max = 100;
    return parseFloat((Math.random() * (max - min) + min).toFixed(3));
}



export function play(){
    let result = getRandomNumber()
    if (result <= arrayPrize[4].chance) {
        return arrayPrize[4].name
    } else if (result <= arrayPrize[3].chance) {
        return arrayPrize[3].name
    } else if (result <= arrayPrize[2].chance) {
        return arrayPrize[2].name
    } else if (result <= arrayPrize[1].chance) {
        return arrayPrize[1].name
    } else {
        return arrayPrize[0].name
    }
}

export interface IPrize {
    name: string
    winner: boolean
}

export function getArrayPrize(): IPrize[] {
    let result: IPrize[] = []
    for (let index = 0; index < 22; index++) {
        if (index != 19) {
            result.push({
                name: play(),
                winner: false
            })
        } else {
            result.push({
                name: play(),
                winner: true
            })
        }
       
    }
    return result
}
