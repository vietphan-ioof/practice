using System;
using System.Collections.Generic;
using Melanchall.DryWetMidi.Core;
using Melanchall.DryWetMidi.Interaction;
using System.IO;
using System.Linq;
using System.Security.Principal;
namespace Vision
{
    class Program
    {
        static void Main(string[] args)
        {
            string name = "Inception.mid";
            string path = "C:\\Users\\madhu\\OneDrive\\Desktop\\Megafile\\Pythonprograms\\Python.pyfiles\\midiToTxt\\Vision";
            ConvertMidiToText(name, path);
        }

        public static void ConvertMidiToText(string name, string textFilePath)
{
    var midiFile = MidiFile.Read(name);
      List<long> NOTENUMBER= new List<long>();
      List<long> TIME = new List<long>();
      List<long> LENGTH= new List<long>();


      Console.WriteLine(midiFile.GetNotes());
      foreach(Melanchall.DryWetMidi.Interaction.Note x in midiFile.GetNotes()){{}
//           Melanchall.DryWetMidi.Interaction.Note 
            Console.WriteLine(x.NoteNumber + " " + x.Time + " " + x.Length + " ");
            NOTENUMBER.Add(x.NoteNumber);
            TIME.Add(x.Time);
            LENGTH.Add(x.Length);
            Console.WriteLine(x.Select(n=> $"{n.NoteNumber} {n.Time} {n.Length}"));
            }
        }
    }
}
