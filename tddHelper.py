import unittest
      
#This is the beginning of a TDD helper program for compiled languages
class StringHelper:
    asd
class TddHelperJava:
    def splitMethodHeaderIntoParts(headerString):
        minMethodLength = 2; #The minimum amount of strings in a header string
        
        if (headerString is None) or not(isinstance(headerString, str)):
            raise(TypeError, "Invalid Header String passed");

        splitHeader = str.split(headerString);
        
##        print("String is " + headerString + " Length of string is " + str(len(splitHeader)));
        
        if len(splitHeader) < minMethodLength:
            raise ValueError;

        #else we have a value method signature
        
        
        return;

#Beginning of the "tests" section for this program
class TddHelperTests(unittest.TestCase):
    def test_null_param_SplitMethodHeaderIntoParts(self):
        #Check for null parameter
        param = None;
        self.assertRaises(TypeError, TddHelperJava.splitMethodHeaderIntoParts, param);
        return;
    
    def test_invalid_paramType_SplitMethodHeaderIntoParts(self):
        #check for an invalid parameter type
        param = 5713;
        self.assertRaises(TypeError, TddHelperJava.splitMethodHeaderIntoParts, param);
        return;

    def test_invalid_param_SplitMethodHeaderIntoParts(self):
        #check for an invalid parameter
##        param = "public static void methodName(int param1, int param2)";
        param = "methodName()";
        self.assertRaises(ValueError, TddHelperJava.splitMethodHeaderIntoParts, param);
        return;

    def test_valid_param_SplitMethodHeaderIntoParts(self):
        #check for a valid parameter
        param = "public static void methodName(int param1, int param2)";
        expectedResult = ""; #Strings of the resulting test methods
        actualResult = TddHelperJava.splitMethodHeaderIntoParts(param);

        
        return;
    
def main():
    unittest.main();

if __name__ == '__main__':
    main();



    
