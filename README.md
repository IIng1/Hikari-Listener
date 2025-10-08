# 🌸 Hikari Listener

**Hikari** is an **AI-based system** with a user interface built using **Streamlit**.
It utilizes the **Qwen1.5** model in combination with **task-specific LoRA adapters** for sentence generation and user translation rating.
For **text-to-speech synthesis**, it supports the **Suno/Bark** models or **Google TTS** as a lightweight alternative for systems without **CUDA** or with low performance.

---

## ✨ Features

* 🔄 **Text generation** with custom user configuration
* 🧩 **Listening exercises** with context-specific generation
* 🚀 **Automatic checking and rating** of user translations
* 🎛️ **User statistics dashboard** (accuracy, activity, and progress tracking)

---

## ⚠️ Warning

> ⚠️ **This project is currently in a prototype stage.**
> Some functions may not work correctly and require further development and optimization.

---

## 📂 Project Structure

```bash
Hikari-Listener/
│
├── data/                     # Data storage
│   ├── audio_result/         # Folder where generated audio files are saved
│   └── statistics/           # Folder for JSON files with user statistics
│
├── develop_utils/            # Development utilities and dataset generation tools (future)
│   ├── core/                 # Core development utilities
│   └── dataset/              # Modules for working with datasets
│
├── lora_adapter/             # Folder for saving LoRA adapters after fine-tuning
│
└── src/                      # Main project source code
    ├── core/                 # Core system logic
    ├── css_gen/              # CSS generation modules
    ├── generation/           # Generation templates and related logic
    └── webui/                # Streamlit-based web UI modules
```

---

## 🔧 How to Run Locally

### 🧠 Manual Setup

```bash
git clone https://github.com/IIng1/Hikari-Listener.git
cd Hikari-Listener
python -m venv Hikari_Listener
Hikari_Listener\Scripts\activate
pip install -r requirements.txt
python app.py
```

> Alternatively, you can try the **Google Colab** version: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IIng1/Hikari-Listener/blob/main/Hikari_Listener.ipynb)


---

## 🗺️ RoadMap

#### DONE:
- Develop a preview of the WEB-UI using StreamLit
- Research, evaluation, and selection of models
- Implementation of basic functionality
- Generate preview dataset (currently in use) for fine-tuning LoRA adapters
- Fine-tuning LoRA adapters for each task and improving inference
- Add the TTS model (suno/bark)
- Add a listening page with colordiff and user translation rating
- Add a statistics page for activity and ratings
- Add Google-TTS for low-performance PCs

#### TO DO:
- Develop an API for functionality
- Development of utilities for expanding datasets
- Expanding the dataset with new utilities
- Re-fine-tuning with a new data set to improve inference results
- Enhance the listening page with detailed translation feedback
- Add a new type of WEB-UI (HTML + CSS / Gradio)
- Further improvements and features to be determined later

---

## 📜 License

**MIT License**
You are free to use, modify, and distribute this project for both personal and commercial purposes.