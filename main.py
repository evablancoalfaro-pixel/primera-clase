meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD" : "Es una exprección que se usa al final de una oración pero representa como risa",
            "BRO": "Es una palabra qie significa hermano en ingles",
            "CREEPY": "Significa algo aterrador",
            "AGGRO": "Es una exprección que se usa cuando la persona esta agresiva"
            }

word = input("Escribe una palabra que no entiendas: ").upper()
if word in meme_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print("El significado es",meme_dict[word])
else:
    print("Esa palabra no la conozco.")
    # ¿Qué hacer si no se encuentra la palabra?
