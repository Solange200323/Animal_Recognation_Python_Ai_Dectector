import json,re

class TourismAssistant:
    STOP_WORDS={"a","an","the","in","on","where","can","i","see","to","about","what","is","are","of","for","it","me","tell"}
    PLURAL_ANIMALS={
        "gorillas":"gorilla",
        "elephants":"elephant",
        "lions":"lion",
        "giraffes":"giraffe",
        "zebras":"zebra",
        "chimpanzees":"chimpanzee",
    }

    def __init__(self,path):
        with open(path,encoding="utf-8") as f: self.data=json.load(f)

    def tokens(self,text):
        tokens=set(re.findall(r"[a-zA-Z]+",text.lower()))
        return {
            self.PLURAL_ANIMALS.get(token,token)
            for token in tokens - self.STOP_WORDS
        }

    def _matches(self,question):
        qt=self.tokens(question)
        matches=[]
        for key,item in self.data.items():
            text=" ".join([key,item["common_name"],item["description"],
                           item["habitat"],item["rwanda_locations"],
                           item["tourism_tip"]," ".join(item["keywords"])])
            score=len(qt & self.tokens(text))
            if score: matches.append((score,key,item))
        matches.sort(reverse=True,key=lambda x:x[0])
        return matches

    def image_for_question(self,question):
        matches=self._matches(question)
        if not matches:
            return None
        _,_,item=matches[0]
        return item.get("image")

    def answer(self,question):
        matches=self._matches(question)
        if not matches:
            return ("I could not find a strong match. Ask about gorillas, lions, elephants, Akagera, Nyungwe, Volcanoes or safari.",[])
        item=matches[0][2]
        answer=f"""### {item["common_name"]}
{item["description"]}

**Habitat:** {item["habitat"]}

**Conservation status:** {item["conservation_status"]}

**Where to see it in Rwanda:** {item["rwanda_locations"]}

**Tourism tip:** {item["tourism_tip"]}"""
        return answer,[x[2]["common_name"] for x in matches[:3]]
