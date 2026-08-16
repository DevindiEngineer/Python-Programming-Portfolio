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
      "id": "3ee0d7dc-1c4d-40b3-9355-6b49539f894c",
      "cell_type": "code",
      "source": "x=10",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 15
    },
    {
      "id": "3607c336-71e8-4a4c-a5f2-f8eb9f83ff09",
      "cell_type": "code",
      "source": "X=200",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 16
    },
    {
      "id": "ff50a6ac-8c70-4fb3-a69f-4a28477fd833",
      "cell_type": "code",
      "source": "print(x)\nprint(X)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "10\n200\n"
        }
      ],
      "execution_count": 17
    },
    {
      "id": "fea24ad5-9a3f-4978-8700-8956c6b53dc0",
      "cell_type": "code",
      "source": "z=\"Devindi\"",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 18
    },
    {
      "id": "282186fa-3d07-4d23-ba1c-3395de6a888e",
      "cell_type": "code",
      "source": "print(z)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "Devindi\n"
        }
      ],
      "execution_count": 19
    },
    {
      "id": "064a477d-ac94-4827-864a-377a2e3b017a",
      "cell_type": "code",
      "source": "a=11.25\nb=125.12456893\nc=7",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": 20
    },
    {
      "id": "99b90a60-e24f-491a-9aae-a54e23499e07",
      "cell_type": "code",
      "source": "print(a)\nprint(b)\nprint(c)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "11.25\n125.12456893\n7\n"
        }
      ],
      "execution_count": 21
    },
    {
      "id": "62e1f00f-76c0-4c7b-9624-f5aa2ee46df6",
      "cell_type": "code",
      "source": "#type command\nprint(type(x))\nprint(type(X))\nprint(type(z))\nprint(type(a))\nprint(type(b))\nprint(type(c))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "<class 'int'>\n<class 'int'>\n<class 'str'>\n<class 'float'>\n<class 'float'>\n<class 'int'>\n"
        }
      ],
      "execution_count": 23
    },
    {
      "id": "26b4ca97-8d30-4e7c-97b0-6166f496a1ff",
      "cell_type": "code",
      "source": "is_available=True\nis_student=False\n\nprint(is_available)\nprint(is_student)\n\nprint(type(is_available))\nprint(type(is_student))",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": "True\nFalse\n<class 'bool'>\n<class 'bool'>\n"
        }
      ],
      "execution_count": 27
    },
    {
      "id": "ac1a2698-63ab-4703-96d1-f736a0f15a95",
      "cell_type": "code",
      "source": "bool(0)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 28,
          "output_type": "execute_result",
          "data": {
            "text/plain": "False"
          },
          "metadata": {}
        }
      ],
      "execution_count": 28
    },
    {
      "id": "26023606-f8db-4f52-b206-31ff9c88e753",
      "cell_type": "code",
      "source": "bool(1)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 29,
          "output_type": "execute_result",
          "data": {
            "text/plain": "True"
          },
          "metadata": {}
        }
      ],
      "execution_count": 29
    },
    {
      "id": "b4b1e463-2046-48e0-bacd-473ce378b836",
      "cell_type": "code",
      "source": "bool(2)",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "execution_count": 30,
          "output_type": "execute_result",
          "data": {
            "text/plain": "True"
          },
          "metadata": {}
        }
      ],
      "execution_count": 30
    },
    {
      "id": "d8490620-da53-4937-8450-f5dd5a71376b",
      "cell_type": "code",
      "source": "#Rule:\n# 0 (or 0.0) → False\n#Any non-zero number (positive or negative) → True",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}