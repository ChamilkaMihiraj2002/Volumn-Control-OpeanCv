# Hand Tracking Volume Control

This project uses hand tracking to control system volume based on the distance between two specific hand landmarks (thumb and index finger). The project leverages OpenCV, Mediapipe, and Pycaw for video capture, hand landmark detection, and audio volume control, respectively.

## Features
- Real-time hand detection and tracking.
- Volume control by adjusting the distance between thumb and index finger.
- Visual feedback using OpenCV to show the hand landmarks and volume percentage.
- Volume bar displayed on the screen for real-time updates.

## Demo

### Hand Detection and Tracking
<img src="demo.gif" alt="Hand Tracking Demo" width="500">

### Volume Control Interface
- Thumb and index finger distance controls the system volume.
- Volume is visualized with a bar and percentage on the screen.

## Requirements

To run the project, you need the following libraries:

- OpenCV
- Mediapipe
- Pycaw
- NumPy
- comtypes

Install them using pip:

```bash
pip install opencv-python mediapipe numpy comtypes pycaw
```

## Setup and Execution

1. Clone the repository:

```bash
git clone [https://github.com/yourusername/hand-tracking-volume-control.git](https://github.com/ChamilkaMihiraj2002/Volumn-Control-OpeanCv.git)
cd hand-tracking-volume-control
```

2. Run the project:

```bash
python volume_control.py
```

## Code Breakdown

### HandTrackingModule

The `HandTrackingModule.py` file contains a class `handDetector`, which handles hand detection and tracking using Mediapipe. The `findHands()` method detects hands in the video feed and optionally draws the hand landmarks on the frame.

```python
import cv2
import mediapipe as mp
import time
```

### Volume Control

The `volume_control.py` file integrates the hand detection with Pycaw to control system audio volume. By measuring the distance between the thumb and index finger, the system volume is adjusted accordingly.

```python
import cv2
import numpy as np
import math
from HandTrackingModule import handDetector
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
```

### Visual Feedback

- A circle is drawn on both the thumb and index finger, and a line is drawn between them.
- The distance between these two fingers determines the system volume.
- A volume bar and percentage are displayed on the screen to provide feedback.

### FPS

Frames per second (FPS) are calculated and displayed to ensure smooth real-time performance.

## Future Improvements
- Add gesture recognition for more advanced controls (e.g., mute/unmute).
- Improve accuracy and performance in low-light conditions.

## License

This project is licensed under the MIT License.

---
