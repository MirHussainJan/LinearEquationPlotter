import matplotlib.pyplot as plt
import numpy as np

def listOfDigits(eq):
    global count
    count = 0
    digits = []
    i = 0
    for q in eq:
        if q.isalpha():
            count += 1
    
    while i < len(eq):
        if eq[i].isdigit():
            j = i + 1
            while j < len(eq) and eq[j].isdigit():
                j += 1
            digits.append(int(eq[i:j]))
            i = j
        elif eq[i] == '-':
            # Handle cases where '-' is the coefficient
            if i + 1 < len(eq) and eq[i+1].isdigit():
                j = i + 1
                while j < len(eq) and eq[j].isdigit():
                    j += 1
                digits.append(int(eq[i:j]))
                i = j
            else:
                digits.append(-1)
                i += 1
        elif eq[i].isalpha():
            # Handle implied coefficients
            if i == 0 or (eq[i-1] != '0' and not eq[i-1].isdigit() and eq[i-1] != '-'):
                digits.append(1 if i == 0 or eq[i-1] != '-' else -1)
            i += 1
        else:
            i += 1
    
    if len(digits) < 3:
        digits.insert(0, 0)
    
    return digits

def evaluateSlope(x_values, eq):
    digits = listOfDigits(eq)
    if digits[1] == 0:
        return np.zeros_like(x_values)  # Handle vertical lines
    m = -digits[0] / digits[1]
    c = digits[-1] / digits[1]
    return (m * x_values) + c

equation = input("Enter Equation (format: ax + by = c): ")
x_val = np.arange(0, 20)

print(listOfDigits(equation))
print("From Main")
print(x_val)

# Fix: Evaluate slope for all x values
functionValuesY = evaluateSlope(x_val, equation)
print(functionValuesY)

# Calculate x and y intercepts
digits = listOfDigits(equation)
y_intercept = digits[-1] / digits[1] if digits[0] != 0 else "No y-intercept (vertical line)"
if digits[0] != 0:
    x_intercept = digits[-1] / digits[0]
else:
    x_intercept = "Single Variable Equation"

print("Count is", count)

# Plot the function
if 'y' not in equation and count < 2:
    plt.plot(functionValuesY, x_val)
else:
    plt.plot(x_val, functionValuesY)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Annotate x and y intercepts
if isinstance(x_intercept, float):
    plt.scatter(x_intercept, 0, color='blue', label=f'x-intercept: ({x_intercept:.2f}, 0)')
else:
    plt.text(0.5, 0.5, x_intercept, fontsize=12, color='blue')
if isinstance(y_intercept, float):
    plt.scatter(0, y_intercept, color='red', label=f'y-intercept: (0, {y_intercept:.2f})')

plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Graph of the Equation: ' + equation)
plt.show()