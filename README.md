# Python Projects Collection

A collection of practical Python applications built with Tkinter GUI and computer vision capabilities. Each project is designed to be simple, functional, and educational.

## 🚀 Projects

### 1. [Language Translator](language-translator/)
A desktop application that translates text between multiple languages using a clean GUI interface.

**Features:**
- Translate between English, German, French, and Spanish
- Simple and intuitive user interface
- Real-time translation using the `translate` library

**Tech Stack:** Python, Tkinter, translate library

### 2. [Currency Converter](currency-converter/)
A real-time currency converter that uses live forex exchange rates to convert between different currencies.

**Features:**
- Support for major currencies (USD, EUR, GBP, JPY, CHF, TRY)
- Custom ISO code input for any currency
- Real-time exchange rates from forex-python
- Error handling with user-friendly messages

**Tech Stack:** Python, Tkinter, forex-python

### 3. [Countdown Timer](countdown-timer/)
A desktop countdown timer application with a graphical interface for setting time intervals.

**Features:**
- Set hours, minutes, and seconds using sliders
- Visual countdown display
- Start, stop, and reset functionality
- Alert notification when timer completes

**Tech Stack:** Python, Tkinter

### 4. [Realtime Object Detection](realtime-object-detection/)
A computer vision application that detects objects in real-time video streams using OpenCV and pre-trained models.

**Features:**
- Real-time object detection from video files or webcam
- Uses SSD MobileNet V3 model for fast processing
- CPU-based processing (no GPU required)
- Support for COCO dataset classes
- Bounding box visualization with confidence scores

**Tech Stack:** Python, OpenCV, NumPy

## 📋 Requirements

Each project has its own `requirements.txt` file with specific dependencies. See individual project directories for detailed requirements.

**General Requirements:**
- Python 3.10.4 or higher
- Tkinter (usually comes with Python)
- Internet connection (for language translator and currency converter)

## 🛠️ Installation

### Option 1: Install All Projects
```bash
# Clone the repository
git clone <repository-url>
cd py-projects

# Install dependencies for each project
cd language-translator && pip install -r requirements.txt
cd ../currency-converter && pip install -r requirements.txt
cd ../countdown-timer && pip install -r requirements.txt
cd ../realtime-object-detection && pip install -r requirements.txt
```

### Option 2: Install Individual Projects
Navigate to any project directory and install its dependencies:
```bash
cd <project-name>
pip install -r requirements.txt
python main.py
```

## 🎯 Usage

Each project can be run independently:

```bash
# Language Translator
cd language-translator
python main.py

# Currency Converter
cd currency-converter
python main.py

# Countdown Timer
cd countdown-timer
python main.py

# Realtime Object Detection
cd realtime-object-detection
python main.py
```

## 📁 Project Structure

```
py-projects/
├── language-translator/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── currency-converter/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── countdown-timer/
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
├── realtime-object-detection/
│   ├── main.py
│   ├── Detector.py
│   ├── requirements.txt
│   ├── README.md
│   ├── model_data/
│   └── videos/
└── README.md
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
