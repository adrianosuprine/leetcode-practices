class Solution(object):
    def romanToInt(self, s):
        roman_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000 
        }
        n = len(s) 
        output = 0
        prev_val = 0
        for i in range(n-1,-1,-1):
            current_val = roman_dict[s[i]]
            if current_val < prev_val:
                output -= current_val
            else:
                output += current_val
            prev_val = current_val
                

                        
                    
        return output 



            




       
        