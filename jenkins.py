import sys

# sys.argv[1] gets the parameter we passed from Jenkins
name = sys.argv[1] if len(sys.argv) > 1 else "Unknown"

print(f"Hello {name}, Jenkins is running your script!")

# "C:\Users\2473982\OneDrive - Cognizant\Desktop\Jenkins\jenkins.py"

# hello i am dev