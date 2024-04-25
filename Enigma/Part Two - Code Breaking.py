from enigma import *
import copy

"""#CODE1"""
def code_1(code_1_possible_reflectors):
    
    crib = "SECRET"

    #We iterate over all possible reflectors
    for name in code_1_possible_reflectors :

        code_1_rot1 = rotor_from_name("V", "M", 14)
        code_1_rot2 = rotor_from_name("Gamma", "J", 2)
        code_1_rot3 = rotor_from_name("Beta", "M", 4)
        code_1_rot4 = rotor_from_name("ID", "A", 1)
        code_1_plugboard = Plugboard()
        code_1_plugboard.build_plugboard("KI XN FL")

        Enigma_code_1 = Enigma(code_1_rot1, code_1_rot2, code_1_rot3, Reflector(name) , code_1_rot4, code_1_plugboard)
        encoded = Enigma_code_1.encode("DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ")
        if encoded.find(crib) >= 0:
            return(f"CODE 1 : \n The message is {encoded}.\n The missing settings were:\n Reflector {name}")

"""CODE 2"""
def code_2(code_2_possible_positions):

    crib = "UNIVERSITY"

    #We iterate over all possible positions
    for position_rot1 in code_2_possible_positions :
        for position_rot2 in code_2_possible_positions:
            for position_rot3 in code_2_possible_positions:

                code_2_rot1 = rotor_from_name("III", position_rot1, 10)
                code_2_rot2 = rotor_from_name("I", position_rot2, 2)
                code_2_rot3 = rotor_from_name("Beta", position_rot3, 23)
                code_2_rot4 = rotor_from_name("ID", "A", 1)
                code_2_plugboard = Plugboard()
                code_2_plugboard.build_plugboard("VH PT ZG BJ EY FS")

                Enigma_code_1 = Enigma(code_2_rot1, code_2_rot2, code_2_rot3, Reflector("B") , code_2_rot4, code_2_plugboard)
                encoded = Enigma_code_1.encode("CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH")
                if encoded.find(crib) >= 0:
                    return(f"CODE 2 :\n The message is {encoded}.\n The missing settings were:\n Positions : {position_rot3},{position_rot2},{position_rot1}.")

"""CODE 3"""
def code_3(available_rotors,available_settings,available_reflectors):

    crib = "THOUSANDS"
    #We iterate over all possible combinations and stop when we found our crib
    for rot1_name in available_rotors :
        for rot2_name in available_rotors:
            for rot3_name in available_rotors:
                for rot1_setting in available_settings:
                    for rot2_setting in available_settings:
                        for rot3_setting in available_settings:
                            for name in available_reflectors :

                                #Initialize the elements of the enigma
                                code_1_rot1 = rotor_from_name(rot1_name, "Y", rot1_setting)
                                code_1_rot2 = rotor_from_name(rot2_name, "M", rot2_setting)
                                code_1_rot3 = rotor_from_name(rot3_name, "E", rot3_setting)
                                code_1_rot4 = rotor_from_name("ID", "A", 1)
                                reflector_1 = Reflector(name)
                                code_1_plugboard = Plugboard()
                                code_1_plugboard.build_plugboard("FH TS BE UQ KD AL")

                                Enigma_code_1 = Enigma(code_1_rot1, code_1_rot2, code_1_rot3, reflector_1, code_1_rot4, code_1_plugboard)
                                encoded = Enigma_code_1.encode("ABSKJAKKMRITTNYURBJFWQGRSGNNYJSDRYLAPQWIAGKJYEPCTAGDCTHLCDRZRFZHKNRSDLNPFPEBVESHPY")
                                if encoded.find(crib) >= 0:
                                    return(f"CODE 3 : \n The message is {encoded}.\n The missing settings were :\n Rotors : {rot3_name}-{rot2_name}-{rot1_name},\n Settings : {rot3_setting},{rot2_setting},{rot1_setting},\n Reflector : {name}")

"""CODE 4"""
def code_4(code_4_plugboard_pairs, code_4_possible_pairs):

    crib = "TUTOR"
    
    #We remove all the known plugboard elements from the alphabet to obtain valid letters to complete the missing pairs
    for char in code_4_plugboard_pairs:
        code_4_possible_pairs = code_4_possible_pairs.replace(char,"")

    #We pick two, which cannot be the same and enter them into the plugboard
    for char1 in code_4_possible_pairs:
        for char2 in code_4_possible_pairs:
            if char1 != char2 :

                #Initialize the elements of the enigma
                code_1_rot1 = rotor_from_name("IV", "U", 10)
                code_1_rot2 = rotor_from_name("III", "W", 12)
                code_1_rot3 = rotor_from_name("V", "S", 24)
                code_1_rot4 = rotor_from_name("ID", "A", 1)
                reflector_1 = Reflector("A")
                code_1_plugboard = Plugboard()
                combination = ("WP RJ A" + char1 + " VF I" + char2 + " HN CG BS")
                code_1_plugboard.build_plugboard(combination)

                Enigma_code_1 = Enigma(code_1_rot1, code_1_rot2, code_1_rot3, reflector_1, code_1_rot4, code_1_plugboard)
                encoded = Enigma_code_1.encode("SDNTVTPHRBNWTLMZTQKZGADDQYPFNHBPNHCQGBGMZPZLUAVGDQVYRBFYYEIXQWVTHXGNW")
                
                #Ive added the AND condition for you to be able to see the correct result faster
                if encoded.find(crib) >= 0 and encoded.find("NOR") >= 0:
                    return(f"CODE 4 : \n The message is {encoded}.\n The missing settings were :\n Plugboard plugs : {combination}.")

"""CODE 5"""
def code_5(code_5_possible_reflectors,crib):

    
    for name in code_5_possible_reflectors :

        #initializing reflector by name
        reflector_1 = Reflector(name)
        
        #Making a copy of the original Reflector Pattern to be able to revert swapped list when necessary
        original_mapping = copy.copy(reflector_1.patterns[name])

        #Transforming string into a list of characters to be able to perform swapping
        lista1_list = []
        for char in original_mapping:
            lista1_list.append(char)
        
        #Copying the list of characters for manipulation
        swap_no_1 = copy.copy(lista1_list)

        #We swap one pair
        for i in range(len(swap_no_1)):
            for j in range(i+1, len(swap_no_1)):
                swap_no_1 = copy.copy(lista1_list)

                dummy = swap_no_1[i]
                swap_no_1[i] = swap_no_1[j]
                swap_no_1[j] = dummy

                #However, because of our rotor structure we also need to swap their corresponding counter parts to correctly map on the left to right path
                
                #Find thier corresponding counterparts
                counter_part_i = swap_no_1.index(chr(65 + i))
                counter_part_j = swap_no_1.index(chr(65 + j))

                #Swap them
                dummy = swap_no_1[counter_part_i]
                swap_no_1[counter_part_i] = swap_no_1[counter_part_j]
                swap_no_1[counter_part_j] = dummy

                #Keeping track of already swapped places so that they are not swapped again
                already_swapped = [x*0 for x in range(len(swap_no_1))]
                
                #Swapped position has index 1
                already_swapped[i] = 1
                already_swapped[j] = 1
                already_swapped[counter_part_i] = 1
                already_swapped[counter_part_j] = 1

                #One more pair is swapped, while keeping the first swap as is
                for k in range(len(swap_no_1)):
                    if already_swapped[k] == 0 :
                        for l in range(k+1, len(swap_no_1)):
                            if already_swapped[l] == 0:

                                #keeping the first swap static, we copy it to another list
                                swap_no_2 = copy.copy(swap_no_1)

                                #Swap the 2nd pair
                                dummy = swap_no_2[k]
                                swap_no_2[k] = swap_no_2[l]
                                swap_no_2[l] = dummy
                                
                                #Find their counterparts
                                counter_part_k = swap_no_2.index(chr(65 + k))
                                counter_part_l = swap_no_2.index(chr(65 + l))

                                #Swap counterparts
                                dummy = swap_no_2[counter_part_k]
                                swap_no_2[counter_part_k] = swap_no_2[counter_part_l]
                                swap_no_2[counter_part_l] = dummy

                                #Change the reflectors pattern to the one with 8 swapped letters           
                                reflector_1.patterns[name] = ''.join(swap_no_2)

                                #Initialize rotors
                                code_5_rot1 = rotor_from_name("IV", "L", 7)
                                code_5_rot2 = rotor_from_name("II", "J", 18)
                                code_5_rot3 = rotor_from_name("V", "A", 6)
                                code_5_rot4 = rotor_from_name("ID", "A", 1)
                                code_5_plugboard = Plugboard()
                                combination = ("UG IE PO NX WT")
                                code_5_plugboard.build_plugboard(combination)

                                #Build Enigma and encode message
                                Enigma_code_1 = Enigma(code_5_rot1, code_5_rot2, code_5_rot3, reflector_1, code_5_rot4, code_5_plugboard)
                                encoded = Enigma_code_1.encode("HWREISXLGTTBYVXRCWWJAKZDTVZWKBDJPVQYNEQIOTIFX")

                                #If we find the message in the encrypted, we stop the algorithm and return the endcoded message
                                for platform in crib:
                                    if encoded.find(platform) >= 0 :
                                        return(f"CODE 5 : \n The message is {encoded}.\n The missing settings were :\n The original reflector used : {reflector_1.name}.")
                                        

            swap_no_1 = copy.copy(lista1_list)

#code 1 input
code_1_possible_reflectors = ["A","B","C"]

#code 2 input
code_2_possible_positions = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"            

#code 3 inputs
code_3_available_rotors = ["II", "IV", "Beta", "Gamma"]
code_3_available_settings = [2, 4, 6, 8, 20, 22, 24, 26]
code_3_available_reflectors = ["A","B","C"]

#code 4 inputs
code_4_plugboard_pairs = "WP RJ A? VF I? HN CG BS"
code_4_possible_pairs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#code 5 inputs
code_5_possible_reflectors = ["B", "C"]
code_5_crib = ["LINKEDIN","SNAPCHAT", "TWITTER", "REDDIT", "PINTEREST","FACEBOOK", "INSTAGRAM", "MYSPACE", "TIKTOK", "YOUTUBE"]

print(code_1(code_1_possible_reflectors))
print(code_2(code_2_possible_positions))
print(code_3(code_3_available_rotors,code_3_available_settings,code_3_available_reflectors))
print(code_4(code_4_plugboard_pairs, code_4_possible_pairs))
print(code_5(code_5_possible_reflectors,code_5_crib))