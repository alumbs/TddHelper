import unittest
      
#This is the beginning of a TDD helper program for compiled languages    
class TddHelperJava:
    def handleTwoMethodQualifiers(splitMethodQualifiers):

        return;

    def handleThreeMethodQualifiers(splitMethodQualifiers):

        return;

    def handleFourMethodQualifiers(splitMethodQualifiers):

        return;

    def parseMethodQualifiers(methodQualifiers):
        if (methodQualifiers is None) or not(isinstance(methodQualifiers, str)):
            raise(TypeError, "Invalid method qualifiers passed");
        
        splitMethodQualifiers = str.split(methodQualifiers);
        print("Split method qualifiers", splitMethodQualifiers);

        #Try making a state machine to handle the parsing
        methodQualifierLength = len(splitMethodQualifiers);

        result = None;
        if methodQualifierLength == 2:
            #Then we know we only have a return value and a methodName
            result = handleTwoMethodQualifiers(splitMethodQualifiers);
##            break;
        elif methodQualifierLength == 3:
            #Then we know we only have a access/instance qualifier,
            #a return value, and a methodName
            result = handleThreeMethodQualifiers(splitMethodQualifiers);
##            break;
        elif methodQualifierLength == 4:
            #Then we know we have an access qualifier, an instance qualifier,
            #a return value, and a methodName
            result = handleFourMethodQualifiers(splitMethodQualifiers);
##            break;
        else: #default case
            result = None;
##            break;
        
        for qualifier in splitMethodQualifiers:
            print(i);
            
        return None;

    def parseMethodParameters(methodParams):

        return None;
    
    def splitMethodHeaderIntoParts(headerString):
        minMethodLength = 2; #The minimum amount of strings in a header string

        #initialize the method qualifiers and return types we expect
        accessModifiers = ["public", "protected", "private"];
        instanceModifier = ["static"];
        modificationModifier = ["final"];
        overrideModifier = ["abstract"];
        reentrancyModifier = ["synchronized"];
        nativeModifier = ["native"];
        strictfpModifier = ["strictfp"];
        primitiveIntDataTypes = ["int", "short", "byte", "long", "float", "double"];
        
        if (headerString is None) or not(isinstance(headerString, str)):
            raise(TypeError, "Invalid Header String passed");

        splitHeader = str.split(headerString);
        
##        print("String is " + headerString + " Length of string is " + str(len(splitHeader)));
        
        if len(splitHeader) < minMethodLength:
            raise ValueError;

        #else we have a valid method signature
        #so now split the method header properly
        #into qualifiers vs. method parameters
        print("String is",headerString,"Index of curly bracket is", headerString.index("("));

        #If no curly bracket/brace is found, it will throw an error
##        try:
##            firstCurlyBracketPos = headerString.index("(");
##            secondCurlyBracePos = headerString.index(")");
##        except ValueError:
##            raise ValueError;
        firstCurlyBracePos = headerString.index("(");
        secondCurlyBracePos = headerString.index(")");
        
        methodQualifiersWithoutParams = headerString[0:firstCurlyBracePos];
##        print("New string w/o params", methodQualifiersWithoutParams);

        methodParams = headerString[firstCurlyBracePos+1:secondCurlyBracePos];
        print("Method params", methodParams);

        #Now parse only the method qualifiers
        result = parseMethodQualifiers(methodQualifiersWithoutParams);
                
        #Next parse the method parameters
        result = parseMethodParameters(methodParams);
        
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
        param = "methodName()";
        self.assertRaises(ValueError, TddHelperJava.splitMethodHeaderIntoParts, param);

        #check for an invalid parameter
        param = "public static methodName)";
        self.assertRaises(ValueError, TddHelperJava.splitMethodHeaderIntoParts, param);

        #check for an invalid parameter
        param = "public static methodName(";
        self.assertRaises(ValueError, TddHelperJava.splitMethodHeaderIntoParts, param);
        return;

    def test_valid_param_SplitMethodHeaderIntoParts(self):
        #check for a valid parameter
        param = "public static void methodName(int param1, int param2)";
        expectedResult = ""; #Strings of the resulting test methods
        actualResult = TddHelperJava.splitMethodHeaderIntoParts(param);

        assert(False);
        return;

    def test_null_param_parseMethodQualifiers(self):
        #Check for null parameter
        param = None;
        self.assertRaises(TypeError, TddHelperJava.parseMethodQualifiers, param);
        return;
    
    def test_invalid_paramType_parseMethodQualifiers(self):
        #check for an invalid parameter type
        param = 5713;
        self.assertRaises(TypeError, TddHelperJava.parseMethodQualifiers, param);
        return;
    
def main():
    unittest.main();

if __name__ == '__main__':
    main();



    
