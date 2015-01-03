import unittest
      
#This is the beginning of a TDD helper program for compiled languages    
class TddHelperJava:
##    def handleMethodQualifiers(splitMethodQualifiers):
##
##        return;

    def handleCreatingUTSignatureForParams(splitMethodParams, result, methodName, actualReturnType):
        newLine = "\n";
        tab = "\t";
        #If we have valid parameters
        if splitMethodParams is not None:
            index = 1;
            for param in splitMethodParams:
                paramDataType = str.split(param)[0];
##                    print("paramDataType", paramDataType);
                result += tab + paramDataType + " param"+str(index)+" = ;//Enter the parameter value"+ newLine;
                index+= 1;
                
        result += tab + actualReturnType + " expectedResult = ;//Specify the expected value" + newLine;

        #If we have valid parameters
        if splitMethodParams is not None:
            paramString = "";
            for index in range(len(splitMethodParams)):
                paramString += "param" + str(index+1) + ", ";

            #Remove the last two comma and space characters
            correctParamStingLength = len(paramString) - len(", ");
            paramString = paramString[0:correctParamStingLength];
            result += tab + actualReturnType + " actualResult = "+methodName+"("+paramString+");"  + newLine;
        else:
            result += tab + actualReturnType + " actualResult = "+methodName+"();"  + newLine;
            
        return result;    

    def createUTForReturnType(methodQualifiers, methodParams):
        minMethodLength = 2; #The minimum amount of strings in a header string
        primitiveIntDataTypes = ["int", "short", "byte", "long", "float", "double"];
        stringReturnType = ["String", "string"];
        voidReturnType = ["void"];
        booleanReturnType = ["Boolean"];
        newLine = "\n";
        tab = "\t";
        splitMethodParams = None;
        
        if (methodQualifiers is None) or not(isinstance(methodQualifiers, str)):
            raise(TypeError, "Invalid method qualifiers passed");
        
        splitMethodQualifiers = str.split(methodQualifiers);

        #If we have valid method parameters, split them up
        if methodParams is None:
            #That means we have no method parameters
            splitMethodParams = None;
        elif not(isinstance(methodParams, str)):
            raise ValueError; #Invalid method params passed
        else:
            splitMethodParams = str.split(methodParams, ",");
##            print (splitMethodParams);

        #Get the length of the split-up method Qualifiers
        methodQualifierLength = len(splitMethodQualifiers);
        
        if methodQualifierLength < minMethodLength:
            #Invalid Method Signature
            raise ValueError;

        #Then we know we at least have a 'return type' and a 'method name'
        #The return type is always before the method name
        actualReturnType = splitMethodQualifiers[methodQualifierLength - minMethodLength];
        actualReturnTypeLower = actualReturnType.lower();

        #The methodName is the next value after the return type
        methodName = splitMethodQualifiers[methodQualifierLength - minMethodLength + 1];

        if actualReturnTypeLower in voidReturnType:
            print ("Void type passed to createUTForReturnType method");
            result = None;
        elif actualReturnTypeLower in primitiveIntDataTypes:
##            print (actualReturnType + " type passed to createUTForReturnType method");
            result = "void test_valid_return_value_" + methodName + "()" + newLine;
            result += "{"  + newLine;
            
            result = TddHelperJava.handleCreatingUTSignatureForParams(splitMethodParams, result, methodName, actualReturnType);
            result += tab + "AssertEquals(expectedResult, actualResult);" + newLine;
            result += "}";
            print (result);
        elif actualReturnType in stringReturnType:
##            print (actualReturnType + " type passed to createUTForReturnType method");
            result = "void test_valid_return_value_" + methodName + "()" + newLine;
            result += "{"  + newLine;
            
            result = TddHelperJava.handleCreatingUTSignatureForParams(splitMethodParams, result, methodName, actualReturnType);
            result += tab + "AssertFalse(actualResult == null);" + newLine;
            result += tab + "AssertFalse(actualResult == \"\");" + newLine;
            result += tab + "AssertTrue(expectedResult.equals(actualResult));" + newLine;
            result += "}";
            print (result);
        elif actualReturnType in booleanReturnType:
##            print (actualReturnType + " data type passed to createUTForReturnType method");
            result = "void test_valid_return_value_" + methodName + "()" + newLine;
            result += "{"  + newLine;
            
            result = TddHelperJava.handleCreatingUTSignatureForParams(splitMethodParams, result, methodName, actualReturnType);
            result += tab + "AssertEquals(expectedResult, actualResult);" + newLine;
            result += "}";
            print(result);
        else: #The return value is not a primitive type
##            print (actualReturnType + " data type passed to createUTForReturnType method");
            result = "void test_valid_return_value_" + methodName + "()" + newLine;
            result += "{"  + newLine;
            
            result = TddHelperJava.handleCreatingUTSignatureForParams(splitMethodParams, result, methodName, actualReturnType);
            result += tab + "AssertFalse(actualResult == null);" + newLine;
            result += tab + "AssertEquals(expectedResult.idProperty, actualResult.idProperty);";
            result += "//specify what property you want to compare since the two objects";
            result += " will not reference the same object" + newLine;
            result += "}";
            print (result);
                
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
        errorMsg = "The method header is invalid";

        try:
            methodQualifiers,methodParams = TddHelperJava.splitMethodHeaderIntoParts(methodHeader);
        except (TypeError, ValueError):
            return errorMsg;

        #Now parse only the method qualifiers
        unitTForReturnType = createUTForReturnType(methodQualifiers, methodParams);
                
        #Next parse the method parameters
        result = createUTForMethodParams(methodParams);
        
        return;

#Beginning of the "tests" section for this program
class TddHelperTests(unittest.TestCase):
    def test_null_param_createUnitTestsMethods(self):
        #Check for null parameter
        param = None;
        expectedResult = "The method header is invalid";

        actualResult = TddHelperJava.createUnitTestsMethods(param);

        assert(expectedResult == actualResult);
        return;
    
    def test_invalid_paramType_createUnitTestsMethods(self):
        #check for an invalid parameter type
        param = 5713;
        expectedResult = "The method header is invalid";

        actualResult = TddHelperJava.createUnitTestsMethods(param);
        assert(expectedResult == actualResult);
        
        return;

    def test_no_opening_brace_in_method_header_createUnitTestsMethods(self):
        #check for no opening brace
        param = "public static methodName)";
        expectedResult = "The method header is invalid";

        actualResult = TddHelperJava.createUnitTestsMethods(param);
        assert(expectedResult == actualResult);
        
        return;

    def test_no_closing_brace_in_method_header_createUnitTestsMethods(self):
        #check for no closing brace
        param = "public static methodName(";
        expectedResult = "The method header is invalid";

        actualResult = TddHelperJava.createUnitTestsMethods(param);
        assert(expectedResult == actualResult);
        
        return;
    
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

    def test_no_opening_brace_in_method_header_SplitMethodHeaderIntoParts(self):
        #check for no opening brace
        param = "public static methodName)";
        self.assertRaises(ValueError, TddHelperJava.splitMethodHeaderIntoParts, param);

        return;

    def test_no_closing_brace_in_method_header_SplitMethodHeaderIntoParts(self):
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

    def test_null_methodQualifier_createUTForReturnType(self):
        #Check for null parameter
        methodQualifiers = None;
        methodParams = None;
        self.assertRaises(TypeError, TddHelperJava.createUTForReturnType, methodQualifiers, methodParams);
        return;
    
    def test_invalid_methodQualifierType_createUTForReturnType(self):
        #check for an invalid parameter type
        methodQualifiers = 5713;
        methodParams = None;
        self.assertRaises(TypeError, TddHelperJava.createUTForReturnType, methodQualifiers, methodParams);
        return;

    def test_invalid_methodQualifierLength_createUTForReturnType(self):
        #check for no return type in method header
        methodQualifiers = "methodName";
        methodParams = None;
        self.assertRaises(ValueError, TddHelperJava.createUTForReturnType, methodQualifiers, methodParams);
        
        return;

    def test_void_return_type_createUTForReturnType(self):
        #check for a void return type in method header      
        methodQualifiers = "void voidMethodName";
        methodParams = None;
        expectedResult = None;
        actualResult = TddHelperJava.createUTForReturnType(methodQualifiers, methodParams);

        assert(expectedResult == actualResult);
        return;

    def test_valid_numberTypeMethodQualifierReturnValue_wNoParams_createUTForReturnType(self):
        methodQualifiers = "int intMethodName";
        methodParams = None;
        newLine = "\n";
        tab = "\t";
        expectedResult = "void test_valid_return_value_intMethodName()" + newLine;
        expectedResult += "{"  + newLine;
        expectedResult += tab + "int expectedResult = ;//Specify the expected value" + newLine;
        expectedResult += tab + "int actualResult = intMethodName();"  + newLine;
        expectedResult += tab + "AssertEquals(expectedResult, actualResult);" + newLine;
        expectedResult += "}";
        
        actualResult = TddHelperJava.createUTForReturnType(methodQualifiers, methodParams);
        assert(expectedResult == actualResult);
        return;

    def test_valid_numberTypeMethodQualifierReturnValue_withInvalidParams_createUTForReturnType(self):
        methodQualifiers = "int intMethodName";
        methodParams = 1234;
        newLine = "\n";
        tab = "\t";

        self.assertRaises(ValueError, TddHelperJava.createUTForReturnType, methodQualifiers, methodParams);
        return;

    def test_valid_numberTypeMethodQualifierReturnValue_withValidParams_createUTForReturnType(self):
        methodQualifiers = "int intMethodName";
        methodParams = "String param1, int param2";
        newLine = "\n";
        tab = "\t";
        expectedResult = "void test_valid_return_value_intMethodName()" + newLine;
        expectedResult += "{"  + newLine;
        expectedResult += tab + "String param1 = ;//Enter the parameter value"  + newLine;
        expectedResult += tab + "int param2 = ;//Enter the parameter value"  + newLine;
        expectedResult += tab + "int expectedResult = ;//Specify the expected value" + newLine;
        expectedResult += tab + "int actualResult = intMethodName(param1, param2);"  + newLine;
        expectedResult += tab + "AssertEquals(expectedResult, actualResult);" + newLine;
        expectedResult += "}";
        
        actualResult = TddHelperJava.createUTForReturnType(methodQualifiers, methodParams);
        assert(expectedResult == actualResult);
        return;

    def test_valid_stringTypeMethodQualifierReturnValue_wNoParams_createUTForReturnType(self):
        methodQualifiers = "String stringMethodName";
        methodParams = None;
        newLine = "\n";
        tab = "\t";
        expectedResult = "void test_valid_return_value_stringMethodName()" + newLine;
        expectedResult += "{"  + newLine;
        expectedResult += tab + "String expectedResult = ;//Specify the expected value" + newLine;
        expectedResult += tab + "String actualResult = stringMethodName();"  + newLine;
        expectedResult += tab + "AssertFalse(actualResult == null);" + newLine;
        expectedResult += tab + "AssertFalse(actualResult == \"\");" + newLine;
        expectedResult += tab + "AssertTrue(expectedResult.equals(actualResult));" + newLine;
        expectedResult += "}";
        
        actualResult = TddHelperJava.createUTForReturnType(methodQualifiers, methodParams);
        assert(expectedResult == actualResult);
        return;

    def test_valid_stringTypeMethodQualifierReturnValue_withInvalidParams_createUTForReturnType(self):
        methodQualifiers = "String stringMethodName";
        methodParams = 1234;
        newLine = "\n";
        tab = "\t";

        self.assertRaises(ValueError, TddHelperJava.createUTForReturnType, methodQualifiers, methodParams);
        return;

    def test_valid_stringTypeMethodQualifierReturnValue_withValidParams_createUTForReturnType(self):
        methodQualifiers = "String stringMethodName";
        methodParams = "String param1, int param2";
        newLine = "\n";
        tab = "\t";
        expectedResult = "void test_valid_return_value_stringMethodName()" + newLine;
        expectedResult += "{"  + newLine;
        expectedResult += tab + "String param1 = ;//Enter the parameter value"  + newLine;
        expectedResult += tab + "int param2 = ;//Enter the parameter value"  + newLine;
        expectedResult += tab + "String expectedResult = ;//Specify the expected value" + newLine;
        expectedResult += tab + "String actualResult = stringMethodName(param1, param2);"  + newLine;
        expectedResult += tab + "AssertFalse(actualResult == null);" + newLine;
        expectedResult += tab + "AssertFalse(actualResult == \"\");" + newLine;
        expectedResult += tab + "AssertTrue(expectedResult.equals(actualResult));" + newLine;
        expectedResult += "}";
        
        actualResult = TddHelperJava.createUTForReturnType(methodQualifiers, methodParams);
        assert(expectedResult == actualResult);
        return;

    def test_valid_objectTypeMethodQualifierReturnValue_wNoParams_createUTForReturnType(self):
        methodQualifiers = "Object objectMethodName";
        methodParams = None;
        newLine = "\n";
        tab = "\t";
        expectedResult = "void test_valid_return_value_objectMethodName()" + newLine;
        expectedResult += "{"  + newLine;
        expectedResult += tab + "Object expectedResult = ;//Specify the expected value" + newLine;
        expectedResult += tab + "Object actualResult = objectMethodName();"  + newLine;
        expectedResult += tab + "AssertFalse(actualResult == null);" + newLine;
        expectedResult += tab + "AssertEquals(expectedResult.idProperty, actualResult.idProperty);";
        expectedResult += "//specify what property you want to compare since the two objects";
        expectedResult += " will not reference the same object" + newLine;
        expectedResult += "}";
        
        actualResult = TddHelperJava.createUTForReturnType(methodQualifiers, methodParams);
        assert(expectedResult == actualResult);
        return;

    def test_valid_objectTypeMethodQualifierReturnValue_withInvalidParams_createUTForReturnType(self):
        methodQualifiers = "Object objectMethodName";
        methodParams = 1234;
        newLine = "\n";
        tab = "\t";

        self.assertRaises(ValueError, TddHelperJava.createUTForReturnType, methodQualifiers, methodParams);
        return;

    def test_valid_objectTypeMethodQualifierReturnValue_withValidParams_createUTForReturnType(self):
        methodQualifiers = "Object objectMethodName";
        methodParams = "String param1, int param2";
        newLine = "\n";
        tab = "\t";

        expectedResult = "void test_valid_return_value_objectMethodName()" + newLine;
        expectedResult += "{"  + newLine;
        expectedResult += tab + "String param1 = ;//Enter the parameter value"  + newLine;
        expectedResult += tab + "int param2 = ;//Enter the parameter value"  + newLine;
        expectedResult += tab + "Object expectedResult = ;//Specify the expected value" + newLine;
        expectedResult += tab + "Object actualResult = objectMethodName(param1, param2);"  + newLine;
        expectedResult += tab + "AssertFalse(actualResult == null);" + newLine;
        expectedResult += tab + "AssertEquals(expectedResult.idProperty, actualResult.idProperty);";
        expectedResult += "//specify what property you want to compare since the two objects";
        expectedResult += " will not reference the same object" + newLine;
        expectedResult += "}";
        
        actualResult = TddHelperJava.createUTForReturnType(methodQualifiers, methodParams);
        assert(expectedResult == actualResult);
        return;

    def test_valid_SelfCreatedObjectTypeMethodQualifierReturnValue_wNoParams_createUTForReturnType(self):
        methodQualifiers = "SelfCreatedObject selfMethodName";
        methodParams = None;
        newLine = "\n";
        tab = "\t";
        expectedResult = "void test_valid_return_value_selfMethodName()" + newLine;
        expectedResult += "{"  + newLine;
        expectedResult += tab + "SelfCreatedObject expectedResult = ;//Specify the expected value" + newLine;
        expectedResult += tab + "SelfCreatedObject actualResult = selfMethodName();"  + newLine;
        expectedResult += tab + "AssertFalse(actualResult == null);" + newLine;
        expectedResult += tab + "AssertEquals(expectedResult.idProperty, actualResult.idProperty);";
        expectedResult += "//specify what property you want to compare since the two objects";
        expectedResult += " will not reference the same object" + newLine;
        expectedResult += "}";
        
        actualResult = TddHelperJava.createUTForReturnType(methodQualifiers, methodParams);
        assert(expectedResult == actualResult);
        return;

    def test_valid_SelfCreatedObjectTypeMethodQualifierReturnValue_withInvalidParams_createUTForReturnType(self):
        methodQualifiers = "SelfCreatedObject selfMethodName";
        methodParams = 1234;
        newLine = "\n";
        tab = "\t";

        self.assertRaises(ValueError, TddHelperJava.createUTForReturnType, methodQualifiers, methodParams);
        return;

    def test_valid_SelfCreatedObjectTypeMethodQualifierReturnValue_withValidParams_createUTForReturnType(self):
        methodQualifiers = "SelfCreatedObject selfMethodName";
        methodParams = "Boolean param1, String param2";
        newLine = "\n";
        tab = "\t";

        expectedResult = "void test_valid_return_value_selfMethodName()" + newLine;
        expectedResult += "{"  + newLine;        
        expectedResult += tab + "Boolean param1 = ;//Enter the parameter value"  + newLine;
        expectedResult += tab + "String param2 = ;//Enter the parameter value"  + newLine;
        expectedResult += tab + "SelfCreatedObject expectedResult = ;//Specify the expected value" + newLine;
        expectedResult += tab + "SelfCreatedObject actualResult = selfMethodName(param1, param2);"  + newLine;
        expectedResult += tab + "AssertFalse(actualResult == null);" + newLine;
        expectedResult += tab + "AssertEquals(expectedResult.idProperty, actualResult.idProperty);";
        expectedResult += "//specify what property you want to compare since the two objects";
        expectedResult += " will not reference the same object" + newLine;
        expectedResult += "}";
        
        actualResult = TddHelperJava.createUTForReturnType(methodQualifiers, methodParams);
        assert(expectedResult == actualResult);
        return;

    def test_valid_BooleanTypeMethodQualifierReturnValue_wNoParams_createUTForReturnType(self):
        methodQualifiers = "Boolean boolMethodName";
        methodParams = None;
        newLine = "\n";
        tab = "\t";
        expectedResult = "void test_valid_return_value_boolMethodName()" + newLine;
        expectedResult += "{"  + newLine;
        expectedResult += tab + "Boolean expectedResult = ;//Specify the expected value" + newLine;
        expectedResult += tab + "Boolean actualResult = boolMethodName();"  + newLine;
        expectedResult += tab + "AssertEquals(expectedResult, actualResult);" + newLine;
        expectedResult += "}";
        
        actualResult = TddHelperJava.createUTForReturnType(methodQualifiers, methodParams);
        assert(expectedResult == actualResult);
        return;

    def test_valid_BooleanTypeMethodQualifierReturnValue_withInvalidParams_createUTForReturnType(self):
        methodQualifiers = "Boolean boolMethodName";
        methodParams = 1234;
        newLine = "\n";
        tab = "\t";

        self.assertRaises(ValueError, TddHelperJava.createUTForReturnType, methodQualifiers, methodParams);
        return;

    def test_valid_BooleanTypeMethodQualifierReturnValue_withValidParams_createUTForReturnType(self):
        methodQualifiers = "Boolean boolMethodName";
        methodParams = "Boolean param1, String param2, int thirdParam";
        newLine = "\n";
        tab = "\t";

        expectedResult = "void test_valid_return_value_boolMethodName()" + newLine;
        expectedResult += "{"  + newLine;
        expectedResult += tab + "Boolean param1 = ;//Enter the parameter value"  + newLine;
        expectedResult += tab + "String param2 = ;//Enter the parameter value"  + newLine;
        expectedResult += tab + "int param3 = ;//Enter the parameter value"  + newLine;
        expectedResult += tab + "Boolean expectedResult = ;//Specify the expected value" + newLine;
        expectedResult += tab + "Boolean actualResult = boolMethodName(param1, param2, param3);"  + newLine;
        expectedResult += tab + "AssertEquals(expectedResult, actualResult);" + newLine;
        expectedResult += "}";
        
        actualResult = TddHelperJava.createUTForReturnType(methodQualifiers, methodParams);
        assert(expectedResult == actualResult);
        return;
    
def main():
    unittest.main();

if __name__ == '__main__':
    main();



    
