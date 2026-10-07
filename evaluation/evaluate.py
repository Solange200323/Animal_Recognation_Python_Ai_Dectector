from pathlib import Path
from PIL import Image
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
from src.animal_recognition import AnimalRecognizer

root=Path(__file__).parent
dataset=root/"dataset"
model=AnimalRecognizer()
true,pred=[],[]

for folder in dataset.iterdir():
    if not folder.is_dir(): continue
    for p in folder.iterdir():
        if p.suffix.lower() not in [".jpg",".jpeg",".png"]: continue
        result=model.predict(Image.open(p).convert("RGB"),1)[0]
        true.append(folder.name.lower())
        pred.append(result["label"].lower())

if not true:
    print("Put labeled images inside evaluation/dataset/<animal>/ first.")
else:
    print("Accuracy :",accuracy_score(true,pred))
    print("Precision:",precision_score(true,pred,average="weighted",zero_division=0))
    print("Recall   :",recall_score(true,pred,average="weighted",zero_division=0))
    print("F1-score :",f1_score(true,pred,average="weighted",zero_division=0))
    print("Confusion matrix:")
    print(confusion_matrix(true,pred))
