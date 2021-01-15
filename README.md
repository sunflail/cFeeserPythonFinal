# cFeeserPythonFinal
final Python project

* Clone the repo
* Create a .env in the same directory
* Add the key: NASA_API=your-api-key-here

# Usage
Very simple tKinter example that will run any of the included python files when the name of the module is typed into the entry field and the run me button pressed.

Included:
* apod - Nasa Pic of Day, will add the image to the tkinter window
* astroapi - Nasa astronauts in space, courtesy of open-notify.org
* calculator - basic calculator, will run in terminal and result sent back to tkinter
* nasaapis - Various NASA api calls, please read the script for more information
* roverpics.txt - example file of data generated during the nasaapis script
* settings - file related to dotenv
* tkinterLearning - main script

Should support running any other scripts with minimal modification. Simply add them to the same folder, add the name to the module import list in tkinterLearning, and make sure that it returns something in a string format.
