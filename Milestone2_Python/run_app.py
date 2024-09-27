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

from template_frame import NutritionApp as Frame1

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'

colorBar = [
    '#FF5733',
    '#33FF57',
    '#3357FF',
    '#FF33FF',
    '#FFFF33',
    '#FF8C33',
    '#33FFF6',
    '#9933FF',
    '#FF3333',
    '#33FF99',
    '#3375FF',
    '#FF3399',
    '#FFC300',
    '#DAF7A6',
    '#C70039',
    '#900C3F',
    '#581845',
    '#FFC0CB',
    '#6495ED',
    '#B8860B',
    '#7FFF00',
    '#FF6347'
]

colorPie = [
    '#FF5733',
    '#33FF57',
    '#3357FF',
    '#FFFF33',
    '#FF33FF',
    '#33FFF6',
    '#9933FF',
    '#B8860B'
]

class DataTable(wx.grid.GridTableBase):
    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        self.data = data

    def GetNumberRows(self):
        return len(self.data.index)

    def GetNumberCols(self):
        return len(self.data.columns)

    def GetValue(self, row, col):
        return self.data.iloc[row, col]

    def SetValue(self, row, col, value):
        self.data.iloc[row, col] = value

    # For better visualisation
    def GetColLabelValue(self, col):
        return self.data.columns[col]

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr


class CalcFrame(Frame1):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.dfMacro_value = []
        self.dfVitamin_value = []
        self.dfMineral_value = []
        self.dfOther_value = []

        self.searchResult_value = []
        self.searchResult_valueFinal = []
        self.searchResult_level = []
        self.searchResult_diet = []

        global filterMacro
        global filterVitamin
        global filterMineral
        global filterOther
        global diet

        FilterMacro = ""
        FilterVitamin = ""
        FilterMineral = ""
        FilterOther = ""
        diet = 0

        # Remove/comment the line below if you want to see every column.
        self.df = self.loadData(r"Food_Nutrition_Dataset.csv", True)
        self.loadTable(self.df)

        # Start from the index number 1 since index 0 doesn't count as the value for index 0 are Macronutrient, Vitamin, and/or Mineral.
        self.labelPie = self.choiceMacro.GetStrings()[1::]
        self.labelBar = self.choiceVitamin.GetStrings()[1::] + self.choiceMineral.GetStrings()[1::] + self.choiceOther.GetStrings()[1::]

        dataForLabel = pd.read_csv(r"Food_Nutrition_Dataset.csv")
        self.label = list(dataForLabel.columns[1::])

        self.value = []

        self.Show(True)
        self.Layout()

        self.maxValueDict = self.findNutritionValue()

    def findNutritionValue(self):
        maxDict = dict()
        dataFrame = self.loadData(r"Food_Nutrition_Dataset.csv")
        labelAll = self.label
        for label in labelAll:
            maxDict[label] = dataFrame[label].max()
        return maxDict


    def explanationText( self, event ):
        labelText = self.checkRadio()
        self.text_filterResult.SetLabel(labelText)

    def explanationText_diet( self, event ):
        labelText = self.checkDiet()
        self.text_filterResult.SetLabel(labelText)

    def checkDiet(self):
        dietDropdown = self.choiceDiet.GetStringSelection()
        if(dietDropdown == "Dietary Needs"):
            return ""
        elif dietDropdown == "Ketogenic Diet":
            return "Ketogenic Diet - Searches for foods that are low in carbohydrates. (Less than 5-10% of the caloric intake)"
        elif dietDropdown == "Low Sodium Diet":
            return "Low Sodium Diet - Searches for foods that are low in sodium content. (Less than 140mg per serving) "
        elif dietDropdown == "Low Cholesterol Diet":
            return "Low Cholesterol Diet - Searches for foods that have less than 20mg of cholesterol per serving."
    
    def checkRadio(self):
        radioValue = self.nutritionLevelFilter.GetStringSelection()
        if(radioValue == "None"):
            return ""
        elif(radioValue == "Low"):
            return "Nutrition Level: Low - Searches for foods that have less than 33% of the highest value for the selected nutrient."
        elif(radioValue == "Medium"):
            return "Nutrition Level: Medium - Searches for foods that have between 33% and 66% of the highest value for the selected nutrient."
        else:
            return "Nutrition Level: High - Searches for foods that have greater than 66% of the highest value for the selected nutrient."
    def loadData(self, file, optionalLine = False):
        dataFrame = pd.read_csv(file)
        if optionalLine:
            dataFrame = dataFrame[["food"]]
        dataFrame = DataTable(dataFrame)
        dataFrame = dataFrame.data
        return dataFrame

    def loadTable(self, dataFrame):
        table = DataTable(dataFrame)
        self.foodData.SetTable(table, takeOwnership=True)
        self.foodData.EnableEditing(False)
        self.foodData.SetColSize(0, 350)

    def test(self, event):
        """
        I found out that adding a custom function in "OnGridCellLeftClick" does some
        funny stuff to the default behavior.
        What I mean is that there was no grid at all when we click on a column because
        I assigned "OnGridCellLeftClick" to a new function.

        .SetGridCursor() allows us to replicate the default behavior where the column we are currently clicking at
        will have a border/grid around it. There might be a better way to do this, but I can't be asked.
        """

        # This also lets us get the name the content that's in that row.
        row = event.GetRow()
        col = event.GetCol()

        # "Highlights" the current column that's being chosen
        self.foodData.SetGridCursor(row, col)

        # [row, 0] ensures that we only get the food name.
        foodName = self.df.iloc[row, 0]
        # print(foodName)

        # Searches for the food(s) based on user's CLICK input
        dataFrame = self.loadData(r".\Food_Nutrition_Dataset.csv", False)
        searchData = dataFrame["food"]

        loc = []
        for item in searchData:
            if re.findall(foodName, item):
                loc.append(True)
            else:
                loc.append(False)
        search_result = dataFrame[loc]

        # Iterate and store each nutrient to the appropriate place.
        # Anything related to Vitamin goes to the array that's for pie chart, while the rest goes to the bar chart.
        labelAll = self.label
        percentageBar = []
        percentagePie = []
        valueBar = []
        valuePie = []

        # print(search_result.iloc[0])

        for i in range(len(labelAll)):
            if labelAll[i] in self.labelBar:
                valueBar.append(search_result.iloc[0][labelAll[i]])
            elif labelAll[i] in self.labelPie:
                valuePie.append(search_result.iloc[0][labelAll[i]])

        """
        .concatenate had to be done for valueBar specifically straight up just because 
        Sodium comes up BEFORE the other minerals.
        
        My initial plan for valueBar is to include all values for the Vitamin first and then Minerals after that.
        """
        valueBar = np.concatenate((valueBar[1:-1], valueBar[0], valueBar[-1]), axis=None)

        # Creates the label for pie chart
        for i in range(len(valuePie)):
            percentagePie.append(f"{self.labelPie[i]}: {(round((valuePie[i]/sum(valuePie))* 100, 2))}%")
        self.createChart(self.pieChartPlot(percentagePie, valuePie, colorPie), self.pieChartPanel)
        self.createChart(self.barChartPlot(percentageBar, valueBar, colorBar), self.barChartPanel)

    def createChart(self, plotChart, panel):
        chart = plotChart
        h, w = panel.GetSize()
        chart.set_size_inches(h / chart.get_dpi(), w / chart.get_dpi())
        canvas = FigureCanvasWxAgg(panel, -1, chart)
        canvas.SetSize(panel.GetSize())

    def barChartPlot(self, labelArray, valueArray, colorArray):
        x = self.labelBar
        y = valueArray
        colors = colorArray
        barChart, (ax1) = plt.subplots(1)

        barChart.subplots_adjust(top=0.93, bottom=0.25)

        bars = ax1.bar(x, y, color=colors)
        # print(len(bars))

        """
        The code to set the text above the bars were mostly obtained from Stackoverflow:
        https://stackoverflow.com/questions/40489821/how-to-write-text-above-the-bars-on-a-bar-plot-python
        
        However, I modified the code to fit it into the context of this software.
        """
        for i in range(len(bars)):
            bar = bars[i]
            value = valueArray[i]
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2.0, value, f'{height:.0f}', ha='center', va='bottom', fontsize="6")

        plt.yticks(fontsize=6)

        # Rotates the label in x axis by 90 degress
        plt.xticks(rotation=90, fontsize=7)
        ax1.set_title('Vitamins, Macronutrients, and Others', fontsize=7)
        return barChart

    def pieChartPlot(self, labelArray, valueArray, colorArray):
        labels = labelArray
        sizes = valueArray
        colors = colorArray

        # Since the value of explode will be same for every section, we can just multiply the array with the label's length
        explode = [0.05] * len(self.labelPie)
        pieChart, (ax1) = plt.subplots(1)

        # Moves the chart to the left. This was done so we can see the legend as well
        pieChart.subplots_adjust(left=0.1, right=0.5)

        ax1.set_title('Minerals')
        ax1.pie(sizes, explode=explode, colors=colors, shadow=True)

        # This lets us set the legend to the right side of the chart.
        ax1.legend(labels, loc="center left", bbox_to_anchor=(1, 0.5), fontsize=8)

        ax1.axis('equal')
        return pieChart

    # def searchFood( self, event ):
    #     key_word = self.searchInput.GetValue()
    #     key_word = key_word.lower()
    #
    # Ensures that only the food row is shown in the table.
    # df = pd.read_csv(r".\Food_Nutrition_Dataset.csv")
    # df = df[["food"]]
    #
    #     foods = df["food"]
    #     loc = []
    #     for item in foods:
    #         if re.findall(key_word, item):
    #             loc.append(True)
    #         else:
    #             loc.append(False)
    #
    #     search_result = df[loc]
    #     tabel = DataTable(search_result)
    #     self.foodData.ClearGrid()
    #     self.foodData.SetTable(tabel,True)
    #     self.foodData.EnableEditing(False)

    #     self.foodData.SetColSize(0, 350)
    ## self.foodData.AutoSize()
    #
    #     num_rows = sum(loc)
    #     label_to_static_txt = "The number of rows: "+str(num_rows)
    #     self.extraInfo.SetLabel(label_to_static_txt)
    #
    #     self.Layout()

    def searchFood( self, event ):
        # sets the df to the table
        df = self.table.data

        # initalises the filter condition
        filter_condition = pd.Series([True] * len(df))

        # pulls the min and the max values
        minValueInput = self.minValueInput.GetValue()
        maxValueInput = self.maxValueInput.GetValue()

        # chacks for if the min value is empty or not
        if minValueInput == "":
            # if its left empty set it to 0
            minValueInput = 0
        else:
            # loops through and checks if it has letter
            for i in minValueInput:
                if i.isalpha():
                    # if its left empty set it to 0
                    minValueInput = 0
            # makes the value a float inseatd of a string
            minValueInput = float(minValueInput)

        # chacks for if the max value is empty or not
        if maxValueInput == "":
            maxValueInput = 99999

        else:
            for i in maxValueInput:
                # loops through and checks if it has a letter
                if i.isalpha():
                    # if its left empty set it to a high number
                    maxValueInput = 99999
            # makes the value a float inseatd of a string
            maxValueInput = float(maxValueInput)

        # adds all the filtered options to the search if there not empty (aka the defult was selected)
        if FilterOther != "":
            filter_condition &= (df[FilterOther] >= minValueInput) & (df[FilterOther] <= maxValueInput)

        if FilterMineral != "":
            filter_condition &= (df[FilterMineral] >= minValueInput) & (df[FilterMineral] <= maxValueInput)

        if FilterVitamin != "":
            filter_condition &= (df[FilterVitamin] >= minValueInput) & (df[FilterVitamin] <= maxValueInput)

        if FilterMacro != "":
            filter_condition &= (df[FilterMacro] >= minValueInput) & (df[FilterMacro] <= maxValueInput)


        #Diet option filters
        if diet != 0:
            #filter for keto diets
            if diet == 1:
                filter_condition &= ((df["Carbohydrates"]) <= ((df["Caloric Value"])*0.1))
            #filter for low sodium diets
            if diet == 2:
                filter_condition &= (df["Sodium"] < 140)
            #for the low colesterol diets
            if diet == 3:
                filter_condition &= (df["Cholesterol"] < 20)


                # searchess based on the key word uses strip and lower to remove case sensitivity
        key_word = self.searchInput.GetValue().strip().lower()
        # runs only if key word is not empty
        if key_word:
            filter_condition &= df['food'].str.contains(key_word, case=False, na=False)

        # runs the search using the made filter conditions
        filtered_df = df[filter_condition]
        #print(filtered_df)

        # make the table of data
        self.foodData.ClearGrid()
        self.foodData.BeginBatch()
        self.foodData.SetTable(DataTable(filtered_df), True)
        self.foodData.EndBatch()
        #self.foodData.AutoSize()

        self.foodData.SetColSize(0, 350)

        # returns  the result of the number of results
        self.extraInfo.SetLabel(f"Results found: {len(filtered_df)}")

        self.Layout()

    def filterFood(self, event):
        # .GetStringCollection() -> Gets the string
        # .GetSelection() -> gets the number

        # Resets the value everytime the filter button is clicked
        self.searchResult_value = []
        self.searchResult_valueFinal = pd.DataFrame(self.searchResult_value, columns=["food"])
        self.searchResult_level = pd.DataFrame(self.searchResult_level, columns=["food"])
        self.searchResult_diet = pd.DataFrame(self.searchResult_diet, columns=["food"])

        mergeResult = []

        macro = self.choiceMacro.GetStringSelection()
        vitamin = self.choiceVitamin.GetStringSelection()
        mineral = self.choiceMineral.GetStringSelection()
        other = self.choiceOther.GetStringSelection()
        nutritionLevel = self.nutritionLevelFilter.GetStringSelection()
        nutrientFilter = self.choiceNutrient.GetStringSelection()
        diet = self.choiceDiet.GetStringSelection()

        # Only 1 filter is allowed
        filterCounter = 0

        # ARRAY AND VARIABLES FOR NUTRITION LEVEL
        errorRadio = ""
        errorDropdown = ""

        # MIN/MAX VALUE - NUTRITION VALUE
        minMacro = self.minValueInput_macro.GetValue()
        maxMacro = self.maxValueInput_macro.GetValue()

        minVitamin = self.minValueInput_vitamin.GetValue()
        maxVitamin = self.maxValueInput_vitamin.GetValue()

        minMineral = self.minValueInput_mineral.GetValue()
        maxMineral = self.maxValueInput_mineral.GetValue()

        minOther = self.minValueInput_other.GetValue()
        maxOther = self.maxValueInput_other.GetValue()

        # ARRAY AND VARIABLES FOR NUTRITION VALUE (Error messages, the actual filter, etc)
        errorMsgOne = ""
        errorMsgTwo = ""
        errorMsgThree = ""
        isError_filterValue = True
        isError_filterLevel = True
        isNotChosen_filterDiet = True
        dropdownArray = [macro, vitamin, mineral, other]
        minArray = [minMacro, minVitamin, minMineral, minOther]
        maxArray = [maxMacro, maxVitamin, maxMineral, maxOther]

        errorNutrient = []
        errorValue = []
        errorComparison = []

        minValueInput = self.minValueInput_macro.GetValue()
        maxValueInput = self.maxValueInput_macro.GetValue()
        choiceDiet = self.choiceDiet.GetSelection()

        # ERROR CHECKING
            # A. Nutrition Value
        print(dropdownArray, minArray, maxArray)
        errorNutrient, errorValue, errorComparison, isError_filterValue, filterCounter = self.checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError_filterValue, filterCounter)
        errorMsgOne, errorMsgTwo, errorMsgThree = self.generateErrorMessage_value(errorNutrient, errorValue, errorComparison)

            # B. Nutrition Level
        errorRadio, errorDropdown, isError_filterLevel, filterCounter = self.checkRadioAndDropdown_level(nutritionLevel, nutrientFilter, filterCounter)

            # C. Diet Level
        isNotChosen_filterDiet, filterCounter = self.checkDropdown_diet(diet, filterCounter)


        # SETTING THE ERROR MESSAGE
        self.errorMsg_filterValue1.SetLabel(errorMsgOne)
        self.errorMsg_filterValue2.SetLabel(errorMsgTwo)
        self.errorMsg_filterValue3.SetLabel(errorMsgThree)
        self.errorMsg_level1.SetLabel(errorRadio)
        self.errorMsg_level2.SetLabel(errorDropdown)

        # Ensures that the filters only happen if there are no errors
        if not isError_filterValue:
            self.searchResult_valueFinal = self.mergeResult_filterRange(self.searchResult_value)
            # print("FILTER VALUE:", self.searchResult_value)
        elif not isError_filterLevel:
            self.searchResult_level = self.filterLevel(self.maxValueDict, nutrientFilter, nutritionLevel)
            # print("FILTER LEVEL:", self.searchResult_level)
        elif not isNotChosen_filterDiet:
            self.searchResult_diet = self.filterDiet(diet)
            # print("FILTER DIET:", self.searchResult_diet)
        else:
            pass

        mergeResult = self.mergeResult_everything(self.searchResult_valueFinal, self.searchResult_level, self.searchResult_diet)

        print("FINAL RESULT:", mergeResult)

        # DISPLAY SEARCH RESULT TO TABLE

        # PRINT RESULT

        # ARRAY AND VARIABLES FOR NUTRITION LEVEL
        errorRadio = False
        errorDropdown = False

        if minValueInput == "":
            minValueInput = 0

        if maxValueInput == "":
            maxValueInput = 99999

        else:
            for i in maxValueInput:
                if i.isalpha():
                    maxValueInput = 99999


        # global diet
        diet = self.choiceDiet.GetSelection()

        self.makeSerchStatment(macro, vitamin, mineral, other, minValueInput, maxValueInput, nutritionLevel, choiceDiet)

    def checkDropdownAndInput_value(self, dropdownArray, minArray, maxArray, isError, counter):
        defaultDropdown = ["Macronutrients", "Vitamins", "Minerals", "Others"]
        errorChooseNutrient = []
        errorInputValue = []
        errorComparisonValue = []

        # ERROR HANDLING
        if dropdownArray != defaultDropdown:
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
                        self.filterRange(dropdownArray[i], float(minArray[i]), float(maxArray[i]), self.searchResult_value)
                        counter += 1
                        isError = False

        return errorChooseNutrient, errorInputValue, errorComparisonValue, isError, counter

    def generateErrorMessage_value(self, nutrientError, inputError, comparisonError):
        nutrientMsg = ""
        inputMsg = ""
        comparisonMsg = ""
        if len(nutrientError) > 0:
            nutrientMsg = "Please choose a nutrient for " + ", ".join(nutrientError)
        if len(inputError) > 0:
            inputMsg = "Please fill the min/max value (Numerical values) for " + ", ".join(inputError)
        if len(comparisonError) > 0:
            comparisonMsg = "Please make sure the min value is not higher than the max value for " + ", ".join(comparisonError)
        return nutrientMsg, inputMsg, comparisonMsg

    def checkRadioAndDropdown_level(self, radioValue, dropdownValue, counter):
        errorMsgRadio = ""
        errorMsgDropdown = ""
        isError = True
        if radioValue == "None" and dropdownValue != "Choose a nutrient":
            errorMsgRadio = "Nutrition level cannot be none!"
        if radioValue != "None" and dropdownValue == "Choose a nutrient":
            errorMsgDropdown = "Please choose a nutrient to filter the nutrition level with."
        if radioValue != "None" and dropdownValue != "Choose a nutrient":
            isError = False
            counter += 1
        return errorMsgRadio, errorMsgDropdown, isError, counter

    def checkDropdown_diet(self, dropdownValue, counter):
        if dropdownValue != "Dietary Needs":
            counter += 1
            return False, counter
        else:
            return True, counter

    def filterDiet(self, dropdownValue):
        dataFrame = self.loadData(r".\Food_Nutrition_Dataset.csv")
        loc = []

        if dropdownValue == "Ketogenic Diet":
            nutrientsCarbo = dataFrame["Carbohydrates"]
            nutrientsCal = dataFrame["Caloric Value"]
            for i in range(len(nutrientsCarbo)):
                if nutrientsCarbo[i] < (nutrientsCal[i] * 0.10):
                    loc.append(True)
                else:
                    loc.append(False)

        if dropdownValue == "Low Sodium Diet":
            nutrients = dataFrame["Sodium"]
            for nutrient in nutrients:
                if nutrient < 140:
                    loc.append(True)
                else:
                    loc.append(False)

        if dropdownValue == "Low Cholesterol Diet":
            nutrients = dataFrame["Cholesterol"]
            for nutrient in nutrients:
                if nutrient < 20:
                    loc.append(True)
                else:
                    loc.append(False)

        searchResult = dataFrame[loc]
        searchResult = searchResult[["food"]]
        return searchResult

    def filterRange(self, dropdownArrayIndex, minValueIndex, maxValueIndex, searchResult_filter):
        dataFrame = self.loadData(r".\Food_Nutrition_Dataset.csv")

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
        return searchResult
        # ^ This is still a DataFrame

        # Updates self.df to the current result, so it works :)))))
        # self.df = searchResult
        # self.foodData.ClearGrid()
        # self.loadTable(self.df)
        # self.Layout()

    def filterLevel(self, maxValueDict, dropdownValue, levelFilter):
        # print(maxValueDict, dropdownValue)
        # print("Max for", dropdownValue, ":", maxValueDict[dropdownValue])
        maxValueNutrient = maxValueDict[dropdownValue]
        lowThreshold = 0.33 * maxValueNutrient
        highThreshold = 0.66 * maxValueNutrient
        dataFrame = self.loadData(r".\Food_Nutrition_Dataset.csv")
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

    def mergeResult_filterRange(self, searchResultArray_value):
        mergedResult = []
        if len(searchResultArray_value) > 1:
            for i in range(1, len(searchResultArray_value)):
                mergedResult = searchResultArray_value[0].merge(searchResultArray_value[i], on="food", how="inner")
        else:
            mergedResult = searchResultArray_value[0]
        return mergedResult

    def mergeResult_everything(self, searchResult_value, searchResult_level, searchResult_diet):
        # Basically prevents empty array being used as the "base" for the merge
        mergedDataframe = []
        print("1", searchResult_value.columns)
        print("2", searchResult_level.columns)
        print("3", searchResult_diet.columns)

        if not searchResult_value.empty:
            mergedDataframe.append(searchResult_value)
        if not searchResult_level.empty:
            mergedDataframe.append(searchResult_level)
        if not searchResult_diet.empty:
            mergedDataframe.append(searchResult_diet)

        if len(mergedDataframe) > 1:
            for i in range(1, len(mergedDataframe)):
                mergedDataframe = mergedDataframe[0].merge(mergedDataframe[i], on="food", how="inner")
        elif len(mergedDataframe) == 0:
            return None
        else:
            mergedDataframe = mergedDataframe[0]
        return mergedDataframe

    # def checkCounter(self):
    #     if counter > 1

    def makeSerchStatment(self, Macro, Vitamin, Mineral, Other, minValueInput, maxValueInput, nutritionLevel, choiceDiet):
        # comment/Uncomment the below prints to see the value of each when filter button is pressed
        # print("===========================")
        # print("Macro: ", Macro)
        # print("Vitamin :", Vitamin)
        # print("Mineral :", Mineral)
        # print("Other :", Other)
        # print("minValueInput :", minValueInput)
        # print("maxValueInput :", maxValueInput)
        # print("nutritionLevel :", nutritionLevel)
        # print("choiceDiet :", choiceDiet)
        # print("===========================")

        self.searchText = ""

        # sets the filtered options as global so that they can be used in the search function
        global FilterMacro
        global FilterVitamin
        global FilterMineral
        global FilterOther

        # sets what mactro is selected
        if Macro != 0:
            if Macro == 1:
                Macro = "Fat"
            elif Macro == 2:
                Macro = "Saturated Fats"
            elif Macro == 3:
                Macro = "Monounsaturated Fats"
            elif Macro == 4:
                Macro = "Polyunsaturated Fats"
            elif Macro == 5:
                Macro = "Carbohydrates"
            elif Macro == 6:
                Macro = "Sugars"
            elif Macro == 7:
                Macro = "Protein"
            elif Macro == 8:
                Macro = "Dietary Fiber"

            # addes the selected macro to the console so you can see the result
            print("Selected macro: ", Macro)

            # sets the filtered macro for later use in the search function
            FilterMacro = Macro
        else:
            FilterMacro = ""

        # sets what Vitamin is selected
        if Vitamin != 0:
            if Vitamin == 1:
                Vitamin = "Vitamin B1"
            elif Vitamin == 2:
                Vitamin = "Vitamin B2"
            elif Vitamin == 3:
                Vitamin = "Vitamin B3"
            elif Vitamin == 4:
                Vitamin = "Vitamin B5"
            elif Vitamin == 5:
                Vitamin = "Vitamin B6"
            elif Vitamin == 6:
                Vitamin = "Vitamin B11"
            elif Vitamin == 7:
                Vitamin = "Vitamin B12"
            elif Vitamin == 8:
                 Vitamin = "Vitamin C"
            elif Vitamin == 9:
                Vitamin = "Vitamin D"
            elif Vitamin == 10:
                Vitamin = "Vitamin E"
            elif Vitamin == 11:
                Vitamin = "Vitamin K"


            # sets the filtered Vitamin for later use in the search function
            FilterVitamin = Vitamin

            # addes the selected Vitamin to the console so you can see the result
            print("Selected Vitamin: ", Vitamin)

        else:
            FilterVitamin = ""

        # sets what Vitamin is selected
        if Mineral != 0:
            if Mineral == 1:
                Mineral = "Calcium"
            elif Mineral == 2:
                Mineral = "Copper"
            elif Mineral == 3:
                Mineral = "Iron"
            elif Mineral == 4:
                Mineral = "Magnesium"
            elif Mineral == 5:
                Mineral = "Manganese"
            elif Mineral == 6:
                Mineral = "Phosphorus"
            elif Mineral == 7:
                Mineral = "Potassium"
            elif Mineral == 8:
                Mineral = "Selenium"
            elif Mineral == 9:
                Mineral = "Zinc"

            # sets the filtered Mineral for later use in the search function
            FilterMineral = Mineral

            # addes the selected Mineral to the console so you can see the result
            print("Selected Mineral: ", Mineral)

        else:
            FilterMineral = ""

        # sets what Other is selected
        if Other != 0:
            if Other == 1:
                Other = "Cholesterol"
            elif Other == 2:
                Other = "Water"
            elif Other == 3:
                Other = "Nutrition Density"


             # sets the filtered Other for later use in the search function
            FilterOther = Other

            # addes the selected Other to the console so you can see the result
            print("Selected Other: ", Other)

        else:
            FilterOther = ""

if __name__ == "__main__":
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()