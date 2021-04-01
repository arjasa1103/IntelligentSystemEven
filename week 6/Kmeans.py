import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy

df = pd.DataFrame(
    {"x": [1.0, 1.5, 3.0, 5.0, 3.5, 4.5, 3.5], "y": [1.0, 2.0, 4.0, 7.0, 5.0, 5.0, 4.5]}
)

k = 2
centroids = {
    i + 1: [np.random.randint(0, 7), np.random.randint(0, 7)] for i in range(k)
}

colmap = {1: "r", 2: "b"}


def assignments(df, centroids):
    for i in centroids.keys():
        df["distance_from_{}".format(i)] = np.sqrt(
            (df["x"] - centroids[i][0]) ** 2 + (df["y"] - centroids[i][1]) ** 2
        )
    centroids_distance_cols = ["distance_from_{}".format(i) for i in centroids.keys()]
    df["closest"] = df.loc[:, centroids_distance_cols].idxmin(axis=1)
    df["closest"] = df["closest"].map(lambda x: int(x.lstrip("distance_from_")))
    df["color"] = df["closest"].map(lambda x: colmap[x])
    return df


def update(centroids):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df["closest"] == i]["x"])
        centroids[i][1] = np.mean(df[df["closest"] == i]["y"])
    return centroids


old_centroids = copy.deepcopy(centroids)

df = assignments(df, centroids)
centroids = update(centroids)
print(centroids)

while True:
    closest_centroids = df["closest"].copy(deep=True)
    centroids = update(centroids)
    df = assignments(df, centroids)
    print(centroids)
    print(df, "\n")
    if closest_centroids.equals(df["closest"]):
        break

fig = plt.figure(figsize=(5, 5))
plt.scatter(df["x"], df["y"], color=df["color"], alpha=0.5, edgecolor="k")
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.ylim(0, 8)
plt.xlim(0, 8)
plt.show()