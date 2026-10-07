# AI Animal Recognition and Tourism Assistant

## Run in VS Code

### 1. Open this folder
Open `AI_Animal_Recognition_Tourism_Assistant` in VS Code.

### 2. Create virtual environment
```powershell
python -m venv venv
```

### 3. Activate
```powershell
.\venv\Scripts\Activate.ps1
```

If blocked:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### 4. Install
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Run
```powershell
python -m streamlit run app.py
```

Open the address shown by Streamlit, normally `http://localhost:8501`.

## Project parts
- `app.py`: Streamlit interface
- `src/animal_recognition.py`: pretrained ViT image recognition
- `src/tourism_assistant.py`: local tourism knowledge assistant
- `data/animals.json`: wildlife information
- `evaluation/evaluate.py`: model evaluation
- `evaluation/dataset/`: labeled test images

Tourism answers about supported animals include photos from Wikimedia Commons with
photographer and license attribution. An internet connection is required to load them.

## Assessment
The project uses a pretrained deep-learning model, Python, data preprocessing through the model processor, evaluation metrics, and Streamlit demonstration.

Do not invent accuracy results. Run the evaluation using your own labeled test images and present the actual results.

## Limitation
A general pretrained model may not identify every Rwanda-specific species correctly. A future improvement is collecting a Rwanda wildlife dataset and fine-tuning the model.
