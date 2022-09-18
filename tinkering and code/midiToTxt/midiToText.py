import py_midicsv as pm
t

csv_string = pm.midi_to_csv("Interstellar.mid")


midi_object = pm.csv_to_midi(csv_string)

#print(midi_object)
print(csv_string)


with open("midi-to-arduino-example1.mid") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(midi_object)






