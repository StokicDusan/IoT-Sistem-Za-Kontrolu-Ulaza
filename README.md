[![Downloads][downloads-shield]][downloads-url]
[![Contributors][contributors-shield]][contributors-url]
[![Commit-activity][commit-activity-shield]][commit-activity-url]
[![Issues][issues-shield]][issues-url]
[![Repo-size][repo-size-shield]][repo-size-url]
[![License][license-shield]][license-url]  
[![Forks][forks-shield]][forks-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Azure IoT Edge system for access control using Custom Vision

This is a project showing how to deploy a solution with Custom Vision AI model to a Raspberry Pi 3 device running Azure IoT Edge. The project uses Custom Vision model for facial recognition and controls a relay module which can be used as a switch opening an automatic door. Apart from controlling access, the solution logs people who got granted access.

This project was initiated as a Bachelor thesis at the School of Electrical Engineering (ETF), University of Belgrade.

## Prerequisites

### Hardware
You can run this solution using the following hardware:

- **Raspberry Pi 3**: Set up Azure IoT Edge on a Raspberry Pi 3,

- **USB Camera**: Connect a camera on a Raspberry Pi 3 USB port,

- **Electronics Components**: Most of what you needed for this solution can be found in the [SparkFun Inventor's Kit][spark-fun-kit-url] which includes:
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
- **Visual Studio Code**: IoT Edge development environment. [Download it from here][vscode-url].
- **Visual Studio Code: Azure IoT Edge Extension**: This extension connects to your IoT Hub and lets you manage your IoT Devices and IoT Edge Devices from VS Code. [Download it from here][azure-extention-url]. Once installed, connect it to your IoT Hub.

## Get started
### To deploy the solution
1. Clone this solution, download zip or the latest [release][release-url],
2. Update the `.env` file with the values for your container registry and make sure that your docker engine has access to it,
3. Build the entire solution by right-clicking on the `deployment.template.json` file and select `Build and push IoT Edge Solution`,
4. Deploy the solution to your device by right-clicking on the `config/deployment.json` file, select `Create Deployment for Single device` and choose your targeted device.
5. Test out the solution!!!  
![greenLED][green-led-gif]  ![redLED][red-led-gif]  

You can find a more comprehensive guide on how to deploy the solution in the [guide][guide-path] directory.

## Provide Feedback 👍
If you encounter any bugs or have suggestions, please file an issue in the [Issues][issues-url] section of the project.

## Big Thanks! 🚀
This solution was heavily influenced by [this][azure-sample-url] Azure-Samples solution. Big love to them for inspiring me to build this soluton.

[green-led-gif]: https://media.giphy.com/media/lZbDOeIHhEeLHcPFfs/giphy-downsized-large.gif
[red-led-gif]: https://media.giphy.com/media/rZxUgucFatEhH0cOLx/giphy-downsized-large.gif
[guide-path]: https://github.com/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza/tree/master/guide
[azure-sample-url]: https://github.com/Azure-Samples/Custom-vision-service-iot-edge-raspberry-pi
[vscode-url]: https://code.visualstudio.com/
[azure-extention-url]: https://marketplace.visualstudio.com/items?itemName=vsciot-vscode.azure-iot-edge
[spark-fun-kit-url]: https://www.sparkfun.com/products/15267
[release-url]: https://github.com/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza/releases
[downloads-shield]: https://img.shields.io/github/downloads/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza/total 
[downloads-url]: https://github.com/StokicDusan/IoT-Sistem-Za-Kontrolu-Ulaza/releases
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
