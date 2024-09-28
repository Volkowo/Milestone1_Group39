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

def findResult_generic(searchInput, array, items):
    for item in items:
        if re.findall(searchInput.lower(), item):
            array.append(True)
        else:
            array.append(False)
    return array

def findResult_breakdown(allLabel, labelBar, labelPie, searchResult):
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
        loc = findResult_keto(nutrientsCarbo, nutrientsCal, loc)

    if dropdownValue == "Low Sodium Diet":
        nutrients = dataFrame["Sodium"]
        loc = findResult_sodium(nutrients, loc)

    if dropdownValue == "Low Cholesterol Diet":
        nutrients = dataFrame["Cholesterol"]
        loc = findResult_cholesterol(nutrients, loc)

    if dropdownValue == "Dietary Needs":
        return dataFrame[["food"]]

    searchResult = dataFrame[loc]
    searchResult = searchResult[["food"]]
    return searchResult

def findResult_keto(carbo, calorie, array):
    for i in range(len(carbo)):
        if carbo[i] < (calorie[i] * 0.10):
            array.append(True)
        else:
            array.append(False)
    return array

def findResult_sodium(items, array):
    for nutrient in items:
        if nutrient < 40:
            array.append(True)
        else:
            array.append(False)
    return array

def findResult_cholesterol(items, array):
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
    labelPie = macronutrients[1::]
    labelBar = vitamins[1::] + minerals[1::] + others[1::]
    return labelPie, labelBar

def createLabel(arrayPie, labelPie):
    percentageArray = []
    for i in range(len(arrayPie)):
        if arrayPie[i] == 0:
            percentageArray.append(f"{labelPie[i]}: 0.0%")
        else:
            percentageArray.append(f"{labelPie[i]}: {(round((arrayPie[i] / sum(arrayPie)) * 100, 2))}%")

    return percentageArray

def concatBarX(arrayValue):
    """
   .concatenate had to be done for valueBar specifically straight up just because
   Sodium comes up BEFORE the other minerals.

   My initial plan for valueBar is to include all values for the Vitamin first and then Minerals after that.
    """
    return np.concatenate((arrayValue[1:-1], arrayValue[0], arrayValue[-1]), axis=None)

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
    mergedResult = []
    if len(searchResultArray_value) > 1:
        for i in range(1, len(searchResultArray_value)):
            mergedResult = searchResultArray_value[0].merge(searchResultArray_value[i], on="food", how="inner")
    else:
        mergedResult = searchResultArray_value[0]
    return mergedResult

def mergeResult_everything(searchResult_value, searchResult_level, searchResult_diet):
    mergedDataframe = []

    # print("BEFORE:", len(mergedDataframe))

    if not searchResult_value.empty:
        # print("VALUE:", searchResult_value)
        mergedDataframe.append(searchResult_value)
    if not searchResult_level.empty:
        # print("LEVEL:", searchResult_level)
        mergedDataframe.append(searchResult_level)
    if not searchResult_diet.empty:
        # print("DIET:", searchResult_diet)
        mergedDataframe.append(searchResult_diet)
    # print("AFTER:", len(mergedDataframe))

    if len(mergedDataframe) == 0:
        return None

    # I geniunely dunno why I had to this.
    # mergedDataFrame = mergedDataFrame[0] doesn't work and it took me 2-3 hours to figure it out.
    mergedResult = mergedDataframe[0]

    for i in range(1, len(mergedDataframe)):
        mergedResult = mergedDataframe[0].merge(mergedDataframe[i], on="food", how="inner")

    return mergedResult

def findNutritionValue(labelAll, dataFrame):
    maxDict = dict()
    for label in labelAll:
        maxDict[label] = dataFrame[label].max()
    return maxDict

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
