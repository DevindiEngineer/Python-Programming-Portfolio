{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9cc5c226-1b14-4649-be0d-0beecea74c9d",
   "metadata": {},
   "source": [
    "# Section 02"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "44398385-0927-4e89-a3fd-f0cea8490328",
   "metadata": {},
   "source": [
    "### 11. Tkinter Application: Area of Rectangle Calculator\n",
    "### a) GUI Setup and Input Components (10 Marks)\n",
    "### Create a Tkinter window titled \"Rectangle Area Calculator\".\n",
    "### Add input fields for:\n",
    "### • Length\n",
    "### • Width"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "38f81a32-8bf3-4a13-b224-3f8920d2ef21",
   "metadata": {},
   "source": [
    "### (b) Layout Management using grid() (10 Marks)\n",
    "### Arrange all widgets neatly using the .grid() geometry manager."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aaa02894-01d1-456a-93aa-9ab57e61fc65",
   "metadata": {},
   "source": [
    "### (c) Area Calculation Functionality (10 Marks)\n",
    "### Add a button labeled \"Calculate Area\".\n",
    "### When the button is clicked:\n",
    "### • Retrieve the values entered for Length and Width.\n",
    "### • Calculate the area using the formula:\n",
    "### Area = Length × Width"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c78af05d-4edc-44a4-b3cc-88aa6275ce87",
   "metadata": {},
   "source": [
    "### (d) Displaying the Result (10 Marks)\n",
    "### Display the calculated area using a Label widget."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b37a305-7cb9-4962-871e-4c5ebb861748",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "\n",
    "window = tk.Tk() \n",
    "window.title(\"Rectangle Area Calculator\")\n",
    "window.geometry(\"400x250\")\n",
    "\n",
    "label0 = tk.Label(window, text=\"Rectangle Area Calculator\", font=(\"Arial\", 14, \"bold\"))\n",
    "label0.pack(pady=10)\n",
    "\n",
    "label1 = tk.Label(window,text=\"Length\", font=(\"Arial\", 10, \"bold\"))\n",
    "label1.pack(pady=10)\n",
    "\n",
    "entry0 = tk.Entry(window)\n",
    "entry0.pack()\n",
    "\n",
    "label2 = tk.Label(window,text=\"Width\", font=(\"Arial\", 10, \"bold\"))\n",
    "label2.pack(pady=10)\n",
    "\n",
    "entry1 = tk.Entry(window)\n",
    "entry1.pack()\n",
    "\n",
    "button = tk.Button(window, text=\"Calculate Area\", command=calculate_area,font=(\"Arial\", 10, \"bold\"))\n",
    "button.pack(pady=10)\n",
    "\n",
    "label_result = tk.Label(window, text=\"Area: \", font=(\"Arial\", 10, \"bold\"))\n",
    "label_result.pack(pady=10)\n",
    "\n",
    "def calculate_area():\n",
    "    try:\n",
    "        length = float(entry0.get())\n",
    "        width = float(entry1.get())\n",
    "        answer = length * width\n",
    "        \n",
    "        label_result.config(text=f\"Area: {answer}\")\n",
    "    except ValueError:\n",
    "        label_result.config(text=\"Please enter valid numbers!\")\n",
    "\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c703cb81-d80d-43f3-8112-1e0adea496eb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
