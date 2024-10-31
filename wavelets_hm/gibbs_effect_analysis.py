import numpy as np
from matplotlib import pyplot as plt

# define parameters for rectangular pulse
M = 100  # number of harmonics to analyze
k = np.arange(1, 101)  # indices of harmonics
T = 10  # period of pulse repetition
tau = 1  # time corresponding to pulse maximum
w = 2 * np.pi * k / T   # angular frequency of harmonics

# compute amplitude and phase spectra for symmetric and asymmetric pulses
c1 = np.zeros(101, dtype=complex)
c1[0] = tau / T
c1[1:1+M] = (np.exp(1j * tau * w / 2) / (1j * w)) - (1 / (1j * w * np.exp(1j * tau * w / 2)))

f1 = np.zeros(101)
f1[0] = 0
f1[1:1+M] = (w / (2 * np.pi))  # frequencies for symmetric pulse

c2 = np.zeros(101, dtype=complex)
c2[0] = tau / T
c2[1:1+M] = (1 / (1j * w)) - (1 / (1j * w * np.exp(1j * tau * w)))

f2 = np.zeros(101)
f2[0] = 0
f2[1:1+M] = (w / (2 * np.pi))  # frequencies for asymmetric pulse

# plot amplitude and phase spectra
plt.figure(figsize=(12, 6))
plt.xlabel('f1', fontsize=14)
plt.ylabel('|c_1|', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.stem(f1, np.abs(c1), 'k.')
plt.title('amplitude spectrum of symmetric rectangular pulse (T=10, tau=1)')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.xlabel('f1', fontsize=14)
plt.ylabel('|c_1|', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.stem(f1, c1, 'k.')
plt.title('phase spectrum of symmetric rectangular pulse (T=10, tau=1)')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.xlabel('f2', fontsize=14)
plt.ylabel('|c_2|', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.stem(f2, np.abs(c2), 'k.')
plt.title('amplitude spectrum of asymmetric rectangular pulse (T=10, tau=1)')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
plt.xlabel('f2', fontsize=14)
plt.ylabel('|c_2|', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.stem(f2, c2, 'k.')
plt.title('phase spectrum of asymmetric rectangular pulse (T=10, tau=1)')
plt.grid(True)
plt.show()

# reconstruct the original signal based on harmonics
t = np.linspace(-T, T, 1000)  # time interval
harmonics = [10, 15, 25, 100]  # number of harmonics for reconstruction

# fundamental frequency
w0 = 2 * np.pi / T

# function to reconstruct the signal
def reconstruct_signal(cn, N):
    signal = np.zeros_like(t, dtype=complex)
    for n in range(1, N+1):
        signal += cn[n] * np.exp(1j * n * w0 * t)
    return np.real(signal)

# signal reconstruction and plotting
plt.figure(figsize=(12, 8))

for i, N in enumerate(harmonics):
    restored_signal = reconstruct_signal(c1, N)
    plt.subplot(2, 2, i+1)
    plt.plot(t, restored_signal, 'black')
    plt.title(f'reconstruction with {N} harmonics')
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.grid(True)

plt.tight_layout()
plt.show()

# define time parameters for rectangular pulse construction
t_rect = np.linspace(-T, T, 1000)  # time interval

# define symmetric rectangular pulse
u_symmetric = np.where(np.abs(t_rect) <= tau / 2, 1, 0)

# define asymmetric rectangular pulse
u_asymmetric = np.where((t_rect >= 0) & (t_rect <= tau), 1, 0)

# plot rectangular pulse graphs
plt.figure(figsize=(12, 6))

# symmetric rectangular pulse
plt.subplot(1, 2, 1)
plt.plot(t_rect, u_symmetric, 'black')
plt.title('symmetric rectangular pulse')
plt.xlabel('t')
plt.ylabel('u(t)')
plt.grid(True)

# asymmetric rectangular pulse
plt.subplot(1, 2, 2)
plt.plot(t_rect, u_asymmetric, 'black')
plt.title('asymmetric rectangular pulse')
plt.xlabel('t')
plt.ylabel('u(t)')
plt.grid(True)

plt.tight_layout()
plt.show()
