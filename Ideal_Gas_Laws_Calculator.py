### Ideal Gas law solver program
import time
#Example Problem: What volume of CO2 is needed to fill an 0.5 moles tank to a pressure of 150.0 atm at 27.0 °C ?
#Example 2: If I have 4 moles of gas at a pressure of 5.6 atm and a volume of 12 L, what is the temperature?

#Rydberg's constant
R = 0.0821
#Conversion factor to go from Celsius to Kelvin
k = 273
#kPa conversion factor
kPa = 101.3

# This variable is used with loop below to target unwanted punctuation.
punctuation = '''!()-[]{};:'"\, <>/?@#$%^&*_~'''

#this asks the user to paste their question into the console.
text = input("Paste the Ideal Gas Law problem here that you want answered *(Make sure there are no punctuation marks attached to the units for each variable)" )

#This block removes any extraneous punctuation that would stop the script from identifying variables
emptyString = " "
for x in punctuation:
    text = text.replace(x,emptyString)

#this function splits the pasted question into individual objects in a list.
m_data = text.split()

#This takes the split up text from the user and removes all spaces 
#and cleans up the list with attached indices.
#The list is then searched for the corresponding units for each variable
#the integer values are then assigned to the corresponding variables which are found one index behind the units.
for index, value in enumerate(m_data):
    if value == "L":
        global volume
        volume = float(m_data[index - 1])
        print("volume is equal to", volume, "Liters")
        break
    if value == "mL":
        volume = float(m_data[index - 1]) / 1000
        print("volume is equal to", volume, "Liters")
        break
    else:
        volume = 0

time.sleep(2)
#This looks for the temperature value and converts accordingly to Kelvin
for index, value in enumerate(m_data):
    if value == "°C":
        global temperature
        temperature = float(m_data[index - 1]) + k
        print("temperature is equal to", temperature, "Kelvin")
        break
    if value == "K":
        temperature = float(m_data[index - 1])
        print("temperature is equal to", temperature, "Kelvin")
        break
    else:
        temperature = 0

time.sleep(2)        
#Identifies pressure value and converts to atm.
for index, value in enumerate(m_data):
    if value == "atm":
        global pressure
        pressure = float(m_data[index - 1])
        print("pressure is equal to", pressure, "atm")
        break
    else:
        pressure = 0

time.sleep(2)
# identifies the moles value and assigns it to the corresponding variable
for index, value in enumerate(m_data):
    global moles
    if value == "moles":
        moles = float(m_data[index - 1])
        print("mass is equal to", moles, "moles")
        break
    else:
        moles = 0

time.sleep(2)
#This function checks for the single missing variable and then solves for it algebraically.        
def solver():
    if moles == 0:
        print("The answer is" ,(pressure * volume) / (R * temperature), "moles.")
        
    if pressure == 0:
        print("The answer is", (moles * R * temperature) / volume, "atm")
        
    if temperature == 0:
        print("The answer is", (pressure * volume) /(R * moles), "Kelvin")
       
    else:  
        print("The answer is",(moles * R * temperature) / (pressure),"Liters")
solver()    