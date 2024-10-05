def classifyTriangle(a,b,c):
    # Check for invalid input
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # Check if it's a triangle
    if (a >= b + c) or (b >= a + c) or (c >= a + b):
        return 'NotATriangle'

    # Classify the triangle
    if a == b == c:
        return 'Equilateral'
    elif (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
        return 'Right'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'