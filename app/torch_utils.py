import io
import torch
import torch.nn
import torchvision.transforms as transforms
from PIL import Image


def transform_image(image_bytes):
    transform = transforms.Compose([
        transforms.Grayscale(3),
        transforms.Resize(256),
        transforms.CenterCrop((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize((0.5395,), (0.3075,))
    ])
    image = Image.open(io.BytesIO(image_bytes))
    return torch.unsqueeze(transform(image), 0)


def predict_class(tensor):
    model = torch.load('app/duce-nonduce-model.pth')
    model.eval()
    labels = ["Duce", "Non Duce"]
    outputs = model(tensor)
    _, predicted = torch.max(outputs, 1)
    return labels[predicted]
