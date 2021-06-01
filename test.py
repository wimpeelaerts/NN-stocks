import talib
import numpy as np
import pandas as pd
import plotly.express as px


c = np.random.randn(100)
rsi = talib.RSI(c)
k, d = talib.STOCHF(rsi, rsi, rsi)

df = pd.DataFrame(data={'Random': c, 'rsi': rsi, 'k': k, 'd': d})

fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
fig.show()


