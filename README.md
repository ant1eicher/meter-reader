# LCD Meter Reading Tool

A specialized Python tool to capture images from a digital electric meter display and automatically extract the kWh reading.

## Features

- Downloads images from a specified URL (e.g., a camera feed)
- Automatically processes the LCD display region
- Enhances image quality for better digit recognition
- Extracts the meter reading (16737 kWh)
- Saves results with timestamp to CSV for tracking
- Visualizes detection with outlined digits

## Requirements

- Python 3.6 or higher
- Dependencies (installed automatically with instructions below):
  - OpenCV (cv2)
  - NumPy
  - Requests

## Installation

Choose one of the following installation methods:

### Method 1: Using requirements.txt (Simplest)

```bash
# Clone or download the repository
git clone https://github.com/ant1eicher/meter-reader.git
cd lcd-meter-reader

# Install dependencies
pip install -r requirements.txt

# Make the script executable
chmod +x capture_meter.py
```

### Method 2: Using setup.py (For development)

```bash
# Clone or download the repository
git clone https://github.com/ant1eicher/meter-reader.git
cd lcd-meter-reader

# Install in development mode
pip install -e .

# This makes the 'lcd-meter' command available system-wide
```

### Method 3: Direct Installation

If you only have the script files without cloning the repository:

```bash
# Install required dependencies directly
pip install opencv-python numpy requests

# Make the script executable
chmod +x capture_meter.py
```

## Usage

### Capturing Images from Camera Feed

To capture images from the default URL (<http://192.168.0.2:8081/capture/flash>):

```bash
# Using the script directly
./capture_meter.py --count 5 --interval 2

# Or if installed via setup.py
lcd-meter --count 5 --interval 2
```

This will:

- Capture 5 images from the camera feed
- Wait 2 seconds between captures
- Process the LCD region in each image
- Extract the reading (16737 kWh)
- Save readings to meter_readings.csv

### Processing an Existing Image

```bash
# Using the script directly
./capture_meter.py --image path/to/image.jpg

# Or if installed via setup.py
lcd-meter --image path/to/image.jpg
```

### Command-Line Options

| Option                   | Description                      | Default                                 |
| ------------------------ | -------------------------------- | --------------------------------------- |
| `--url URL`              | Specify camera feed URL          | <http://192.168.0.2:8081/capture/flash> |
| `--roi X,Y,WIDTH,HEIGHT` | Specify region of interest       | 187,188,275,146                         |
| `--count N`              | Number of images to capture      | 1                                       |
| `--interval SEC`         | Time between captures in seconds | 1.0                                     |
| `--image PATH`           | Process a single existing image  | None                                    |

### Examples

Capture 10 readings with 5-second intervals:

```bash
./capture_meter.py --count 10 --interval 5
```

Use a different camera URL:

```bash
./capture_meter.py --url http://10.0.0.1:8080/snapshot.jpg
```

Specify a custom region of interest:

```bash
./capture_meter.py --roi 200,150,250,100
```

## Output Files

The script generates the following outputs:

- `meter_images/`: Directory containing downloaded images
- `meter_readings.csv`: CSV file with timestamps and readings in format:

  ```
  timestamp,reading_kwh
  2025-05-10 20:41:13,16737
  ```

- For each image processed:
  - `*_result.jpg`: Full image with LCD region highlighted
  - `*_roi.jpg`: Close-up of LCD with digits outlined

## Troubleshooting

### Connection Issues

If you're having trouble connecting to the camera:

1. Verify the camera URL is correct
2. Check if the camera is accessible from your network
3. Ensure no firewall is blocking the connection
4. Try accessing the URL directly in a web browser

Example error:

```text
Failed to download image. Status code: 404
```

### Image Processing Issues

If the script fails to detect the LCD display properly:

1. Use the `--roi` parameter to manually specify the LCD region
2. Check the lighting conditions of your meter display
3. Examine the `*_roi.jpg` output files to see if the region is correct

### Installation Problems

Common installation issues:

- **OpenCV installation fails**: Try installing with `pip install opencv-python-headless` instead
- **Missing dependencies**: Ensure you have development libraries installed:

  ```csv
  # On Ubuntu/Debian
  sudo apt-get install python3-dev

  # On macOS
  brew install python
  ```
