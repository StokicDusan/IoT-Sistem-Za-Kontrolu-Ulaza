[![Contributors][contributors-shield]][contributors-url]
[![Commit-activity][commit-activity-shield]][commit-activity-url]
[![Issues][issues-shield]][issues-url]
[![Repo-size][repo-size-shield]][repo-size-url]
[![License][license-shield]][license-url]  
[![Forks][forks-shield]][forks-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

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

Wiring scheme can be seen in the image below:  

<img src="https://github.com/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza/blob/master/assets/sema_bb3_bb2.png" alt="scheme" align="center" width="90%" height="auto" />
<br/>

### Services
You must have the following services set up to use this solution:
- **Azure IoT Hub**: This is your Cloud gateway which is needed to manage your IoT Edge devices. All deployments to Edge devices are made through an IoT Hub. You can use the Free Standard tier for this solution.
- **Azure Container Registry**: This is where you host your containers (e.g. IoT Edge modules). Deployment manifests refer to this container registry for the IoT Edge devices to download their images. You can use the Basic tier for this solution.
- **Stream Analytics Job**: This is where your data is aggregated, filtered and outputted into a table in your Azure Storage Account. You can use the Standard tier for this solution.
- **Azure Storage Account**: This is where you store output form your Stream Analytics Job.

### Tooling
You need the following dev tools to do IoT Edge development in general, to make this solution run and edit it:
- **Visual Studio Code**: IoT Edge development environment. [Download it from here](https://code.visualstudio.com/).
- **Visual Studio Code: Azure IoT Edge Extension**: This extension connects to your IoT Hub and lets you manage your IoT Devices and IoT Edge Devices from VS Code. [Download it from here](https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-edge). Once installed, connect it to your IoT Hub.

## Get started
### To deploy the solution on a Raspberry Pi 3
From your mac or PC:
1. Clone this solution,
2. Update the `.env` file with the values for your container registry and make sure that your docker engine has access to it,
3. Build the entire solution by right-clicking on the `deployment.template.json` file and select `Build and push IoT Edge Solution`,
4. Deploy the solution to your device by right-clicking on the `config/deployment.json` file, select `Create Deployment for Single device` and choose your targeted device.
5. Test out the solution!!!  
![greenLED](https://giphy.com/gifs/led-iot-raspberry-pi-3-F6fwrkMoHZD1MUaINe) ![redLED](https://giphy.com/gifs/electronics-iot-raspberry-pi-3-rZxUgucFatEhH0cOLx)

You can find a more detailed guide on how to deploy the solution [here](https://github.com/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza/tree/master/guide).

## Big Thanks! 🚀
This solution was heavily influenced by [this](https://github.com/Azure-Samples/Custom-vision-service-iot-edge-raspberry-pi) Azure-Samples solution. Big love to them for inspiring me to build this soluton.

[contributors-shield]: https://img.shields.io/github/contributors/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza
[contributors-url]: https://github.com/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza?style=social
[forks-url]: https://github.com/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza/network/members
[issues-shield]: https://img.shields.io/github/issues/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza
[issues-url]: https://github.com/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza/issues
[commit-activity-shield]: https://img.shields.io/github/last-commit/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza
[commit-activity-url]: https://github.com/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza/graphs/commit-activity
[license-url]: https://github.com/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza/blob/master/LICENSE
[license-shield]: https://img.shields.io/github/license/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza
[repo-size-shield]: https://img.shields.io/github/repo-size/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza
[repo-size-url]: https://img.shields.io/github/repo-size/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=plastice&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/stokicdusan
