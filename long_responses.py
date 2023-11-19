import random

R_EATING = "i don't like eating anything bcz i'm a bot obviously!"
def unknown():
    response = ['Could you please rephrase that?',
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response 