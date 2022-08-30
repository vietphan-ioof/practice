import qrcode

img = qrcode.make("pantsinator9000.png")
type(img)
img.save("some_file.png")



'''

TODO:
    - it would be preferred if the entire program was in one file, but that woudl seem insane to ppull off 
    with the complexity of minecraft.
    
    - after maximum bytes reached in the program we split it off into multiple qr codes


    - we'll need a custom qr code reader than can process multiple qr codes.

    - combine all the resulting files into a coherant program that we can execute on our computer

    - the issue with this is that the user would have to install custom software and would diminish the beauty
    of playing minecraft from a piece of paper.

    With paper back you can store it well all you need is a good scanner.



'''











