def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and a>c :
        print(" Birinchi raqam")

    if b>a and b > c:
        print("ikkinchi raqam")    

    if c > a and c > b:
        print("Uchinchi raqam") 
    return a , b , c

print(main(2,4,1))

