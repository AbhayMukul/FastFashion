import pandas as pd
import numpy as np
import statistics as st

# Read file and set row number(s) to use as the column name(s)
df = pd.read_csv("data\FastFashionMain.csv");


mean_cotton = st.mean(np.array(df['cotton']));
print(mean_cotton)