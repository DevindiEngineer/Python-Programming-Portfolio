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
      "id": "a5c1019f-6991-4334-b5a8-2c74a2f0d732",
      "cell_type": "code",
      "source": "pet_name=input(\"What is your pet name?\")\nhome_town=input(\"What is your home town?\")\ndream_job=input(\"What is your dream job?\")\nprint(pet_name)\nprint(home_town)\nprint(dream_job)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdin",
          "text": "What is your pet name? Shaggy\nWhat is your home town? Kottawa\nWhat is your dream job? Software Engineer\n"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Shaggy\nKottawa\nSoftware Engineer\n"
        }
      ],
      "execution_count": 1
    },
    {
      "id": "4f8986cd-7e46-43c1-896c-032f8f14d0b5",
      "cell_type": "code",
      "source": "birth_year=input(\"Input your birth year?\")\nprint(birth_year)\nprint(type(birth_year))\nbirth_year=int(birth_year)\nprint(type(birth_year))\nprint(birth_year)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdin",
          "text": "Input your birth year? 2005\n"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "2005\n<class 'str'>\n<class 'int'>\n2005\n"
        }
      ],
      "execution_count": 7
    },
    {
      "id": "b3ab7af8-a191-4601-a71e-4c013130251a",
      "cell_type": "code",
      "source": "has_subscription=True\nprint(has_subscription)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "True\n"
        }
      ],
      "execution_count": 6
    },
    {
      "id": "6f6ada98-2451-45c8-89eb-2bdd8d1befa0",
      "cell_type": "code",
      "source": "coffee_price=input(\"Input price of coffee?\")\nprint(type(coffee_price))\ncoffee_price=float(coffee_price)\nprint(type(coffee_price))\nprint(coffee_price)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdin",
          "text": "Input price of coffee? 799.99\n"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "<class 'str'>\n<class 'float'>\n799.99\n"
        }
      ],
      "execution_count": 9
    },
    {
      "id": "242e935e-01b9-43f5-8760-d9789d401a03",
      "cell_type": "code",
      "source": "item_name=input(\"What is the item name?\")\nquantity_available=int(input(\"How many items available?\"))\nprint(type(item_name))\nprint(type(quantity_available))\nprint(item_name)\nprint(quantity_available)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdin",
          "text": "What is the item name? Burger\nHow many items available? 36\n"
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "<class 'str'>\n<class 'int'>\nBurger\n36\n"
        }
      ],
      "execution_count": 11
    },
    {
      "id": "8d84c4dc-6eb1-4961-9871-0cdc37fc0929",
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