# How to Run
To run this project, you need to run the following commands on /shell:
- cd <to_root_dir_of_this_project>
- python -m venv venv
- for windows 
  - source .\venv\Scripts\activate
- for linux
  - source venv/bin/activate
- pip install -r requirements.txt
- python main.py

# Sample Run
> python main.py
- Enter 1 for expert1, 2 for expert2, and 3 for expert3: 1
- Enter an integer number between 2 to 10: 3
- oops script output
- The number 3 is a prime number.
- functional script output
- The number 3 is a prime number.

# Project Constraints
- This project has been tested in windows with python 3.10
- It is written in a manner that it should work properly with 
  - Linux environment
  - and older version of python 3
- we have moved the hardcoded expert details in the config file to read that you need to install pyyaml lib.



