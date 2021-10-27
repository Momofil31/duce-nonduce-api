# Duce-Non Duce API

Inspired by the great TV show game "Duce/Non Duce" invented by the italian comedian Valerio Lundini, this API classifies a provided image as Duce or Non Duce.

It uses a Binary Classifier built with PyTorch (Resnet18) and trained on a dataset composed of 237 images of Benito Mussolini (aka The Duce) and other common objects, animals, people and landscapes.
[Here](https://colab.research.google.com/drive/1zq6u_23rIQRTmiAAA1TeZo2q1J-iE4i0?usp=sharing) the colab notebook used to train the model.

## How to use (under construction)

The API receives and HTTP POST request and respond with a JSON object in a restful fashion.

This is the API URL: [duce-non-duce-api.herokuapp.com](duce-non-duce-api.herokuapp.com)

The request should be of type `form-data` and contain a field named `file` with the image you want to classify. The image should be `.jpg`, `.png` or `.jpeg`.

The response is a JSON string as the following format:

`{ "prediction": "Duce" }` or `{ "prediction": "Non Duce" }`

If an error occurs the response is as the following:

`{ "error": "prediction failed" }`

Possible error codes are:

- `prediction failed`
- `format not supported`

## How to run on your machine (under construction)

To run locally:

1. Create and activate a python virtual environment

   `python3 -m venv venv`

   `source venv/bin/activate` (On macOS & Linux)

   `venv\bin\activate.bat` (On windows)

2. Install required modules via `pip`

   `pip3 install -r requirements.txt`

3. Run the app on localhost

   `cd app`
   `flask run`
