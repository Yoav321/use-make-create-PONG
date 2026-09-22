# Use-Modify-Create: Pong
This repository contains starter code and a series of GitHub issues that will help you build a simple Pong-style game using the Pygame package.

## Setup
Run the following commands in a terminal window. This sets up a virtual environment that pulls in the packages you need and will ensure that your environment is good to go without having to worry about installing packages system-wide.

### Windows
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Mac / Linux
```
python3 -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
```

## Run
### In VS Code
Push the **run** button to run the game in VS Code.

### In a Web browser
At the terminal type `pygbag .` (make sure to include the dot) It should give you a URL to click. It is usually [http://localhost:8000](http://localhost:8000)

## Create Issues
Every feature will be created as GitHub Issue. Look in `Issues.md` and copy the information into a new GitHub issue. The text next to each number is the Issue title, the branch name and checklist of acceptance criteria go into the description field.

## Implement Features
To implement a feature:
1. Create a branch following the branch name in `Issues.md`.
2. In VS Code switch to the new branch.
3. Implement the code in `main.py`, and test it thoroughly to ensure it works.
4. Commit and push your code to the branch.
5. Create a Pull Request (PR) that is formatted like the following:
```
Closes #X 

Added xxxx. Tested locally and with pygbag.
```
X refers to the issue number it closes, and it will auto-close the issue when it is merged.

6. Merge the PR into the `main` branch. Delete the feature branch.

## Notes for pygbag
`pygbag` is the library that will allow you to view your game on the web. A few requirements are needed:
- The main file must be called `main.py`, and the `main()` function must have `async` before it.
- The game loop needs the line `await asyncio.sleep(0)`
- The line `asyncio.run(main())` must be at the bottom of the code and nothing else must follow it.
- Any sound must be in `.ogg` format
- Any images must be in `.png`, `.jpg`, or `.webp` format.
