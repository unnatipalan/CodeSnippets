"""
We are exploring method chaining in Pandas as explained in
https://towardsdatascience.com/the-unreasonable-effectiveness-of-method-chaining-in-pandas-15c2109e3c69
"""
import pandas as pd
import numpy as np
import sklearn

from sklearn.datasets import load_wine

data = load_wine()
wine = pd.DataFrame(data.data,
                    columns=data.feature_names)
print(wine.head())

# Method chaining and capturing the resultset in a new data frame.
wine_modified = (
    wine.rename(columns={"color_intensity": "ci"})
    .assign(color_filter=lambda x: np.where((x.hue > 1) & (x.ci > 7), 1, 0))
    .query("alcohol > 14 and color_filter == 1")
    .sort_values("alcohol", ascending=False)
    .reset_index(drop=True)
    .loc[:, ["alcohol", "ci", "hue"]]
)

print(wine_modified.head())