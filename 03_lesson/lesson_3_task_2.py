from smartphone import smartphone
catalog = [
    smartphone(brand "iphone", model: "16 pro", number: +79626970043),
    smartphone(brand "iphone", model: "15 pro", number: +79626970043),
    smartphone(brand "iphone", model: "14", number: +79626970043),
    smartphone(brand "iphone", model: "12 pro", number: +79626970043),
    smartphone(brand "iphone", model: "11 pro", number: +79626970043)
]
for " smartphone in catalog ":
print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}.")
