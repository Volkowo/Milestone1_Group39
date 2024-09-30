# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class NutritionApp
###########################################################################

class NutritionApp ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1200,900 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        everything = wx.BoxSizer( wx.VERTICAL )

        self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.searchAndTable = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        PageOneContainer = wx.BoxSizer( wx.VERTICAL )

        searchBarAndTable = wx.BoxSizer( wx.HORIZONTAL )

        self.searchInput = wx.TextCtrl( self.searchAndTable, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
        searchBarAndTable.Add( self.searchInput, 0, wx.ALL|wx.EXPAND, 5 )


        searchBarAndTable.Add( ( 10, 0), 0, 0, 5 )

        self.searchButton = wx.Button( self.searchAndTable, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0 )
        searchBarAndTable.Add( self.searchButton, 0, wx.ALL, 5 )

        self.extraInfo = wx.StaticText( self.searchAndTable, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.extraInfo.Wrap( -1 )

        searchBarAndTable.Add( self.extraInfo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        PageOneContainer.Add( searchBarAndTable, 0, wx.EXPAND, 5 )

        tableAndChart = wx.BoxSizer( wx.HORIZONTAL )

        table = wx.BoxSizer( wx.VERTICAL )

        self.foodData = wx.grid.Grid( self.searchAndTable, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )

        # Grid
        self.foodData.CreateGrid( 5, 5 )
        self.foodData.EnableEditing( True )
        self.foodData.EnableGridLines( True )
        self.foodData.EnableDragGridSize( False )
        self.foodData.SetMargins( 0, 0 )

        # Columns
        self.foodData.EnableDragColMove( False )
        self.foodData.EnableDragColSize( True )
        self.foodData.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.foodData.EnableDragRowSize( True )
        self.foodData.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.foodData.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        table.Add( self.foodData, 1, wx.ALL, 5 )


        tableAndChart.Add( table, 0, wx.EXPAND, 5 )

        chart = wx.BoxSizer( wx.VERTICAL )

        self.pieChartPanel = wx.Panel( self.searchAndTable, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        chart.Add( self.pieChartPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.barChartPanel = wx.Panel( self.searchAndTable, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        chart.Add( self.barChartPanel, 1, wx.EXPAND |wx.ALL, 5 )


        tableAndChart.Add( chart, 1, wx.EXPAND, 5 )


        PageOneContainer.Add( tableAndChart, 1, wx.EXPAND, 5 )


        self.searchAndTable.SetSizer( PageOneContainer )
        self.searchAndTable.Layout()
        PageOneContainer.Fit( self.searchAndTable )
        self.notebook.AddPage( self.searchAndTable, _(u"Search"), False )
        self.filter = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        filterContainer = wx.BoxSizer( wx.VERTICAL )

        self.filter_nutritionValue = wx.StaticText( self.filter, wx.ID_ANY, _(u"Filter by Nutrition Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.filter_nutritionValue.Wrap( -1 )

        self.filter_nutritionValue.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        filterContainer.Add( self.filter_nutritionValue, 0, wx.ALL, 5 )

        filter_nutritionValueMacro = wx.BoxSizer( wx.HORIZONTAL )

        choiceMacroChoices = [ _(u"Macronutrients"), _(u"Fat"), _(u"Saturated Fats"), _(u"Monounsaturated Fats"), _(u"Polyunsaturated Fats"), _(u"Carbohydrates"), _(u"Sugars"), _(u"Protein"), _(u"Dietary Fiber") ]
        self.choiceMacro = wx.Choice( self.filter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceMacroChoices, 0 )
        self.choiceMacro.SetSelection( 0 )
        filter_nutritionValueMacro.Add( self.choiceMacro, 0, wx.ALL, 5 )


        filter_nutritionValueMacro.Add( ( 50, 1), 0, wx.EXPAND, 5 )

        self.minValueText_macro = wx.StaticText( self.filter, wx.ID_ANY, _(u"Min Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.minValueText_macro.Wrap( -1 )

        filter_nutritionValueMacro.Add( self.minValueText_macro, 0, wx.ALL, 5 )

        self.minValueInput_macro = wx.TextCtrl( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        filter_nutritionValueMacro.Add( self.minValueInput_macro, 0, wx.ALL, 5 )


        filter_nutritionValueMacro.Add( ( 30, 0), 0, wx.EXPAND, 5 )

        self.maxValueText_macro = wx.StaticText( self.filter, wx.ID_ANY, _(u"Max Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.maxValueText_macro.Wrap( -1 )

        filter_nutritionValueMacro.Add( self.maxValueText_macro, 0, wx.ALL, 5 )

        self.maxValueInput_macro = wx.TextCtrl( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        filter_nutritionValueMacro.Add( self.maxValueInput_macro, 0, wx.ALL, 5 )


        filterContainer.Add( filter_nutritionValueMacro, 0, wx.EXPAND, 5 )

        filter_nutritionValueVitamin = wx.BoxSizer( wx.HORIZONTAL )

        choiceVitaminChoices = [ _(u"Vitamins"), _(u"Vitamin A"), _(u"Vitamin B1"), _(u"Vitamin B11"), _(u"Vitamin B12"), _(u"Vitamin B2"), _(u"Vitamin B3"), _(u"Vitamin B5"), _(u"Vitamin B6"), _(u"Vitamin C"), _(u"Vitamin D"), _(u"Vitamin E"), _(u"Vitamin K") ]
        self.choiceVitamin = wx.Choice( self.filter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceVitaminChoices, 0 )
        self.choiceVitamin.SetSelection( 0 )
        filter_nutritionValueVitamin.Add( self.choiceVitamin, 0, wx.ALL, 5 )


        filter_nutritionValueVitamin.Add( ( 106, 1), 0, wx.EXPAND, 5 )

        self.minValueText_vitamin = wx.StaticText( self.filter, wx.ID_ANY, _(u"Min Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.minValueText_vitamin.Wrap( -1 )

        filter_nutritionValueVitamin.Add( self.minValueText_vitamin, 0, wx.ALL, 5 )

        self.minValueInput_vitamin = wx.TextCtrl( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        filter_nutritionValueVitamin.Add( self.minValueInput_vitamin, 0, wx.ALL, 5 )


        filter_nutritionValueVitamin.Add( ( 30, 0), 0, wx.EXPAND, 5 )

        self.maxValueText_vitamin = wx.StaticText( self.filter, wx.ID_ANY, _(u"Max Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.maxValueText_vitamin.Wrap( -1 )

        filter_nutritionValueVitamin.Add( self.maxValueText_vitamin, 0, wx.ALL, 5 )

        self.maxValueInput_vitamin = wx.TextCtrl( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        filter_nutritionValueVitamin.Add( self.maxValueInput_vitamin, 0, wx.ALL, 5 )


        filterContainer.Add( filter_nutritionValueVitamin, 0, wx.EXPAND, 5 )

        filter_nutritionValueMinerals = wx.BoxSizer( wx.HORIZONTAL )

        choiceMineralChoices = [ _(u"Minerals"), _(u"Calcium"), _(u"Copper"), _(u"Iron"), _(u"Magnesium"), _(u"Manganese"), _(u"Phosphorus"), _(u"Potassium"), _(u"Selenium"), _(u"Sodium"), _(u"Zinc") ]
        self.choiceMineral = wx.Choice( self.filter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceMineralChoices, 0 )
        self.choiceMineral.SetSelection( 0 )
        filter_nutritionValueMinerals.Add( self.choiceMineral, 0, wx.ALL, 5 )


        filter_nutritionValueMinerals.Add( ( 106, 1), 0, wx.EXPAND, 5 )

        self.minValueText_mineral = wx.StaticText( self.filter, wx.ID_ANY, _(u"Min Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.minValueText_mineral.Wrap( -1 )

        filter_nutritionValueMinerals.Add( self.minValueText_mineral, 0, wx.ALL, 5 )

        self.minValueInput_mineral = wx.TextCtrl( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        filter_nutritionValueMinerals.Add( self.minValueInput_mineral, 0, wx.ALL, 5 )


        filter_nutritionValueMinerals.Add( ( 30, 0), 0, wx.EXPAND, 5 )

        self.maxValueText_mineral = wx.StaticText( self.filter, wx.ID_ANY, _(u"Max Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.maxValueText_mineral.Wrap( -1 )

        filter_nutritionValueMinerals.Add( self.maxValueText_mineral, 0, wx.ALL, 5 )

        self.maxValueInput_mineral = wx.TextCtrl( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        filter_nutritionValueMinerals.Add( self.maxValueInput_mineral, 0, wx.ALL, 5 )


        filterContainer.Add( filter_nutritionValueMinerals, 0, wx.EXPAND, 5 )

        filter_nutritionValueOthers = wx.BoxSizer( wx.HORIZONTAL )

        choiceOtherChoices = [ _(u"Others"), _(u"Cholesterol"), _(u"Water"), _(u"Nutrition Density"), _(u"Caloric Value") ]
        self.choiceOther = wx.Choice( self.filter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceOtherChoices, 0 )
        self.choiceOther.SetSelection( 0 )
        filter_nutritionValueOthers.Add( self.choiceOther, 0, wx.ALL, 5 )


        filter_nutritionValueOthers.Add( ( 79, 0), 0, wx.EXPAND, 5 )

        self.minValueText_other = wx.StaticText( self.filter, wx.ID_ANY, _(u"Min Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.minValueText_other.Wrap( -1 )

        filter_nutritionValueOthers.Add( self.minValueText_other, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.minValueInput_other = wx.TextCtrl( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        filter_nutritionValueOthers.Add( self.minValueInput_other, 0, wx.ALL, 5 )


        filter_nutritionValueOthers.Add( ( 30, 0), 0, wx.EXPAND, 5 )

        self.maxValueText_other = wx.StaticText( self.filter, wx.ID_ANY, _(u"Max Value"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.maxValueText_other.Wrap( -1 )

        filter_nutritionValueOthers.Add( self.maxValueText_other, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.maxValueInput_other = wx.TextCtrl( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        filter_nutritionValueOthers.Add( self.maxValueInput_other, 0, wx.ALL, 5 )


        filterContainer.Add( filter_nutritionValueOthers, 0, wx.EXPAND, 5 )

        self.errorMsg_filterValue1 = wx.StaticText( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errorMsg_filterValue1.Wrap( -1 )

        filterContainer.Add( self.errorMsg_filterValue1, 0, wx.ALL, 5 )

        self.errorMsg_filterValue2 = wx.StaticText( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errorMsg_filterValue2.Wrap( -1 )

        filterContainer.Add( self.errorMsg_filterValue2, 0, wx.ALL, 5 )

        self.errorMsg_filterValue3 = wx.StaticText( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errorMsg_filterValue3.Wrap( -1 )

        filterContainer.Add( self.errorMsg_filterValue3, 0, wx.ALL, 5 )


        filterContainer.Add( ( 0, 15), 0, wx.EXPAND, 5 )

        self.filter_nutritionLevel = wx.StaticText( self.filter, wx.ID_ANY, _(u"Filter by Nutrition Level"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.filter_nutritionLevel.Wrap( -1 )

        self.filter_nutritionLevel.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        filterContainer.Add( self.filter_nutritionLevel, 0, wx.ALL, 5 )

        filter_nutritionLevel = wx.BoxSizer( wx.VERTICAL )

        nutritionLevelFilterChoices = [ _(u"None"), _(u"Low"), _(u"Medium"), _(u"High") ]
        self.nutritionLevelFilter = wx.RadioBox( self.filter, wx.ID_ANY, _(u"Nutrition Level"), wx.DefaultPosition, wx.DefaultSize, nutritionLevelFilterChoices, 1, wx.RA_SPECIFY_COLS )
        self.nutritionLevelFilter.SetSelection( 0 )
        filter_nutritionLevel.Add( self.nutritionLevelFilter, 0, wx.ALL|wx.EXPAND, 5 )

        choiceNutrientChoices = [ _(u"Choose a nutrient"), _(u"Fat"), _(u"Saturated Fats"), _(u"Monounsaturated Fats"), _(u"Polyunsaturated Fats"), _(u"Carbohydrates"), _(u"Sugars"), _(u"Protein"), _(u"Dietary Fiber"), _(u"Vitamin A"), _(u"Vitamin B1"), _(u"Vitamin B11"), _(u"Vitamin B12"), _(u"Vitamin B2"), _(u"Vitamin B3"), _(u"Vitamin B5"), _(u"Vitamin B6"), _(u"Vitamin C"), _(u"Vitamin D"), _(u"Vitamin E"), _(u"Vitamin K"), _(u"Calcium"), _(u"Copper"), _(u"Iron"), _(u"Magnesium"), _(u"Manganese"), _(u"Phosphorus"), _(u"Potassium"), _(u"Selenium"), _(u"Sodium"), _(u"Zinc"), _(u"Cholesterol"), _(u"Water"), _(u"Nutrition Density"), _(u"Caloric Value") ]
        self.choiceNutrient = wx.Choice( self.filter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceNutrientChoices, 0 )
        self.choiceNutrient.SetSelection( 3 )
        filter_nutritionLevel.Add( self.choiceNutrient, 0, wx.ALL|wx.EXPAND, 5 )


        filterContainer.Add( filter_nutritionLevel, 0, wx.TOP|wx.EXPAND, 5 )

        self.errorMsg_level1 = wx.StaticText( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errorMsg_level1.Wrap( -1 )

        filterContainer.Add( self.errorMsg_level1, 0, wx.ALL, 5 )

        self.errorMsg_level2 = wx.StaticText( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errorMsg_level2.Wrap( -1 )

        filterContainer.Add( self.errorMsg_level2, 0, wx.ALL, 5 )


        filterContainer.Add( ( 0, 10), 0, wx.EXPAND, 5 )

        self.filter_nutritionLevel1 = wx.StaticText( self.filter, wx.ID_ANY, _(u"Filter by Dietary Needs"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.filter_nutritionLevel1.Wrap( -1 )

        self.filter_nutritionLevel1.SetFont( wx.Font( 13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        filterContainer.Add( self.filter_nutritionLevel1, 0, wx.ALL, 5 )

        filter_dietaryNeeds = wx.BoxSizer( wx.HORIZONTAL )

        choiceDietChoices = [ _(u"Dietary Needs"), _(u"Ketogenic Diet"), _(u"Low Sodium Diet"), _(u"Low Cholesterol Diet") ]
        self.choiceDiet = wx.Choice( self.filter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceDietChoices, 0 )
        self.choiceDiet.SetSelection( 0 )
        filter_dietaryNeeds.Add( self.choiceDiet, 0, wx.ALL, 5 )


        filterContainer.Add( filter_dietaryNeeds, 0, wx.EXPAND, 5 )


        filterContainer.Add( ( 0, 25), 0, wx.EXPAND, 5 )

        self.text_extraFilterInfo = wx.StaticText( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text_extraFilterInfo.Wrap( -1 )

        self.text_extraFilterInfo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        filterContainer.Add( self.text_extraFilterInfo, 0, wx.ALL, 5 )

        self.text_filterResult = wx.StaticText( self.filter, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.text_filterResult.Wrap( -1 )

        self.text_filterResult.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        filterContainer.Add( self.text_filterResult, 0, wx.ALL, 5 )


        filterContainer.Add( ( 0, 50), 0, wx.EXPAND, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        self.filterButton = wx.Button( self.filter, wx.ID_ANY, _(u"Filter"), wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
        bSizer14.Add( self.filterButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer14.Add( ( 25, 0), 1, wx.EXPAND, 5 )

        self.resetButton = wx.Button( self.filter, wx.ID_ANY, _(u"Reset Filter"), wx.DefaultPosition, wx.Size( 140,-1 ), 0 )
        bSizer14.Add( self.resetButton, 0, wx.ALL, 5 )


        filterContainer.Add( bSizer14, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.filter.SetSizer( filterContainer )
        self.filter.Layout()
        filterContainer.Fit( self.filter )
        self.notebook.AddPage( self.filter, _(u"Filter"), True )

        everything.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( everything )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.searchButton.Bind( wx.EVT_BUTTON, self.searchFood )
        self.foodData.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.nutritionBreakdown )
        self.nutritionLevelFilter.Bind( wx.EVT_RADIOBOX, self.explanationText )
        self.choiceDiet.Bind( wx.EVT_CHOICE, self.explanationText_diet )
        self.filterButton.Bind( wx.EVT_BUTTON, self.filterFood )
        self.resetButton.Bind( wx.EVT_BUTTON, self.resetFilter )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def searchFood( self, event ):
        event.Skip()

    def nutritionBreakdown( self, event ):
        event.Skip()

    def explanationText( self, event ):
        event.Skip()

    def explanationText_diet( self, event ):
        event.Skip()

    def filterFood( self, event ):
        event.Skip()

    def resetFilter( self, event ):
        event.Skip()


