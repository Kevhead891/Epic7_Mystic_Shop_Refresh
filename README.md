# E7-Auto-Shop-Refresh

Original : https://github.com/EmaOlay/E7-Auto-Shop-Refresh <br>

## Disclaimer

<p>SmileGate's terms of service state that macros are a bannable offense. That being said, I have played since day 1 and have used macros before to automate quests and have yet to be banned. I have also used macros in Arknights since day 1 and have yet to be banned. Use at your own risk even if there is a good chance that you won't get banned because the probability is not 0%. <p>

## Requirements :

- You will need python 3.6+
- You will need to install the modules listed in requirements.txt

## Specs For Execution

- I used LDPlayer with resolution 1600x900
- My personal Screen Resolution is set to 1920x1080

## How to Run

- In command prompt

```Command prompt

python .\diretory_path_to_python_file

```

- Or using VSCode or Pycharm just hit the run/ run in terminal

## Changelog differences vs EmaOlay

### _Classes_

<p>I created a class to make it easier for me to organize the code. <p>

- Created a class for the refresher
- Split up the actions into methods : Initialize, Scan, Drag, and Refresh
- This allowed me to save some time as Ema's code would swipe an extra time because of the contador value.

### _Confidence Parameters_

- Added Confidence Parameters = 0.9 to all of the image locate functions, that way I don't have to take my own screenshots. Just adjust this value if the script is not scanning correctly.

### _Buying Bookmarks_

- Noticed in the christmas event that the background would mess with the image recognition regardless of confidence value.
- Opted to Hardcode based off the relative coordinates obtained from pyautogui center function.
- This could cause issues if your monitor resolution is smaller/bigger so you may have to tweak these.

```python
pyautogui.click(x= round(1.9 * Coven_point[0]), y= round(Coven_point[1] + 30), clicks=2, interval=0.05, button='left')
```

![Logo](.\readme_pic1.PNG)

### TLDR

- Organized it into classes and reduced script execution time.
- Reduced the reliance on having to take your own screenshots by adding confidence parameter.

## Closing Statements

This code is free to be used and modified. If you can improve upon this code please send me a link as I wish to improve.
