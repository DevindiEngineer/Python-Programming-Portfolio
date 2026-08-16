{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "04dd8dc4-981b-4e5f-8242-7b737d37c621",
      "cell_type": "code",
      "source": "name=\"Kamal\"\nage=25\nheight=5.9",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 1
    },
    {
      "id": "a5906f01-ab22-4b38-b62c-24908a5a36f4",
      "cell_type": "code",
      "source": "print(name)\nprint(age)\nprint(height)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Kamal\n25\n5.9\n"
        }
      ],
      "execution_count": 2
    },
    {
      "id": "35304771-a4df-4324-969b-7d882d087c1f",
      "cell_type": "code",
      "source": "print(type(name))\nprint(type(age))\nprint(type(height))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "<class 'str'>\n<class 'int'>\n<class 'float'>\n"
        }
      ],
      "execution_count": 4
    },
    {
      "id": "f878c202-384f-4d3e-b301-c7c7f546bbef",
      "cell_type": "code",
      "source": "my_name=input(\"What is your name?\")\nprint(my_name)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdin",
          "text": "What is your name? Dew Wicky\n"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Dew Wicky\n"
        }
      ],
      "execution_count": 9
    },
    {
      "id": "b64cc622-35df-4b31-883f-a5e95590cfd1",
      "cell_type": "code",
      "source": "x=None\nprint(x)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "None\n"
        }
      ],
      "execution_count": 12
    },
    {
      "id": "a0136720-5364-4481-8946-640d5abc74ad",
      "cell_type": "code",
      "source": "my_age=input(\"How old are you?\")\nprint(my_age)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdin",
          "text": "How old are you? 21\n"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "21\n"
        }
      ],
      "execution_count": 13
    },
    {
      "id": "3b970bcf-1fb7-4293-bb6b-dff34677fde1",
      "cell_type": "code",
      "source": "number1=int(input(\"Enter Number 1 :\"))\nnumber2=int(input(\"Enter Number 2 :\"))\nanswer=number1+number2\nprint(answer)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdin",
          "text": "Enter Number 1 : 150\nEnter Number 2 : 250\n"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "400\n"
        }
      ],
      "execution_count": 16
    },
    {
      "id": "c1866e57-e025-4a58-a502-1b6b9f33ca0a",
      "cell_type": "code",
      "source": "number1=input(\"Enter number 1:\")\nnumber2=input(\"Enter number 2:\")\nprint(number1)\nprint(number2)\nprint(type(number1))\nprint(type(number2))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdin",
          "text": "Enter number 1: 150\nEnter number 2: 250\n"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "150\n250\n<class 'str'>\n<class 'str'>\n"
        }
      ],
      "execution_count": 18
    },
    {
      "id": "2fff75ec-26a9-45e9-9096-f6cc9a12f33c",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}