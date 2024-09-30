# Unit Testing Report

[//]: # (Please provide your GitHub repository link.)
### GitHub Repository URL: https://github.com/Volkowo/Milestone1_Group39.git

---

[//]: # (The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to )

[//]: # (the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.)


## 1. **Test Summary**

[//]: # (list all tested functions related to the five required features and the corresponding test functions designed to test )

[//]: # (those functions, for example:)

| **Tested Functions**              | **Test Functions**                                       |
|-----------------------------------|----------------------------------------------------------|
| `loadCSVFile()`                   | `test_loadCSVExist()` <br> `test_loadFakeCSV()`           |
| `loadData()`                      | `test_loadDataWithoutOptionalLine()` <br> `test_loadDataWithOptionalLine()` <br> `test_loadDataWrongCSV()` |
| `findNutritionValue()`            | `test_findNutritionValue()` <br> `test_findNutritionValue_emptyLabel()` |
| `findResult_generic()`            | `test_genericSearch_ExactMatch()` <br> `test_genericSearch_partialMatch()` <br> `test_genericSearch_emptyInput()` <br> `test_genericSearch_emptyArray()` |
| `findResult_breakdown()`          | `test_breakdown()` <br> `test_breakdown_emptyEveryLabel()` <br> `test_breakdown_emptyLabelBar()` |
| `findResult_keto()`               | `test_findKeto()` <br> `test_findKeto_wrongLength()`      |
| `findResult_sodium()`             | `test_findSodium()` <br> `test_findSodium_empty()`        |
| `findResult_cholesterol()`        | `test_findCholesterol()` <br> `test_findCholesterol_empty()` |
| `filterDiet()`                    | `test_filterKeto()` <br> `test_filterSodium()` <br> `test_filterCholesterol()` <br> `test_filterNone()` |
| `getLabelPieBar()`                | `test_getLabelNotEmpty()` <br> `test_getLabelEmpty()` <br> `test_getLabelEmptyMacro()` <br> `test_getLabelEmptyOthers()` |
| `createLabel()`                   | `test_createLabel()` <br> `test_createLabel_diffLength()` |
| `concatBarX()`                    | `test_concatBarX()` <br> `test_concatBarX_empty()`        |
| `checkDropdownAndInput_value()`   | `test_checkDAI_defaultDropdownAndFilledInput()` <br> `test_checkDAI_diffDropdownAndEmptyInput()` <br> `test_checkDAI_diffDropdownAndAlphaInput()` <br> `test_checkDAI_minGreaterMax()` <br> `test_checkDAI_correct()` |
| `filterRange()`                   | `test_filterRange()`                                      |
| `generateErrorMessage_value()`    | `test_GEM_nutrient()` <br> `test_GEM_input()` <br> `test_GEM_comparison()` <br> `test_GEM_nutrientAndInput()` <br> `test_GEM_nutrientAndComparison()` <br> `test_GEM_inputAndComparison()` <br> `test_GEM_everyError()` <br> `test_GEM_noError()` |
| `checkRadioAndDropdown_level()`   | `test_checkRAD_radio()` <br> `test_checkRAD_dropdown()` <br> `test_checkRAD_noError()` |
| `checkResult()`                   | `test_checkResult_notEmpty()` <br> `test_checkResult_empty()` |
| `filterLevel()`                   | `test_filterLevel_low()` <br> `test_filterLevel_medium()` <br> `test_filterLevel_high()` <br> `test_filterLevel_wrongValue()` |
| `mergeResult_filterRange()`       | `test_mergeResult_moreThanOne()` <br> `test_mergeResult_one()` <br> `test_mergeResult_none()` |
| `mergeResult_everything()`        | `test_ME_emptyValue()` <br> `test_ME_emptyDiet()` <br> `test_ME_emptyLevel()` <br> `test_ME_everything()` <br> `test_ME_noValue()` <br> `test_ME_falseLevel()` <br> `test_ME_noMerge()` |
| `checkDiet()`                     | `test_CD_default()` <br> `test_CD_keto()` <br> `test_CD_sodium()` <br> `test_CD_cholesterol()` |
| `checkRadio()`                    | `test_CR_default()` <br> `test_CR_low()` <br> `test_CR_medium()` <br> `test_CR_high()` |
| `errorChecking_filters()`         | `test_ECF_errorLevel()` <br> `test_ECF_errorFilter()` <br> `test_ECF_onlyDiet()` <br> `test_ECF_noError()` |
| `processFinalResult()`            | `test_processFinalResult_noError()` <br> `test_processFinalResult_error()` <br> `test_processFinalResult_reset()` |
| `determineFoodSearch()`           | `test_determineFood_emptyMerged()` <br> `test_determinedFood_filledMerged()` |

---

## 2. **Test Case Details**

### Test Case 1:
- **Test Function/Module**
  - `test_loadCSVExist()`
  - `test_loadFakeCSV()`
- **Tested Function/Module**
  - `loadCSVFile(filepath)`
- **Description**
  - Brief Description:\
  The function will attempt to read and load the csv file.
  - Input:
    - Path to the .csv file.
  - Output:
    - The csv file being read by pandas
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output**           |
|-------------------------------|-------------------------------|
| `loadCSV(r".\Food_Nutrition_Dataset.csv")`               | The file being read by pandas |

- **1) Code for the Test Function**
```python
def test_loadCSVExist():                          
    wineData = loadCSVFile(r".\Food_Nutrition_Data
    assert isinstance(wineData, pd.DataFrame)     
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**        | **Expected Output**                            |
|--------------------------|------------------------------------------------|
| `divide(r"./fictionalCSV.csv")`               | Exception with the message `"File not found."` |

- **2) Code for the Test Function**
```python
def test_loadFakeCSV(file, optionalLine=False):                               
    with pytest.raises(Exception) as exc_info:        
        loadCSVFile(r"./fictionalCSV.csv")              
```
### Test Case 2:
- **Test Function/Module**
  - `test_loadDataWithoutOptionalLine()`
  - `test_loadDataWithOptionalLine()`
- **Tested Function/Module**
  - `loadData(file, optionalLine=False)`
- **Description**
    - Brief Description:\
    The function will load the CSV file and then converts it into a dataframe. optionalLine determines the amount of columns that will be returned.
  - Input:
    - **file**: Path to the .csv file.
    - **optionalLine**: True or False. Default value is false
  - Output:
    - DataFrame
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output**                           |
|-------------------------------|-----------------------------------------------|
| `loadData(r".\Food_Nutrition_Dataset.csv", False) `               | Dataframe with every column in said .csv file |
| `loadData(r".\Food_Nutrition_Dataset.csv", True) `              | Dataframe with only the column "food" .       |

- **1) Code for the Test Function**
```python
def test_loadDataWithoutOptionalLine():
    # This means that every column is gonna be included in the table
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", False)
    assert "Fat" in dataFrame.columns 
```
```python
def test_loadDataWithOptionalLine():
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", True)
    assert "food" in dataFrame.columns and "Vitamin B1" not in dataFrame.columns
```

- **2) Invalid Input and Expected Output** \
It is important to note that error handling for this is handled through the function loadData().

| **Invalid Input**               | **Expected Output** |
|---------------------------------|---------------------|
| `loadData(r".\bruh.csv", True)` |  Exception with the message `"File not found."` |

- **2) Code for the Test Function**
```python
def test_loadDataWrongCSV():
    with pytest.raises(Exception) as exc_info:
        dataFrame = loadData(r"./fictionalCSV.csv")
```

### Test Case 3:
- **Test Function/Module**
  - `test_findNutritionValue()`
- **Tested Function/Module**
  - `findNutritionValue(labelAll, dataFrame)`
- **Description**
  - Brief Description:\
    The function will find the maximum value for each nutrient and put them into a dictionary.\
    The keys are the nutrient, while the values are the maximum value.
  - Input:
    - **labelAll**: List. Contains the name of every nutrient.
    - **dataFrame**: dataframe. The dataframe file that will be used to find the values.
  - Output:
    - Dictionary
- **1) Valid Input and Expected Output** \
In the actual software, labelAll and dataFrame are already defined before running this function.

| **Valid Input**                           | **Expected Output**            |
|-------------------------------------------|--------------------------------|
| `findNutritionValue(labelAll, dataFrame)` | A dictionary that is not empty |

- **1) Code for the Test Function**
```python
def test_findNutritionValue():
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    # Iterate through every key value in the dictionary to find if there is any empty (or "") values
    for key in maxDict.keys():
        assert maxDict[key] is None or maxDict[key] != ""
```
- **2) Invalid Input and Expected Output** \
Errors in loading the CSV data are handled through the function loadCSVFile(), which is inside the function loadData(). Because of this, Testing for incorrect CSV files in this function, as those scenarios are already covered by the error handling implemented in loadCSVFile().

| **Invalid Input**                     | **Expected Output**                                      |
|---------------------------------------|----------------------------------------------------------|
| `findNutritionValue([], dataFrame)`)` | ValueError with the message `This array cannot be empty` |

- **2) Code for the Test Function**
```python
def test_findNutritionValue_emptyLabel(): # NEW TESTCASE
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")

    with pytest.raises(ValueError) as exc_info:
        maxDict = findNutritionValue([], dataFrameForDict)
```

### Test Case 4:
- **Test Function/Module**
  - `test_genericSearch_ExactMatch()`
  - `test_genericSearch_partialMatch()`
  - `test_genericSearch_emptyInput()`
  - `test_genericSearch_emptyArray()`
- **Tested Function/Module**
  - `findResult_generic(searchInput, array, items)`
- **Description**
  - Brief Description:\
    The function will try and find item(s) that have matching string with searchInput.
  - Input:
    - **searchInput**: string. The user's input.
    - **array**: List. The array where the result will be stored.
    - **items**: List. The iterated array which contains a list of items.
  - Output:
    - List
- **1) Valid Input and Expected Output**  

| **Valid Input**                                    | **Expected Output**                                          |
|----------------------------------------------------|--------------------------------------------------------------|
| `findResult_generic("Apricot Jam", foodAray)` | A list containing food(s) that has "Apricot Jam" in its name |
| `findResult_generic("", foodAray)`           | A list that returns every food in the original dataframe     |
| `findResult_generic("Cheese", foodAray)`    | A list containing food(s) with "cheese" in its name          |

- **1) Code for the Test Function**
```python
def test_genericSearch_ExactMatch():
    results = findResult_generic("Apricot Jam", foodArray)
    assert sum(results) == 1

def test_genericSearch_partialMatch():
    results = findResult_generic("Cheese", foodArray)
    assert sum(results) == 47

def test_genericSearch_emptyInput():
    results = findResult_generic("", foodArray)
    assert sum(results) == len(foodArray)
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `findResult_generic("Cheese", results, [])`               | An empty array      |

- **2) Code for the Test Function**
```python
def test_genericSearch_emptyArray(): # NEW TESTCASE
    results = []
    findResult_generic("Cheese", results, [])
    assert not results
```


### Test Case 5:
- **Test Function/Module**
  - `test_breakdown()`
  - `test_breakdown_emptyAllLabel()`
  - `test_breakdown_emptyEveryLabel()`
  - `test_breakdown_emptyLabelBar()`
  - `test_breakdown_emptySearchResult()`
- **Tested Function/Module**
  - `findResult_breakdown(allLabel, labelBar, searchResult)`
- **Description**
  - Brief Description:\
    This function is one of the function that runs when displaying the nutritional breakdown as charts. \
    The function will sort allLabel, which contains the name of every nutrient, into two arrays: barArray and pie Array. These two arrays will be used as the charts' labels.\
    labelBar lists all the nutrient that should go into barArray.
  - Input:
    - **allLabel**: List. Contains the name of every nutrient from the .csv file.
    - **labelBar**: List. The list of nutrients that should go into barArray.
    - **searchResult**: Dataframe. Contains the all the relevant information for the food that the user clicked.
  - Output:
    - 2 Arrays
- **1) Valid Input and Expected Output**  \
In the actual software, allLabel, labelBar, and searchResult are defined before this function runs. The valid input is under the assumption that each variable have the appropriate values.

| **Valid Input**                                    | **Expected Output**              |
|----------------------------------------------------|----------------------------------|
| `test_breakdown(allLabel, labelBar, searchResult)` | 2 lists with elements inside it. |

- **1) Code for the Test Function**
```python
def test_breakdown():
    # Simulate the act of user clicking on a food name in the table.
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", False)
    searchData = dataFrame["food"]
    results = []
    results = findResult_generic("Apricot Jam", results, searchData)
    searchResult = dataFrame[results]

    valueBar, valuePie = findResult_breakdown(allLabel, labelForBar, searchResult)

    for label in labelForBar:
        assert label in searchResult.columns
    for label in labelForPie:
        assert label in searchResult.columns
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                                  | **Expected Output**                                                      |
|--------------------------------------------------------------------|--------------------------------------------------------------------------|
| `test_breakdown([], [], ["A", "B", "C"])`                 | 2 empty lists                                                            |
| `test_breakdown(["Vitamin A", "Water", "Fat"], [], searchResult)` | An empty list for valueBar <br> The list valuePie have values inside it. |
| `test_breakdown([], [], ["A", "B", "C"])`                 | 2 empty lists                                                            |

- **2) Code for the Test Function**
```python
def test_breakdown_emptyEveryLabel(): # NEW TESTCASE
    valueBar, valuePie = findResult_breakdown([], [], ["A", "B", "C"])
    assert not valueBar
    assert not valuePie

def test_breakdown_emptyLabelBar(): # NEW TESTCASE
    # Simulate the act of user clicking on a food name in the table.
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", False)
    searchData = dataFrame["food"]
    results = []
    results = findResult_generic("Apricot Jam", results, searchData)
    searchResult = dataFrame[results]

    valueBar, valuePie = findResult_breakdown(["Vitamin A", "Water", "Fat"], [], searchResult)
    assert not valueBar
    assert valuePie

def test_breakdown_emptySearchResult(): # NEW TESTCASE
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", False)
    searchData = dataFrame["food"]
    results = []
    results = findResult_generic("asdfghjkl", results, searchData)
    searchResult = dataFrame[results]

    valueBar, valuePie = findResult_breakdown(["Vitamin A", "Water", "Fat"], [], searchResult)
    assert not valueBar
    assert not valuePie
```

### Test Case 6:
- **Test Function/Module**
  - `test_findKeto()`
  - `test_findKeto_wrongLength()`
- **Tested Function/Module**
  - `findResult_keto(carbo, calorie)`
- **Description**
  - Brief Description:\
    This function filters for food based on a certain condition. \
    In the case of this function, it will only include food with carbohydrate that is less than 10% of its caloric value.
  - Input:
    - **Carbo**: List. Contains the value of carbohydrate for every food.
    - **Calorie**: List. Contains the value of calorie for every food.
  - Output:
    - List
- **1) Valid Input and Expected Output**  \
In the actual software, the variable carbo and calorie are defined before this function runs. The valid input is under the assumption that each variable have the appropriate values.

| **Valid Input**                   | **Expected Output**                                           |
|-----------------------------------|---------------------------------------------------------------|
| `findResult_keto(carbo, calorie)` | A list containing the name of food that fulfils the condition |

- **1) Code for the Test Function**
```python
def test_findKeto():
    # True if carbo is less than 10% of the calorie
    itemsCarbo = [15, 50, 10, 30, 5]
    itemsCalorie = [200, 600, 120, 300, 100]
    expectedResult = [True, True, True, False, True]
    results = []

    results = findResult_keto(itemsCarbo, itemsCalorie)

    assert results == expectedResult
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                                      | **Expected Output**                                                        |
|------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `findResult_keto([15, 30, 25], [200, 300])` | ValueError with the value `Carbo and Calorie array have different length!` |

- **2) Code for the Test Function**
```python
def test_findKeto_wrongLength():
    # This shouldn't be possible at all but...
    itemsCarbo = [15, 50, 10, 30]
    itemsCalorie = [200, 600, 120, 300, 100]
    expectedResult = [True, True, True, False, True]
    results = []

    with pytest.raises(ValueError) as exc_info:
        findResult_keto(itemsCarbo, itemsCalorie)
```

### Test Case 7:
- **Test Function/Module**
  - `test_findSodium()`
  - `test_findSodium_empty()`
- **Tested Function/Module**
  - `findResult_sodium(items)`
- **Description**
  - Brief Description:\
    This function filters for food based on a certain condition. \
    In reality, low sodium diet is a type of diet where the users consume food with sodium less than 140mg per serving. However, after thoroughly testing the filter, we have found out that every food in the .csv file falls under this condition. This is why we have modified the condition slightly. \ 
  The condition now is that the filter will check if the food contains less than 40mg of sodium per serving.
  - Input:
    - **items**: List. Contains the value of sodium for every food.
  - Output:
    - List
- **1) Valid Input and Expected Output**  \
In the actual software, the variable items have been defined before the function is run. The valid input assumes that the variable was defined correctly.

| **Valid Input**                                    | **Expected Output**             |
|----------------------------------------------------|---------------------------------|
| `findResult_sodium(items)` | A list with elements inside it. |

- **1) Code for the Test Function**
```python
def test_findSodium():
    # True if less than 40
    items = [10, 15, 25, 5, 50]
    expectedResult = [True, True, True, True, False]

    results = findResult_sodium(items)

    assert results == expectedResult
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                      | **Expected Output**                                |
|----------------------------------------|----------------------------------------------------|
| `findResult_sodium([])` | An empty list                                      |
- **2) Code for the Test Function**
```python
def test_findSodium_empty():
    items = []
    expectedResult = [True, True, True, True, False]

    results = findResult_sodium(items)

    assert not results
```

### Test Case 8:
- **Test Function/Module**
  - `test_findCholesterol()`
  - `test_findCholesterol_empty()`
- **Tested Function/Module**
  - `findResult_cholesterol(items)`
- **Description**
  - Brief Description:\
    This function filters for food based on a certain condition. \
    In the case of this function, it will only include food that contains less than 20mg of cholesterol per serving.
  - Input:
    - **items**: List. Contains the value of sodium for every food.
  - Output:
    - List
- **1) Valid Input and Expected Output**  \
In the actual software, the variable items have been defined before the function is run. The valid input assumes that the variable was defined correctly.

| **Valid Input**                                    | **Expected Output**             |
|----------------------------------------------------|---------------------------------|
| `findResult_cholesterol(items)` | A list with elements inside it. |

- **1) Code for the Test Function**
```python
def test_findCholesterol():
    # True if less than 20
    items = [10, 15, 25, 5, 50]
    expectedResult = [True, True, False, True, False]

    results = findResult_cholesterol(items)

    assert results == expectedResult
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                      | **Expected Output** |
|----------------------------------------|----------------|
| `findResult_cholesterol([])` | An empty list  |
- **2) Code for the Test Function**
```python
def test_findCholesterol_empty():
    items = []
    expectedResult = [True, True, False, True, False]

    results = findResult_cholesterol(items)

    assert not results
```

### Test Case 8:
- **Test Function/Module**
  - `test_filterKeto()`
  - `test_filterSodium()`
  - `test_filterCholesterol()`
  - `test_filterNone()`
- **Tested Function/Module**
  - `filterDiet(dropdownValue)`
- **Description**
  - Brief Description:\
    This function is for one of the filter. It is important to note that the function `findResult_keto()`, `findResult_sodium()`, and `findResult_cholesterol()` are related to this function. \
    It will filter foods based on a user's dietary needs. There are 3 dietary filters provided in the software:
    - Ketogenic Diet
    - Low Sodium Diet
    - Low Cholesterol Diet
  - Input:
    - **dropdownValue**: String. Specifies the type of diet. In the actual software, this value is obtained from the dropdown menu from the GUI with `.GetStringSelection()`. 
  - Output:
    - Dataframe
- **1) Valid Input and Expected Output**  \

| **Valid Input**                      | **Expected Output**                                          |
|--------------------------------------|--------------------------------------------------------------|
| `filterDiet("Ketogenic Diet")`       | A dataframe with elements that fulfills a certain condition. |
| `filterDiet("Low Sodium Diet")`      | A dataframe with elements that fulfills a certain condition.      |
| `filterDiet("Low Cholesterol Diet")` | A dataframe with elements that fulfills a certain condition       |

- **1) Code for the Test Function**
```python
ddef test_filterKeto():
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
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `filterDiet("Dietary Needs")` | An empty dataframe  |
- **2) Code for the Test Function**
```python
def test_filterNone():
    results = filterDiet("Dietary Needs")

    # Get the original data for comparison
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv")

    assert results.empty
```

### Test Case 9:
- **Test Function/Module**
  - `test_getLabelNotEmpty()`
  - `test_getLabelEmpty()`
  - `test_getLabelEmptyMacro()`
  - `test_getLabelEmptyOthers()`
- **Tested Function/Module**
  - `getLabelPieBar(macronutrients, vitamins, minerals, others))`
- **Description**
  - Brief Description:\
    This function is to get the name of the nutrients and separate them into 2 lists. These 2 lists will then be used for the pie chart and bar chart.
  - Input:
    - **macronutrient**: List. Lists all nutrients that can be categorized as a macronutrient.
    - **vitamins**: List. Lists all nutrients that can be categorized as a vitamin.
    - **minerals**: List. Lists all nutrients that can be categorized as a mineral.
    - **other**: List. Lists all nutrients that cannot be categorized to macronutrient, vitamin, and mineral.
  - Output:
    - 2 lists
- **1) Valid Input and Expected Output**  \
In the actual software, the 4 lists would have been defined before this function is called. The valid testing assumes that the 4 lists have been correctly defined beforehand.

| **Valid Input**                      | **Expected Output**                                                       |
|--------------------------------------|---------------------------------------------------------------------------|
| `getLabelPieBar(macronutrients, vitamins, minerals, others)`       | A list with elements for labelPie <br> A list with elements for labelBar. |

- **1) Code for the Test Function**
```python
def test_getLabelNotEmpty():
    labelPie, labelBar = getLabelPieBar(macronutrients, vitamins, minerals, others)
    assert labelPie == labelForPie and labelBar == labelForBar
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                   | **Expected Output**                                           |
|-------------------------------------|---------------------------------------------------------------|
| `getLabelPieBar([], ["Vitamin A, Vitamin B"], ["Sodium"], ["Water"])` | An empty list for labelPie <br> A non-empty list for labelBar |
| `getLabelPieBar(["Fat"], ["Vitamin A", "Vitamin B"], ["Sodium"], [])` | A non-empty list for labelPie <br> An empty list for labelBar |
| `getLabelPieBar([], [], [], [])`    | 2 empty lists                                                 |
- **2) Code for the Test Function**
```python
def test_getLabelEmpty():
    # This shouldn't be possible but...
    macronutrients = []
    vitamins = []
    minerals = []
    others = []
    labelPie, labelBar = getLabelPieBar(macronutrients, vitamins, minerals, others)

    # Since labelPie and labelBar is empty, it shouldn't be the same as labelForPie and labelForbar
    assert labelPie != labelForPie and labelBar != labelForBar
    assert not labelPie and not labelBar

def test_getLabelEmptyMacro(): # NEW TESTCASE
    macronutrients = []
    labelPie, labelBar = getLabelPieBar(macronutrients, vitamins, minerals, others)
    assert labelPie != labelForPie and labelBar == labelForBar
    assert not labelPie and labelBar

def test_getLabelEmptyOthers(): # NEW TESTCASE
    others = []
    labelPie, labelBar = getLabelPieBar(macronutrients, vitamins, minerals, others)
    assert labelPie == labelForPie and labelBar != labelForBar
    assert labelPie and not labelBar

```

### Test Case 10:
- **Test Function/Module**
  - `test_createLabel()`
  - `test_createLabel_diffLength()`
- **Tested Function/Module**
  - `createLabel(arrayPie, labelPie)`
- **Description**
  - Brief Description:\
    This function is to produce an array that will be used as label for the pie chart. The label will specify the percentage for each related nutrient.
  - Input:
    - **arrayPie**: List. Contains the value of each nutrient for said food.
    - **labelPie**: List. Contains the name of the related nutrients.
  - Output:
    - List
- **1) Valid Input and Expected Output**  \
In the actual software, the variable arrayPie is defined through the function `findResult_breakdown()`. The valid testing assumes that the variables are defined correctly beforehand.

| **Valid Input**                      | **Expected Output** |
|--------------------------------------|--------------------|
| `createLabel(arrayPie, labelPie)` | A non-empty list.  |

- **1) Code for the Test Function**
```python
def test_createLabel():
    labelArray = []
    outputExpected = ['Fat: 0.05%', 'Saturated Fats: 0.19%', 'Monounsaturated Fats: 0.0%', 'Polyunsaturated Fats: 0.0%', 'Carbohydrates: 59.19%', 'Sugars: 39.92%', 'Protein: 0.46%', 'Dietary Fiber: 0.2%']
    # We need to emulate the process of breaking down the food that user has clicked for this to work.
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", False)
    searchData = dataFrame["food"]
    results = []
    results = findResult_generic("Apricot Jam", searchData)
    searchResult = dataFrame[results]

    valueBar, valuePie = findResult_breakdown(allLabel, labelForBar, searchResult)

    labelArray = createLabel(valuePie, labelForPie)
    assert labelArray == outputExpected
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                                   | **Expected Output**                                             |
|---------------------------------------------------------------------|-----------------------------------------------------------------|
| `createLabel(["A"], ["B", "C"])`             | ValueError with the message `The arrays have different length!` |

- **2) Code for the Test Function**
```python
def test_createLabel_diffLength(): # NEW TESTCASE
    with pytest.raises(ValueError) as exc_info:
        createLabel(["A"], ["B", "C"])
```

### Test Case 11:
- **Test Function/Module**
  - `test_concatBarX()`
  - `test_concatBarX_empty()`
- **Tested Function/Module**
  - `concatBarX(arrayValue)`
- **Description**
  - Brief Description:\
    This function is to produce an array that will be used for the x axis in the bar chart. It consists of the name of the nutrients.
  - Input:
    - **arrayValue**: List. Contains the name of the nutrients
  - Output:
    - List
- **1) Valid Input and Expected Output**  \
In the actual software, the variable arrayValue is defined through the function `findResult_breakdown()`. The valid testing assumes that the variables are defined correctly beforehand.

| **Valid Input**           | **Expected Output** |
|---------------------------|--------------------|
| `concatBarX(arrayValue)` | A non-empty list.  |

- **1) Code for the Test Function**
```python
def test_concatBarX():
    results = []
    # Same as before, we need to emulate the process of breaking down the food that user has clicked for this to work.
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", False)
    searchData = dataFrame["food"]
    results = []
    results = findResult_generic("Apricot Jam", searchData)
    searchResult = dataFrame[results]

    valueBar, valuePie = findResult_breakdown(allLabel, labelForBar, searchResult)

    # Using np (numpy) made the array a bit different than usualy so I had to convert valueBar as well
    results = concatBarX(valueBar)
    valueBar = np.array(valueBar)

    # The purpose of the function was to move the initial value to the 2nd last position of said array
    assert valueBar[0] == results[-2]
```
- **2) Invalid Input and Expected Output**

| **Invalid Input** | **Expected Output** |
|-------------------|--------------------|
| `concatBarX([]])` | An empty list      |

- **2) Code for the Test Function**
```python
def test_concatBarX_empty(): # NEW TESTCASE!
    searchResult = []
    results = concatBarX(searchResult)

    assert not results
```

### Test Case 12:
- **Test Function/Module**
  - `test_checkDAI_defaultDropdownAndFilledInput()`
  - `test_checkDAI_diffDropdownAndEmptyInput()`
  - `test_checkDAI_diffDropdownAndAlphaInput()`
  - `test_checkDAI_minGreaterMax()`
  - `test_checkDAI_correct()`
- **Tested Function/Module**
  - `checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)`
- **Description**
  - Brief Description:\
    This function does the error handling for one of the filter, which is the one that lets user filter foods based on a defined min/max range for a chosen nutrient. \
    There are 4 categories of nutrient: Macronutrient, Vitamin, Mineral, and Other. Each category have their own 2 input fields that represent the minimum and maximum value.
  - Input:
    - **dropdownArray**: List. Contains 4 values which represent the nutrient that was chosen from each dropdown menu.
    - **minArray**: List. Contains 4 values which represent the minimum value that was obtained from user's input for each category of nutrient.
    - **maxArray**: List. Contains 4 values which represent the maximum value that was obtained from user's input for each category of nutrient.
    - **isError**: bool. Default value is True. Indicates whether there is any error in any of the input.
    - **searchResultArray**: List. An empty list that will be used for another function that is inside `checkDropdownAndInput_value()`. Will only be used if there are no errors in the input.
  - Output:
    - **errorChooseNutrient**: List. Contains the name of the nutrient and/or nutrient category that has an error.
    - **errorInputValue**: List. Contains the name of the nutrient and/or nutrient category that has an error.
    - **errorComparisonValue**: List. Contains the name of the nutrient and/or nutrient category that has an error.
    - **isError**: bool
- **1) Valid Input and Expected Output**  \
 The valid testing assumes that the variables are defined correctly beforehand.

| **Valid Input**                                                                              | **Expected Output**                                                                                    |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)` | 3 empty lists for `errorChooseNutrient`, `errorInputValue`, and `errorComparisonValue`. <br>True for isError |

- **1) Code for the Test Function**
```python
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

```
- **2) Invalid Input and Expected Output** \
There will be an explanation after the table on what is the invalid input for each invalid testing.

| **Invalid Input**                                                                                                   | **Expected Output**                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `checkDropdownAndInput_value(defaultDropdownArray, filledMinArray, filledMaxArray, isError, searchResultArray])`    | A non empty list for `errorChooseNutrient` <br> An empty list for `errorInputValue` <br> An empty list for `errorComparisonValue` <br> `False` for isError |
| `checkDropdownAndInput_value(dropdownArray, emptyMinArray, emptyMaxArray, isError, searchResultArray])`             | An empty list for `errorChooseNutrient` <br> A non empty list for `errorInputValue` <br> An empty list for `errorComparisonValue` <br> `False` for isError |
| `checkDropdownAndInput_value(dropdownArray, filledAlphaMinArray, filledAlphaMaxArray, isError, searchResultArray])` | An empty list for `errorChooseNutrient` <br> A non empty list for `errorInputValue` <br> An empty list for `errorComparisonValue` <br> `False` for isError |
| `checkDropdownAndInput_value(dropdownArray, bigMinArray, smallMaxArray, isError, searchResultArray])`               | An empty list for `errorChooseNutrient` <br> An empty list for `errorInputValue` <br> A non empty list for `errorComparisonValue` <br> `False` for isError |
- First Invalid Testing \
  The invalid input is the array that consists the value of dropdown menu, where the user did not change the value and kept the default one.
- Second Invalid Testing \
  The invalid input is the array that stores the minimum value and maximum value. The user changed the value for the dropdown menu but did not fill the input field.
- Third Invalid Testing \
  The invalid input is the array that stores the minimum value and maximum value. The user changed the value for the dropdown menu and fill the input field. However, they put non-numeric values in the input field.
- Fourth Invalid Testing \
  The invalid input is the array that stores the minimum value and maximum value. The user changed the value for the dropdown menu and fill the input field. However, the minimum range is higher than the maximum range.

- **2) Code for the Test Function**
```python
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
```

### Test Case 13:
- **Test Function/Module**
  - `test_filterRange()`
- **Tested Function/Module**
  - `filterRange(dropdownArrayIndex, minValueIndex, maxValueIndex, searchResult_filter)`
- **Description**
  - Brief Description:\
    This function is a part of `checkDropdownAndInput_value()`, where it handles the filtering. It is important to note that this function, in the real software, will only run once all validations from `checkDropdownAndInput_value()` have passed. \
    This is why there are no invalid testing for this function. All invalid testing have been done by the function `checkDropdownAndInput_value()`.
  - Input:
    - **dropdownArrayIndex**: String. Contains the name of the nutrient.
    - **minValueIndex**: Float. Contains the minimum range in the type of float.
    - **maxValueIndex**: Float. Contains the maximum range in the type of float.
    - **searchResult_filter**: Dataframe. Contains the list of foods that are between the minimum and maximum range for a nutrient.
  - Output:
    - Dataframe
- **1) Valid Input and Expected Output**  \

| **Valid Input**           | **Expected Output** |
|---------------------------|--------------------|
| `filterRange(dropdownArrayIndex, minValueIndex, maxValueIndex, searchResult_filter)` | A non-empty list.  |

- **1) Code for the Test Function**
```python
def test_filterRange():
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
```
- **2) Invalid Input and Expected Output** \
As stated previously, all of the invalid inputs were handled by `checkDropdownAndInput_value()`.All of the variables have to be properly defined before being passed to `filterRange()`.

### Test Case 14:
- **Test Function/Module**
  - `test_GEM_nutrient()`
  - `test_GEM_input()`
  - `test_GEM_comparison()`
  - `test_GEM_nutrientAndInput()`
  - `test_GEM_nutrientAndComparison()`
  - `test_GEM_inputAndComparison()`
  - `test_GEM_everyError()`
  - `def test_GEM_noError()`
- **Tested Function/Module**
  - `generateErrorMessage_value(nutrientError, inputError, comparisonError)
- **Description**
  - Brief Description:\
    This function generates error messages for the range filter.
  - Input:
    - **nutrientError**: List. Contains the name of the nutrient categories that are considered as invalid.
    - **inputError**: List. Contains the name of the nutrient and/or nutrient categories that are considered as invalid.
    - **comparisonError**: List. Contains the name of the nutrient and/or nutrient categories that are considered as invalid.
  - Output:
    - nutrientError: String
    - inputError: String
    - comparisonError: String \
    These 3 outputs are the error messages.
- **1) Valid Input and Expected Output**  \
 The valid testing assumes that the variables are defined correctly beforehand.

| **Valid Input**                                                      | **Expected Output**                                                                                                                               |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `generateErrorMessage_value(["Macronutrients", "Vitamins"], [], [])` | nutrientError: `"Please choose a nutrient for Macronutrients, Vitamins"` <br> inputError: Empty string (`""`) <br> comparisonError: Empty String (`""`) |
| `generateErrorMessage_value([], ["Vitamins"], [])`                   | nutrientError: Empty String (`""`) <br> inputError: `"Please fill the min/max value (Numerical values) for Vitamins"` <br> comparisonError: Empty String (`""`) |
| `generateErrorMessage_value([], [], ["Macronutrients", "Vitamins", "Minerals"])` | nutrientError: Empty string (`""`) <br> inputError: Empty string (`""`) <br> comparisonError: Please make sure the min value is not higher than the max value for Macronutrients, Vitamins, Minerals |
| `generateErrorMessage_value(["Macronutrients", "Vitamins"], ["Vitamins"], [])` | nutrientError: `"Please choose a nutrient for Macronutrients, Vitamins"` <br> inputError: `"Please fill the min/max value (Numerical values) for Vitamins"` <br> comparisonError: Empty String (`""`) |
| `generateErrorMessage_value(["Macronutrients", "Vitamins"], [], ["Others"])` | nutrientError: `"Please choose a nutrient for Macronutrients, Vitamins"` <br> inputError: Empty string (`""`) <br> comparisonError: `"Please make sure the min value is not higher than the max value for Others"` |
| `generateErrorMessage_value([], ["Macronutrients"], ["Others"])`     | nutrientError: Empty String (`""`) <br> inputError: `"Please fill the min/max value (Numerical values) for Macronutrients"` <br> comparisonError: `"Please make sure the min value is not higher than the max value for Others"` |
| `generateErrorMessage_value(["Others"], ["Macronutrients"], ["Vitamins", "Minerals"])`                     | nutrientError: `"Please choose a nutrient for Others"` <br> inputError: `"Please fill the min/max value (Numerical values) for Macronutrients"` <br> comparisonError: `"Please make sure the min value is not higher than the max value for Vitamins, Minerals"` |

- **1) Code for the Test Function**
```python
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
    assert inputMsg == ""
    assert comparisonMsg == ""

def test_GEM_input():
    # Test -> Test generated error message for test_checkDAI_diffDropdownAndEmptyInput() and test_checkDAI_diffDropdownAndAlphaInput()

    nutrientMsg = ""
    inputMsg = ""
    comparisonMsg = ""
    errorChooseNutrient = []
    errorInputValue = ["Vitamins"]
    errorComparisonValue = []

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert nutrientMsg == ""
    assert inputMsg == "Please fill the min/max value (Numerical values) for Vitamins"
    assert comparisonMsg == ""

def test_GEM_comparison():
    # Test -> Test generated error message for test_checkDAI_test_checkDAI_minGreaterMax()
    nutrientMsg = ""
    inputMsg = ""
    comparisonMsg = ""
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = ["Macronutrients", "Vitamins", "Minerals"]

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert nutrientMsg == ""
    assert inputMsg == ""
    assert comparisonMsg == "Please make sure the min value is not higher than the max value for Macronutrients, Vitamins, Minerals"

def test_GEM_nutrientAndInput():
    # Test -> generate error message for 2 errors. Default dropdown and missing input.
    errorChooseNutrient = ["Macronutrients", "Vitamins"]
    errorInputValue = ["Vitamins"]
    errorComparisonValue = []

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert nutrientMsg == "Please choose a nutrient for Macronutrients, Vitamins"
    assert inputMsg == "Please fill the min/max value (Numerical values) for Vitamins"
    assert comparisonMsg == ""

def test_GEM_nutrientAndComparison():
    # Test -> generate error message for 2 errors. Default dropdown and error in min/max value.
    errorChooseNutrient = ["Macronutrients", "Vitamins"]
    errorInputValue = []
    errorComparisonValue = ["Others"]

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert nutrientMsg == "Please choose a nutrient for Macronutrients, Vitamins"
    assert inputMsg == ""
    assert comparisonMsg == "Please make sure the min value is not higher than the max value for Others"

def test_GEM_inputAndComparison():
    # Test -> generate error message for 2 errors. Default dropdown and error in min/max value.
    errorChooseNutrient = []
    errorInputValue = ["Macronutrients"]
    errorComparisonValue = ["Others"]

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert nutrientMsg == ""
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

```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                        | **Expected Output** |
|------------------------------------------|---------------------|
| `generateErrorMessage_value([], [], [])` | 3 empty strings     |

- **2) Code for the Test Function**
```python
def test_GEM_noError(): # NEW TESTCASE
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []

    nutrientMsg, inputMsg, comparisonMsg = generateErrorMessage_value(errorChooseNutrient, errorInputValue, errorComparisonValue)
    assert nutrientMsg == ""
    assert inputMsg == ""
    assert comparisonMsg == ""
```

### Test Case 15:
- **Test Function/Module**
  - `test_checkRAD_radio()`
  - `test_checkRAD_dropdown()`
  - `test_checkRAD_noError()`
- **Tested Function/Module**
  - `checkRadioAndDropdown_level(radioValue, dropdownValue)`
- **Description**
  - Brief Description:\
    This function generates the error message for the nutrition level filter.
  - Input:
    - **radioValue**: String. Contains the value from the radio button.
    - **dropdownValue**: String. Contains the value from the dropdown button.
  - Output:
    - errorMsgRadio: String.
    - errorMsgDropdown: String.
    - isError: Bool. Indicates whether there is an invalid input for this filter or not.
- **1) Valid Input and Expected Output**  \

| **Valid Input**                             | **Expected Output**                                                                                  |
|---------------------------------------------|------------------------------------------------------------------------------------------------------|
| `checkRadioAndDropdown_level("Low", "Fat")` | errorMsgRadio: Empty String (`""`)  <br> errorMsgDropdown: Empty String (`""`) <br> isError: `False` |

- **1) Code for the Test Function**
```python
def test_checkRAD_noError():
    # TEST -> No error so uhhh no error messages.

    radioValue = "Low"
    dropdownValue = "Fat"
    errorMsgRadio = ""
    errorMsgDropdown = ""
    isError = True

    errorMsgRadio, errorMsgDropdown, isError = checkRadioAndDropdown_level(radioValue, dropdownValue)

    assert errorMsgRadio == "" and errorMsgDropdown == "" and not isError

```
- **2) Invalid Input and Expected Output**

| **Invalid Input** | **Expected Output** |
|-------------------|--------------------|
| `checkRadioAndDropdown_level("None", "Fat")`              | errorMsgRadio: `"Nutrition level cannot be none!"` <br> errorMsgDropdown: Empty String (`""`) <br> isError: `True` |
| `checkRadioAndDropdown_level("Low", "Choose a nutrient")` | errorMsgRadio: Empty String (`""`) <br> errorMsgDropdown: `"Please choose a nutrient to filter the nutrition level with."` <br> isError: `True` |

- **2) Code for the Test Function**
```python
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
```

### Test Case 16:
- **Test Function/Module**
  - `test_checkResult_notEmpty()`
  - `test_checkResult_empty()`
- **Tested Function/Module**
  - `checkResult(finalResult)`
- **Description**
  - Brief Description:\
    This function counts the length of a list and append the length into a string.
  - Input:
    - **finalResult**: List. Contains the list of the filter result.
  - Output:
    - `f"{len(finalResult)} result(s) were found!"`, or
    - `"No result(s) were found."`
- **1) Valid Input and Expected Output**  \
The valid testing assumes that the input variable has been defined correctly beforehand.

| **Valid Input**                             | **Expected Output**         |
|---------------------------------------------|-----------------------------|
| `checkResult(finalResult)` | `"70 result(s) were found!"` |

- **1) Code for the Test Function**
```python
def test_checkResult_notEmpty():
    # This isn't the actual search result, but it should suffice for the purpose of testing because it's trying to count the length of an array.
    arrayResult = foodArray
    message = ""

    message = checkResult(arrayResult)

    assert message == "70 result(s) were found!"
```
- **2) Invalid Input and Expected Output**

| **Invalid Input** | **Expected Output** |
|-------------------|--------------------|
| `checkResult([])` | `"No result(s) were found."` |

- **2) Code for the Test Function**
```python
def test_checkResult_empty():
    # This isn't the actual search result, but it should suffice for the purpose of testing because it's trying to count the length of an array.
    arrayResult = []
    message = ""

    message = checkResult(arrayResult)

    assert message == "No result(s) were found."
```

### Test Case 17:
- **Test Function/Module**
  - `test_filterLevel_low()`
  - `test_filterLevel_medium()`
  - `test_filterLevel_high()`
  - `test_filterLevel_wrongValue()`
- **Tested Function/Module**
  - `filterLevel(maxValueDict, dropdownValue, levelFilter)`
- **Description**
  - Brief Description:\
    This function filters the food Dataframe based on nutrition level.
  - Input:
    - **maxValueDict**: Dict. Contains a collection of the highest value for each nutrient.
    - **dropdownValue**: String. The name of the nutrient that is obtained from the dropdown menu.
    - **levelFilter**: String. The level for the filter. The value is obtained from the radio button.
  - Output:
    - searchResult: Dataframe
- **1) Valid Input and Expected Output**  \
The valid testing assumes that the input variable has been defined correctly beforehand.

| **Valid Input**                                      | **Expected Output**                                                                                                                                                                                          |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `filterLevel(maxValueDict, dropdownValue, "Low")`    | A DataFrame containing the name of foods that meet the condition. The condition is that the selected nutrient is less than 33% of its maximum value.                                                         |
| `filterLevel(maxValueDict, dropdownValue, "Medium")` | A DataFrame containing the name of foods that meet the condition. The condition is that the selected nutrient has to be more than 33% of its maximum value while also be less than 66% of its maximum value. |
| `filterLevel(maxValueDict, dropdownValue, "High")`   | A DataFrame containing the name of foods that meet the condition. The condition is that the selected nutrient is more than 66% of its maximum value.                                                         |

- **1) Code for the Test Function**
```python
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
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                               | **Expected Output** |
|-----------------------------------------------------------------|--------------------|
| `filterLevel(maxValueDict, dropdownValue, "Choose a nutrient")` | An empty Dataframe |

- **2) Code for the Test Function**
```python
def test_filterLevel_wrongValue(): # NEW TESTCASE
    # We need to emulate the process of finding the highest value of each nutrient for this.
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    maxValueNutrient = maxDict["Fat"]
    highThreshold = 0.66 * maxValueNutrient

    dropdownValue = "Choose a nutrient"
    levelFilter = "High"

    results = filterLevel(maxDict, dropdownValue, levelFilter)

    assert results.empty
```

## Test Case 18:
- **Test Function/Module**
  - `test_mergeResult_moreThanOne()`
  - `test_mergeResult_one()`
  - `test_mergeResult_none()`
- **Tested Function/Module**
  - `mergeResult_filterRange(searchResultArray_value)`
- **Description**
  - Brief Description:\
    This function combines all the result from the filter range into one Dataframe. The reason this is necessary is because the user can filter foods with multiple nutrients and multiple min/max ranges.
  - Input:
    - **searchResultArray_value**: Dataframe. Contains a collection of the filter result.
  - Output:
    - mergedResult: Dataframe
- **1) Valid Input and Expected Output**  \
The valid testing assumes that the input variable has been defined correctly beforehand.

| **Valid Input**                                             | **Expected Output**                                                                                                                             |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `mergeResult_filterRange(searchResultArray_moreThanOnevalue)` | A DataFrame containing the name of foods that meet multiple filter conditions.                                                               |
| `mergeResult_filterRange(searchResultArray_value)`          | A DataFrame containing the name of foods that meet one filter conditions.                                                                       |

- **1) Code for the Test Function**
```python
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
    searchResultArray_moreThanOnevalue = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Fat", "Vitamin A", "Minerals", "Others"]
    minArray = ["3", "8", "", ""]
    maxArray = ["8", "12", "", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)
    searchResultArray_moreThanOnevalue = mergeResult_filterRange(searchResultArray)

    assert searchResultArray_moreThanOnevalue.equals(mergedResult_expected)

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
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                    | **Expected Output** |
|------------------------------------------------------|--------------------|
| `mergeResult_filterRange(searchResultArray_invalid)` | An empty Dataframe |

- **2) Code for the Test Function**
```python
def test_mergeResult_none(): # NEW TESTCASE
    # We need to emulate the user filtering the food 
    searchResultArray = []
    searchResultArray_invalid = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Fat", "Vitamins", "Minerals", "Others"]
    minArray = ["665", "", "", ""]
    maxArray = ["667", "", "", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)
    searchResultArray_invalid = mergeResult_filterRange(searchResultArray)

    # If the user only filters with 1 nutrient, it'll use the first index instead.
    assert searchResultArray_invalid.empty
```

## Test Case 19:
- **Test Function/Module**
  - `test_ME_emptyValue()`
  - `test_ME_emptyDiet()`
  - `test_ME_emptyLevel()`
  - `test_ME_everything()`
  - `test_ME_noValue()`
  - `test_ME_falseLevel()`
  - `test_ME_noMerge()`
- **Tested Function/Module**
  - `mergeResult_everything(isError_value, minValueArray, isError_level, levelValue, searchResult_value, searchResult_level, searchResult_diet)`
- **Description**
  - Brief Description:\
    This function combines all the result from every filter into one Dataframe.
  - Input:
    - **isError_value**: Bool. Indicates whether there is an invalid input for range filter or not. Used for validation
    - **minValueArray**: List. A collection of the minimum range that user has put in the input field. Used for validation together for isError_value.
    - **isError_level**: Bool. Indicates whether there is an invalid input for nutrition level filter or not. Used for validation
    - **levelValue**: String. Specifies the filter level. Used for validation together with isError_level.
    - **searchResult_value**: Dataframe. Collection of food from nutrition filter range.
    - **searchResult_level**: Dataframe. Collection of food from nutrition level range.
    - **searchResult_diet**: Dataframe. Collection of food from dietary needs.
  - Output:
    - mergedResult: Dataframe
- **1) Valid Input and Expected Output**  \
The valid testing assumes that the input variable has been defined correctly beforehand.

| **Valid Input**                                                                                                                                   | **Expected Output**    |
|---------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| `mergeResult_everything(isError_value, minValueArray, isError_level, levelValue, searchResult_value, searchResult_level, searchResult_diet)` | A non-empty Dataframe  |
| `mergeResult_everything(isError_value, minValueArray, isError_level, levelValue, searchResult_value, searchResult_level, emptysearchResult_diet)` | A non-empty Dataframe. |

- **1) Code for the Test Function**
```python
def test_ME_emptyDiet(): # UPDATED!
    """
    In the actual software, this function will only run after the required checks are done.

    Checks what happens if the searchResult_diet is empty, while the other filters aren't empty.
    """
    mergedResult = []
    isError_value = False
    minValueArray = ["8", "", "", ""]
    isError_level = False

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
    dropdownValue = "Sodium"
    levelFilter = "Low"

    results_level = filterLevel(maxDict, dropdownValue, levelFilter)

    searchResults_diet = []
    results_diet = pd.DataFrame(searchResults_diet, columns=["food"])

    mergedResult_expected = results_value.merge(results_level, on="food", how="inner")

    mergedResult = mergeResult_everything(isError_value, minValueArray, isError_level, levelFilter, results_value, results_level, results_diet)

    assert mergedResult.equals(mergedResult_expected)

def test_ME_everything():
    """
    In the actual software, this function will only run after the required checks are done.

    Combines every result.
    """
    isError_value = False
    minValueArray = ["8", "", "", ""]
    isError_level = False
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

    mergedResult = mergeResult_everything(isError_value, minValueArray, isError_level, levelFilter, results_value, results_level, results_diet)

    assert mergedResult.equals(mergedResult_expected)
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                                                                                                                           | **Expected Output** |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| `mergeResult_everything(isError_value, minValueArray, isError_level, levelValue, searchResult_value, emptySearchResult_level, searchResult_diet)`           | An empty Dataframe.                                                       |
| `mergeResult_everything(isError_value, minValueArray, isError_level, levelValue, emptySearchResult_value, SearchResult_level, searchResult_diet)`           | An empty Dataframe. 
| `mergeResult_everything(isError_value, minValueArray, isError_level, levelValue, emptySearchResult_value, emptySearchResult_level, emptySearchResult_diet)` | An empty Dataframe.
| `mergeResult_everything(True, ["", "", "", ""], True, "None", emptySearchResult_value, emptySearchResult_level, emptySearchResult_diet)`                    | An empty Dataframe.
| `mergeResult_everything(isError_value, minValueArray, isError_level, "None", emptySearchResult_value, emptySearchResult_level, emptySearchResult_diet)`                    | An empty Dataframe.

- **2) Code for the Test Function**
```python
def test_ME_emptyValue(): # UPDATED!
    """
    In the actual software, this function will only run after the required checks are done.

    Checks what would happen if searchResult_value is empty, while
    the other filters have results.
    """
    mergedResult = []
    isError_value = False
    minValueArray = ["8", "", "", ""]
    isError_level = False

    # We need to emulate the user doing the whole filter except the first one.
    searchResult_value = []
    results_value = pd.DataFrame(searchResult_value, columns=["food"])

    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)
    dropdownValue = "Fat"
    levelFilter = "Low"

    results_level = filterLevel(maxDict, dropdownValue, levelFilter)
    results_diet = filterDiet("Ketogenic Diet")

    mergedResult_expected = results_level.merge(results_diet, on="food", how="inner")

    mergedResult = mergeResult_everything(isError_value, minValueArray, isError_level, levelFilter, results_value, results_level, results_diet)

    assert mergedResult.empty

def test_ME_emptyLevel(): # UPDATED
    """
    In the actual software, this function will only run after the required checks are done.

    Checks what happens if the searchResult_level is empty, while the other filters aren't empty.
    """

    isError_value = False
    minValueArray = ["8", "", "", ""]
    isError_level = False

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

    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")

    levelFilter = "Medium"
    searchResults_level = []
    results_level = pd.DataFrame(searchResults_level, columns=["food"])
    # print(results_level)

    results_diet = filterDiet("Ketogenic Diet")

    mergedResult_expected = results_value.merge(results_diet, on="food", how="inner").merge(results_level, on="food", how="inner")

    mergedResult = mergeResult_everything(isError_value, minValueArray, isError_level, levelFilter, results_value, results_level, results_diet)
    print(mergedResult_expected)
    assert mergedResult.empty

def test_ME_noValue():
    """
    In the actual software, this function will only run after the required checks are done.

    Checks if the final result is NONE or not. We can simulate this by making 3 empty dataframes.
    """
    
    isError_value = False
    minValueArray = ["8", "", "", ""]
    isError_level = False
    levelFilter = "Medium"

    searchResult_value = []
    results_value = pd.DataFrame(searchResult_value, columns=["food"])

    searchResults_diet = []
    results_diet = pd.DataFrame(searchResults_diet, columns=["food"])

    searchResults_level = []
    results_level = pd.DataFrame(searchResults_level, columns=["food"])

    mergedResult = mergeResult_everything(isError_value, minValueArray, isError_level, levelFilter, results_value, results_level, results_diet)

    assert mergedResult.empty
    
def test_ME_falseLevel(): # NEW TESTCASE
    """
    In the actual software, this function will only run after the required checks are done.

    Checks what happens if the searchResult_level is empty, while the other filters aren't empty.
    """

    isError_value = False
    minValueArray = ["8", "", "", ""]
    isError_level = False

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

    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")

    levelFilter = "None"
    searchResults_level = []
    results_level = pd.DataFrame(searchResults_level, columns=["food"])
    # print(results_level)

    results_diet = filterDiet("Ketogenic Diet")

    mergedResult_expected = results_value.merge(results_diet, on="food", how="inner").merge(results_level, on="food", how="inner")

    mergedResult = mergeResult_everything(isError_value, minValueArray, isError_level, levelFilter, results_value, results_level, results_diet)
    assert not mergedResult.empty


def test_ME_noMerge(): #NEW TESTCASE
    """
    In the actual software, this function will only run after the required checks are done.

    Combines every result.
    """
    isError_value = True
    minValueArray = ["", "", "", ""]
    isError_level = True
    searchResultArray = []
    mergedResult = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Fat", "Vitamins", "Minerals", "Others"]
    minArray = ["", "", "", ""]
    maxArray = ["", "", "", ""]

    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray,
                                                                                                      minArray,
                                                                                                      maxArray, isError,
                                                                                                      searchResultArray)
    results_value = mergeResult_filterRange(searchResultArray)

    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)
    maxValueNutrient = maxDict["Fat"]
    lowThreshold = 0.33 * maxValueNutrient
    dropdownValue = "Choose a nutrient"
    levelFilter = "None"

    results_level = filterLevel(maxDict, dropdownValue, levelFilter)
    results_diet = pd.DataFrame(columns=["food"])

    mergedResult_expected = results_value.merge(results_diet, on="food", how="inner").merge(results_level, on="food", how="inner")

    mergedResult = mergeResult_everything(isError_value, minValueArray, isError_level, levelFilter, results_value, results_level, results_diet)

    assert mergedResult.empty
```

### Test Case 20:
- **Test Function/Module**
  - `test_CD_default()`
  - `test_CD_keto()`
  - `test_CD_sodium()`
  - `test_CD_cholesterol()`
- **Tested Function/Module**
  - `checkDiet(dietDropdown)
- **Description**
  - Brief Description:\
    This function returns a string that gives the user additional context about the filter that is based on 3 dietary needs.
  - Input:
    - **dietDropdown**: String. Contains the value for the dropdown menu.
  - Output:
    - `""`, 
    - `Ketogenic Diet - Searches for foods that are low in carbohydrates. (Less than 5-10% of the caloric intake)"`,
    - `"Low Sodium Diet - Searches for foods that are low in sodium content. (Less than 140mg per serving)"`, or
    - `"Low Cholesterol Diet - Searches for foods that have less than 20mg of cholesterol per serving."`
- **1) Valid Input and Expected Output**  \
The valid testing assumes that the input variable has been defined correctly beforehand.

| **Valid Input**                             | **Expected Output**         |
|---------------------------------------------|-----------------------------|
| `checkDiet("Ketogenic Diet")` | `"Ketogenic Diet - Searches for foods that are low in carbohydrates. (Less than 5-10% of the caloric intake)"` |
| `checkDiet("Low Sodium Diet")` | `"Low Sodium Diet - Searches for foods that are low in sodium content. (Less than 140mg per serving)"` |
| `checkDiet("Low Cholesterol Diet")` | `"Low Cholesterol Diet - Searches for foods that have less than 20mg of cholesterol per serving."` |

- **1) Code for the Test Function**
```python
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

```
- **2) Invalid Input and Expected Output**

| **Invalid Input**            | **Expected Output** |
|------------------------------|------------------|
| `checkDiet("Dietary Needs")` | `""` |

- **2) Code for the Test Function**
```python
def test_CD_default():
    # TEST -> Checks returned string if dropdown value is the default one.
    labelMessage = checkDiet("Dietary Needs")
    assert labelMessage == ""
```

### Test Case 21:
- **Test Function/Module**
  - `test_CR_default()`
  - `test_CR_low()`
  - `test_CR_medium()`
  - `test_CR_high()`
- **Tested Function/Module**
  - `checkRadio(radioValue)`
- **Description**
  - Brief Description:\
    This function returns a string that gives the user additional context about the nutritional level filter.
  - Input:
    - **radioValue**: String. Contains the value from the radio button.
  - Output:
    - `""`, 
    - `"Nutrition Level: Low - Searches for foods that have less than 33% of the highest value for the selected nutrient."`,
    - `"Nutrition Level: Medium - Searches for foods that have between 33% and 66% of the highest value for the selected nutrient."`, or
    - `"Nutrition Level: High - Searches for foods that have greater than 66% of the highest value for the selected nutrient."`
- **1) Valid Input and Expected Output**  \
The valid testing assumes that the input variable has been defined correctly beforehand.

| **Valid Input**        | **Expected Output**         |
|------------------------|-----------------------------|
| `checkRadio("Low")`    | `"Nutrition Level: Low - Searches for foods that have less than 33% of the highest value for the selected nutrient."` |
| `checkRadio("Medium")` | `"Nutrition Level: Medium - Searches for foods that have between 33% and 66% of the highest value for the selected nutrient."` |
| `checkRadio("High")`   | `"Nutrition Level: High - Searches for foods that have greater than 66% of the highest value for the selected nutrient."` |

- **1) Code for the Test Function**
```python
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

```
- **2) Invalid Input and Expected Output**

| **Invalid Input**    | **Expected Output** |
|----------------------|------------------|
| `checkRadio("None")` | `""` |

- **2) Code for the Test Function**
```python
def test_CR_default():
    # TEST -> Checks what string gets returned if user picks the default radio for level filter.
    labelMessage = checkRadio("None")
    assert labelMessage == ""
```

### Test Case 22:
- **Test Function/Module**
  - `test_ECF_errorLevel()`
  - `test_ECF_errorFilter()`
  - `test_ECF_onlyDiet()`
  - `test_ECF_noError()`
- **Tested Function/Module**
  - `errorChecking_filters(isError_filterValue, isError_filterLevel, searchResultArray_value, maxValueDict, nutrientFilter, nutritionLevel, diet)`
- **Description**
  - Brief Description:\
    This function checks if the boolean variable for each filter is True or False. If False, then proceed with the respective filter.
  - Input:
    - **isError_filterValue**: Bool. Indicates whether there is an error or not for said the filter.
    - **isError_filterLevel**: Bool. Indicates whether there is an error or not for said the filter.
    - **searchResultArray_value**: Dataframe. Contains the list of food that was filtered from nutrition range filter.
    - **maxValueDict**: Dict. A dictionary containing the maximum value for each nutrient as the value and the nutrient name as the key.
    - **nutrientFilter**: String. The value obtained from the dropdown menu for nutrition level filter.
    - **nutrientLevel**: String. The level for nutrition level filter.
    - **diet**: String. The dietary need that the user chose.
  - Output:
    - searchResult_level: Dataframe.
    - searchResult_diet: Dataframe.
    - searchResult_valueFinal: Dataframe. Combines every search result for nutrition range filter into one Dataframe.
- **1) Valid Input and Expected Output**  \
The valid testing assumes that the input variable has been defined correctly beforehand.

| **Valid Input**        | **Expected Output**                                                                                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `errorChecking_filters(isError_filterValue, isError_filterLevel, searchResultArray_value, maxValueDict, nutrientFilter, nutritionLevel, diet)`    | `searchResult_level`: A non-empty Dataframe <br> `searchResult_diet`: A non-empty Dataframe <br> `searchResult_valueFinal`: A non-empty Dataframe |

- **1) Code for the Test Function**
```python
def test_ECF_noError():
    searchResult_valueFinal = pd.DataFrame(columns=["food"])
    searchResult_level = pd.DataFrame(columns=["food"])
    searchResult_diet = pd.DataFrame(columns=["food"])

    isError_value = False
    isError_level = False

    # Emulate doing the filter for filter value
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

    # Emulate finding the max value for each nutrient
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    nutrientFilter = "Fat"
    nutrientLevel = "Low"
    diet = "Low Cholesterol Diet"

    searchResult_valueFinal, searchResult_level, searchResult_diet = errorChecking_filters(
        isError_value,
        isError_level,
        searchResultArray,
        maxDict,
        nutrientFilter,
        nutrientLevel,
        diet
    )

    assert not searchResult_level.empty
    assert not searchResult_diet.empty
    assert not searchResult_valueFinal.empty
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                                                                                                 | **Expected Output**                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| ``errorChecking_filters(isError_filterValue, True, searchResultArray_value, maxValueDict, nutrientFilter, nutritionLevel, diet)`` | `searchResult_level`: A non-empty Dataframe <br> `searchResult_diet`: An empty dataframe <br> `searchResult_valueFinal`: A non-empty Dataframe |
| ``errorChecking_filters(True, isError_filterLevel, searchResultArray_value, maxValueDict, nutrientFilter, nutritionLevel, diet)`` | `searchResult_level`: A non-empty Dataframe <br> `searchResult_diet`: A non-empty Dataframe <br> `searchResult_valueFinal`: An empty dataframe |
| ``errorChecking_filters(True, True, searchResultArray_value, maxValueDict, nutrientFilter, nutritionLevel, "Dietary Need")``       | `searchResult_level`: A non-empty Dataframe <br> `searchResult_diet`: A non-empty Dataframe <br> `searchResult_valueFinal`: A non-empty Dataframe |

- **2) Code for the Test Function**
```python
def test_ECF_errorLevel():
    searchResult_valueFinal = pd.DataFrame(columns=["food"])
    searchResult_level = pd.DataFrame(columns=["food"])
    searchResult_diet = pd.DataFrame(columns=["food"])

    isError_value = False
    isError_level = True

    # Emulate doing the filter for filter value
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

    # Emulate finding the max value for each nutrient
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    nutrientFilter = "Choose a nutrient"
    nutrientLevel = "None"
    diet = "Low Cholesterol Diet"

    searchResult_valueFinal, searchResult_level, searchResult_diet = errorChecking_filters(
        isError_value,
        isError_level,
        searchResultArray,
        maxDict,
        nutrientFilter,
        nutrientLevel,
        diet
    )

    assert searchResult_level.empty
    assert not searchResult_diet.empty
    assert not searchResult_valueFinal.empty

def test_ECF_errorFilter():
    searchResult_valueFinal = pd.DataFrame(columns=["food"])
    searchResult_level = pd.DataFrame(columns=["food"])
    searchResult_diet = pd.DataFrame(columns=["food"])

    searchResultArray = []

    isError_value = True
    isError_level = False

    # Emulate finding the max value for each nutrient
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    nutrientFilter = "Fat"
    nutrientLevel = "Low"
    diet = "Low Cholesterol Diet"

    searchResult_valueFinal, searchResult_level, searchResult_diet = errorChecking_filters(
        isError_value,
        isError_level,
        searchResultArray,
        maxDict,
        nutrientFilter,
        nutrientLevel,
        diet
    )

    assert not searchResult_level.empty
    assert not searchResult_diet.empty
    assert searchResult_valueFinal.empty

def test_ECF_onlyDiet():
    searchResult_valueFinal = pd.DataFrame(columns=["food"])
    searchResult_level = pd.DataFrame(columns=["food"])
    searchResult_diet = pd.DataFrame(columns=["food"])

    searchResultArray = []

    isError_value = True
    isError_level = True

    # Emulate finding the max value for each nutrient
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    nutrientFilter = "Choose a nutrient"
    nutrientLevel = "None"
    diet = "Low Cholesterol Diet"

    searchResult_valueFinal, searchResult_level, searchResult_diet = errorChecking_filters(
        isError_value,
        isError_level,
        searchResultArray,
        maxDict,
        nutrientFilter,
        nutrientLevel,
        diet
    )

    assert searchResult_level.empty
    assert not searchResult_diet.empty
    assert searchResult_valueFinal.empty
```

### Test Case 23:
- **Test Function/Module**
  - `test_processFinalResult_noError()`
  - `test_processFinalResult_error()`
- **Tested Function/Module**
  - `processFinalResult(isError_value, minValueArray, isError_level, levelValue, searchResult_valueFinal, searchResult_level, searchResult_diet, errorMessages, defaultDropdown, dropdownArray, minArray, maxArray, nutritionLevel, nutrientFilter, diet):
- **Description**
  - Brief Description:\
    This function process the final result by merging every Dataframe. `mergeResult_everything` and `checkResult` are a part of this function.
  - Input:
    - **isError_value**: Bool. Indicates whether there is an invalid input for range filter or not. Used for validation
    - **minValueArray**: List. A collection of the minimum range that user has put in the input field. Used for validation together for isError_value.
    - **isError_level**: Bool. Indicates whether there is an invalid input for nutrition level filter or not. Used for validation
    - **levelValue**: String. Specifies the filter level. Used for validation together with isError_level.
    - **searchResult_valueFinal**: Dataframe. The combined collection of food from nutrition filter range.
    - **searchResult_level**: Dataframe. Collection of food from nutrition level range.
    - **searchResult_diet**: Dataframe. Collection of food from dietary needs.
    - **errorMessages**: List. A list of all error messages from filter.
    - **defaultDropdown**: List. A list of the default value for the dropdown values for nutrition filter range.
    - **dropdownArray**: List. A list of all the nutrients the user chose for nutrition filter range.
    - **minArray**: List. A list of all the minimum range the user input for nutrition filter range.
    - **maxArray**: List. A list of all the maximum range the user input for nutrition filter range.
    - **nutrientFilter**: String. The value obtained from the dropdown menu for nutrition level filter.
    - **nutrientLevel**: String. The level for nutrition level filter.
    - **diet**: String. The dietary need that the user chose.
  - Output:
    - mergeResult: Dataframe.
    - labelMessage: String. Used to display a message to show how many foods were filtered.
- **1) Valid Input and Expected Output**  \
The valid testing assumes that the input variable has been set correctly beforehand with pre-defined values.

| **Valid Input**                                                                                                                                                                                                                                                                               | **Expected Output**                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| `processFinalResult(isError_value, minValueArray, isError_level, levelValue, searchResult_valueFinal, searchResult_level, searchResult_diet, errorMessages, defaultDropdown, dropdownArray, minArray, maxArray, nutritionLevel, nutrientFilter, diet)`                                        | `labelMessage`: `"402 results were found!"` <br> `mergeResult`: A non-empty Dataframe                                     |
| `processFinalResult(isError_value, minValueArray, isError_level, levelValue, searchResult_valueFinal, searchResult_level, searchResult_diet, errorMessages, defaultDropdown, dropdownArray_default, emptyMinArray, emptyMaxArray, defaultNutritionLevel, defaultNutrientFilter, defaultDiet)` | `labelMessage`: `"No filter was chosen."`  <br> `mergeResult`: A non-empty Dataframe that contains the original Dataframe |

- **1) Code for the Test Function**
```python
def test_processFinalResult_noError():
    # We have to initialize everything since this function is the final step of the filter process.
    mergeResult = []
    labelMessage = ""

    searchResult_valueFinal = pd.DataFrame(columns=["food"])
    searchResult_level = pd.DataFrame(columns=["food"])
    searchResult_diet = pd.DataFrame(columns=["food"])

    isError_value = False
    isError_level = False

    errorMessages = ["", "", "", "", ""]

    defaultDropdown = ["Macronutrients", "Vitamins", "Minerals", "Others"]

    # Emulate doing the filter for filter value
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

    # Emulate finding the max value for each nutrient
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    nutrientFilter = "Fat"
    nutrientLevel = "Low"
    diet = "Dietary Needs"

    searchResult_valueFinal, searchResult_level, searchResult_diet = errorChecking_filters(
        isError_value,
        isError_level,
        searchResultArray,
        maxDict,
        nutrientFilter,
        nutrientLevel,
        diet
    )

    # The actual function that's being tested
    mergeResult, labelMessage = processFinalResult(
        isError_value,
        minArray,
        isError_level,
        nutrientLevel,
        searchResult_valueFinal,
        searchResult_level,
        searchResult_diet,
        errorMessages,
        defaultDropdown,
        dropdownArray,
        minArray,
        maxArray,
        nutrientLevel,
        nutrientFilter,
        diet
    )
    assert labelMessage == "402 result(s) were found!"
    assert not mergeResult.empty

def test_processFinalResult_reset():
    mergeResult = []
    labelMessage = ""

    searchResult_valueFinal = pd.DataFrame(columns=["food"])
    searchResult_level = pd.DataFrame(columns=["food"])
    searchResult_diet = pd.DataFrame(columns=["food"])

    isError_value = False
    isError_level = False

    errorMessages = ["", "", "", "", ""]

    defaultDropdown = ["Macronutrients", "Vitamins", "Minerals", "Others"]
    minArray = ["", "", "", ""]
    maxArray = ["", "", "", ""]

    # Emulate doing the filter for filter value
    searchResultArray = []
    mergedResult = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Macronutrients", "Vitamins", "Minerals", "Others"]
    minArray = ["", "", "", ""]
    maxArray = ["", "", "", ""]
    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray, minArray, maxArray, isError, searchResultArray)

    # Emulate finding the max value for each nutrient
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    nutrientFilter = "Choose a nutrient"
    nutrientLevel = "None"
    diet = "Dietary Needs"

    # The actual function that's being tested
    mergeResult, labelMessage = processFinalResult(
        isError_value,
        minArray,
        isError_level,
        nutrientLevel,
        searchResult_valueFinal,
        searchResult_level,
        searchResult_diet,
        errorMessages,
        defaultDropdown,
        dropdownArray,
        minArray,
        maxArray,
        nutrientLevel,
        nutrientFilter,
        diet
    )

    print(mergeResult)
    print(labelMessage)
    dataFrame = loadData(r"Food_Nutrition_Dataset.csv", True)

    assert len(mergeResult) == (len(dataFrame))
    assert labelMessage == "No filter was chosen."

```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                                                                                                                                                                                                                                                                   | **Expected Output**                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| `processFinalResult(isError_value, minValueArray, isError_level, levelValue, searchResult_valueFinal, searchResult_level, searchResult_diet, ["error", "", "", ""], defaultDropdown, dropdownArray_default, emptyMinArray, emptyMaxArray, defaultNutritionLevel, defaultNutrientFilter, defaultDiet)` | `labelMessage`: `""`  <br> `mergeResult`: An empty Dataframe |

- **2) Code for the Test Function**
```python
    # We have to initialize everything since this function is the final step of the filter process.
    mergeResult = []
    labelMessage = ""

    searchResult_valueFinal = pd.DataFrame(columns=["food"])
    searchResult_level = pd.DataFrame(columns=["food"])
    searchResult_diet = pd.DataFrame(columns=["food"])

    isError_value = False
    isError_level = False

    errorMessages = ["error", "", "", "", ""]

    defaultDropdown = ["Macronutrients", "Vitamins", "Minerals", "Others"]
    minArray = ["", "", "", ""]
    maxArray = ["", "", "", ""]

    # Emulate doing the filter for filter value
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

    # Emulate finding the max value for each nutrient
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    nutrientFilter = "Fat"
    nutrientLevel = "Low"
    diet = "Dietary Needs"

    searchResult_valueFinal, searchResult_level, searchResult_diet = errorChecking_filters(
        isError_value,
        isError_level,
        searchResultArray,
        maxDict,
        nutrientFilter,
        nutrientLevel,
        diet
    )

    # The actual function that's being tested
    mergeResult, labelMessage = processFinalResult(
        isError_value,
        minArray,
        isError_level,
        nutrientLevel,
        searchResult_valueFinal,
        searchResult_level,
        searchResult_diet,
        errorMessages,
        defaultDropdown,
        dropdownArray,
        minArray,
        maxArray,
        nutrientLevel,
        nutrientFilter,
        diet
    )

    assert not mergeResult
    assert labelMessage == ""
```
### Test Case 24:
- **Test Function/Module**
  - `test_determineFood_emptyMerged()`
  - `test_determinedFood_filledMerged()`
- **Tested Function/Module**
  - `determineFoodSearch(dataFrame, mergedResult, keyword)`
- **Description**
  - Brief Description:\
    This function will check whether the user have done a filter or not. \
    If not, then use the whole dataframe to search through the user's input. Else, use the filtered result to search through the user's input.
  - Input:
    - **dataFrame**: Dataframe. Contains the original non-modified Dataframe from the .csv file.
    - **mergedResult**: Dataframe. The merged result for all filters.
    - **keyword**: String. User's input in the search bar.
  - Output:
    - DataFrame
- **1) Valid Input and Expected Output**  \
The valid testing assumes that the input variable has been defined correctly beforehand.

| **Valid Input**                                         | **Expected Output**    |
|---------------------------------------------------------|------------------------|
| `determineFoodSearch(dataFrame, mergedResult, keyword)` | A non-empty Dataframe. |

- **1) Code for the Test Function**
```python
def test_determinedFood_filledMerged():
    # Emulate the process of filtering first
    mergedResult = []
    labelMessage = ""

    searchResult_valueFinal = pd.DataFrame(columns=["food"])
    searchResult_level = pd.DataFrame(columns=["food"])
    searchResult_diet = pd.DataFrame(columns=["food"])

    isError_value = False
    isError_level = False

    errorMessages = ["", "", "", "", ""]

    defaultDropdown = ["Macronutrients", "Vitamins", "Minerals", "Others"]
    minArray = ["", "", "", ""]
    maxArray = ["", "", "", ""]

    # Emulate doing the filter for filter value
    searchResultArray = []
    mergedResult_filter = []
    errorChooseNutrient = []
    errorInputValue = []
    errorComparisonValue = []
    isError = True
    dropdownArray = ["Macronutrients", "Vitamins", "Minerals", "Others"]
    minArray = ["", "", "", ""]
    maxArray = ["", "", "", ""]
    errorChooseNutrient, errorInputValue, errorComparisonValue, isError = checkDropdownAndInput_value(dropdownArray,
                                                                                                      minArray,
                                                                                                      maxArray, isError,
                                                                                                      searchResultArray)
    # Emulate finding the max value for each nutrient
    dataFrameForDict = loadData(r"Food_Nutrition_Dataset.csv")
    maxDict = findNutritionValue(allLabel, dataFrameForDict)

    nutrientFilter = "Caloric Value"
    nutrientLevel = "High"
    diet = "Dietary Needs"

    searchResult_valueFinal, searchResult_level, searchResult_diet = errorChecking_filters(
        isError_value,
        isError_level,
        searchResultArray,
        maxDict,
        nutrientFilter,
        nutrientLevel,
        diet
    )

    # The actual function that's being tested
    mergedResult, labelMessage = processFinalResult(
        isError_value,
        minArray,
        isError_level,
        nutrientLevel,
        searchResult_valueFinal,
        searchResult_level,
        searchResult_diet,
        errorMessages,
        defaultDropdown,
        dropdownArray,
        minArray,
        maxArray,
        nutrientLevel,
        nutrientFilter,
        diet
    )

    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", True)

    searchResult = determineFoodSearch(dataFrame, mergedResult, "Apricot Jam")

    assert len(searchResult) == 0
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                             | **Expected Output**                                  |
|---------------------------------------------------------------|------------------------------------------------------|
| `determineFoodSearch(dataFrame, emptyMergedResult, keyword)`` | A non-empty Dataframe that has all of the food name. |

- **2) Code for the Test Function**
```python
def test_determineFood_emptyMerged():
    dataFrame = loadData(r".\Food_Nutrition_Dataset.csv", True)
    mergedResult = pd.DataFrame(columns=["food"])

    searchResult = determineFoodSearch(dataFrame, mergedResult, "Apricot Jam")

    assert len(searchResult) == 1
```

## 3. **Testing Report Summary**

[//]: # (Include a screenshot of unit_test.html showing the results of all the above tests. )

[//]: # ()
[//]: # (You can use the following command to run the unit tests and generate the unit_test.html report.)

[//]: # ()
[//]: # (```commandline)

[//]: # (pytest test_all_functions.py --html=unit_test.html --self-contained-html)

[//]: # (```)

[//]: # (Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related )

[//]: # (to the five required features.)

![unit_test_summary](./Unit_test.png)
