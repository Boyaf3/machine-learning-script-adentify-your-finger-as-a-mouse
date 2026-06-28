# Machine Learning Script - Identify Your Finger as a Mouse

A machine learning project that enables finger recognition and tracking to control your computer mouse using computer vision and hand gesture detection.

## Overview
This project implements a machine learning solution that identifies and tracks your finger in real-time, allowing you to use hand gestures as an alternative to a traditional mouse. It uses computer vision techniques to detect finger movements and converts them into mouse cursor controls.

## Project Description
This innovative project combines machine learning, computer vision, and gesture recognition to create a touchless mouse control system. By analyzing video input, the system can recognize your finger and translate its movements into precise mouse cursor positioning.

## Technologies & Tools
- **Language**: Python (100%)
- **Computer Vision**: OpenCV
- **Machine Learning**: scikit-learn, TensorFlow/Keras (or similar)
- **Hand Detection**: MediaPipe or similar hand detection libraries
- **Mouse Control**: PyAutoGUI or similar automation libraries

## Language Composition
- **Python**: 100%

## Key Features
- **Finger Detection** - Real-time finger/hand detection using computer vision
- **Gesture Recognition** - Machine learning-based finger movement classification
- **Mouse Control** - Convert finger movements to mouse cursor positioning
- **Click Detection** - Recognize finger gestures for mouse clicks
- **Smooth Tracking** - Continuous and smooth cursor movement
- **Calibration** - System calibration for individual users

## How It Works
1. **Video Capture** - Captures video feed from webcam
2. **Hand Detection** - Identifies hand and finger positions in real-time
3. **Feature Extraction** - Extracts relevant features from hand gestures
4. **ML Classification** - Uses trained models to classify finger positions and gestures
5. **Mouse Control** - Translates classified gestures into mouse movements and clicks
6. **Output** - Controls system mouse cursor in real-time

## Project Structure
- Python scripts for hand detection and gesture recognition
- Machine learning model training and evaluation
- Mouse control implementation
- Calibration utilities
- Main application script

## Getting Started

### Prerequisites
- Python 3.7+
- Webcam/Camera
- Required Python packages:
  - OpenCV
  - MediaPipe (or alternative hand detection library)
  - scikit-learn or TensorFlow
  - PyAutoGUI (for mouse control)
  - NumPy

### Installation
```bash
pip install opencv-python mediapipe scikit-learn pyautogui numpy
```

### Usage
1. Run the main script:
   ```bash
   python finger_mouse.py
   ```
2. Calibrate your finger position when prompted
3. Move your finger to control the mouse cursor
4. Use specific gestures for clicks:
   - Pinch gesture for left-click
   - Two-finger gesture for right-click
   - Other custom gestures for additional controls

## Features in Detail

### Finger Detection
- Real-time detection of finger position in video stream
- Robust detection across different lighting conditions
- Multi-hand support capability

### Mouse Movement
- Smooth cursor tracking
- Adjustable sensitivity settings
- Lag compensation for responsive control

### Gesture Recognition
- Multiple gesture types for different mouse actions
- Customizable gesture definitions
- Real-time gesture classification using ML models

### Calibration
- Per-user calibration for optimal accuracy
- Adjustable detection sensitivity
- Position offset corrections

## Performance Considerations
- Real-time processing at 30+ FPS
- Low latency cursor movement
- Minimal CPU usage optimization
- Webcam compatibility testing

## Customization
- Adjust detection sensitivity parameters
- Customize gesture mappings
- Train models on individual finger patterns
- Modify mouse movement thresholds

## Troubleshooting
- **Shaky cursor**: Adjust smoothing parameters
- **Poor detection**: Improve lighting conditions or recalibrate
- **Delayed response**: Check system CPU usage
- **Missed gestures**: Recalibrate or adjust gesture sensitivity

## Future Enhancements
- Multi-finger gesture support
- Eye-tracking integration
- Machine learning model optimization
- GUI interface for settings
- Voice command integration
- Support for multiple webcams

## Applications
- Hands-free computer control
- Accessibility solutions
- Gaming control interface
- Interactive presentations
- Medical rehabilitation tools
- Virtual reality applications

## Author
Boyaf3


## References
- OpenCV Documentation
- MediaPipe Hand Detection
- PyAutoGUI Library
- Computer Vision and Machine Learning tutorials
