# pydownsongs
Pydownsongs is intended for both developers and regular users to download songs
# Installation
Install by typing the following in CMD/PowerShell (Windows):  
```bash
python -m pip install pydownsongs
```  
For Mac/Linux, type the following in Terminal/PowerShell:    
```bash
python3 -m pip install pydownsongs
```   
Note: The script requires Python3 and is not supported for Python2
# Usage
Refer to these quality levels first:  
1: Very High  
2: High  
3: Medium  
4: Low   
5: Very Low   
  
Pydownsongs can be used in following ways:  
- directly through command line:  
Give the list of songs directly in command line followed by quality level number    
```bash
pydownsongs <song1> <song2> .... <qualitynumber>
```
Example:   
```bash  
pydownsongs "Closer chainsmokers" 3
```   
- by using the file method directly in command line:   
You can store the name of songs in a text file and can download songs using command like this:   
```bash
pydownsongs -f <filename> <qualitynumber>
```   
Example:   
```bash
pydownsongs -f songs.txt 4
```   
- by calling download function in through a python program:   
```python
import pydownsongs
pydownsongs.download(songname, qualitylevel)
```   
Example:   
```python
import pydownsongs
pydownsongs.download("closer chain smokers", 2)
```  
- by calling downloadarray function through python program:   
This function can be called to download a list of songs   
```python
arr = ["a", "b", "c"]
pydownsongs.downloadarray(arr, 4)
```   
Example:   
```python
arr = ["closer chainsmokers", "yaara tere wargaa jass manak"]
pydownsongs.downloadarray(arr, 4)
```   

# Notes
(I assume that the songs rank top on youtube when given the names that you have mentioned in the list. If there may be duplicate songs, consider writing keywords with songname like if you want to search the song Closer, you may type "Closer chainsmokers".)
Make sure that you have active Internet Connection otherwise the script would show you "No Internet Connection" and would exit itself. If any song(s) could not be downloaded by the script it would show "Some error occured" after the song and the name of that song would be copied to failedtemp.txt (this file would be created in the folder in which you are running the script if there are any fails).

# Disclaimer
This script does not promote the downloading of copyright content. This is solely for educational purposes for learning web scrapping by python. I am not responsible for any piracy.