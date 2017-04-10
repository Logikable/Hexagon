### README

We sought to build a mobile app that can enable the user to discreetly and subtly execute specific, individual commands in potentially hostile situations using 1:N fingerprint recognition.

By calibrating HEXAGON with the user's fingerprints, the application can be configured to activate a unique function for each fingerprint. For HackTech 2017, we mapped and demoed the following three sample functions: auto-calling 911, auto-texting an emergency contact with user coordinates, and locking an IoT door.

#### Basic Requirements

* Synaptics Fingerprint Sensor Development Kit
* SourceAFIS API
* Xamarin Studio/C# IDE
* ngrok server
* PHP 5+
* JDK 1.8
* Twilio console
* Intel Edison
* Grove LCD screen
* Grove LED light

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
6. Setup and flash an Intel Edison, and connect it to wifi through SSH. Copy the IOT folder to the root directory, enter IOT, and run "node StealthIO.js" in the terminal to obtain the HARDWARE_URL. 
7. Launch Synaptics Fingerprint Manager, and leave it running in the background.
8. Run the StealthApp from Xamarin/your C# IDE.
9. Using the Synaptics development kit, press a finger onto the sensor.
10. Depending on the finger provided, the app will either call the emergency number, send the user a message, or activate the IoT device.
