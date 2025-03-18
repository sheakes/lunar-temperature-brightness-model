# 🌕 Lunar Temperature Brightness Model

## 📌 Overview

This project models the **radio brightness temperature** of the Moon by simulating heat flow through its regolith (lunar soil). The model accounts for solar radiation, thermal conduction, and radiative cooling to estimate how the lunar surface temperature evolves over time and contributes to observed radio flux density.

## 🚀 Features

- Simulates **heat transfer** through lunar regolith using a thermal resistor-capacitor ladder model.
- Models **solar heating** and **infrared cooling** over multiple lunar phases.
- Computes the **brightness temperature** observed at radio wavelengths.
- Uses **NumPy** for efficient numerical computations.
- Designed for easy modification and expansion for different observational frequencies.

## 📂 Project Structure

```
📦 lunar_brightness_model
├── 📜 README.md            # Project documentation (this file)
├── 📜 requirements.txt     # Dependencies for installation
├── 📜 environment.yml      # Conda environment setup
├── 📜 LICENSE              # Open-source license information
├── 📂 src/                 # Source code
│   ├── 📜 model.py         # Core lunar temperature model
│   ├── 📜 heat_transfer.py # Functions for regolith heat transfer calculations
│   ├── 📜 radio_flux.py    # Functions for radio brightness calculations
│   └── 📜 utils.py         # Utility functions
├── 📂 data/                # Input data files
├── 📂 notebooks/           # Jupyter notebooks for experimentation
└── 📂 results/             # Output results and plots
```

## 🔧 Installation

### Using Conda

```bash
conda create --name env_lunar_brightness python=3.11
conda activate env_lunar_brightness
conda install -c conda-forge numpy scipy matplotlib jupyterlab
```

### Using Pip

```bash
python -m venv env_lunar_brightness
source env_lunar_brightness/bin/activate  # macOS/Linux
.\env_lunar_brightness\Scripts\activate   # Windows
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Model

To run a simulation:

```bash
python src/model.py
```

To explore results interactively:

```bash
jupyter lab
```

## 📊 Example Output

![Lunar Temperature Plot](https://your-image-url-here.com)

## 📜 References

- Tapping, K. (2024). *Lunar Brightness Temperature Modeling.* Internal Research Notes.
- Keihm, S. J. (1984). Interpretation of the Microwave Emission from the Moon. *Journal of Geophysical Research.*

## 🛠️ Contributing

Pull requests are welcome! For improvements or bug fixes, please open an issue or submit a PR.

## 📄 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions or discussions, feel free to reach out.

