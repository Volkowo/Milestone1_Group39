import wx.grid
import matplotlib

matplotlib.use('WXAgg')
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

import wx
import wx.grid
import pandas as pd
import re

import pytest

from all_functions import *
# 70 foods
foodArray = ["cream cheese", "neufchatel cheese", "requeijao cremoso light catupiry", "ricotta cheese", "cream cheese low fat",
             "cream cheese fat free", "gruyere cheese", "cheddar cheese", "parmesan cheese", "romano cheese", "parmesan cheese grated",
             "port salut cheese", "swiss cheese", "goat cheese hard", "gouda cheese", "pepper jack cheese lucerne", "caraway cheese",
             "gjetost cheese", "tilsit cheese", "goat cheese", "brick cheese", "asadero cheese", "camembert cheese", "provolone cheese reduced fat",
             "roquefort cheese", "queso blanco cheese", "queso seco cheese", "goat cheese soft", "mozzarella cheese", "chihuahua cheese",
             "limburger cheese", "muenster cheese", "queso fresco cheese", "brie cheese", "pimento cheese", "mexican cheese", "feta cheese",
             "mozzarella cheese fat free", "provolone cheese", "anejo cheese", "honey", "apple butter", "fruit jam", "chocolate hazelnut spread",
             "peanut butter", "peanut spread", "chicken spread", "cheese spread", "tahini", "orange marmalade", "american cheese spread",
             "apricot jam", "chunky peanut butter", "ham and cheese spread", "chicken and rice casserole homade", "picnic loaf", "corn tamale",
             "baked potato with cheese sauce bacon", "chinese egg roll", "butter croissant", "enchilada with cheese beef", "corned beef hash with potatoes",
             "biscuit with egg cheese bacon", "bagel with ham egg cheese", "quesadilla with chicken", "corn rice", "kung pao chicken", "beef empanada",
             "frijoles with cheese", "burrito with beef"]

vitamins = [
    "Vitamins",
    "Vitamin A",
    "Vitamin B1",
    "Vitamin B11",
    "Vitamin B12",
    "Vitamin B2",
    "Vitamin B3",
    "Vitamin B5",
    "Vitamin B6",
    "Vitamin C",
    "Vitamin D",
    "Vitamin E",
    "Vitamin K"
]

minerals = [
    "Minerals",
    "Calcium",
    "Copper",
    "Iron",
    "Magnesium",
    "Manganese",
    "Phosphorus",
    "Potassium",
    "Selenium",
    "Sodium",
    "Zinc"
]

macronutrients = [
    "Macronutrients",
    "Fat",
    "Saturated Fats",
    "Monounsaturated Fats",
    "Polyunsaturated Fats",
    "Carbohydrates",
    "Sugars",
    "Protein",
    "Dietary Fiber"
]

others = [
    "Others",
    "Cholesterol",
    "Water",
    "Nutrition Density",
    "Caloric Value"
]

labelForPie = [
    'Fat', 'Saturated Fats', 'Monounsaturated Fats', 'Polyunsaturated Fats', 'Carbohydrates', 'Sugars', 'Protein', 'Dietary Fiber']
labelForBar = [
    'Vitamin A', 'Vitamin B1', 'Vitamin B11', 'Vitamin B12', 'Vitamin B2', 'Vitamin B3', 'Vitamin B5', 'Vitamin B6', 'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K', 'Calcium', 'Copper', 'Iron', 'Magnesium', 'Manganese', 'Phosphorus', 'Potassium', 'Selenium', 'Sodium', 'Zinc', 'Cholesterol', 'Water', 'Nutrition Density', 'Caloric Value']
allLabel = [
    'Caloric Value', 'Fat', 'Saturated Fats', 'Monounsaturated Fats', 'Polyunsaturated Fats', 'Carbohydrates', 'Sugars', 'Protein', 'Dietary Fiber', 'Cholesterol', 'Sodium', 'Water', 'Vitamin A', 'Vitamin B1', 'Vitamin B11', 'Vitamin B12', 'Vitamin B2', 'Vitamin B3', 'Vitamin B5', 'Vitamin B6', 'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K', 'Calcium', 'Copper', 'Iron', 'Magnesium', 'Manganese', 'Phosphorus', 'Potassium', 'Selenium', 'Zinc', 'Nutrition Density']

# TESTCASE: loadCSV
def test_loadCSVExist():
    wineData = loadCSVFile(r".\Food_Nutrition_Dataset.csv")
    assert isinstance(wineData, pd.DataFrame)

def test_loadFakeCSV():
    with pytest.raises(Exception) as exc_info:
        loadCSVFile(r"./fictionalCSV.csv")

 # TESTCASE: loadData()
def test_loadDataWithoutOptionalLine():
    # This means that every column is gonna be included in the table
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", False)
    assert "Fat" in dataFrame.columns

def test_loadDataWithOptionalLine():
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", True)
    assert "food" in dataFrame.columns and "Vitamin B1" not in dataFrame.columns

def test_loadDataWrongCSV():
    with pytest.raises(Exception) as exc_info:
        dataFrame = loadData(r"./fictionalCSV.csv")

# TESTCASE: findNutritionValue() - Finds the highest value for each nutrient
def test_findNutritionValue():
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    # Iterate through every key value in the dictionary to find if there is any empty (or "") values
    for key in maxDict.keys():
        assert maxDict[key] is None or maxDict[key] != ""

# TESTCASE: findResult_generic
def test_genericSearch_ExactMatch():
    results = []
    results = findResult_generic("Apricot Jam", results, foodArray)
    assert sum(results) == 1

def test_genericSearch_partialMatch():
    results = []
    results = findResult_generic("Cheese", results, foodArray)
    assert sum(results) == 47

def test_genericSearch_emptyInput():
    results = []
    results = findResult_generic("", results, foodArray)
    assert sum(results) == len(foodArray)

# TESTCASE; findResult_breakdown
def test_breakdown():
    # Simulate the act of user clicking on a food name in the table.
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", False)
    searchData = dataFrame["food"]
    results = []
    results = findResult_generic("Apricot Jam", results, searchData)
    searchResult = dataFrame[results]

    valueBar, valuePie = findResult_breakdown(allLabel, labelForBar, labelForPie, searchResult)

    for label in labelForBar:
        assert label in searchResult.columns
    for label in labelForPie:
        assert label in searchResult.columns

# TESTCASE: findResult_keto
def test_findKeto():
    results = []
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv")
    nutrientsCarbo = dataFrame["Carbohydrates"]
    nutrientsCal = dataFrame["Caloric Value"]

    results = findResult_keto(nutrientsCarbo, nutrientsCal, results)
    assert sum(results) == 1006

# TESTCASE: findResult_sodium
def test_findSodium():
    results = []
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv")
    nutrients = dataFrame["Sodium"]

    results = findResult_sodium(nutrients, results)
    assert sum(results) == 2394

# TESTCASE: findResult_cholesterol
def test_findCholesterol():
    results = []
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv")
    nutrients = dataFrame["Cholesterol"]

    results = findResult_cholesterol(nutrients, results)
    assert sum(results) == 1727

# TESTCASE: filterDiet()
def test_filterKeto():
    results = filterDiet("Ketogenic Diet")

    # Get the original data for comparison
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv")

    # Check that all of the returned results actually have food with carbohydrate that's less than 10% of the caloric value by iterating through the index by comparing it with the original data
    for i in results.index:
        carb = dataFrame.loc[i, "Carbohydrates"]
        cal = dataFrame.loc[i, "Caloric Value"]
        assert carb < (cal * 0.10)

def test_filterSodium():
    results = filterDiet("Low Sodium Diet")

    # Get the original data for comparison
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv")

    # Same thing as the previous test case, this is the part where we can ensure that the whole food inside the result array has less than 140mg of sodium by comparing it with the original data
    for i in results.index:
        sodium = dataFrame.loc[i, "Sodium"]
        assert sodium < 140

def test_filterCholesterol():
    results = filterDiet("Low Cholesterol Diet")

    # Get the original data for comparison
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv")

    # Same thing as the previous test case, this is the part where we can ensure that the whole food actually is accurate by comparing it with the original data
    for i in results.index:
        cholesterol = dataFrame.loc[i, "Cholesterol"]
        assert cholesterol < 20

def test_filterNone():
    results = filterDiet("Dietary Needs")

    # Get the original data for comparison
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv")

    # Since choosing dietary needs will return the whole data, we can compare it to something like this: results = dataFrame
    assert results.equals(dataFrame[["food"]])

# TESTCASE: getLabelPieBar():
def test_getLabelNotEmpty():
    labelPie, labelBar = getLabelPieBar(macronutrients, vitamins, minerals, others)
    assert labelPie == labelForPie and labelBar == labelForBar

def test_getLabelEmpty():
    # This shouldn't be possible but...
    macronutrients = []
    vitamins = []
    minerals = []
    others = []
    labelPie, labelBar = getLabelPieBar(macronutrients, vitamins, minerals, others)

    # Since labelPie and labelBar is empty, it shouldn't be the same as labelForPie and labelForbar
    assert labelPie != labelForPie and labelBar != labelForBar

# TESTCASE: createLabel()
def test_createLabel():
    labelArray = []
    outputExpected = ['Fat: 0.05%', 'Saturated Fats: 0.19%', 'Monounsaturated Fats: 0.0%', 'Polyunsaturated Fats: 0.0%', 'Carbohydrates: 59.19%', 'Sugars: 39.92%', 'Protein: 0.46%', 'Dietary Fiber: 0.2%']
    # We need to emulate the process of breaking down the food that user has clicked for this to work.
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", False)
    searchData = dataFrame["food"]
    results = []
    results = findResult_generic("Apricot Jam", results, searchData)
    searchResult = dataFrame[results]

    valueBar, valuePie = findResult_breakdown(allLabel, labelForBar, labelForPie, searchResult)

    labelArray = createLabel(valuePie, labelForPie)
    assert labelArray == outputExpected

# TESTCASE: concatBarX
def test_concatBarX():
    results = []
    # Same as before, we need to emulate the process of breaking down the food that user has clicked for this to work.
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", False)
    searchData = dataFrame["food"]
    results = []
    results = findResult_generic("Apricot Jam", results, searchData)
    searchResult = dataFrame[results]

    valueBar, valuePie = findResult_breakdown(allLabel, labelForBar, labelForPie, searchResult)

    # Using np (numpy) made the array a bit different than usualy so I had to convert valueBar as well
    results = concatBarX(valueBar)
    valueBar = np.array(valueBar)

    # The purpose of the function was to move the initial value to the 2nd last position of said array
    assert valueBar[0] == results[-2]

# TESTCASE: checkDropdownAndInput_value
def test_checkDAI_defaultDropdownAndFilledInput():
    # Test -> Min/max value are filled but didn't change dropdown value

    searchResultArray = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Macronutrients", "Vitamins", "Minerals", "Others"]
    minArray = ["0", "", "", ""]
    maxArray = ["34", "", "55", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)

    assert len(errorChooseNutrient) == 2 and len(errorInputValue) == 0 and len(errorComparisonValue) == 0 and isError == True

def test_checkDAI_diffDropdownAndEmptyInput():
    # Test -> Min/max value are empty but dropdown value(s) were changed

    searchResultArray = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Fat", "Vitamins", "Minerals", "Others"]
    minArray = ["", "", "", ""]
    maxArray = ["", "", "", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)

    assert len(errorChooseNutrient) == 0 and len(errorInputValue) == 1 and len(errorComparisonValue) == 0 and isError == True

def test_checkDAI_diffDropdownAndAlphaInput():
    # Test -> Dropdown value(s) were changed but min/max value are not number

    searchResultArray = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Macronutrients", "Vitamin A", "Minerals", "Water"]
    minArray = ["", "b", "", "a"]
    maxArray = ["", "help", "", "noooo"]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)

    assert len(errorChooseNutrient) == 0 and len(errorInputValue) == 2 and len(errorComparisonValue) == 0 and isError == True

def test_checkDAI_minGreaterMax():
    # Test -> Dropdown value(s) were changed but min value is higher than max value

    searchResultArray = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Fat", "Vitamin D", "Sodium", "Others"]
    minArray = ["3", "4", "5", ""]
    maxArray = ["1", "2", "3", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)

    assert len(errorChooseNutrient) == 0 and len(errorInputValue) == 0 and len(errorComparisonValue) == 3 and isError == True

def test_checkDAI_correct():
    # Test -> every input is correct for said field basically
    # filterRange will be tested separately below.

    searchResultArray = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Fat", "Vitamin D", "Sodium", "Others"]
    minArray = ["1", "3", "2", ""]
    maxArray = ["5", "4", "3", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)

    assert len(errorChooseNutrient) == 0 and len(errorInputValue) == 0 and len(errorComparisonValue) == 0 and isError == False

# TESTCASE: filterRange()
def test_filterRange():
    """
    It's important to note that this function (in the real software) will only run once all of the checks have passed. (The 4-5 test cases above)
    That's why the test will immediately start under the assumption that all checks are successful.

    What I'm trying to say is that I can make 4-5 extra use cases, but it will be exactly the same as the 4-5 use cases above since
    they are checking the same thing.
    """
    searchResultArray = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Fat", "Vitamins", "Minerals", "Others"]
    minArray = ["1", "", "", ""]
    maxArray = ["5", "", "", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)

    assert not errorChooseNutrient and not errorInputValue and not errorComparisonValue and not isError and len(searchResultArray) > 0

# TESTCASE: generateErrorMessage_value() ; these test cases are related to checkDropdownAndInput_value
def test_GEM_nutrient():
    # Test -> Test generated error message for test_checkDAI_defaultDropdownAndFilledInput()

    nutrientMsg = ""
    inputMsg = ""
    comparisonMsg = ""
    errorChooseNutrient = ["Macronutrients", "Vitamins"]
    errorInputValue = []
    errorComparisonValue = []

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert nutrientMsg == "Please choose a nutrient for Macronutrients, Vitamins"

def test_GEM_input():
    # Test -> Test generated error message for test_checkDAI_diffDropdownAndEmptyInput() and test_checkDAI_diffDropdownAndAlphaInput()

    nutrientMsg = ""
    inputMsg = ""
    comparisonMsg = ""
    errorChooseNutrient = []
    errorInputValue = ["Vitamins"]
    errorComparisonValue = []

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert inputMsg == "Please fill the min/max value (Numerical values) for Vitamins"

def test_GEM_comparison():
    # Test -> Test generated error message for test_checkDAI_test_checkDAI_minGreaterMax()
    nutrientMsg = ""
    inputMsg = ""
    comparisonMsg = ""
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = ["Macronutrients", "Vitamins", "Minerals"]

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert comparisonMsg == "Please make sure the min value is not higher than the max value for Macronutrients, Vitamins, Minerals"

def test_GEM_nutrientAndInput():
    # Test -> generate error message for 2 errors. Default dropdown and missing input.
    errorChooseNutrient = ["Macronutrients", "Vitamins"]
    errorInputValue = ["Vitamins"]
    errorComparisonValue = []

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert nutrientMsg == "Please choose a nutrient for Macronutrients, Vitamins"
    assert inputMsg == "Please fill the min/max value (Numerical values) for Vitamins"

def test_GEM_nutrientAndComparison():
    # Test -> generate error message for 2 errors. Default dropdown and error in min/max value.
    errorChooseNutrient = ["Macronutrients", "Vitamins"]
    errorInputValue = []
    errorComparisonValue = ["Others"]

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert nutrientMsg == "Please choose a nutrient for Macronutrients, Vitamins"
    assert comparisonMsg == "Please make sure the min value is not higher than the max value for Others"

def test_GEM_inputAndComparison():
    # Test -> generate error message for 2 errors. Default dropdown and error in min/max value.
    errorChooseNutrient = []
    errorInputValue = ["Macronutrients"]
    errorComparisonValue = ["Others"]

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert inputMsg == "Please fill the min/max value (Numerical values) for Macronutrients"
    assert comparisonMsg == "Please make sure the min value is not higher than the max value for Others"

def test_GEM_everyError():
    # Test -> Generate 3 errors. All of them basically
    errorChooseNutrient = ["Others"]
    errorInputValue = ["Macronutrients"]
    errorComparisonValue = ["Vitamins", "Minerals"]

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert nutrientMsg == "Please choose a nutrient for Others"
    assert inputMsg == "Please fill the min/max value (Numerical values) for Macronutrients"
    assert comparisonMsg == "Please make sure the min value is not higher than the max value for Vitamins, Minerals"

# TESTCASE: checkRadioAndDropdown_level()
def test_checkRAD_radio():
    # TEST -> Chose "None" for radio button but chose a value for the dropdown
    radioValue = "None"
    dropdownValue = "Fat"
    errorMsgRadio = ""
    errorMsgDropdown = ""
    isError = True

    errorMsgRadio, errorMsgDropdown, isError = checkRadioAndDropdown_level(radioValue, dropdownValue)

    assert errorMsgRadio == "Nutrition level cannot be none!" and errorMsgDropdown == "" and isError

def test_checkRAD_dropdown():
    # TEST -> Chose an actual value for radio button but didn't pick a value for the dropdown
    radioValue = "Low"
    dropdownValue = "Choose a nutrient"
    errorMsgRadio = ""
    errorMsgDropdown = ""
    isError = True

    errorMsgRadio, errorMsgDropdown, isError = checkRadioAndDropdown_level(radioValue, dropdownValue)

    assert errorMsgRadio == "" and errorMsgDropdown == "Please choose a nutrient to filter the nutrition level with." and isError

def test_checkRAD_noError():
    # TEST -> No error so uhhh no error messages.

    radioValue = "Low"
    dropdownValue = "Fat"
    errorMsgRadio = ""
    errorMsgDropdown = ""
    isError = True

    errorMsgRadio, errorMsgDropdown, isError = checkRadioAndDropdown_level(radioValue, dropdownValue)

    assert errorMsgRadio == "" and errorMsgDropdown == "" and not isError

# TESTCASE: checkResult()
def test_checkResult_notEmpty():
    # This isn't the actual search result, but it should suffice for the purpose of testing because it's trying to count the length of an array.
    arrayResult = foodArray
    message = ""

    message = checkResult(arrayResult)

    assert message == "70 result(s) were found!"

def test_checkResult_empty():
    # This isn't the actual search result, but it should suffice for the purpose of testing because it's trying to count the length of an array.
    arrayResult = []
    message = ""

    message = checkResult(arrayResult)

    assert message == "No result(s) were found."

# filterRange
def test_filterLevel_low():
    # We need to emulate the process of finding the highest value of each nutrient for this.
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    maxValueNutrient = maxDict["Fat"]
    lowThreshold = 0.33 * maxValueNutrient

    dropdownValue = "Fat"
    levelFilter = "Low"

    results = filterLevel(maxDict, dropdownValue, levelFilter)

    # Checks whether every result in results actually meet the requirement (Nutrient has to be less than 33% of the nutrient's highest value)
    for i in results.index:
        fat = dataFrameForDict.loc[i, "Fat"]
        assert fat < lowThreshold

def test_filterLevel_medium():
    # We need to emulate the process of finding the highest value of each nutrient for this.
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    maxValueNutrient = maxDict["Fat"]
    lowThreshold = 0.33 * maxValueNutrient
    highThreshold = 0.66 * maxValueNutrient

    dropdownValue = "Fat"
    levelFilter = "Medium"

    results = filterLevel(maxDict, dropdownValue, levelFilter)

    # Checks whether every result in results actually meet the requirement (Nutrient has to be between 33% to 66% of the nutrient's highest value)
    for i in results.index:
        fat = dataFrameForDict.loc[i, "Fat"]
        assert lowThreshold <= fat <= highThreshold

def test_filterLevel_high():
    # We need to emulate the process of finding the highest value of each nutrient for this.
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    maxValueNutrient = maxDict["Fat"]
    highThreshold = 0.66 * maxValueNutrient

    dropdownValue = "Fat"
    levelFilter = "High"

    results = filterLevel(maxDict, dropdownValue, levelFilter)

    # Checks whether every result in results actually meet the requirement (Nutrient has to be contain more than 66% of the nutrient's highest value)
    for i in results.index:
        fat = dataFrameForDict.loc[i, "Fat"]
        assert fat > highThreshold

# TESTCASE: mergeResult_filterRange()
def test_mergeResult_moreThanOne():
    """
    In the actual software, this function (mergeResult_filterRange) only goes after the filterRange.
    """

    # We need to emulate the user filtering the food with 2 or more nutrients.
    searchResultArray1 = []
    mergedResult1 = []
    errorChooseNutrient1 = []
    errorInputValue1 = []
    errorComparisonValue1 = []
    isError1 = True
    dropdownArray1 = ["Fat", "Vitamins", "Minerals", "Others"]
    minArray1 = ["3", "", "", ""]
    maxArray1 = ["8", "", "", ""]

    errorChooseNutrient1, errorInputValue1, errorComparisonValue1, isError1 = checkDropdownAndInput_value(dropdownArray1, minArray1, maxArray1, isError1, searchResultArray1)
    mergedResult1 = mergeResult_filterRange(searchResultArray1)

    searchResultArray2 = []
    mergedResult2 = []
    errorChooseNutrient2 = []
    errorInputValue2 = []
    errorComparisonValue2 = []
    isError2 = True
    dropdownArray2 = ["Macronutrients", "Vitamin A", "Minerals", "Others"]
    minArray2 = ["", "8", "", ""]
    maxArray2 = ["", "12", "", ""]

    errorChooseNutrient2, errorInputValue2, errorComparisonValue2, isError2 = checkDropdownAndInput_value(
        dropdownArray2, minArray2, maxArray2, isError2, searchResultArray2)
    mergedResult2 = mergeResult_filterRange(searchResultArray2)
    mergedResult_expected = mergedResult1.merge(mergedResult2, on="food", how="inner")

    # The actual testing starts here.
    searchResultArray = []
    mergedResult = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Fat", "Vitamin A", "Minerals", "Others"]
    minArray = ["3", "8", "", ""]
    maxArray = ["8", "12", "", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)
    mergedResult = mergeResult_filterRange(searchResultArray)

    assert mergedResult.equals(mergedResult_expected)

def test_mergeResult_one():
    # We need to emulate the user filtering the food with 1 nutrient.
    searchResultArray = []
    mergedResult = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Fat", "Vitamins", "Minerals", "Others"]
    minArray = ["3", "", "", ""]
    maxArray = ["8", "", "", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)
    mergedResult = mergeResult_filterRange(searchResultArray)

    # If the user only filters with 1 nutrient, it'll use the first index instead.
    assert mergedResult.equals(searchResultArray[0])

# TESTCASE: mergeResult_everything
def test_ME_emptyValue():
    """
    In the actual software, this function will only run after the required checks are done.

    Checks if the searchResult_value is empty or not
    """
    mergedResult = []

    # We need to emulate the user doing the whole filter except the first one.
    searchResult_value = []
    results_value = pd.DataFrame(searchResult_value, columns=["food"])

    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)
    maxValueNutrient = maxDict["Fat"]
    lowThreshold = 0.33 * maxValueNutrient
    dropdownValue = "Fat"
    levelFilter = "Low"

    results_level = filterLevel(maxDict, dropdownValue, levelFilter)
    results_diet = filterDiet("Ketogenic Diet")

    mergedResult_expected = results_level.merge(results_diet, on="food", how="inner")

    mergedResult = mergeResult_everything(results_value, results_level, results_diet)

    assert mergedResult.equals(mergedResult_expected)

def test_ME_emptyDiet():
    """
    In the actual software, this function will only run after the required checks are done.

    Checks if the searchResult_diet is empty or not
    """
    mergedResult = []

    # We need to emulate the user doing the whole filter except the second one.
    searchResultArray = []
    mergedResult = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Fat", "Vitamins", "Minerals", "Others"]
    minArray = ["3", "", "", ""]
    maxArray = ["8", "", "", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray,
                                                                                                      minArray,
                                                                                                      maxArray, isError,
                                                                                                      searchResultArray)
    results_value = mergeResult_filterRange(searchResultArray)

    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)
    maxValueNutrient = maxDict["Fat"]
    lowThreshold = 0.33 * maxValueNutrient
    dropdownValue = "Fat"
    levelFilter = "Low"

    results_level = filterLevel(maxDict, dropdownValue, levelFilter)

    searchResults_diet = []
    results_diet = pd.DataFrame(searchResults_diet, columns=["food"])

    mergedResult_expected = results_value.merge(results_level, on="food", how="inner")

    mergedResult = mergeResult_everything(results_value, results_level, results_diet)

    assert mergedResult.equals(mergedResult_expected)

def test_ME_emptyLevel():
    """
    In the actual software, this function will only run after the required checks are done.

    Checks if the searchResult_level is empty or not
    """

    # We need to emulate the user doing the whole filter except the third one.
    searchResultArray = []
    mergedResult = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Fat", "Vitamins", "Minerals", "Others"]
    minArray = ["3", "", "", ""]
    maxArray = ["8", "", "", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray,
                                                                                                      minArray,
                                                                                                      maxArray, isError,
                                                                                                      searchResultArray)
    results_value = mergeResult_filterRange(searchResultArray)

    searchResults_level = []
    results_level = pd.DataFrame(searchResults_level, columns=["food"])
    results_diet = filterDiet("Ketogenic Diet")

    mergedResult_expected = results_value.merge(results_diet, on="food", how="inner")

    mergedResult = mergeResult_everything(results_value, results_level, results_diet)

    assert mergedResult.equals(mergedResult_expected)

def test_ME_everything():
    """
    In the actual software, this function will only run after the required checks are done.

    Combines every result
    """
    searchResultArray = []
    mergedResult = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Fat", "Vitamins", "Minerals", "Others"]
    minArray = ["3", "", "", ""]
    maxArray = ["8", "", "", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray,
                                                                                                      minArray,
                                                                                                      maxArray, isError,
                                                                                                      searchResultArray)
    results_value = mergeResult_filterRange(searchResultArray)

    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)
    maxValueNutrient = maxDict["Fat"]
    lowThreshold = 0.33 * maxValueNutrient
    dropdownValue = "Fat"
    levelFilter = "Low"

    results_level = filterLevel(maxDict, dropdownValue, levelFilter)
    results_diet = filterDiet("Ketogenic Diet")

    mergedResult_expected = results_value.merge(results_diet, on="food", how="inner").merge(results_level, on="food", how="inner")

    mergedResult = mergeResult_everything(results_value, results_level, results_diet)

    assert mergedResult.equals(mergedResult_expected)

def test_ME_noValue():
    """
    In the actual software, this function will only run after the required checks are done.

    Checks if the final result is NONE or not. We can simulate this by making 3 empty dataframes.
    """

    searchResult_value = []
    results_value = pd.DataFrame(searchResult_value, columns=["food"])

    searchResults_diet = []
    results_diet = pd.DataFrame(searchResults_diet, columns=["food"])

    searchResults_level = []
    results_level = pd.DataFrame(searchResults_level, columns=["food"])

    mergedResult = mergeResult_everything(results_value, results_level, results_diet)

    assert mergedResult is None

# TESTCASE: checkDiet()
def test_CD_default():
    # TEST -> Checks returned string if dropdown value is the default one.
    labelMessage = checkDiet("Dietary Needs")
    assert labelMessage == ""

def test_CD_keto():
    # TEST -> Checks returned string if dropdown value is ketogenic diet.
    labelMessage = checkDiet("Ketogenic Diet")
    assert labelMessage == "Ketogenic Diet - Searches for foods that are low in carbohydrates. (Less than 5-10% of the caloric intake)"

def test_CD_sodium():
    # TEST -> Checks returned string if dropdown value is low sodium diet.
    labelMessage = checkDiet("Low Sodium Diet")
    assert labelMessage == "Low Sodium Diet - Searches for foods that are low in sodium content. (Less than 140mg per serving)"

def test_CD_cholesterol():
    # TEST -> Checks returned string if dropdown value is low cholesterol diet.
    labelMessage = checkDiet("Low Cholesterol Diet")
    assert labelMessage == "Low Cholesterol Diet - Searches for foods that have less than 20mg of cholesterol per serving."

# TESTCASE: checkRadio()
def test_CR_default():
    # TEST -> Checks what string gets returned if user picks the default radio for level filter.
    labelMessage = checkRadio("None")
    assert labelMessage == ""

def test_CR_low():
    # TEST -> Checks what string gets returned if user picks low for level filter.
    labelMessage = checkRadio("Low")
    assert labelMessage == "Nutrition Level: Low - Searches for foods that have less than 33% of the highest value for the selected nutrient."

def test_CR_medium():
    # TEST -> Checks what string gets returned if user picks medium for level filter.
    labelMessage = checkRadio("Medium")
    assert labelMessage == "Nutrition Level: Medium - Searches for foods that have between 33% and 66% of the highest value for the selected nutrient."

def test_CR_high():
    # TEST -> Checks what string gets returned if user picks high for level filter.
    labelMessage = checkRadio("High")
    assert labelMessage == "Nutrition Level: High - Searches for foods that have greater than 66% of the highest value for the selected nutrient."

