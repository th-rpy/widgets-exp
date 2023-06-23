To create a dictionary from the unique values of two cells in Excel, you can use VBA (Visual Basic for Applications) code. Here's an example of how you can accomplish this:

1. Press ALT+F11 to open the VBA Editor in Excel.
2. Insert a new module by clicking on "Insert" and then selecting "Module."
3. In the module, paste the following code:

```vba
Function CreateDictionary(ByVal cell1 As Range, ByVal cell2 As Range) As Object
    Dim dict As Object
    Set dict = CreateObject("Scripting.Dictionary")
    
    ' Get the values from cell1 and cell2
    Dim value1 As Variant
    Dim value2 As Variant
    value1 = cell1.Value
    value2 = cell2.Value
    
    ' Add the values to the dictionary
    If Not dict.Exists(value1) Then
        dict.Add value1, value2
    End If
    
    ' Return the dictionary
    Set CreateDictionary = dict
End Function
```

4. Close the VBA Editor.
5. In your Excel worksheet, enter the formula `=CreateDictionary(A1, B1)` in a cell, where `A1` and `B1` are the cells containing the values you want to use.
6. Press Enter to see the dictionary created as the result.

Note: This code assumes that the values in the two cells are located in cells A1 and B1, respectively. You can modify the range references (`A1` and `B1`) in the formula to match the actual cell references you are using.

The VBA code creates a dictionary object, checks if the value from `cell1` already exists in the dictionary, and if not, adds the values from `cell1` and `cell2` as key-value pairs to the dictionary. Finally, it returns the dictionary as the result of the custom Excel function `CreateDictionary`.
