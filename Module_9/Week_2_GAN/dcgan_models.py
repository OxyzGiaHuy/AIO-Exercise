import torch
import torch.nn as nn
import numpy as np

class DCGAN_Generator(nn.Module):
    """
    Generator model for DCGAN.
    Takes a latent noise vector and generates an image.
    """
    def __init__(self, latent_dim, img_shape, ngf=64):
        super().__init__()
        channels, img_h, img_w = img_shape
        self.latent_dim = latent_dim
        self.img_shape = img_shape
        self.ngf = ngf # number of generator filters
        
        self.init_size = img_h // 4 # base on 2 upsamples
        
        self.output_feartures = ngf * 4
        self.fc = nn.Linear(latent_dim, self.output_feartures * self.init_size * self.init_size)

        self.conv_block = nn.Sequential(
            # Input after fc and reshape: (linear_output_features, init_size, init_size) e.g., (ngf*4, 8, 8)

            # Block 1: 8x8 -> 16x16 spatial
            # Output channels: ngf * 2
            nn.Upsample(scale_factor=2), 
            nn.Conv2d(128, 128, kernel_size=3, padding=1), # Conv to refine features after upsampling
            # instead, we can use convTranpose:
            # nn.ConvTranspose2d(self.initial_features, 128, kernel_size=4, stride=2, padding=1)
            # guess why kernel_size = 4 (?)
            nn.BatchNorm2d(ngf * 2),
            nn.LeakyReLU(0.2, inplace=True),

            # Block 2: 16x16 -> 32x32 spatial
            # Output channels: ngf
            nn.ConvTranspose2d(ngf * 2, ngf, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(inplace=True),

            # Final layer: 32x32 spatial, output channels
            # Standard: ConvTranspose -> Tanh, no BatchNorm/ReLU
            nn.ConvTranspose2d(ngf, channels, kernel_size=3, stride=1, padding=1, bias=False), # Using 3x3 k, s=1, p=1 to match user's final layer handling for 32x32
            nn.Tanh() # Output pixel values in [-1, 1] range
        )

    def forward(self, z):
        # Project latent vector to initial feature map size
        x = self.fc(z)
        # Reshape to (batch_size, features, height, width)
        x = x.view(x.shape[0], self.output_features, self.init_size, self.init_size)

        # Apply convolutional blocks
        img = self.conv_blocks(x)
        return img
    

class DCGAN_Discriminator(nn.Module):
    """
    Discriminator model for DCGAN.
    Takes an image and outputs a probability (real or fake).
    """
    def __init__(self, img_shape, ndf=64):
        super().__init__()
        channels, img_h, img_w = img_shape
        self.img_shape = img_shape
        self.ndf = ndf

        # 32 -> 16 -> 8 -> 4 -> 2
        self.final_conv_size = img_h // (2**4) # Assuming square image and consistent strides

        self.main = nn.Sequential(
            # Input: (channels, img_h, img_w) e.g., (1, 32, 32)

            # Block 1: 32x32 -> 16x16 spatial. Output channels: ndf. No BatchNorm.
            # Standard DCGAN uses k=4, s=2, p=1.
            nn.Conv2d(channels, ndf, kernel_size=4, stride=2, padding=1),
            nn.LeakyReLU(0.2, inplace=True),

            # Block 2: 16x16 -> 8x8
            nn.Conv2d(ndf, ndf * 2, kernel_size=4, stride=2, padding=1), 
            nn.BatchNorm2d(ndf * 2), # BatchNorm after Conv+Activation
            nn.LeakyReLU(0.2, inplace=True),

            # Block 3: 8x8 -> 4x4
            nn.Conv2d(ndf * 2, ndf * 4, kernel_size=4, stride=2, padding=1), 
            nn.BatchNorm2d(ndf * 4),
            nn.LeakyReLU(0.2, inplace=True),

            # Block 4: 4x4 -> 2x2
            nn.Conv2d(ndf * 4, ndf * 8, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ndf * 8),
            nn.LeakyReLU(0.2, inplace=True),
        )

        self.adv_layer = nn.Sequential(
            nn.Linear(ndf * 8 * self.final_conv_size * self.final_conv_size, 1), # Flattened size: ndf*8 * 2 * 2
            nn.Sigmoid() # Output probability between 0 and 1
        )

    def forward(self, img):
        # Pass image through convolutional blocks
        x = self.main(img)
        # Flatten the output for the linear layer
        x = x.view(x.size(0), -1)
        # Pass through the adversarial layer
        validity = self.adv_layer(x)
        return validity