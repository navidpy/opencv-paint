# OpenCV Paint 🎨

A simple paint application built with Python using OpenCV, NumPy, and Matplotlib.
This project demonstrates how to create a basic drawing tool using mouse events.

## Features

- Freehand drawing using the mouse
- Real-time canvas rendering with OpenCV
- Image processing using NumPy
- Visualization support with Matplotlib
- Exit the application by pressing the ESC key
- Simple and beginner-friendly code structure

## Technologies Used

- Python 3
- OpenCV (cv2)
- NumPy
- Matplotlib

## Installation

1. Clone the repository:
```bash
git clone https://github.com/navidpy/opencv-paint.git
```

2. Navigate to the project directory:
```bash
cd opencv-paint
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application with:
```bash
python main.py
```

Use the mouse to draw on the canvas window.  
Press the **ESC** key to exit the application.

## Demo

![OpenCV Paint Demo](https://raw.githubusercontent.com/navidpy/opencv-paint/main/assets/demo.png)

## How It Works

- Mouse events are captured using OpenCV.
- Drawing is performed directly on a NumPy array.
- Matplotlib can be used to display or analyze the final output image.

## Future Improvements

- Brush size control
- Color selection
- Save drawing as an image file
- Add keyboard shortcuts
- Add shape drawing tools

## Contributing

Contributions are welcome.  
Please open an issue before submitting major changes.

## License

This project is licensed under the MIT License.

If you find this project useful, consider giving it a star ⭐
