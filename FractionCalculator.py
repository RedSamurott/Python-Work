# -----------------------------------------------------------------------------
# 
# File Name: FractionCalculator.py
#
# Author: Donald Summers, code majorly authored by Doug Galarus
#
# Description:  A simple calculator for fraction addition, subtraction,
#               multiplication, and division using Tkinter, with also
#               the use of my ExceptionalFractions.py program
#
# How to use:   Execute the script and the calculator graphical user interface 
#               is displayed. Interact with the interface by entering fraction
#               values and selecting the addition, subtractor, multiply operator 
#               or divisor buttons.
#
#               python FractionCalculator.py
#
# -----------------------------------------------------------------------------

# Import tkinter package. Note that an alias is not provided, so functionality
# is referenced directly.
from tkinter import *

# Import Tk-themed widgets package.
from tkinter import ttk

# Import my ExceptionalFractions file for my math
import ExceptionalFractions as EF

# -----------------------------------------------------------------------------
# Function: clickAdd
#
# Inputs:
#   none
#
# Return Value:
#   none
#
# Example Use:
#   clickAdd()
#
# Description:
#   Callback / Event Handler for click on Addition button.
#   Gets the values of the fractions from the entry widgets.
#   Computes the sum and sets the result label to show the value.
#   Changes the operator label to display +.
#
# Exceptions:
#   Does not throw exceptions directly. If an exception occurs in the process
#   of getting the fractions, then displays the Exception text in the error label.
#   If no exception is thrown in the process, the error label is set to the 
#   empty string.
# -----------------------------------------------------------------------------
def clickAdd():
    # Change the operator label to display +.
    lblOperator.config(text="+")
    # Try to get the values, compute the result and display the result.
    try:
        # Get the fraction values from the entry widgets.
        f1,f2 = getFractions()
        # Set the result label to the sum.
        setResult(EF.addFractions(f1,f2))
        # If execution gets to this point then there are no errors.
        # Set the error label to the empty string to clear prior errors.
        lblError.config(text="")
    # Handle exceptions.
    except Exception as e:
        # Display the exception in the error label.
        lblError.config(text="ERROR: " + str(e))


# -----------------------------------------------------------------------------
# Function: clickSubtract
#
# Inputs:
#   none
#
# Return Value:
#   none
#
# Example Use:
#   clickSubtract()
#
# Description:
#   Callback / Event Handler for click on Subtraction button.
#   Gets the values of the fractions from the entry widgets.
#   Computes the difference and sets the result label to show the value.
#   Changes the operator label to display -.
#
# Exceptions:
#   Does not throw exceptions directly. If an exception occurs in the process
#   of getting the fractions, then displays the Exception text in the error label.
#   If no exception is thrown in the process, the error label is set to the 
#   empty string.
# -----------------------------------------------------------------------------    
def clickSubtract():
    # Change the operator label to display -.
    lblOperator.config(text="-")
    # Try to get the values, compute the result and display the result.
    try:
        # Get the fraction values from the entry widgets.
        f1,f2 = getFractions()
        # Set the result label to the difference.
        setResult(EF.subtractFractions(f1,f2))
        # If execution gets to this point then there are no errors.
        # Set the error label to the empty string to clear prior errors.
        lblError.config(text="")
    # Handle exceptions.
    except Exception as e:
        # Display the exception in the error label.
        lblError.config(text="ERROR: " + str(e))

# -----------------------------------------------------------------------------
# Function: clickMultiply
#
# Inputs:
#   none
#
# Return Value:
#   none
#
# Example Use:
#   clickMultiply()
#
# Description:
#   Callback / Event Handler for click on Multiply button.
#   Gets the values of the fractions from the entry widgets.
#   Computes the product and sets the result label to show the value.
#   Changes the operator label to display x.
#
# Exceptions:
#   Does not throw exceptions directly. If an exception occurs in the process
#   of getting the fractions, then displays the Exception text in the error label.
#   If no exception is thrown in the process, the error label is set to the 
#   empty string.
# -----------------------------------------------------------------------------
def clickMultiply():
    # Change the operator label to display x.
    lblOperator.config(text="x")
    # Try to get the values, compute the result and display the result.
    try:
        # Get the fraction values from the entry widgets.
        f1,f2 = getFractions()
        # Set the result label to the product.
        setResult(EF.multiplyFractions(f1,f2))
        # If execution gets to this point then there are no errors.
        # Set the error label to the empty string to clear prior errors.
        lblError.config(text="")
    # Handle exceptions.
    except Exception as e:
        # Display the exception in the error label.
        lblError.config(text="ERROR: " + str(e))

# -----------------------------------------------------------------------------
# Function: clickDivide
#
# Inputs:
#   none
#
# Return Value:
#   none
#
# Example Use:
#   clickDivide()
#
# Description:
#   Callback / Event Handler for click on Division button.
#   Gets the values of the fractions from the entry widgets.
#   Computes the quotent and sets the result label to show the value.
#   Changes the operator label to display ÷.
#
# Exceptions:
#   Does not throw exceptions directly. If an exception occurs in the process
#   of getting the fractions, then displays the Exception text in the error label.
#   If no exception is thrown in the process, the error label is set to the 
#   empty string.
# -----------------------------------------------------------------------------
def clickDivide():
    # Change the operator label to display ÷.
    lblOperator.config(text="÷")
    # Try to get the values, compute the result and display the result.
    try:
        # Get the fraction values from the entry widgets.
        f1,f2 = getFractions()
        # Set the result label to the quotient.
        setResult(EF.divideFractions(f1,f2))
        # If execution gets to this point then there are no errors.
        # Set the error label to the empty string to clear prior errors.
        lblError.config(text="")
    # Handle exceptions.
    except Exception as e:
        # Display the exception in the error label.
        lblError.config(text="ERROR: " + str(e))

# -----------------------------------------------------------------------------
# Function: getFractions
#
# Inputs:
#   none
#
# Return Value:
#   Tuple containing the two fractions values.
#
# Example Use:
#   getFractions()
#
# Description:
#   Helper function to get the two fraction values from the entry widgets.
#
# Exceptions:
#   Raises an Exception "Invalid Fraction(s)" if an exception is raised in the
#   process of converting the contents of the entry widgets to Fractions.
#   This should only happen if a string value that do not correspond to 
#   an Fractions is entered in one or both of the entry widgets.
# ----------------------------------------------------------------------------- 
def getFractions():
    # Try to get the values and convert them to Fractions.
    try:
        # Get the string values from the entry widgets and convert to int.
        n1 = int(eNumber1.get())
        d1 = int(eNumber2.get())
        n2 = int(eNumber3.get())
        d2 = int(eNumber4.get())
    # Handle exceptions.
    except:
        # If an exception occurs raise and exception indicating one or both of
        # the entries are invalid fractions. This occurs if the contents cannot
        # be converted.
        raise Exception("Invalid Fraction(s)")
    return (n1,d1),(n2,d2)
        


# -----------------------------------------------------------------------------
# Function: setResult
#
# Inputs:
#   n - two fractions as a tuple
#
# Return Value:
#   none
#
# Example Use:
#   setResult(n)
#
# Description:
#   Helper function to the result label to show the given fraction.
#
# Exceptions:
#   Exceptions are not caught or raised directly in the function. The input
#   is not checked to be an fraction nor will an exception be raised if not.
#   Use is controlled, so only fraction values should be passed.
# ----------------------------------------------------------------------------- 
def setResult(n):
    lblResultN.config(text=str(n[0]))
    lblResultD.config(text=str(n[1]))
    

# Set the root Tkinter window for the application.
root = Tk()
# Set the title of the window.
root.title("Fraction Calculator")

# Create a frame and attach it to the root window with 10px padding.
frm = ttk.Frame(root, padding=10)
# Set the geometry manager of the frame to grid().
frm.grid()

# Define fonts that will be used for various widgets in the application.
# Font for the header shown at the top of the frame.
fontHeader = ("Helvetica", 20, "bold")
# Font for the instructions shown beneath the header.
fontInstructions = ("Helvetica", 12)
# Font for the operator text.
fontOperator = ("Helvetica", 16)
# Font for number labels.
fontNumbers = ("Helvetica", 16)

# Define a style for operator buttons.
style = ttk.Style()
style.configure('op.TButton', font=fontOperator, foreground="blue")

# Setup the label to display the header at the top of the frame.
ttk.Label(frm, text="Fraction Calculator", font=fontHeader).grid(column=0, row=0, columnspan=5)

# Setup the label to display instructions beneath the header.
ttk.Label(frm, text="Enter fractions and choose an operation\nto see the result.\n", font=fontInstructions).grid(column=0, row=1, columnspan=5)

# Entry widget for entry of the first numerator.
eNumber1 = ttk.Entry(frm, justify="right", width=5, font=fontNumbers)
eNumber1.grid(column=0, row=2)
# Set the initial value to 1.
eNumber1.insert(0,"1")

# Symbol showing the fraction.
lblFraction1 = ttk.Label(frm, text="---------", font=fontOperator, foreground="blue")
lblFraction1.grid(column=0, row=3)

# Entry widget for entry of the first denominator.
eNumber2 = ttk.Entry(frm, justify="right", width=5, font=fontNumbers)
eNumber2.grid(column=0, row=4)
# Set the initial value to 1.
eNumber2.insert(0,"2")

# Operator label, initialized to +.
lblOperator = ttk.Label(frm, text="+", font=fontOperator, foreground="blue")
lblOperator.grid(column=1, row=3)

# Entry widget for entry of the second numerator.
eNumber3 = ttk.Entry(frm, justify="right", width=5, font=fontNumbers)
eNumber3.grid(column=2, row=2)
# Set the initial value to 3.
eNumber3.insert(0,"1")

# Symbol showing the fraction.
lblFraction2 = ttk.Label(frm, text="---------", font=fontOperator, foreground="blue")
lblFraction2.grid(column=2, row=3)

# Entry widget for entry of the second denominator.
eNumber4 = ttk.Entry(frm, justify="right", width=5, font=fontNumbers)
eNumber4.grid(column=2, row=4)
# Set the initial value to 1.
eNumber4.insert(0,"3")

# Label to display = symbol.
ttk.Label(frm, text="=", font=fontOperator, foreground="blue").grid(column=3, row=3)

# Label to display the result. Set to 4 by default.
lblResultN = ttk.Label(frm, text="5", font=fontNumbers)
lblResultN.grid(column=4, row=2)

# Symbol showing the fraction.
lblFraction3 = ttk.Label(frm, text="---------", font=fontOperator, foreground="blue")
lblFraction3.grid(column=4, row=3)

# Label to display the result. Set to 4 by default.
lblResultD = ttk.Label(frm, text="6", font=fontNumbers)
lblResultD.grid(column=4, row=4)

# Label to show errors, if they occur, between the numbers and the operator buttons.
# Errors will be shown in red.
lblError = ttk.Label(frm, text="", foreground="red")
lblError.grid(column=0, row=5, columnspan=5)

# Operator button for addition.
btnAdd = ttk.Button(frm, text="+", width=3, style="op.TButton", command=clickAdd)
btnAdd.grid(column=0, row=6)

# Operator button for subtraction.
btnSubtract = ttk.Button(frm, text="-", width=3, style="op.TButton", command=clickSubtract)
btnSubtract.grid(column=1, row=6)

# Operator button for multiply.
btnMultiply = ttk.Button(frm, text="x", width=3, style="op.TButton", command=clickMultiply)
btnMultiply.grid(column=2, row=6)

# Operator button for division.
btnDivide = ttk.Button(frm, text="÷", width=3, style="op.TButton", command=clickDivide)
btnDivide.grid(column=3, row=6)

# Mainloop sets up display and loops to process events.
root.mainloop()