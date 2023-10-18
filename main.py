import spacy

model = spacy.load('en_core_web_lg')

secret_word = "pizza"
token_secret_word = model(secret_word)

given_word = input("votre mot")
token_given_word = model(given_word)

similarity = token_given_word.similarity(token_secret_word)

if similarity == 1:
    print('gagné !')
else:
    message = "le mot "+token_given_word.text+" est a"+str(similarity*100) +"°C"
    print(message)



