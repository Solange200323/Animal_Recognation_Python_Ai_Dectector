from transformers import pipeline
import json

class AnimalRecognizer:
    def __init__(self):
        self.classifier=pipeline("image-classification", model="google/vit-base-patch16-224")
        with open("data/animals.json",encoding="utf-8") as f:
            self.data=json.load(f)

    def predict(self,image,top_k=5):
        return [{"label":x["label"],"score":float(x["score"])}
                for x in self.classifier(image,top_k=top_k)]

    def animal_info(self,label):
        label=label.lower().strip()
        aliases={"african elephant":"elephant","mountain gorilla":"gorilla",
                 "plains zebra":"zebra","african lion":"lion"}
        key=aliases.get(label,label)
        return self.data.get(key)
