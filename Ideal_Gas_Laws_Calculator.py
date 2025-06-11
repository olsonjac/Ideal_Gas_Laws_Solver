### Ideal Gas law solver program. 
# Pressure x Volume = moles x Ideal gas constant x Temperature

# Example Problem: What volume of CO2 is needed to fill an 0.5 moles tank to a pressure of 150.0 atm at 27.0 Celsius? 
# Example 2: If I have 4 moles of gas at a pressure of 5.6 atm and a volume of 12 Liters, what is the temperature?
# Example 3: At what temperature would 2.10 moles of N2 gas have a pressure of 1.25 atm and in a 25.0 L tank?
# Example 4: What volume is occupied by 5.03 moles of O2 at 28 °C and a pressure of 0.998 atm?
# Example 5: What volume is occupied by 5.03 grams of O2 at 28 °C and a pressure of 0.998 atm?

def calculator():
  """Parse a pasted ideal gas law word problem and output the missing value.

  The user is prompted to paste a single sentence problem that contains the
  numeric values and units for pressure, volume, temperature and amount of gas
  (either in moles or grams). Units can be written next to numbers (e.g. ``23C``)
  or separated from them by a space.
  After parsing the text and converting values to standard units, the function
  prints the computed value of the one variable that was omitted from the
  question.
  """

  import time
  import re
  # Ideal gas constant
  R = 0.0821
  #Conversion factor to go from Celsius to Kelvin
  k = 273
#kPa conversion factor
  kPa = 101.3
  print("Welcome to the ideal gas laws calculator!")

#common gases with their atomic weights for grams to mole conversions
  gas_symbol = {
      "H2": 2.016,
      "O2": 32.0,
      "N2": 28.014,
      "F2": 37.998,
      "Cl2": 70.90,
      "Br2": 159.808,
      "I2": 253.808,
      "He": 4.003,
      "Ne": 20.18,
      "Ar": 39.95,
      "Kr": 83.798,
      "Xe": 131.293,
      "Rn": 222,
      "Hydrogen": 2.016,
      "Oxygen": 32.0,
      "Nitrogen": 28.014,
      "Fluorine": 37.998,
      "Chlorine": 70.90,
      "Bromine": 159.808,
      "Iodine": 253.808,
      "Helium": 4.003,
      "Neon": 20.18,
      "Argon": 39.95,
      "Krypton": 83.798,
      "Xenon": 131.293,
      "Radon": 222
  }


# This variable is used with loop below to target unwanted punctuation.
  punctuation = '''!()-[]{};:'"\, <>/?@#$%^&*_~'''

#instructions for the program
  print("Copy and paste the Ideal Gas Law problem here that you want answered.")
#this asks the user to paste their question into the console.
  text = input("(Units can be written with or without a space, e.g. 23C or 23 C)" )

  # allow units to be attached to numbers, e.g. "23C" or "150atm"
  unit_pattern = r"(\d+(?:\.\d+)?)(°C|C|Celsius|K|Kelvin|L|Liters|liter|mL|milliliters|atm|atmospheres|moles|mol|g|grams|kg|kilograms)"
  text = re.sub(unit_pattern, r"\1 \2", text)

#This block removes any extraneous punctuation that would stop the script from identifying variables
  emptyString = " "
  for x in punctuation:
      text = text.replace(x,emptyString)

#this function splits the pasted question into individual objects in a list.
  m_data = text.split()
  lower_tokens = [token.lower() for token in m_data]
  gas_symbol_lower = {k.lower(): v for k, v in gas_symbol.items()}

  # Initialize variables in case they aren't found in the text
  volume = 0
  temperature = 0
  pressure = 0
  moles = 0

#This takes the split up text from the user and removes all spaces 
#and cleans up the list with attached indices.
#The list is then searched for the corresponding units for each variable
#the integer values are then assigned to the corresponding variables which are found one index behind the units.
  for index, value in enumerate(m_data):
      val = value.lower()
      if val in ("l", "liter", "liters"):
          volume = float(m_data[index - 1])
          print("volume is equal to", volume, "Liters")
          break
      if val in ("ml", "milliliters"):
          volume = float(m_data[index - 1]) / 1000
          print("volume is equal to", volume, "Liters")
          break

  time.sleep(1.5)
#This looks for the temperature value and converts accordingly to Kelvin
  for index, value in enumerate(m_data):
      val = value.lower()
      if val in ("°c", "celsius", "c"):
          temperature = float(m_data[index - 1]) + k
          print("temperature is equal to", temperature, "Kelvin")
          break
      if val in ("k", "kelvin"):
          temperature = float(m_data[index - 1])
          print("temperature is equal to", temperature, "Kelvin")
          break

  time.sleep(1.5)        
#Identifies pressure value and converts to atm.
  for index, value in enumerate(m_data):
      val = value.lower()
      if val in ("atm", "atmospheres"):
          pressure = float(m_data[index - 1])
          print("pressure is equal to", pressure, "atm")
          break

  time.sleep(1.5)

# identifies the moles value and assigns it to the corresponding variable
  gas_name = None
  for key_lower in gas_symbol_lower:
      if key_lower in lower_tokens:
          gas_name = key_lower
          break

  for index, value in enumerate(m_data):
      val = value.lower()
      if val in ("moles", "mol"):
          moles = float(m_data[index - 1])
          print("mass is equal to", moles, "moles")
          break
      elif val in ("g", "grams", "kg", "kilograms"):
          grams = float(m_data[index - 1])
          if val in ("kg", "kilograms"):
              grams *= 1000
          if gas_name:
              moles = grams / gas_symbol_lower[gas_name]
              print("mass is equal to", moles, "moles")
          break
  time.sleep(1.5)

  def solver(pressure, volume, moles, temperature, R):
      """Solve for whichever ideal gas variable is missing.

      The calculator sets any variable it cannot parse from the question to
      zero. ``solver`` checks which one of pressure, volume, temperature or
      moles is zero and rearranges ``PV = nRT`` to compute that value.
      """
      if moles == 0:
          print("The answer is" ,(pressure * volume) / (R * temperature), "moles.")
      elif pressure == 0:
          print("The answer is", (moles * R * temperature) / volume, "atm")
      elif temperature == 0:
          print("The answer is", (pressure * volume) /(R * moles), "Kelvin")
      else:
            print("The answer is",(moles * R * temperature) / (pressure),"Liters")
  solver(pressure, volume, moles, temperature, R)
calculator()
