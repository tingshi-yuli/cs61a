from wave import open
from struct import Struct
from math import floor

frame_rate = 11025

def encode(x):
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name="song.wav", seconds=2):
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t += 1
    out.close()

def tri(frequency, amplitude=0.3):
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t / period - floor(0.5 + t / period)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return amplitude * tri_wave
    return sampler

e_freq, g_freq, c_freq = 329.63, 392.00, 261.63

def both(f, g):
    return lambda t: f(t) + g(t)

def note(f, start, end, fade=0.01):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start or seconds > end:
            return 0
        elif seconds < start + fade:
            return f(t) * (seconds - start) / fade
        elif seconds > end - fade:
            return f(t) * (end - seconds) / fade
        else:
            return f(t)
    return sampler

def mario_at(octave):
    c, e = tri(c_freq * octave), tri(e_freq * octave)
    g, low_g = tri(g_freq * octave), tri(g_freq * octave / 2)
    return mario(c, e, g, low_g)

def mario(c, e, g, low_g):
    z = 0
    song = note(e, z, z + 1/8)
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(c, z, z + 1/8))
    z += 1/8
    song = both(song, note(e, z, z + 1/8))
    z += 1/4
    song = both(song, note(g, z, z + 1/4))
    z += 1/2
    song = both(song, note(low_g, z, z + 1/3))
    return song

play(mario_at(1))