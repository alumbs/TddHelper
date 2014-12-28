import unittest
      
#This is the beginning of a TDD helper program for compiled languages    
class TddHelperJava:
##    def handleMethodQualifiers(splitMethodQualifiers):
##
##        return;

    def createUTForReturnType(methodQualifiers):
        minMethodLength = 2; #The minimum amount of strings in a header string
        primitiveIntDataTypes = ["int", "short", "byte", "long", "float", "double"];
        commonReturnType = ["String"];
        
        if (methodQualifiers is None) or not(isinstance(methodQualifiers, str)):
            raise(TypeError, "Invalid method qualifiers passed");
        
        splitMethodQualifiers = str.split(methodQualifiers);
##        print("Split method qualifiers", splitMethodQualifiers);

        #Try making a state machine to handle the parsing
        methodQualifierLength = len(splitMethodQualifiers);

        result = None;
        if methodQualifierLength >= minMethodLength:
            #Then we know we at least have a 'return type' and a 'method name'
##            result = handleMethodQualifiers(splitMethodQualifiers);
##            unitTestResult = "void test_"
            result = None;
        else: #Invalid Method Signature
            raise ValueError;
            
        return result;

    def createUTForMethodParams(methodParams):

        return None;
    
    def splitMethodHeaderIntoParts(headerString):
        minMethodLength = 2; #The minimum amount of strings in a header string

        #check if the input is a valid string
        if (headerString is None) or not(isinstance(headerString, str)):
            raise(TypeError, "Invalid Header String passed");

        #check if we have valid braces
        #If no brace is found, it will throw an error
        firstCurlyBracePos = headerString.index("(");
        secondCurlyBracePos = headerString.index(")");
        
        methodQualifiersWithoutParams = headerString[0:firstCurlyBracePos];

        methodParams = headerString[firstCurlyBracePos+1:secondCurlyBracePos];
        
        return methodQualifiersWithoutParams, methodParams;

    def createUnitTestsMethods(methodHeader):
        #initialize the method qualifiers and return types we expect
        accessModifiers = ["public", "protected", "private"];
        instanceModifier = ["static"];
        modificationModifier = ["final"];
        overrideModifier = ["abstract"];
        reentrancyModifier = ["synchronized"];
        nativeModifier = ["native"];
        strictfpModifier = ["strictfp"];

        methodQualifiers,methodParams = splitMethodHeaderIntoParts(methodHeader);

        #Now parse only the method qualifiers
        unitTForReturnType = createUTForReturnType(methodQualifiers);
                
        #Next parse the method parameters
        result = createUTForMethodParams(methodParams);
        
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
        #check for no opening brace
        param = "public static methodName)";
        self.assertRaises(ValueError, TddHelperJava.splitMethodHeaderIntoParts, param);

        #check for no closing brace
        param = "public static methodName(";
        self.assertRaises(ValueError, TddHelperJava.splitMethodHeaderIntoParts, param);
        return;

    def test_valid_param_SplitMethodHeaderIntoParts(self):
        #check for a valid parameter
        param = "public static void methodName(int param1, int param2)";

        #Strings of the resulting test methods
        expectedResult1 = "public static void methodName";
        expectedResult2 = "int param1, int param2";
        actualResult1,actualResult2 = TddHelperJava.splitMethodHeaderIntoParts(param);

        assert(expectedResult1 == actualResult1);
        assert(expectedResult2 == actualResult2);
        return;

    def test_null_param_createUTForReturnType(self):
        #Check for null parameter
        param = None;
        self.assertRaises(TypeError, TddHelperJava.createUTForReturnType, param);
        return;
    
    def test_invalid_paramType_createUTForReturnType(self):
        #check for an invalid parameter type
        param = 5713;
        self.assertRaises(TypeError, TddHelperJava.createUTForReturnType, param);
        return;

    def test_invalid_param_createUTForReturnType(self):
        #check for no return type in method header
        param = "methodName";
        self.assertRaises(ValueError, TddHelperJava.createUTForReturnType, param);
        
        return;
    
def main():
    unittest.main();

if __name__ == '__main__':
    main();



    
