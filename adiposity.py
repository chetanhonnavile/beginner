import sys
import re

class BAICalculator:
    """ Class to calculate Body Adiposity Index based on given age, height and hip circumference """
    def __init__(self, sampleNum, data = {}):
        self.sampleNum = sampleNum
        self.data = data

    def update(self, age, height, hip):
        """
        Updates the data dict with user input values

        returns: None
        """
        self.age = age
        self.height = height
        self.hip = hip
        details = {self.sampleNum:{"age":self.age,
                                  "height":self.height, 
                                  "hip":self.hip}}
        self.data.update(details)

    def getSampleDetails(self, sampleNum) -> dict:
        """
        param: Takes sampleId

        returns: dictionary of details containing age, height and hipcircumference
        """
        return self.data[sampleNum]

    def getAllSampleDetails(self) -> dict:
        """
        returns: Details of all sampleId in dictionary format
        """
        return self.data

    def computeBai(self, values) -> int:
        """
        param: Values nothing but age, height and hipcircumference
        Computes the BAI using formula 
        return: usually float value
        """
        return int((values["hip"]/values["height"]**1.5)-18)

    def displayStats(self):
        """ Displays the result for which category does the sampleId belong """
        stats = {}
        for sampleId, values in self.data.items():
            self.data[sampleId]["result"]=self.computeBai(values)
        
        for i, j in self.data.items():
            if 20 <= self.data[i]["age"] <= 39:
                if self.data[i]["result"] < 9:
                    self.data[i]["bai"] = "Underweight"
                elif 9 < self.data[i]["result"] < 21:
                    self.data[i]["bai"] = "Healthy"
                elif 22 < self.data[i]["result"] < 25:
                    self.data[i]["bai"] = "Overweight"
                else:
                    self.data[i]["bai"] = "Obese"

            if 40 <= self.data[i]["age"] <= 59:
                if self.data[i]["result"] < 11:
                    self.data[i]["bai"] = "Underweight"
                elif 11 < self.data[i]["result"] < 23:
                    self.data[i]["bai"] = "Healthy"
                elif 23 < self.data[i]["result"] < 29:
                    self.data[i]["bai"] = "Overweight"
                else:
                    self.data[i]["bai"] = "Obese"

            if 60 <= self.data[i]["age"] <= 79:
                if self.data[i]["result"] < 13:
                    self.data[i]["bai"] = "Underweight"
                elif 13 < self.data[i]["result"] < 25:
                    self.data[i]["bai"] = "Healthy"
                elif 25 < self.data[i]["result"] < 31:
                    self.data[i]["bai"] = "Overweight"
                else:
                    self.data[i]["bai"] = "Obese"
            
                 
        print("Summary of aggregated stats".center(40,"*"))
        print("{:<15} {:<15}".format('SampleId', 'Result'))
        print("-"*30)
        for k, v in self.data.items():
            print ("{:<15} {:<15}".format(i, self.data[i]["bai"]))
        
        print("-"*30)


def quit():
    sys.exit("Thanks for using BAI Application!")

    
def convertToMeters(num, unit):
    """
    param: unit in inches or feet

    returns : unit in meters
    """
    if unit.lower() in ["inches", "in"]:
        return num*0.0254
    elif unit.lower() in ["ft", "feet"]:
        return num*0.3048
    else:
        return num

def convertToInches(num, unit):
    """
    param: unit in meters or feet

    returns : unit in inches
    """
    if unit.lower() in ["ft", "feet"]:
        return num*12
    elif unit.lower() in ["m", "mts"]:
        return num*39.3701
    else:
        return num

def checkHeight():
    """
    Evaluate the input Height from user
    checks : bad characters
             bad units

    returns: Height in meters
    """
    while(True):
        height = input("Height: ")
        regex = re.compile(r'(^[0-9]{1,3}\.?[0-9]*)([a-z]*)$')
        match = regex.match(height)
        if match:
            if not match.group(1):
                print("No height found, pls re-enter")
                continue
            if not match.group(2):
                print("Bad units specified")
                continue
            num_regex = re.compile('^[0-9]+\.?[0-9]*$')
            num = float(num_regex.match(match.group(1)).group(0))
            height_in_meters = convertToMeters(num, match.group(2))
            return height_in_meters
        else:
            print("Height: Bad height input, pls re enter")

def checkAge():
    """
    Ensures "Age" is of int value and in accepted range

    """
    while(True):
        try:
            age = int(input("Age: "))
            if age in range(20, 80):
                break
            print("Age must be between 20 - 79")       
        except ValueError:
            print("pls enter only integer value")     
    return age

def checkHipCircumference():
    """
    Ensure Hip circumference is error free input 
    without any bad characters, bad input size units.

    returns: Hip circumference in inches
    """
    while(True):
        hipCircumference = input("Hip Circumference: ")
        regex = re.compile(r'(^[0-9]{1,3}\.?[0-9]*)([a-z]*)$')
        match = regex.match(hipCircumference)
        if match:
            if not match.group(1):
                print("No hipCircumference found, pls re-enter")
                continue
            if not match.group(2):
                print("Bad units specified")
                continue
            num_regex = re.compile('^[0-9]+\.?[0-9]*$')
            num = float(num_regex.match(match.group(1)).group(0))
            hipc_inches = convertToInches(num, match.group(2))
            return hipc_inches        
        else:
            print("Hip: Bad hipcircumference input, pls re enter")

    
def main():
    print("Welcome to BAI Calculator".center(50,"-"))
    sampleNumber = 0
    Flag = True
    max_attempts = 0
    while(Flag):       
        print("""Press the option keys as below:
            1 or C: Continue with entering sample details
            2 or Q: Quit the application""")
        resp = input()
        if resp in [str(2), 'q', 'Q']:
            quit()
        elif resp in [str(1), 'c', 'C']:
            while(True):
                sampleNumber += 1
                sampleId = "sample"+str(sampleNumber).zfill(3)
                print(f"Please Enter the details for {sampleId}")
                age    = checkAge()
                height = checkHeight()
                hipc   = checkHipCircumference()
                sample = BAICalculator(sampleId)
                sample.update(age, height, hipc)
                Flag1 = True
                while(Flag1):
                    print("""Press the option keys as below:
                    1 or C: Continue with entering sample details
                    2 or Q: Quit the application
                    3 or G: Display group(s) stats""")
                    resp = input()
                    if resp in [str(1), 'c', 'C']:
                        break
                    elif resp in [str(2), 'q', 'Q']:
                        quit()
                    elif resp in [str(3), 'g', 'G']:
                        sample.displayStats()
                    else:
                        print("Bad input, pls try again!!")
        else:
            max_attempts += 1
            if max_attempts == 3:
                print("You have reached maximum attempts, pls start over")
                quit()

            print("Bad input, pls try again!!")
            

if __name__ == "__main__":
    main()


            
                            


        
