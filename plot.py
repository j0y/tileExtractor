# Copyright 2022 Google LLC.
# SPDX-License-Identifier: Apache-2.0

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal

nStatisticValues = 8
image = np.array(Image.open('examples/maps/sandstone_partial.png').convert('L'), float)

# Window the image.
window_x = np.hanning(image.shape[1])
window_y = np.hanning(image.shape[0])
image *= np.outer(window_y, window_x)
# Transform to frequency domain.
spectrum = np.fft.rfft2(image)
# Partially whiten the spectrum. This tends to make the autocorrelation sharper,
# but it also amplifies noise. The -0.6 exponent is the strength of the
# whitening normalization, where -1.0 would be full normalization and 0.0 would
# be the usual unnormalized autocorrelation.
spectrum *= (1e-12 + np.abs(spectrum))**-0.6
# Exclude some very low frequencies, since these are irrelevant to the texture.
fx = np.arange(spectrum.shape[1])
fy = np.fft.fftshift(np.arange(spectrum.shape[0]) - spectrum.shape[0] // 2)
fx, fy = np.meshgrid(fx, fy)
spectrum[np.sqrt(fx**2 + fy**2) < 10] = 0
# Compute the autocorrelation and inverse transform.
acorr = np.real(np.fft.irfft2(np.abs(spectrum)**2))

#get y size
indOfXTop = np.argpartition(acorr[0], -nStatisticValues)[-nStatisticValues:]
#indeOfTopSorted = indOfTop[np.argsort(acorr[indOfTop])]
print(indOfXTop)

#get x size
acorrY = np.transpose(acorr)
indOfYTop = np.argpartition(acorrY[0], -nStatisticValues)[-nStatisticValues:]
print(indOfYTop)


#TODO: cut dimensions from 0, 0 to statistically significant value or crop to rectangle of sign value sides
showGraph = False
saveGraph = False
if (showGraph or saveGraph):
    plt.figure(figsize=(10, 10))
    plt.imshow(acorr, cmap='Blues', vmin=0, vmax=np.percentile(acorr, 99.5))
    plt.xlim(0, image.shape[1] / 2)
    plt.ylim(0, image.shape[0] / 2)
    plt.title('2D autocorrelation', fontsize=18)
    plt.xlabel('Horizontal lag (px)', fontsize=15)
    plt.ylabel('Vertical lag (px)', fontsize=15)
    if saveGraph:
        plt.savefig('result.png')
    if (showGraph):
        plt.show()
