import pandas as pd
from sklearn import tree
import graphviz

dataset = pd.read_csv("animals.csv")
dataset = dataset.drop("animal_name", axis=1)

train_features = dataset.iloc[:80, :-1]
test_features = dataset.iloc[80:, :-1]
train_targets = dataset.iloc[:80, -1]
test_targets = dataset.iloc[80:, -1]

treedata = tree.DecisionTreeClassifier(criterion="entropy").fit(
    train_features, train_targets
)

dot_data = tree.export_graphviz(treedata, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("animals")

print("Prediction accuracy :", treedata.score(test_features, test_targets) * 100, "%")
