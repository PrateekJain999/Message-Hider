import wave
# read wave audio file
song = wave.open("song.wav", mode='rb')
# Read frames and convert to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# The "secret" text message
string=input("ENTER THE SECRETE MSG : ")

string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'     #GENERAL FORMULA 

bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))   #convert string to bit form and then in list form

for i, bit in enumerate(bits):                       # Replace LSB of each byte of the audio data by one bit from the text bit array
    frame_bytes[i] = (frame_bytes[i] & 254) | bit

frame_modified = bytes(frame_bytes)            #modified frames.

with wave.open('song_embedded.wav', 'wb') as fd:         #convert bits to wav formart audio.
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
print("hide data")
song.close()
