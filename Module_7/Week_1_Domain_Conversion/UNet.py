import torch
import torch.nn as nn

# Conv2d -> BN -> ReLU
class ConvBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.conv_block = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1, bias=False),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        x = self.conv_block(x)
        return x
    
# Down-Sample
class Encoder(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.MaxPool2d(2),
            ConvBlock(in_channels, out_channels)
        )

    def forward(self, x):
        x = self.encoder(x)
        return x
    
# Up-sample
class Decoder(nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(in_channels, out_channels, kernel_size=4, stride=2, padding=1, bias=False)
        )
        self.conv_block = ConvBlock(in_channels, out_channels)

    def forward(self, x1, x2):
        x1 = self.decoder(x1)
        x = torch.cat([x1, x2], dim=1) # skip connection
        x = self.conv_block(x)
        return x
    
class UNet(nn.Module):
    def __init__(self, n_channels, n_classes):
        super().__init__()
        self.n_channels = n_channels
        self.n_classes = n_classes

        self.in_conv = ConvBlock(n_channels, 64)

        self.enc_1 = Encoder(64, 128)
        self.enc_2 = Encoder(128, 256)
        self.enc_3 = Encoder(256, 512)
        self.enc_4 = Encoder(512, 1024)

        self.dec_1 = Decoder(1024, 512)
        self.dec_2 = Decoder(512, 256)
        self.dec_3 = Decoder(256, 128)
        self.dec_4 = Decoder(128, 64)

        self.out_conv = ConvBlock(64, n_classes)

    def forward(self, x):
        x1 = self.in_conv(x)
        print(f'Shape Input Conv: {x1.shape}')
        x2 = self.enc_1(x1)
        print(f'Shape Encoder 1: {x2.shape}')
        x3 = self.enc_2(x2)
        print(f'Shape Encoder 2: {x3.shape}')
        x4 = self.enc_3(x3)
        print(f'Shape Encoder 3: {x4.shape}')
        x5 = self.enc_4(x4)
        print(f'Shape Encoder 4: {x5.shape}')

        x = self.dec_1(x5, x4)
        print(f'Shape Decoder 1: {x.shape}')
        x = self.dec_2(x, x3)
        print(f'Shape Decoder 2: {x.shape}')
        x = self.dec_3(x, x2)
        print(f'Shape Decoder 3: {x.shape}')
        x = self.dec_4(x, x1)
        print(f'Shape Decoder 4: {x.shape}')

        x = self.out_conv(x)
        print(f'Shape Output decoder: {x.shape}')

        return x
