import tensorflow as tf
from tensorflow.keras.datasets import imdb

# Broj reci koje uzimamo u obzir
vocab_size = 40000  

# data load
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=vocab_size)

print(f"Broj trening primera: {len(x_train)}")
print(f"Prva recenzija (kao sekvenca brojeva): {x_train[0]}")
print(f"Oznaka sentimenta (0=negativan, 1=pozitivan): {y_train[0]}")




#dekodiranje recenzije

# ucitavanje recnika rec -> indeks
word_index = imdb.get_word_index()

# Pomak za rezervisane indekse
# Keras rezerviše indekse 0, 1, 2, 3 za posebne znakove (<PAD>, <START>, itd.)
index_word = {index + 3: word for word, index in word_index.items()}
index_word[0] = "<PAD>"
index_word[1] = "<START>"
index_word[2] = "<UNK>"
index_word[3] = "<UNUSED>"

# Dekodiranje prve recenzije
decoded_review = ' '.join([index_word.get(i, '?') for i in x_train[0]])


# Naravno, recenzije su "ocerupane" jer koristimo samo 10,000 najcescih reci
print("\nDekodirana recenzija:\n")
print(decoded_review)



#Priprema Podataka — Padding Sekvenci
"""
Neuronske mreže očekuju da svi ulazi budu iste dužine.
Pošto su recenzije različitih dužina (neke imaju 50 reči, neke 300),
moramo ih "poravnati":

Kraće recenzije dopunjavamo sa <PAD> (0).

Dužim recenzijama skratimo broj reči.

Mi ćemo izabrati da sve recenzije budu dužine npr. 256 reči.
"""

from tensorflow.keras.preprocessing.sequence import pad_sequences

# Definisemo maksimalnu duzinu recenzije
maxlen = 256

# Primena padding-a
x_train_padded = pad_sequences(x_train, maxlen=maxlen, padding='post')
x_test_padded = pad_sequences(x_test, maxlen=maxlen, padding='post')

print(f"Oblik trening podataka: {x_train_padded.shape}")
print(f"Primer jedne recenzije nakon padding-a:\n{x_train_padded[0]}")

"""
Koristimo pad_sequences iz Keras-a.

maxlen=256 – sve recenzije ce biti tačno 256 tokena.

padding='post' – dodaje nule na kraju kracih recenzija.
"""



# Kreiranje modela: 
"""
- Embedding sloj: pretvara indekse reci u vektore -> Word Embeddings
- GlobalAveragePooling1D -sabija informacije iz embedding vektora
- Dense sloj - skriveni sloj koristi aktivacionu formulu ReLU.
- Dense izlazni sloj - 1 neuron sa sigmoidnom aktivacionom formulom za binarnu klasifikaciju
"""

"""
Embedding sloj: Uči reprezentaciju reči tokom treniranja (dimenzija 16).

GlobalAveragePooling1D: Smanjuje dimenzionalnost tako što uzima prosečnu vrednost iz embedding vektora.

Dense(16, activation='relu'): Klasičan skriveni sloj.

Dense(1, activation='sigmoid'): Pošto radimo binarnu klasifikaciju (pozitivno/negativno).

Loss funkcija: binary_crossentropy je standard za binarne probleme.

Optimizer: adam je dobar izbor za početak.
"""


from tensorflow.keras import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense
from tensorflow.keras.layers import Dropout

# Parametri
embedding_dim = 16

# Definisanje modela
# ovaj model je pokazao probleme u predikciji i zato cemo korisitit LSTM
"""model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim),
    GlobalAveragePooling1D(),
    Dense(16, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])"""


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dropout, Dense

embedding_dim = 32

model = Sequential([
    Embedding(input_dim = vocab_size, output_dim = embedding_dim),
    LSTM(64),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# Kompajliranje modela
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Prikaz modela
model.build(input_shape = (None, 256))
model.summary()



# treniranje modela
"""
epochs=10 - 10 prolaza kroz trening skup.

batch_size=512 - koliko primera koristi po jednom koraku.

validation_data - pratimo kako model radi na test skupu tokom treniranja.

verbose=1 - da vidis detaljan izlaz.
"""


# Treniranje modela
history = model.fit(
    x_train_padded,
    y_train,
    epochs=5,
    batch_size=512,
    validation_data=(x_test_padded, y_test),
    verbose=1
)

# evaluacija i vizuelizacija

"""
Prikazati grafike za loss i accuracy kroz epohe.

Uraditi finalnu evaluaciju na test skupu.
"""


import matplotlib.pyplot as plt

# Funkcija za crtanje grafika
def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs_range = range(1, len(acc) + 1)

    plt.figure(figsize=(14, 5))

    # Accuracy graf
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    # Loss graf
    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')

    plt.show()

# Poziv funkcije
plot_history(history)


results = model.evaluate(x_test_padded, y_test, verbose=2)
print(f"\nTest Accuracy: {results[1]:.4f}")


# Testiranje nad sopstvenoj recenziji

"""
Keras model očekuje tokenizovanu i "padded" recenziju.
Moramo:

Pretvoriti recenziju u tokene.

Primijeniti padding.

Napraviti predikciju.


"""
import numpy as np

def encode_review(review):
    word_index = imdb.get_word_index()
    encoded = [1]  # 1 je <START> token

    for word in review.lower().split():
        index = word_index.get(word, 2)  # 2 je <UNK> za nepoznate reči
        if index < 10000:
            encoded.append(index)

    return encoded

# Primer recenzije
my_review = "This movie was absolutely wonderful with great acting and story"
my_review2 = "Amazing movie! Excellent acting, fantastic story, loved it!"
reviews = [
    "This movie was absolutely wonderful with great acting and story",
    "Amazing movie! Excellent acting, fantastic story, loved it!",
    "The movie was fantastic! Brilliant acting and a touching story. I loved every minute of it.",
    "An excellent film with a captivating plot and outstanding performances. Highly recommended!",
    "A masterpiece! The direction, soundtrack, and visuals were absolutely stunning.",
    "This was one of the best movies I've seen this year. Great pacing and emotional depth.",
    "Amazing experience, I would definitely watch it again. A true cinematic gem.",
    "The movie was boring and predictable. I almost fell asleep halfway through.",
    "Terrible acting and a weak storyline. A complete waste of time.",
    "I had high expectations, but this film was a disaster. Poor script and bad direction.",
    "One of the worst movies I've ever watched. Don't bother.",
    "Disappointing from start to finish. Nothing made sense and the ending was awful.",
    "Some parts were enjoyable, but overall it lacked depth and originality.",
    "It was okay, not great but not terrible either. Just an average movie.",
    "Good visuals but the story was confusing and slow.",
    "I liked the actors, but the plot didn't hold my attention.",
    "Mixed feelings about this one. It had potential but failed to deliver.",


]
for review in reviews:
    # Tokenizacija i padding
    encoded_review = encode_review(review)
    padded_review = pad_sequences([encoded_review], maxlen=256, padding='post')

    #predikcija
    prediction = model.predict(padded_review)

    print(f"Verovatnoća da je recenzija pozitivna: {prediction[0][0]:.4f}")
    if prediction[0][0] >= 0.5:
        print("Model predviđa da je recenzija: ", review, " POZITIVNA recenzija")
    else:
        print("Model predviđa da je recenzija: ", review, " NEGATIVNA recenzija")

















































