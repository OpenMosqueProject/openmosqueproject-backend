# This is a sample Python script.
import uvicorn


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def welcome():
    return {"message": "Assalamualikum from Open Mosque Project"}
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
