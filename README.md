# Qt Linux Deployment Script

## Overview

This script automates the process of deploying a Qt application on Linux. It ensures that the necessary Qt libraries and dependencies are included alongside the executable to enable successful execution on a target system without requiring Qt to be installed.

## Features

- **Automatic Library Detection**: Uses `ldd` to find required shared libraries.
- **Custom Qt Path Support**: Allows specifying different Qt versions and paths.
- **Dependency Copying**: Copies required Qt and OpenCV libraries.
- **Run Script Generation**: Creates a `run.sh` script to set up the environment and execute the application.

## Prerequisites

- **Qt Framework**: Installed in `~/Qt/<version>/gcc_64/`.
- **Executable File**: A compiled Qt application.
- **Python**: The script is written in Python and requires Python 3.

## Usage

### 1. Run the Deployment Script

```sh
python script_name.py <qt_version> <executable_path>
```

Example:
```sh
python deploy.py 5.15.2 ./my_qt_app
```

### 2. Execute the Application

Once the script completes, it generates a `run.sh` script to set up the environment and launch the application.

```sh
./run.sh
```

## How It Works

1. **Detects Qt Directory**: Checks if the specified Qt version exists in `~/Qt/`.
2. **Copies Required Libraries**:
   - Copies `lib` and `plugins` from the Qt installation to the current directory.
   - Uses `ldd` to identify and copy additional dependencies.
   - Searches custom paths (e.g., OpenCV libraries) if needed.
3. **Creates Execution Script**:
   - Generates `run.sh` to set up `LD_LIBRARY_PATH`.
   - Grants execution permissions to the script.

## Example Output

```
Found Qt directory at ~/Qt/5.15.2/gcc_64
Copied lib to /current_directory
Copied plugins to /current_directory
Copied libQt5Core.so.5 to /current_directory
Copied libQt5Gui.so.5 to /current_directory
...
Generated run.sh script.
```

## Notes

- Ensure that `run.sh` is executable (`chmod +x run.sh`).
- Modify `custom_paths` in the script if additional dependencies are required.

## Author

**Mahmoud Hany** - Computer Engineering Student & AI Enthusiast

