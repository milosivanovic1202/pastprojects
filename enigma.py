class PlugLead:
    def __init__(self, mapping : str):
        #Check if input is alphabetic and if so take it as uppercase
        if mapping.isalpha() and len(mapping)==2 and mapping[0] != mapping[1]:
                self.mapping = mapping.upper()
        else:
            raise ValueError("Input needs to be an alphabetical string of 2 with different letters.")
            
    def encode(self, character : str):
        #We can take only one character as input
        if len(character) == 1:
            #If the character is in our pairs, assign its pair to potential output
            if character in self.mapping:
                self.character = self.mapping.replace(character,'')
            else:
                #Plugboard returns the same alphabetic if there is no pair
                self.character = character
        else:
            raise ValueError("No such lead found. Only one character is taken as input.")
        
        return self.character

class Plugboard(PlugLead):
    def __init__(self):
         self.plugleads = []
         self.plugs = []

    def add(self, pluglead = PlugLead):
        #Check : There are at most 10 plugs per board
        if len(self.plugleads) < 10:
            #Check if plug already assigned to the input letters
            if pluglead.mapping in self.plugleads or pluglead.mapping[0] in ''.join(self.plugs) or pluglead.mapping[1] in ''.join(self.plugs):
                raise ValueError("Plug already assigned to these letters.")
            else:    
                self.plugleads.append(pluglead)
                self.plugs.append(pluglead.mapping)
        else:
            raise ValueError("Only 10 leads at a time")
    
    #Adding multiple leads at once by input as formatted in the tasks
    def build_plugboard(self, string : str):
        self.building_leads = string.split(" ")
        for lead in self.building_leads:
            self.add(PlugLead(lead))

    def encode(self, character : str):
        #We modify the encode of the parent class to consider if plugleads are present at all
        if len(self.plugleads) != 0:
            for i in range(len(self.plugleads)):
                self.mapping = self.plugleads[i].mapping
                lead = super().encode(character)
                if lead != character:
                    break
        else:
            lead = character
        return lead
 
# In this Class I will heavily rely on UNICODE aritmethic as learned in the 2nd Week
# Insead of rotating positions,we will transform the input, run it through the rotor and transform it back
# This transformation is possible because increasing the setting is the same as decreasing the position as stated in the Task
class rotor_from_name:
    def __init__(self, name : str, position : str = "A", setting : int = 1):
        #We include ID to be able to have 4 rotors in our enigma machine without manual labour
        self.patterns = {"ID" :"ABCDEFGHIJKLMNOPQRSTUVWXYZ", 
                         "I" : "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
                         "II" :"AJDKSIRUXBLHWTMCQGZNPYFVOE",
                         "III" : "BDFHJLCPRTXVZNYEIWGAKMUSQO",
                         "IV" : "ESOVPZJAYQUIRHXLNFTGKDCMWB",
                         "V" : "VZBRGITYUPSDNHLXAWMJQOFECK",
                         "GAMMA" : "FSOKANUERHMBTIYCWLQPZXVGJD",
                         "BETA" : "LEYJVCNIXWPBQMDRTAKZGFUHOS"}
        
        #Check for existence of the Rotor by name
        if name.upper() in self.patterns.keys():
            self.name = name.upper()
        else:
            raise ValueError(f"The rotor {name} is not supported.")
        
        notch_list = {"I" : "Q",
                      "II" :"E",
                      "III" : "V",
                      "IV" : "J",
                      "V" : "Z"}
        
        #Check if rotor has notch
        if self.name in notch_list:
            self.notch = (ord(notch_list[self.name]) - 65) 
        else :
            self.notch = None

        #Initialize the transformation settings
        self.setting = setting - 1
        self.position = (ord(position.upper()) - 65)   
        
    def encode_right_to_left(self, character : str):
        if character.isalpha() and len(character) == 1 :
            #As stated above, we transform the input
            self.character_rtl = ((ord(character.upper()) - 65) + self.position - self.setting) % 26
            #We transform the output back
            return chr((ord(self.patterns[self.name][self.character_rtl]) - 65 - self.position + self.setting) % 26 + 65)
        else :
            raise ValueError("Only one character is taken as input.")

    def encode_left_to_right(self, character : str):
        if character.isalpha() and len(character) == 1 :
            self.adju_char =chr((ord(character) - 65 + self.position - self.setting) % 26 + 65)
            self.character_ltr =chr((self.patterns[self.name].find(self.adju_char) - self.position + self.setting) % 26 + 65)
            return(self.character_ltr)
        else :
            raise ValueError("Only one character is taken as input.")

class Reflector(rotor_from_name):
    def __init__(self, name : str):
        self.position = 0
        self.setting = 0
        self.patterns = {"A": "EJMZALYXVBWFCRQUONTSPIKHGD",
                         "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                         "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL"}
        if name.upper() in self.patterns.keys():
            self.name = name.upper()
        else:
            raise ValueError(f"The reflector {name} is not supported.")
        self.notch = None

class Enigma:
    def __init__(self, rot1 : rotor_from_name, rot2 : rotor_from_name, rot3 : rotor_from_name, reflector : Reflector, rot4 = rotor_from_name("ID" , "A", 1), plugboard = Plugboard()):
        self.rotors = [rot1 , rot2 , rot3 , rot4, reflector]
        self.plugboard = plugboard
        self.notches = [x.notch for x in self.rotors]
        self.starting_positions = [x.position for x in self.rotors]
        

    def encode(self, characters : str):
        self.encrypted = ""
        self.plugstring = ""

        #We first let the string go through the plugboard pairs
        for char in characters:
            self.plugstring += self.plugboard.encode(char)
        
        characters = self.plugstring

        for character in characters:
            #We keep track of rotations conditioned by notches
            self.notch_position_adjustments = [i*0 for i in range(len(self.rotors))]
            self.character = character

            #Only the first 3 rotors can rotate
            for i in range(2):
                #If Rotor has a notch
                if self.rotors[i].notch != None:
                        #If rotor is on a notch
                        if self.starting_positions[i] == self.rotors[i].notch:
                            # Rotor 1 turns anyways so we only turn the 2nd if 1st in notch position
                            if i == 0:
                                self.notch_position_adjustments[i+1] += 1
                            # Rotor 2 and Rotor 3 turn if Rotor 2 in notch position
                            elif i == 1:
                                self.notch_position_adjustments[i] += 1
                                self.notch_position_adjustments[i+1] += 1

            #Turn rotor one. Important is here to turn it after we turned the 2nd conditionally, otherwise the notch will not be considered
            self.starting_positions[0] = (self.starting_positions[0] + 1) % 26

            for i in range(len(self.rotors)):
                # Rotors turn at most once for each key press
                self.starting_positions[i] = (self.starting_positions[i] + min(1,self.notch_position_adjustments[i])) % 26

            # We change the positions of the rotors accordingly
            for i in range(len(self.rotors)):
                self.rotors[i].position = self.starting_positions[i]
            
            # Encode the string Right To Left
            for i in range(4):
                self.character = self.rotors[i].encode_right_to_left(self.character)

            # Reflector operation
            self.character = self.rotors[4].encode_right_to_left(self.character)   

            # Encode the Left to Right
            for i in reversed(range(4)):
                self.character = self.rotors[i].encode_left_to_right(self.character)

            self.encrypted = self.encrypted + self.character

        self.final_encryption = ""
        #We encode the resulting string back through the plugboard
        for char in self.encrypted:
            self.final_encryption += self.plugboard.encode(char)
        
        return self.final_encryption
    

