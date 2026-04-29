import pandas as pd

data = pd.read_csv("./day25/squirrel_data.csv")
data = pd.DataFrame(data["Primary Fur Color"])

cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]
gray = data[data["Primary Fur Color"] == "Gray"]


print(len(cinnamon))
print(len(black))
print(len(gray))

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray), len(cinnamon), len(black)],
}

df = pd.DataFrame(data_dict)
df.to_csv("./day25/squirrel_count.csv")
