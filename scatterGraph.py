import pandas as pd
import plotly_express as px

df = pd.read_csv("data.csv")
figure1 = px.scatter(df, x = "date", y = "cases", color = "country")
figure1.show()