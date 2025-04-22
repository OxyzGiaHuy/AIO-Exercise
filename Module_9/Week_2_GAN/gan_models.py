import torch.nn as nn
import numpy as np

class Generator(nn.Module):
    def __init__(self, latent_dim, img_shape):
        super().__init__()
        self.latent_dim = latent_dim
        self.img_shape = img_shape
        output_dim = int(np.prod(img_shape))  # Flatten

        self.model = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(128, 256),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(0.2, inplace=True),
            
            nn.Linear(512, 1024),
            nn.BatchNorm1d(1024),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(1024, output_dim),
            nn.Tanh()
        )
    
    def forward(self, z):
        img = self.model(z)
        img = img.view(img.size(0), *self.img_shape) # reshape (B, C, H, W)
        return img


class Discriminator(nn.Module):
    def __init__(self, img_shape):
        super().__init__()
        self.img_shape = img_shape
        input_dim = int(np.prod(img_shape))
        self.model = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(512, 256),
            nn.LeakyReLU(0.2, inplace=True),

            nn.Linear(256, 1),
            nn.Sigmoid()
        )
    
    def forward(self, img):
        img_flat = img.view(img.size(0), -1)
        validity = self.model(img_flat)
        return validity
