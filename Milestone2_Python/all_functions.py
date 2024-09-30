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

from run_app import DataTable as DataTable

def findResult_generic(searchInput, items):
    array = []
    for item in items:
        if re.findall(searchInput.lower(), item):
            array.append(True)
        else:
            array.append(False)
    return array

def findResult_breakdown(allLabel, labelBar, searchResult):
    barArray = []
    pieArray = []

    for i in range(len(allLabel)):
        if allLabel[i] in labelBar:
            barArray.append(searchResult.iloc[0][allLabel[i]])
        else:
            pieArray.append(searchResult.iloc[0][allLabel[i]])

    return barArray, pieArray


def filterDiet(dropdownValue):
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv")
    loc = []

    if dropdownValue == "Ketogenic Diet":
        nutrientsCarbo = dataFrame["Carbohydrates"]
        nutrientsCal = dataFrame["Caloric Value"]
        loc = findResult_keto(nutrientsCarbo, nutrientsCal)

    if dropdownValue == "Low Sodium Diet":
        nutrients = dataFrame["Sodium"]
        loc = findResult_sodium(nutrients)

    if dropdownValue == "Low Cholesterol Diet":
        nutrients = dataFrame["Cholesterol"]
        loc = findResult_cholesterol(nutrients)

    if dropdownValue == "Dietary Needs":
        return pd.DataFrame(columns=["food"])

    searchResult = dataFrame[loc]
    searchResult = searchResult[["food"]]
    return searchResult

def findResult_keto(carbo, calorie):
    array = []
    try:
        if len(carbo) != len(calorie):
            raise ValueError("Carbo and Calorie array have different length!")
        for i in range(len(carbo)):
            if carbo[i] < (calorie[i] * 0.10):
                array.append(True)
            else:
                array.append(False)
        return array
    except ValueError:
        raise

def findResult_sodium(items):
    array = []
    for nutrient in items:
        if nutrient < 40:
            array.append(True)
        else:
            array.append(False)
    return array

def findResult_cholesterol(items):
    array = []
    for nutrient in items:
        if nutrient < 20:
            array.append(True)
        else:
            array.append(False)
    return array

def getLabelPieBar(macronutrients, vitamins, minerals, others):
    labelPie = []
    labelBar = []

    # Start from the index number 1 since index 0 doesn't count as the value for index 0 are Macronutrient, Vitamin, and/or Mineral.
    if macronutrients:
        labelPie = macronutrients[1::]

    if vitamins and minerals and others:
        labelBar = vitamins[1::] + minerals[1::] + others[1::]
    return labelPie, labelBar

def createLabel(arrayPie, labelPie):
    percentageArray = []
    try:
        if len(arrayPie) != len(labelPie):
            raise ValueError("The 2 arrays have different length!")
        for i in range(len(arrayPie)):
            if arrayPie[i] == 0:
                percentageArray.append(f"{labelPie[i]}: 0.0%")
            else:
                percentageArray.append(f"{labelPie[i]}: {(round((arrayPie[i] / sum(arrayPie)) * 100, 2))}%")
        return percentageArray
    except ValueError:
        raise



def concatBarX(arrayValue):
    """
   .concatenate had to be done for valueBar specifically straight up just because
   Sodium comes up BEFORE the other minerals.

   My initial plan for valueBar is to include all values for the Vitamin first and then Minerals after that.
    """
    concatResult = []
    if arrayValue:
        concatResult = np.concatenate((arrayValue[1:-1], arrayValue[0], arrayValue[-1]), axis=None)
    return concatResult

def checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray):
    defaultDropdown = ["Macronutrients", "Vitamins", "Minerals", "Others"]
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []

    # ERROR HANDLING
    for i in range(len(dropdownArray)):
        # checks if the value for said dropdown is default or not
        if dropdownArray[i] in defaultDropdown and (minArray[i] or maxArray[i]):
            errorChooseNutrient.append(dropdownArray[i])

        # checks if the min/max value is empty or not
        elif dropdownArray[i] not in defaultDropdown and (not minArray[i] or not maxArray[i]):
            errorInputValue.append(dropdownArray[i])

        elif dropdownArray[i] not in defaultDropdown and (minArray[i] and maxArray[i]):
            if minArray[i].isalpha() or maxArray[i].isalpha():
                errorInputValue.append(dropdownArray[i])
            elif float(minArray[i]) > float(maxArray[i]):
                errorComparisonValue.append(dropdownArray[i])
            else:
                filterRange(dropdownArray[i], float(minArray[i]), float(maxArray[i]), searchResultArray)
                isError = False

    return errorChooseNutrient, errorInputValue, errorComparisonValue, isError

def generateErrorMessage_value(nutrientError, inputError, comparisonError):
    nutrientMsg = ""
    inputMsg = ""
    comparisonMsg = ""
    if len(nutrientError) > 0:
        nutrientMsg = "Please choose a nutrient for " + ", ".join(nutrientError)
    if len(inputError) > 0:
        inputMsg = "Please fill the min/max value (Numerical values) for " + ", ".join(inputError)
    if len(comparisonError) > 0:
        comparisonMsg = "Please make sure the min value is not higher than the max value for " + ", ".join(
            comparisonError)
    return nutrientMsg, inputMsg, comparisonMsg

def checkRadioAndDropdown_level(radioValue, dropdownValue):
    errorMsgRadio = ""
    errorMsgDropdown = ""
    isError = True
    if radioValue == "None" and dropdownValue != "Choose a nutrient":
        errorMsgRadio = "Nutrition level cannot be none!"
    if radioValue != "None" and dropdownValue == "Choose a nutrient":
        errorMsgDropdown = "Please choose a nutrient to filter the nutrition level with."
    if radioValue != "None" and dropdownValue != "Choose a nutrient":
        isError = False
    return errorMsgRadio, errorMsgDropdown, isError

def checkResult(finalResult):
    if len(finalResult) > 0:
        return f"{len(finalResult)} result(s) were found!"
    else:
        return "No result(s) were found."

def filterRange(dropdownArrayIndex, minValueIndex, maxValueIndex, searchResult_filter):
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv")

    nutrients = dataFrame[dropdownArrayIndex]
    loc = []

    for nutrient in nutrients:
        if minValueIndex <= nutrient <= maxValueIndex:
            loc.append(True)
        else:
            loc.append(False)

    searchResult = dataFrame[loc]
    searchResult = searchResult[["food"]]
    searchResult_filter.append(searchResult)

def filterLevel(maxValueDict, dropdownValue, levelFilter):
    # print(maxValueDict, dropdownValue)
    # print("Max for", dropdownValue, ":", maxValueDict[dropdownValue])
    maxValueNutrient = maxValueDict[dropdownValue]
    lowThreshold = 0.33 * maxValueNutrient
    highThreshold = 0.66 * maxValueNutrient
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv")
    nutrients = dataFrame[dropdownValue]
    loc = []

    for nutrient in nutrients:
        if levelFilter == "Low" and nutrient < lowThreshold:
            loc.append(True)
        elif levelFilter == "Medium" and (lowThreshold <= nutrient <= highThreshold):
            loc.append(True)
        elif levelFilter == "High" and nutrient > highThreshold:
            loc.append(True)
        else:
            loc.append(False)

    searchResult = dataFrame[loc]
    searchResult = searchResult[["food"]]
    return searchResult

def mergeResult_filterRange(searchResultArray_value):
    # print(searchResultArray_value)
    mergedResult = pd.DataFrame(columns=["food"])
    if len(searchResultArray_value) > 1:
        for i in range(1, len(searchResultArray_value)):
            mergedResult = searchResultArray_value[0].merge(searchResultArray_value[i], on="food", how="inner")
    elif len(searchResultArray_value) == 1:
        mergedResult = searchResultArray_value[0]
    return mergedResult

def mergeResult_everything(isError_value, minValueArray, isError_level, levelValue, searchResult_value, searchResult_level, searchResult_diet):
    mergedDataframe = []

    # print("BEFORE:", len(mergedDataframe))

    if not isError_value and any(value != "" for value in minValueArray):
        # print("VALUE:", searchResult_value)
        mergedDataframe.append(searchResult_value)
    if not isError_level and levelValue != "None":
        # print("LEVEL:", searchResult_level)
        mergedDataframe.append(searchResult_level)
    if not searchResult_diet.empty:
        # print("DIET:", searchResult_diet)
        mergedDataframe.append(searchResult_diet)
    # print("AFTER:", len(mergedDataframe))

    if len(mergedDataframe) == 0:
        return pd.DataFrame(columns=["food"])

    # I geniunely dunno why I had to this.
    # mergedDataFrame = mergedDataFrame[0] doesn't work and it took me 2-3 hours to figure it out.
    mergedResult = mergedDataframe[0]

    for i in range(1, len(mergedDataframe)):
        mergedResult = mergedResult.merge(mergedDataframe[i], on="food", how="inner")

    return mergedResult

def findNutritionValue(labelAll, dataFrame):
    maxDict = dict()

    try:
        if not labelAll:
            raise ValueError("This array cannot be empty")
        for label in labelAll:
            maxDict[label] = dataFrame[label].max()
        return maxDict
    except ValueError:
        raise


def checkDiet(dietDropdown):
    if dietDropdown == "Dietary Needs":
        return ""
    elif dietDropdown == "Ketogenic Diet":
        return "Ketogenic Diet - Searches for foods that are low in carbohydrates. (Less than 5-10% of the caloric intake)"
    elif dietDropdown == "Low Sodium Diet":
        return "Low Sodium Diet - Searches for foods that are low in sodium content. (Less than 140mg per serving)"
    else:
        return "Low Cholesterol Diet - Searches for foods that have less than 20mg of cholesterol per serving."

def checkRadio(radioValue):
    if radioValue == "None":
        return ""
    elif radioValue == "Low":
        return "Nutrition Level: Low - Searches for foods that have less than 33% of the highest value for the selected nutrient."
    elif radioValue == "Medium":
        return "Nutrition Level: Medium - Searches for foods that have between 33% and 66% of the highest value for the selected nutrient."
    else:
        return "Nutrition Level: High - Searches for foods that have greater than 66% of the highest value for the selected nutrient."

def errorChecking_filters(isError_filterValue, isError_filterLevel, searchResultArray_value, maxValueDict, nutrientFilter, nutritionLevel, diet):
    # Ensures that there are no errors.
    searchResult_valueFinal = pd.DataFrame(columns=["food"])
    searchResult_level = pd.DataFrame(columns=["food"])
    searchResult_diet = pd.DataFrame(columns=["food"])

    if not isError_filterValue:
        searchResult_valueFinal = mergeResult_filterRange(searchResultArray_value)
        # print("FILTER VALUE:", searchResult_valueFinal)
    if not isError_filterLevel:
        searchResult_level = filterLevel(maxValueDict, nutrientFilter, nutritionLevel)
        # print("FILTER LEVEL:", searchResult_level)
    searchResult_diet = filterDiet(diet)
    # print("FILTER DIET:", searchResult_diet)

    return searchResult_valueFinal, searchResult_level, searchResult_diet

def processFinalResult(isError_value, minValueArray, isError_level, levelValue, searchResult_valueFinal, searchResult_level, searchResult_diet, errorMessages, defaultDropdown, dropdownArray, minArray, maxArray, nutritionLevel, nutrientFilter, diet):
    """
    Basically handles merging the final result.
    Checks if the final results is empty or None.
    Also returns a message that tells the filter result.
    """
    mergeResult = []
    searchResultMsg = ""

    # If there are no error messages, do the merging.
    """
    The logic here is that no error messages = no errors in the filter.
    There could be a better way to do this but I'm too sleep deprived to figure it out
    """
    if all(value == "" for value in minArray) and all(value == "" for value in maxArray) and defaultDropdown == dropdownArray and nutritionLevel == "None" and nutrientFilter == "Choose a nutrient" and diet == "Dietary Needs":
        dataFrame = loadData(r"Food_Nutrition_Dataset.csv", True)
        searchResultMsg = "No filter was chosen."
        return dataFrame, searchResultMsg
    if all(errorMessage == "" for errorMessage in errorMessages):
        mergeResult = mergeResult_everything(isError_value, minValueArray, isError_level, levelValue, searchResult_valueFinal, searchResult_level, searchResult_diet)
        searchResultMsg = checkResult(mergeResult)
        return mergeResult, searchResultMsg

    # Returns the whole data if the user didn't choose any filter. Think of it as a way to "reset" the filter.

    # If the merge is empty then below gets returned instead.
    return mergeResult, searchResultMsg

def determineFoodSearch(dataFrame, mergedResult, keyword):
    """
    Checks whether the user have done a filter or not.
    If not, then use the whole dataframe to search through the user's input.
    Else, use the filtered result to search through the user's input.
    """
    if mergedResult.empty:
        foods = dataFrame["food"]
        loc = findResult_generic(keyword, foods)
        searchResult = dataFrame[loc]
        return searchResult
    else:
        foods = mergedResult["food"]
        loc = findResult_generic(keyword, foods)
        searchResult = mergedResult[loc]
        return searchResult

def loadData(file, optionalLine=False):
    dataFrame = loadCSVFile(file)
    if optionalLine:
        dataFrame = dataFrame[["food"]]
    dataFrame = DataTable(dataFrame)
    dataFrame = dataFrame.data
    return dataFrame

def loadCSVFile(filePath):
    try:
        return pd.read_csv(filePath)
    except FileNotFoundError:
        raise Exception("File not found.")
