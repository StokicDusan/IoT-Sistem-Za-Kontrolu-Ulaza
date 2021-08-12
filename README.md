# Azure IoT Edge system for access control using Custom Vision

This is a project showing how to deploy a Custom Vision model to a Raspberry Pi 3 device running Azure IoT Edge. The project uses Custom Vision model for facial recognition and controls a relay module which can be used as a switch opening an automatic door.

## Prerequisites

### Hardware
You can run this solution using the following hardware:

- **Raspberry Pi 3**: Set up Azure IoT Edge on a Raspberry Pi 3,  

- **USB Camera**: Connect a camera on a Raspberry Pi 3 USB port,  

- **Electronics Components**: Most of what you needed for this solution can be found in the [SparkFun Inventor's Kit](https://www.sparkfun.com/products/15267) which includes:
  * Solderless Breadboard,
  * Ultrasonic Distance Sensor,
  * Relay module,
  * Jumper Wires,
  * Red, Green and Yellow LED,
  * 3x 220Ω, 1x 1kΩ and 1x 2kΩ resistor.  

### Services
You must have the following services set up to use this solution:
- **Azure IoT Hub**: This is your Cloud gateway which is needed to manage your IoT Edge devices. All deployments to Edge devices are made through an IoT Hub. You can use the free sku for this sample.
- **Azure Container Registry**: This is where you host your containers (e.g. IoT Edge modules). Deployment manifests refer to this container registry for the IoT Edge devices to download their images.You can use the free sku for this sample.
- **Stream Analytics Job**: This is where you host your containers (e.g. IoT Edge modules). Deployment manifests refer to this container registry for the IoT Edge devices to download their images.You can use the free sku for this sample.
- **Azure Storage Acoount**: This is where you host your containers (e.g. IoT Edge modules). Deployment manifests refer to this container registry for the IoT Edge devices to download their images.You can use the free sku for this sample.


![IoT Edge deployment workflow](assets/IoTEdgeDeployment.gif)

### Tooling
You need the following dev tools to do IoT Edge development in general, to make this sample run and edit it:
- **Visual Studio Code**: IoT Edge development environment. [Download it from here](https://code.visualstudio.com/).
- **Visual Studio Code: Azure IoT Edge Extension**: An extension that connects to your IoT Hub and lets you manage your IoT Devices and IoT Edge Devices right from VS Code. A must-have for IoT Edge development. [Download it from here](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-edge). Once installed, connect it to your IoT Hub.

To learn more about this development environment, check out [this tutorial](https://docs.microsoft.com/en-us/azure/iot-edge/how-to-deploy-modules-vscode) and [this video](https://www.youtube.com/watch?v=C5eTQ1cwlLk&t=1s&index=35&list=PLlrxD0HtieHh5_pOv-6xsMxS3URD6XD52):

[![Visual Studio Code Extension Video](assets/VSCodeExtensionVideo.png)](https://www.youtube.com/watch?v=C5eTQ1cwlLk&t=1s&index=35&list=PLlrxD0HtieHh5_pOv-6xsMxS3URD6XD52)


## Description of the solution
### Modules
This solution is made of 3 modules:

- **Camera capture** - this module captures the video stream from a USB camera, sends the frames for analysis to the custom vision module and shares the output of this analysis to the edgeHub. This module is written in python and uses [OpenCV](https://opencv.org/) to read the video feed.
- **Custom vision** - it is a web service over HTTP running locally that takes in images and classifies them based on a custom model built via the [Custom Vision website](https://azure.microsoft.com/en-us/services/cognitive-services/custom-vision-service/). This module has been exported from the Custom Vision website and slightly modified to run on a ARM architecture. You can modify it by updating the model.pb and label.txt files to update the model.
- **SenseHat display** - this module gets messages from the edgeHub and blinks the raspberry Pi's senseHat according to the tags specified in the inputs messages. This module is written in python and requires a [SenseHat](https://www.raspberrypi.org/products/sense-hat/) to work. The amd64 template does not include this module since it is a raspberry pi only device.

### Communication between modules
This is how the above three modules communicate between themselves and with the cloud:

![Communication patterns between modules](assets/CommunicationPatterns.png)

## Get started
### To deploy the solution on a Raspberry Pi 3
From your mac or PC:
1. Clone this sample
2. Update the `.env` file with the values for your container registry and make sure that your docker engine has access to it
3. Build the entire solution by right-clicking on the `deployment.template.json` file and select `Build and push IoT Edge Solution` (this can take a while...especially to build open-cv, numpy and pillow...)
4. Deploy the solution to your device by right-clicking on the `config/deployment.json` file, select `Create Deployment for Single device` and choose your targeted device
5. Monitor the messages being sent to the Cloud by right-clicking on your device from the VS Code IoT Edge Extension and select `Start Monitoring D2C Message`.

### To deploy the solution on an x64 PC
From your mac or
1. Clone this sample
2. Update the `.env` file with the values for your container registry and make sure that your docker engine has access to it
3. Build the entire solution by opening the control palette (Ctrl+Shift+P), select `Build and push IoT Edge Solution` (this can take a while...especially to build numpy and pillow...) and select the `deployment.test-amd64.template.json` manifest file (it includes a test video file to simulate a camera)
4. Deploy the solution to your device by right-clicking on the `config/deployment.json` file, select `Create Deployment for Single device` and choose your targeted device
5. Monitor the messages being sent to the Cloud by right-clicking on your device from the VS Code IoT Edge Extension and select `Start Monitoring D2C Message` 

Note: To stop Device to Cloud (D2C) monitoring, use the `Azure IoT Hub: Stop monitoring D2C messages` command from the Command Palette (Ctrl+Shift+P).

## Going further
### Update the AI model
Download your own custom vision model from the custom vision service. You just need to replace the `ImageClassifierService/app/model.pb` and `ImageClassifierService/app/labels.txt` provided by the export feature of Custom Vision. 
### Update the configuration of the camera capture module
Explore the various [configuration options of the camera module](https://github.com/Azure-Samples/Custom-vision-service-iot-edge-raspberry-pi/tree/master/modules/CameraCapture), to score your ai model against a camera feed vs a video clip, to resize your images, to see logs, etc.
