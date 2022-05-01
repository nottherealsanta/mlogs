import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.title("Uber pickups in NYC")


# x = np.outer(np.linspace(-1, 1, 20), np.ones(20))
# y = x.copy().T  # transpose
# z = np.cos(x) * y + np.sin(x * 2) * y
# trace = go.Surface(x=x, y=y, z=z)
# data = [trace]
# layout = go.Layout(title="3D Surface plot")
# fig = go.Figure(
#     data=data,
#     frames=[
#         go.Frame(data=[go.Scatter3d(x=[0.5,0.5], y=[0.5,0.5], z=[0.5,0.5], mode="markers", marker=dict(size=10, color="red"))]),
#     ],
# )

# Generate curve data
t = np.linspace(-1, 1, 100)
x = t + t**2
y = t - t**2
xm = np.min(x) - 1.5
xM = np.max(x) + 1.5
ym = np.min(y) - 1.5
yM = np.max(y) + 1.5
N = 50
s = np.linspace(-1, 1, N)
xx = s + s**2
yy = s - s**2


# Create figure
fig = go.Figure(
    data=[
        go.Scatter3d(x=x, y=y, mode="lines", line=dict(width=2, color="blue")),
        go.Scatter3d(x=x, y=y, mode="lines", line=dict(width=2, color="blue")),
    ],
    layout=go.Layout(
        # xaxis=dict t(range=[ym, yM], autorange=False, zeroline=False),
        title_text="Kinematic Generation of a Planar Curve",
        hovermode="closest",
        updatemenus=[
            dict(
                type="buttons",
                buttons=[dict(label="Play", method="animate", args=[None])],
            )
        ],
    ),
    frames=[
        go.Frame(
            data=[
                go.Scatter3d(
                    x=[xx[k]],
                    y=[yy[k]],
                    mode="markers",
                    marker=dict(color="red", size=10),
                )
            ]
        )
        for k in range(N)
    ],
)

st.plotly_chart(fig)
