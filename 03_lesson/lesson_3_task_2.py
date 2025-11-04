from smartphone import Smartphone

catalog = [
    Smartphone("iphone", "16 pro", "+79626970043"),
    Smartphone("iphone", "15 pro", "+79626970043"),
    Smartphone("iphone", "14", "+79626970043"),
    Smartphone("iphone", "12 pro", "+79626970043"),
    Smartphone("iphone", "11 pro", "+79626970043")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}.")
