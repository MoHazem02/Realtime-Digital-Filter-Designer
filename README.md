# Realtime Digital Filter Designer

![image](https://github.com/MoHazem02/Realtime-Digital-Filter-Designer/assets/66066832/b2bb6b66-2e88-472c-a49a-b424d06147e0)

![image](https://github.com/MoHazem02/Realtime-Digital-Filter-Designer/assets/66066832/1abcb0a0-e31f-484f-8f9d-3b4c7b499332)


![image](https://github.com/MoHazem02/Realtime-Digital-Filter-Designer/assets/66066832/1edbae27-a28f-41d1-a5a8-bf5124943ad3)


## Overview

Realtime Digital Filter Designer is a desktop application developed in Python using libraries such as PyQt5, pyqtgraph, warnings, scipy, numpy, and pandas. This application empowers users to design digital filters, correct phase responses, and implement filters on loaded or realtime-generated signals.

## Features

### 1. Filter Design

- Design digital filters by placing zeros and poles on the z-plane.
  - Drag zeros and poles to reposition them.
  - Highlight and delete zeros and poles as needed.
  - Plot magnitude and phase responses of the designed filter.
  - Option to add conjugates for complex elements.

### 2. Phase Response Correction

- Correct the phase response of the designed filter by adding custom allpass filters.
  - Load predefined filters from a library.
  - Enable/disable added all-pass elements via a drop-down menu.

### 3. Realtime Signal Filtering

- Implement designed filters on loaded signals or realtime-generated signals.
  - Track the y-coordinates of the cursor for signal processing.
  - Live plotting of original and filtered signals simultaneously.
  - Control the speed/temporal-resolution of the filtering process using a slider.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MoHazem02/Realtime-Digital-Filter-Designer.git
    ```

2. Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python application.py
    ```

## Usage

1. Open the application.
2. Design your digital filter by placing zeros and poles.
3. Correct the phase response with custom allpass filters.
4. Implement your designed filter on loaded or realtime-generated signals.
5. Explore various options and functionalities provided by the application.

## Dependencies

- [PyQt5](https://pypi.org/project/PyQt5/)
- [PyQtGraph](https://pypi.org/project/pyqtgraph/)
- [Warnings](https://docs.python.org/3/library/warnings.html)
- [SciPy](https://www.scipy.org/)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)

## Contributing

Feel free to contribute to the development of this Realtime Digital Filter Designer by opening issues or submitting pull requests.


## Acknowledgments

Thank you to the contributors and users who help improve and grow this Realtime Digital Filter Designer. Your feedback and suggestions are highly appreciated.

[Visit the Repository](https://github.com/MoHazem02/Realtime-Digital-Filter-Designer)
