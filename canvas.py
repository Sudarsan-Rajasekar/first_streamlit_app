import streamlit as st
import sys
import pandas as pd
import numpy as np
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import pickle
import random

st.write("Draw any digit in the Canvas..(0 to 9)")
canvas_img = st_canvas(
        fill_color="rgba(255, 165, 0, 0.5)",  # Fixed fill color with some opacity
        stroke_width=8,
        background_color="rgba(255, 255, 255)",
        # background_image=Image.open(bg_image) if bg_image else None,
        # update_streamlit=realtime_update,
        height=28*5,
        width=28*5
        # drawing_mode=drawing_mode,
        # point_display_radius=point_display_radius if drawing_mode == "point" else 0,
        # key="full_app",
    )
img_arr = canvas_img.image_data
# st.write(img_arr.shape)

# Define the CNN model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv_layers = nn.Sequential(
            nn.Conv2d(1, 8, kernel_size=3, stride=1, padding=1),
            nn.Conv2d(8, 16, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Dropout(0.25),
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        self.fc_layers = nn.Sequential(
            nn.Linear(64 * 7 * 7, 128),
            nn.ReLU(),
            nn.Dropout(0.25),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = x.view(x.size(0), -1)
        x = self.fc_layers(x)
        return x
    
# Load the trained model from the pickle file
model_filename = 'my_model.pkl'
with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

# Create an instance of the model
model = Net()

# Load the trained model's state_dict into the instance
model.load_state_dict(loaded_model.state_dict())

# Set the model to evaluation mode
model.eval()


img = Image.fromarray(img_arr)
img = img.resize((28,28))
img = img.convert('L')

# st_canvas(background_image=img ,height=28*5,
#         width=28*5)



# Convert the image to a tensor and apply normalization
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # Normalize to range [-1, 1]
])
img_tensor = transform(img).unsqueeze(0)
img_tensor = 1-img_tensor
# st.write(img_tensor)

emojis = ['🎈','🎁','🐠','👗','🍉','🏈','🍫','🍅','🛴','🍏','🍓','🥕','🍄']

with torch.no_grad():
    pred = model(img_tensor)
    # st.write(pred.detach().numpy())
    arr = nn.Softmax()(pred)
    arr = arr.detach().numpy()
    digit = np.argmax(pred)
    st.write("")
    st.write(f"<h1 style='color: purple;'>Predicted Digit: {digit}</h1>", unsafe_allow_html=True)
    emoji = random.choice(emojis)
    st.write(f"<h3 style='color: purple;'>{emoji*digit}</h3>", unsafe_allow_html=True)

