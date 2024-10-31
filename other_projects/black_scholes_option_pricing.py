import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# function to calculate the option price using the black-scholes model
def black_scholes(S, K, r, T, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

# model parameters
S = 100   # current price of the underlying asset
K = 100   # strike price of the option
r = 0.05  # risk-free interest rate
T = 1     # time to expiration (in years)
sigma = 0.2  # volatility

# plot of the option price dependence on the current price of the underlying asset
plt.figure(figsize=(10, 6))
S_values = np.linspace(50, 150, 100)
call_prices = black_scholes(S_values, K, r, T, sigma)
plt.plot(S_values, call_prices, label='option price')
plt.xlabel('current price of the underlying asset')
plt.ylabel('option price')
plt.title('option price vs current price of the underlying asset')
plt.legend()
plt.grid(True)
plt.show()

# plot of the option price dependence on the strike price
plt.figure(figsize=(10, 6))
K_values = np.linspace(50, 150, 100)
call_prices = black_scholes(S, K_values, r, T, sigma)
plt.plot(K_values, call_prices, label='option price')
plt.xlabel('strike price')
plt.ylabel('option price')
plt.title('option price vs strike price')
plt.legend()
plt.grid(True)
plt.show()

# plot of the option price dependence on time to expiration
plt.figure(figsize=(10, 6))
T_values = np.linspace(0.01, 2, 100)
call_prices = black_scholes(S, K, r, T_values, sigma)
plt.plot(T_values, call_prices, label='option price')
plt.xlabel('time to expiration (years)')
plt.ylabel('option price')
plt.title('option price vs time to expiration')
plt.legend()
plt.grid(True)
plt.show()

# plot of the option price dependence on volatility
plt.figure(figsize=(10, 6))
sigma_values = np.linspace(0.05, 0.5, 100)
call_prices = black_scholes(S, K, r, T, sigma_values)
plt.plot(sigma_values, call_prices, label='option price')
plt.xlabel('volatility')
plt.ylabel('option price')
plt.title('option price vs volatility')
plt.legend()
plt.grid(True)
plt.show()

# plot of delta changes
plt.figure(figsize=(10, 6))
deltas = [norm.cdf((np.log(s / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))) for s in S_values]
plt.plot(S_values, deltas)
plt.xlabel('current price of the underlying asset')
plt.ylabel('delta')
plt.title('delta vs current price of the underlying asset')
plt.grid(True)
plt.show()

# plot of theta changes
plt.figure(figsize=(10, 6))
thetas = []
for t in T_values:
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    theta = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(t)) - r * K * np.exp(-r * t) * norm.cdf(d2)
    thetas.append(theta)

plt.plot(T_values, thetas)
plt.xlabel('time to expiration (years)')
plt.ylabel('theta')
plt.title('theta vs time to expiration')
plt.grid(True)
plt.show()
