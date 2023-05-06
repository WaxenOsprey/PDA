
const fruit = ["Apple", "Banana", "Grape", "Melon", "Orange", "Raspberry", "Strawberry", "Lemon"]

const y = "Orange"

const FruitSearch = (fruit, y) => {
    for (let i = 0; i < fruit.length; i++) {
        if (fruit[i] === y)
        return fruit[i]
    } 

}
result = FruitSearch(fruit, y)
console.log( "Result:", result)

