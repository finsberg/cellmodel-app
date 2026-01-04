# Cardiac Cell Model Simulator

Welcome! This is a simple application that simulates cardiac cell behavior (using the O'Hara Rudy model). You can use this app to visualize how different drugs affect heart beats.

You can check out a live version of this app [here](https://finsberg.github.io/cellmodel-app). However this version runs in your web browser and may be slower. For the best experience, follow the instructions below to run it on your own computer.

## 🏁 Prerequisites (Do this once)

To run this app, you need a tool called **uv**. Think of `uv` as a manager that automatically downloads the correct version of Python and all the necessary "ingredients" (libraries) needed to run this code.

### Install `uv`

Open your terminal (Command Prompt on Windows, Terminal on macOS) and copy-paste the command for your system:

**🪟 Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**🍏 macOS:**
```bash
/bin/bash -c "$(curl -fsSL https://astral.sh/uv/install.sh)"
```
**🐧 Linux:**
```bash
/bin/bash -c "$(curl -fsSL https://astral.sh/uv/install.sh)"
```

### 🚀 Running the App
Now, in the terminal, navigate to the folder where you saved this code. Then, run the following command:

```bash
uv run streamlit run app.py
```
This command tells `uv` to set up everything and start the app. After a few moments, your web browser should open automatically, showing the app interface.


### 🛑 Stopping the App

To stop the app, just go back to your terminal and press `Ctrl + C`.


## Simulating common drugs
There is a list of scaling factors for common drugs below found [here](https://computationalphysiology.github.io/drug-database/docs/drug_factors.html). You can enter these scaling factors in the app to simulate the effect of these drugs on cardiac cells.


### License
This project is licensed under the MIT License. 
