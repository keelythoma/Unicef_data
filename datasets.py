#| label: data-import
#| message: false

import pandas as pd
import numpy as np
from plotnine import *
import matplotlib.pyplot as plt
import geopandas as gpd

# Import your data
indicator1 = pd.read_csv("data/unicef_indicator_1.csv")
indicator2 = pd.read_csv("data/unicef_indicator_2.csv")
metadata = pd.read_csv("data/unicef_metadata.csv")

# Display first few rows
indicator1.head()
