import mido
from mido import MidiFile


for message in MidiFile('Interstellar.mid').play():
        output.send(message)

