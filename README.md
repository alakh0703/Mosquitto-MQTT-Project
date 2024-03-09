# Mosquitto Project

This project uses Mosquitto, an open source MQTT broker, to send data from a publisher to a subscriber using the concept of IoTs.

## MQTT

MQTT (Message Queuing Telemetry Transport) is a lightweight publish/subscribe messaging protocol designed for low bandwidth, high latency, or unreliable networks². It is commonly used for IoT applications, where devices communicate with each other or with a server.

## Mosquitto

Mosquitto is an open source implementation of a server for version 5.0, 3.1.1, and 3.1 of the MQTT protocol³. It is easy to install and use, and supports various platforms, such as Windows, Linux, MacOS, and more.

## Installation

To install and run Mosquitto on Windows, follow these step-by-step instructions:

- Download Mosquitto for Windows from the official Mosquitto website⁴.
- Run the installer and follow the wizard.
- Ensure the "Start Mosquitto Broker" option is checked at the end of the installation.
- Open a Command Prompt and navigate to the Mosquitto directory (optional).
- Run the command `mosquitto` to start the Mosquitto broker.

## Usage

To use the Mosquitto project, you need to have two Command Prompt windows open: one for the publisher and one for the subscriber.

- In the publisher window, run the command `mosquitto_pub -t test -m "Hello world"` to publish a message "Hello world" to the topic "test".
- In the subscriber window, run the command `mosquitto_sub -t test` to subscribe to the topic "test" and receive the message.
- You should see the message "Hello world" appear in the subscriber window.

You can also use different topics, messages, and options for the mosquitto_pub and mosquitto_sub commands. For more details, you can refer to the Mosquitto documentation³ or the Mosquitto man pages⁵.


## Contact

If you have any questions or feedback, please contact me.
