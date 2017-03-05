### README

#### Basic Requirements

* Synaptics Fingerprint Sensor Development Kit
* SourceAFIS API
* Xamarin Studio/C# IDE
* ngrok server
* PHP 5+
* JDK 1.8
* Twilio console

#### Usage

1. Clone StealthApp from Github
2. Using the Synaptics development kit, generate 3 images from 3 distinct fingers. Large fingers work best. Rename the files (found in C:\Images) to 2L.bmp, 3L.bmp, and 4L.bmp.
3. Set up the PHP webserver by running "php -S localhost:8000", and run "ngrok http 8000" to connect the webserver to the internet.
4. Configure a TwiML App in the Twilio console (All Products and Services -> Phone Numbers -> Tools -> TwiML Apps) so that the voice URL is the ngrok URL.
5. Open the C# file (Program.cs) and configure the arguments:
  * DIR, JAVA_DIR, and STATUS_DIR should be the directory in which StealthApp is in.
  * ACCOUNT_SID, AUTH_TOKEN, and APP_ID can be found in the Twilio Console. APP_ID is found where the TwiML Apps are configured.
  * HARDWARE_URL is the url of the URL of the hardware that receives the IOT data.
  * FROM_NUMBER, TO_NUMBER, and EMERGENCY represent the Twilio number, user's number, and the emergency numbers respectively.
6. Launch Synaptics Fingerprint Manager, and leave it running in the background.
7. Run the StealthApp from Xamarin/your C# IDE.
8. Using the Synaptics development kit, press a finger onto the sensor.
9. Depending on the finger provided, the app will either call the emergency number, send the user a message, or activate the IoT device.
