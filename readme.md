# Documentation for script

### Requirements

---

- Visual Studio Code (To run the code)
  - [link](https://code.visualstudio.com/download)
- I haven't tested this on windows so for now just assume it only works on mac
- google chrome (make sure you have your school account logged into a profile)
- python
  - [link](https://www.python.org/downloads/)

### Data Input

---

- In order to run the script, you need to populate a csv file with data, the easy way to do this is go into google sheets and put whatever information you want under the correct headers
  - You can leave things blank and it will leave it blank in the form
  - You can also have multiple rows and the script will submit multiple forms

### Steps to using the included google sheets template

---

- In order to use the template included in this zip, go to google sheets and create a new spreadsheet and press on file > open > upload > and take the template.csv file in this folder and drag it into the upload
- Google sheets should then open up a page like this with headings such as CL Name(s), Residential Area, etc.
  ![https://imgur.com/22gF2ko](https://imgur.com/22gF2ko)
- Fill out the template and download it as a csv (important)
  - drag the downloaded file into the directory that the automation script is saved in and rename the file to `walkThrough.csv`
    - Note: if you don't do this and rename it correctly, the script won't work
- For the Residential Apartment column, I only coded in `Newell Apartments` and `University Court Apartments` so far (make sure you put it exactly as I just spelt it in the column).
- I included a template of what it would look like when populated in `walkThroughExample.csv`

### Install the required packages

---

- Next, you need to install the required packages by doing `pip install -r requirements.txt` in the vscode terminal

### Running the script

---

- Before we run the script we need to make sure we are using a logged in profile (just to make the script easier to run)

  - If you're a masochist and want to go through the manual way, go for it
    - Just replace the username and password variables in `main()` with your google account and also follow the comments I left
    - After that, make sure you comment out `chrome_options.add_argument("--user-data-dir="+path)` at the top in the `setup()` function. (You can comment by just adding a `#` in front of the code)

- A much easier way to do this however is to simply go to `chrome://version` on your google chrome browser (using the chrome profile you want to use to fill out the form), copying the profile path

  - It should look like: /Users/{your username here}/Library /Application Support/Google/Chrome/Profile 1
  - After this, paste that into the `userPath` variable in `main()` (surrounded by `''`)

- Now we can run the script
  - You can do this by either right clicking anywhere when you are looking at the `walkthroughautomation.py` file and pressing run code, or by pressing the "play" button in the upper right corner of vscode
  - When the script is done, it should print `All Done!` in the output terminal
