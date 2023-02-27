from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from scipy import linalg
from math import pi, cos
import streamlit as st

st.title("MY PLOTS")
data = pd.read_table('weather.txt', delimiter=',')
x = np.abs(data["Tmean"]).to_numpy()
x_90 = x[:90]
y = data['day'].to_numpy()
y_90=y[:90]
plt.plot(x_90, y_90, ".")
st.pyplot(plt.gcf())


def line(t, a, b, c):
    return a * np.cos(2*pi*t+b)+c


popt, pcov = curve_fit(line, x_90, y_90)
e = np.repeat(10., 90)
popt, pcov = curve_fit(line, x_90, y_90, sigma=e)
popt
pcov
print("b= ", popt[1], "+/-", pcov[1, 1]**.5)
print("a= ", popt[0], "+/-", pcov[0, 0]**.5)
plt.errorbar(x_90, y_90, yerr=e, fmt="none")
xfine = np.linspace(0., 100., 100)
plt.plot(xfine, line(xfine, popt[0], popt[1], popt[2]), 'r-')
st.pyplot(plt.gcf())
