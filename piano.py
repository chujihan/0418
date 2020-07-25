import turtle as t
from winsound import Beep

freq = { "c4":262, "d4":294, "e4":330, "f4":349, "g4":392, "a4":440, "b4":494, "c5":523, "d5":587, "e5":659, "f5":698, "g5":784, "a5":880, "b5":988, "c6":1047 }

def play_freq(n):
    Beep(freq[n],300)

def key_q():
    play_freq("c4")
def key_w():
    play_freq("d4")
def key_e():
    play_freq("e4")
def key_r():
    play_freq("f4")
def key_t():
    play_freq("g4")
def key_y():
    play_freq("a4")
def key_u():
    play_freq("b4")
def key_a():
    play_freq("c5")
def key_s():
    play_freq("d5")
def key_d():
    play_freq("e5")
def key_f():
    play_freq("f5")
def key_g():
    play_freq("g5")
def key_h():
    play_freq("a5")
def key_j():
    play_freq("b5")
def key_k():
    play_freq("c6")

t.setup(600,600)
s = t.Screen()

s.onkey(key_q, "q")
s.onkey(key_w, "w")
s.onkey(key_e, "e")
s.onkey(key_r, "r")
s.onkey(key_t, "t")
s.onkey(key_y, "y")
s.onkey(key_u, "u")
s.onkey(key_a, "a")
s.onkey(key_s, "s")
s.onkey(key_d, "d")
s.onkey(key_f, "f")
s.onkey(key_g, "g")
s.onkey(key_h, "h")
s.onkey(key_j, "j")
s.onkey(key_k, "k")
s.listen()

