import sys

# This prints the list of arguments passed to this file
print(sys.argv)

# This prints full python version
print(sys.version)
# Output: '3.11.5 (main, Jul 10 2025, 20:10:45) [GCC 12.2]'

print(sys.version_info)
# Output: sys.version_info(major=3, minor=11, micro=5, releaselevel='final', serial=0)

# We can kill processes too 
print("Starting program...")
sys.exit(0)
print("This will NOT print")
