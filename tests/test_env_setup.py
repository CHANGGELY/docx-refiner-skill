import sys
try:
    import docx
    import PIL
    print("Environment setup correctly: docx and PIL found.")
except ImportError as e:
    print(f"Environment setup failed: {e}")
    sys.exit(1)
