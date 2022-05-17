import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score
from ks_metric import ks_score
import streamlit as st
import plotly.graph_objects as go
st.set_page_config(layout="wide")

st.write("# AUC & KS ")

class_sep = st.slider("Class seperation slider - [how easy is the problem] ",0.0, 1.0, 0.5, 0.01)

# sample data
X, y = make_classification(
    n_samples=1000, class_sep=class_sep, random_state=0
)  # 1000 samples with 20 features

# split train-test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# simple Logistic Model
model = LogisticRegression(random_state=23)
model.fit(X_train, y_train)

# predictions
y_train_pred = model.predict_proba(X_train)[:, 1] # probability of class 1
y_test_pred = model.predict_proba(X_test)[:, 1]

# roc curve
fpr, tpr, thres = roc_curve(y_test, y_test_pred)
fnr = 1 - tpr
tnr = 1 - fpr

col1, col2 = st.columns(2)

# plot
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=thres[1:], y=tnr, mode="lines", name="tnr"))

# plot tpr
fig1.add_trace(go.Scatter(x=thres[1:], y=fnr, mode="lines", name="fnr"))
fig1.add_shape(
    type="line",
    x0=thres[1:][(tnr - fnr).argmax()],
    y0=fnr[(tnr - fnr).argmax()],
    x1=thres[1:][(tnr - fnr).argmax()],
    y1=tnr[(tnr - fnr).argmax()],
    line=dict(
        color="MediumPurple",
        width=2,
        dash="dot",
    ),
    name="KS",
)
fig1.add_annotation(
    text=f"KS: {((tnr-fnr).max()*100).round(2)}",
    x=thres[1:][(tnr - fnr).argmax()] - 0.05,
    y=(fnr[(tnr - fnr).argmax()] + tnr[(tnr - fnr).argmax()]) / 2,
    showarrow=False,
    bgcolor="#aaffaa",
)
fig1.update_layout(
    title="KS",
    xaxis_title="Threshold",
    yaxis_title="% Below Threshold",
)

with col1:
    st.plotly_chart(fig1)
    st.write("KS :", ks_score(y_test, y_test_pred).round(2))
    st.write("tnr - fnr :", (tnr - fnr).max().round(4))
    _, ks_thres = ks_score(y_test, y_test_pred, return_threshold=True)
    st.write("KS Threshold :", ks_thres.round(4))

# roc
fig2 = go.Figure()
fig2.add_trace(
    go.Scatter(
        x=fpr,
        y=tpr,
        mode="lines",
        name="ROC",
        fill='tozeroy'
    )
)
fig2.add_trace(
    go.Scatter(
        x=np.linspace(0, 1, 10),
        y=np.linspace(0, 1, 10),
        mode="lines",
        name="Random Classifer",
    )
)

fig2.update_layout(
    title="AUC-ROC",
    xaxis_title="FPR",
    yaxis_title="TPR",
)

with col2:
    st.plotly_chart(fig2)
    st.write("AUC :", roc_auc_score(y_test, y_test_pred).round(3))
    st.write("tpr - fpr :", (tpr - fpr).max().round(4))
    J = tpr - fpr
    ix = np.argmax(J)
    best_thresh = thres[ix]
    st.write("J thres :", best_thresh.round(4))




