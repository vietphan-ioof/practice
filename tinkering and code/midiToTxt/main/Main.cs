using System;
using System.IO;
using Melanchall.DryWetMidi;
namespace File 
{
    class Program
    {
        public static void ConvertMidiToText(string midiFilePath, string textFilePath)
{
    var midiFile = MidiFile.Read(midiFilePath);
    File.WriteAllLines(textFilePath,midiFile.GetNotes().Select(n => $"{n.NoteNumber} {n.Time} {n.Length}"));
}
    
       static void main(string[] args){
            string MidiFilePath= "C:\\Users\\madhu\\OneDrive\\Desktop\\Megafile\\Python programs\\Python.pyfiles\\midiToTxt\\main";
            string textFilePath = "C:\\Users\\madhu\\OneDrive\\Desktop\\Megafile\\Python programs\\Python.pyfiles\\midiToTxt\\main";
            var midiFile = MidiFile.Read("Interstellar.mid");
        }
    }
}
