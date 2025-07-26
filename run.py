# run.py

"""
Main entry point to start the Gestro application.
"""

from app.main import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Gestro exited by user.")
    except Exception as e:
        print(f"[ERROR] Unexpected error occurred: {e}")
