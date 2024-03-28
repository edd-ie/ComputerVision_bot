# [PyBot](https://github.com/edd-ie/ComputerVision_bot)

Simple python image matching application

## Table of Contents

1. [Getting started](#Getting-started)
2. [Usage](#Usage)
4. [Contributors](#contributors)
5. [Licenses](#license)
6. [Resources](#Sources)

## <a id="Getting-started">Getting started</a>
### Cloning

**Clone** the project files to your local repository:

- HTTPS => `https://github.com/ComputerVision_bot.git`
- SSH => `git@github.com:edd-ie/ComputerVision_bot.git`
- Git CLI => `gh repo clone edd-ie/ComputerVision_bot`

Open the terminal and Navigate to the clone project folder:

Run: 
```bash
pip install -r requirements.txt
```

## <a id="Usage">Usage</a>

Navigate to the ```Test.py``` file

Comment out line 18 i.e 
```shot.findPos('Images/hazard.jpg', "rectangle", 0.85, method='win')  # pygui, pil, win```

Run in the terminal :
```bash
python Test.py
```

This will print the list of windows and their addresses currently open in your pc.

Copy the window name you want to observe and paste in line 17 ```shot.__int__('here')```

From the selected window take a screenshot of the thing you want to locate and save it in the Images folder of the project.

Uncomment out line 18

Paste the image name in ```shot.findPos('Images/here.jpg'...```

Run: 
```bash
python Test.py
```


## <a id="contributors">Contributors</a>

This project was created by : [Edd.ie](https://github.com/edd-ie)

## <a id="license">Licenses</a>

The project is licensed under the [BSD 3-Clause "New" or "Revised" License](https://github.com/highlightjs/highlight.js/blob/main/LICENSE), thus redistribution and use in source and binary forms are permitted provided that the conditions are met

## <a id="sources">Resources</a>

The application uses knowledge applied from [OpenCV Object detection in games](https://teams.microsoft.com/l/message/19:420b382a-7013-4d80-9f8a-27f917335621_e1d506b2-ebc8-48a9-ad25-970522d2c3eb@unq.gbl.spaces/1711060020264?context=%7B%22contextType%22%3A%22chat%22%7D) Youtube playlist

[OpenCV](https://docs.opencv.org/4.9.0/) - Computer vision library