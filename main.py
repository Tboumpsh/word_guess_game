# main.py


import sys
import os

# اضافه کردن پوشه اصلی پروژه به مسیر
sys.path.append(os.path.dirname(__file__))


from game.ui import start_game

if __name__ == "__main__":
  
    start_game()
