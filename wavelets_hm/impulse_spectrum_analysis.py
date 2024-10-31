import numpy as np
from matplotlib import pyplot as plt

# function to compute fourier coefficients
def compute_fourier_coefficients(M, T, tau):
    k = np.arange(1, M + 1)  # harmonic numbers
    w = 2 * np.pi * k / T  # harmonic frequencies
    
    # initializing array for fourier coefficients
    c = np.zeros(M + 1, dtype=complex)
    c[0] = tau / T  # constant component
    c[1:] = 4 * ((np.sin(w * tau / 2)**2) / (T * tau * w**2)) * np.exp(-1j * w * tau)
    
    # frequency array depending on period
    f = np.zeros(M + 1)
    f[1:] = w / (2 * np.pi)  # normalized frequencies
    
    return f, c

# function to plot impulse
def plot_impulse(f, c, label, title):
    plt.figure(figsize=(12, 6))
    plt.xlabel(label, fontsize=14)
    plt.ylabel('|c|', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.stem(f, np.abs(c), 'k.')
    plt.title(title)
    plt.grid(True)
    plt.show()

# defining parameters
M = 100

# calculations and plotting
parameters = [
    (10, 1, 'f1', 'Triangular pulse (T=10, tau=1)'),
    (10, 2, 'f2', 'Triangular pulse (T=10, tau=2)'),
    (20, 1, 'f3', 'Triangular pulse (T=20, tau=1)'),
    (10, 1, 'f4', 'Triangular pulse - centered at zero (T=10, tau=1)'),
    (10, 1, 'f5', 'Sawtooth pulse (T=10, tau=1)'),
    (10, 1, 'f6', 'Sawtooth pulse - centered at zero (T=10, tau=1)')
]

for T, tau, label, title in parameters:
    f, c = compute_fourier_coefficients(M, T, tau)
    plot_impulse(f, c, label, title)
