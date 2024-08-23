# Software Design Document

## Project Name: XXXX
## Group Number: 039

## Team members

| Student Number | Name      | 
|----------------|-----------|
| s5340805        | Toby Nilson |
| s5330262        | Jason Kenaz | 


<div style="page-break-after: always;"></div>



# Table of Contents

<!-- TOC -->
* [Table of Contents](#table-of-contents)
  * [1. System Vision](#1-system-vision)
    * [1.1 Problem Background](#11-problem-background)
    * [1.2 System capabilities/overview](#12-system-capabilitiesoverview)
    * [1.3	Potential Benefits](#13potential-benefits)
  * [2. Requirements](#2-requirements)
    * [2.1 User Requirements](#21-user-requirements)
    * [2.2	Software Requirements](#22software-requirements)
    * [2.3 Use Case Diagrams](#23-use-case-diagrams)
    * [2.4 Use Cases](#24-use-cases)
  * [3.	Software Design and System Components](#3-software-design-and-system-components-)
    * [3.1	Software Design](#31software-design)
    * [3.2	System Components](#32system-components)
      * [3.2.1 Functions](#321-functions)
      * [3.2.2 Data Structures / Data Sources](#322-data-structures--data-sources)
      * [3.2.3 Detailed Design](#323-detailed-design)
  * [4. User Interface Design](#4-user-interface-design)
    * [4.1 Structural Design](#41-structural-design)
    * [4.2	Visual Design](#42visual-design)
<!-- TOC -->


<div style="page-break-after: always;"></div>



### 1.1 Problem Background
<!-- - Problem Identification: What problem does this system solve?
- Dataset: What is the dataset used?
- Data Input/Output: What kind of data input and output is required?
- Target Users: Who will use the system, and why? -->
- Problem Identification\
The problem addressed by this tool is the lack of comprehensive tools that integrate both analysis and visualization of nutritional information for a wide range of foods. The purpose of this tool is to combine both functionalities efficiently so that the users can get valuable insights from nutritional data.
- Dataset\
The dataset for this project is provided by the client in the ".csv" file format. It provides detailed nutritional information for a wide range of common food items. These information provide critical data that can help in understanding the nutritional content of various foods.
- Data\
<!-- TO DO: Don't forget to add this later -->
- Target Users
  - **People with Specific Dietary Needs**\
  Individuals with dietary restrictions because of disease, allergies, or personal preferences can utilize the tool to track their nutritional intake and plan their diets.
  - **Nutritionist and Dietitians**\
  These professionals can utilize the tool to analyze and visualize the nutritional breakdown of various foods either for their clients or research purposes.
  - **Researchers**\
  Researchers can apply the tool for nutritional studies, helping them identify correlations between dietary habits and health markers in order to research how certain nutrients can affect an individual's health. <br>
In summary, the system provides detailed analysis, visualization, and filtering functionalities for anyone interested in dietary, health and medical research. The primary goal of this tool is to offer insights that support better dietary decisions and health outcomes.

### 1.2 System capabilities/overview
- System Functionality\
The tool will let users search for foods by name and break down their nutritional information through visualizations. These visualizations come in the form of pie charts and bar graphs. The search function will also include filters that enable users to find foods based on defined nutritional ranges, specific levels of nutritional content, and/or specific dietary needs (e.g., ketogenic diet, low sodium, low cholesterol) to facilitate diet planning.
- Features and Functionalities\
<!-- Describe the key features and functionalities of the system. -->
1. **Food Search**\
Enable users to search for foods by name and display all the nutritional information;
2. **Nutrition Breakdown**\
Enable users to select one food, and display pie charts & bar graphs showing the breakdown of different nutrients for the selected food.
3. **Nutrition Range Filter**\
Enable users to select one of nutrition and input minimum & maximum values, and the tool will display a list of foods that fall within those ranges.
4. **Nutrition Level Filter**\
Enable users to filter foods by nutritional content levels—low, mid, and high—including fat, protein, carbohydrates, sugar, and nutritional density. The three levels are defined as follows:
- Low: Less than 33% of the highest value.
- Mid: Between 33% and 66% of the highest value.
- High: Greater than 66% of the highest value.
5. **Dietary Filter**\
Enable users to filter foods based on the three dietary needs that the software have provided. The three dietary needs are: keto, low-sodium, and low-cholesterol diet. The requirements for these dietary needs are defined as follow:
- Ketogenic (Keto) Diet \
Low in carbohydrates, which is less than 5-10% of caloric intake.
- Low Sodium Diet \
Foods with low sodium content, which usually is less than 140mg per serving.
- Low Cholesterol Diet \
Low cholestrol foods that have less than 20mg per serving. \
Additional dietary needs will be added if the system can be finished before the due date.

### 1.3	Benefit Analysis
<!-- How will this system provide value or benefit? -->
- The system assists users in meal preparation based on their dietary needs with the help of the in-depth filters. This leads to a more personalized nutrition management for each user as they can plan their diet and food choices through the provided filters.
- Advanced filtering options enable users to quickly find foods that meet their dietary needs and/or nutritional goals, which helps them save time in meal planning and grocery shopping. The dietary filter also helps users in identifying foods that are suitable to their diet.
- The system helps users make informed decision about their food choices through detailed nutritional data and visualizations.
- Nutritional breakdowns can also be presented in visual formats, such as pie charts and bar graphs, to help users in understanding key information through a format that is more understandable and digestible.


## 2. Requirements

### 2.1 User Requirements

Detail how users are expected to interact with or use the program. What functionalities must the system provide from the end-user perspective? This can include both narrative descriptions and a listing of user needs.

Note: Since no specific client or user is assigned, you may create a fictional user. Who do you envision using your software?

### 2.2	Software Requirements
Define the functionality the software will provide. This section should list requirements formally, often using the word "shall" to describe functionalities.

Example Functional Requirements:  
- R1.1 The program shall accept multiple file names as arguments from the command line.  
- R1.2 Each file name can be a simple file name or include the full path of the file with one or more levels.  

- etc …

### 2.3 Use Case Diagram
Provide a system-level Use Case Diagram illustrating all required features.

Example:  
![Use Case Diagram](./UCD.png)

### 2.4 Use Cases
Include at least 5 use cases, each corresponding to a specific function.


| Use Case ID    | xxx  |
|----------------|------|
| Use Case Name  | xxxx |
| Actors         | xxxx |
| Description    | xxxx |
| Flow of Events | xxxx |
| Alternate Flow | xxxx |



## 3.	Software Design and System Components 

### 3.1	Software Design
Include a flowchart that illustrates how your software will operate.

Example:  
![Software Design](./software_design_flowchart.png)

### 3.2	System Components

#### 3.2.1 Functions
List all key functions within the software. For each function, provide:
- Description: Brief explanation of the function’s purpose.
- Input Parameters: List parameters, their data types, and their use.
- Return Value: Describe what the function returns.
- Side Effects: Note any side effects, such as changes to global variables or data passed by reference.

#### 3.2.2 Data Structures / Data Sources
List all data structures or sources used in the software. For each, provide:

- Type: Type of data structure (e.g., list, set, dictionary).
- Usage: Describe where and how it is used.
- Functions: List functions that utilize this structure.

#### 3.2.3 Detailed Design
Provide pseudocode or flowcharts for all functions listed in Section 3.2.1 that operate on data structures. For instance, include pseudocode or a flowchart for a custom searching function.


## 4. User Interface Design

### 4.1 Structural Design
Present a structural design, a hierarchy chart, showing the overall interface’s structure. Address:

- Structure: How will the software be structured?
- Information Grouping: How will information be organized?
- Navigation: How will users navigate through the software?
- Design Choices: Explain why these design choices were made.

Example:  
![Structural Design](./Structural_Design.png)

### 4.2	Visual Design
Include all wireframes or mock-ups of the interface. Provide a discussion, explanation, and justification for your design choices. Hand-drawn wireframes are acceptable.

- Interface Components: Clearly label all components.
- Screens/Menus: Provide wireframes for different screens, menus, and options.
- Design Details: Focus on the layout and size of components; color and graphics are not required. 

Example:  
![Visual Design](./visual_design.png)



