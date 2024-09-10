def check_multiple(x):
    if x % 3 == 0 and x % 5 == 0:
        return "Zoom"
    elif x % 3 == 0:
        return "Zip"
    elif x % 5 == 0:
        return "Zap"
    else:
        return "Invalid"
    
def main():
    x = int(input("Enter a number:"))
    output = check_multiple(x)
    print(f"{output}")

if __name__ == "__main__":
    main()