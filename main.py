from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def print_hello():
    return {"msg":"Hi from test"}

@app.get("/test/{name}")
def add_names(name:str):
    with open("names.txt", "a") as f:
        f.write(f"{name} \n")
    return {"msg": "saved user"}




word = ["a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

@app.post("/ceaser")
def Ceaser_cipher(unencrypted:dict):
    c = ""
    if unencrypted["mode"] ==  "encrypt":
        for i in unencrypted["text"].lower():
            a = (ord(i) -97)
            b = (a + unencrypted["offset"]) % 26
            c += (word[b])
        return {"encrypted_text": c }
    elif unencrypted["mode"] == "decrypt":
        for i in unencrypted["text"].lower(): 
            a = (ord(i) - 97)
            b = (a - unencrypted["offset"]) % 26
            c += (word[b])
        return {"decrypted_text": c }
    else:
        return "Something is wrong here."

@app.get("/fence/encrypt")
def Extracts_the_text(text:str):
    double = ""
    unpaired = ""
    text_without_spaces = text.replace(" ", "")
    for idx, itm in enumerate(text_without_spaces):
        if idx % 2 == 0:
            double += itm
        else:
            unpaired += itm
    return {"encrypted_text":double + unpaired}
   

@app.post("/fence/decrypt")
def Post_decoding(encoded:dict):

    
    word_connection = ""
    if len(encoded["text"]) % 2 == 0:
        list_of_double =  encoded["text"][:int(len(encoded["text"])/2)]
        list_of_unpeired = encoded["text"][int(len(encoded["text"])/2):]
        for i in range(int(len(list_of_double))):
            word_connection += list_of_double[i]
            word_connection += list_of_unpeired[i]
        return { "decrypted": word_connection }
    else:
        list_of_double = encoded["text"]  [:int(len(encoded["text"])//2 + 1)]
        list_of_unpeired = encoded["text"]   [int(len(encoded["text"])//2 + 1):]
        for i in range(int(len(list_of_unpeired))):
            word_connection += list_of_double[i]
            word_connection += list_of_unpeired[i]
        word_connection += list_of_double[-1]
        return { "decrypted": word_connection }


















