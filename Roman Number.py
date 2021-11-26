"""Takes a Hindu-ARabic Numeral and converts it into a Roman Numeral"""
import tkinter
Window = Tk()

Numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M'] #Initsialise Roman Numerals
Values = [1, 5, 10, 50, 100, 500, 1000]
Roman = dict(zip(Numerals, Values))
print(Roman, Numerals, Values, sep = '\n')

def take_number():
    
    
    
