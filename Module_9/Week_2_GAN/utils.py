import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import os
import numpy as np
import matplotlib.pyplot as plt
from torchvision.utils import make_grid

# --- Dataset Loading ---
def get_device():
    """Returns the appropriate device (cuda or gpu)"""
    return "cuda" if torch.cuda.is_available() else "cpu"

# --- Dataset Loading ---
def get_mnist_dataloader(root_dir = 'mnist_data', img_size = 32, batch_size = 64, shuffle = True):
    """
    Loads the MNIST dataset and returns a DataLoader.

    Args:
        root_dir (str): Directory to save/load MNIST data.
        img_size (int): Desired size for image resizing.
        batch_size (int): Batch size for the dataloader.
        shuffle (bool): Whether to shuffle the dataset.

    Returns:
        torch.utils.data.DataLoader: The MNIST dataloader.
    """
    transform = transforms.Compose([
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5], std=[0.5])
    ])

    dataset = torchvision.datasets.MNIST(
        root=root_dir,
        train=True,
        download=True,
        transform=transform
    )
    
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle
    )
    return dataloader

# --- Directory Creation ---
def create_dir(path):
    """Creates a directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)

# --- Inference Plotting (for Conditional GANs) ---
def plot_conditional_generations(generator, latent_dim, num_classes, num_sample=5, device="cpu", save_path=None):
    """
    Generates and plots images for each class using a conditional generator.

    Args:
        generator (nn.Module): The trained conditional generator model.
        latent_dim (int): The dimension of the latent noise vector.
        num_classes (int): The number of classes.
        num_sample (int): The number of samples to generate per class.
        device (str): The device to run inference on ('cuda' or 'cpu').
        save_path (str, optional): Path to save the plot. If None, shows the plot.
    """
    pass