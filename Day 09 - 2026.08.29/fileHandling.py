{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3f597cdf-a4bc-40c5-a343-f692631f5bf2",
   "metadata": {},
   "source": [
    "# File Handling"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "09c94f54-3a99-439a-b3df-be78749fd1e8",
   "metadata": {},
   "source": [
    "## Manual close method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "bcb97139-a07c-4591-85b5-dc718687e17b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "D:\\python_content.txt\n"
     ]
    }
   ],
   "source": [
    "myfile = open(r\"D:\\python_content.txt\")\n",
    "print(myfile.name)\n",
    "myfile.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb33c0d2-3b31-42e0-a8d8-4e3c0b78666e",
   "metadata": {},
   "source": [
    "## Auto close method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "a9ab4a74-d5c1-4134-b174-7a3f4314ed18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "D:\\python_content.txt\n"
     ]
    }
   ],
   "source": [
    "with open(r\"D:\\python_content.txt\",\"r\") as X:\n",
    "    print(X.name)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fef4343c-9ee8-4c49-9169-42ac603ed13f",
   "metadata": {},
   "source": [
    "## Manual close method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "6ce45578-6356-4202-9b09-fea183d673b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\LENOVO\\OneDrive\\Desktop\\Python\\Day 09 - 2026.08.29\\python_contents.txt\n"
     ]
    }
   ],
   "source": [
    "mypythonfile = open(r\"C:\\Users\\LENOVO\\OneDrive\\Desktop\\Python\\Day 09 - 2026.08.29\\python_contents.txt\")\n",
    "print(mypythonfile.name)\n",
    "mypythonfile.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "75c6ef08-ec74-407c-85f3-d76f3a6624a8",
   "metadata": {},
   "source": [
    "## Auto close method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "25ac1cf2-0391-41db-b96b-f3d075de8766",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\LENOVO\\OneDrive\\Desktop\\Python\\Day 09 - 2026.08.29\\python_contents.txt\n"
     ]
    }
   ],
   "source": [
    "with open(r\"C:\\Users\\LENOVO\\OneDrive\\Desktop\\Python\\Day 09 - 2026.08.29\\python_contents.txt\", \"r\") as x:\n",
    "    print(x.name)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ea449d2-45b4-4a51-9679-f4a3aa681104",
   "metadata": {},
   "source": [
    "### Verify"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "c6989e15-d23a-4685-8871-31a9c2a44488",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "D:\\python_content.txt\n",
      "closed False\n",
      "closed True\n"
     ]
    }
   ],
   "source": [
    "y = open(r\"D:\\python_content.txt\")\n",
    "print(y.name)\n",
    "print(\"closed\",y.closed)# false means file still opens\n",
    "y.close()\n",
    "print(\"closed\",y.closed) # true means file closes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d5fa5311-9e79-4095-b16d-3556895aac5a",
   "metadata": {},
   "source": [
    "### Read the whole file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "9bb57cf4-cab3-4b4b-ac66-1be9d4638f38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lorem ipsum dolor sit bad, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
      "\n",
      "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n",
      "\n",
      "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
     ]
    }
   ],
   "source": [
    "x = open(r\"D:\\python_content.txt\")\n",
    "print(x.read())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "b1a7c2c5-e045-4a99-8f8b-00612c269a74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python is a high-level, interpreted programming language celebrated for its clear syntax and exceptional readability. Developed by Guido van Rossum and released in 1991, its design philosophy emphasizes code simplicity, allowing developers to express complex concepts in fewer lines of code than languages like C++ or Java. Featuring a robust standard library and dynamic semantic systems, Python supports multiple programming paradigms, including object-oriented, imperative, and functional programming. Today, it stands as a dominant force driving innovation across data science, machine learning, web development, and automation.\n"
     ]
    }
   ],
   "source": [
    "y = open(r\"C:\\Users\\LENOVO\\OneDrive\\Desktop\\Python\\Day 09 - 2026.08.29\\python_contents.txt\")\n",
    "print(y.read())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba37d629-8a12-4ea6-84aa-28082a58dfbc",
   "metadata": {},
   "source": [
    "### Read line by line"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "c9aa3f1b-a60e-474c-975a-db3a220a29b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lorem ipsum dolor sit bad, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "x = open(r\"D:\\python_content.txt\")\n",
    "print(x.readline()) # first line only "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "1a9e178a-f1c3-481d-81cd-fc8c2d611719",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lorem ipsum dolor sit bad, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
      "\n",
      "\n",
      "\n",
      "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n",
      "\n",
      "\n",
      "\n",
      "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
     ]
    }
   ],
   "source": [
    " # enter line also a line  this prints with blanks between the lines \n",
    "x = open(r\"D:\\python_content.txt\")\n",
    "print(x.readline())\n",
    "print(x.readline())\n",
    "print(x.readline())\n",
    "print(x.readline())\n",
    "print(x.readline())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "9fb786a0-2d06-465e-9a43-292a069dd3db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lorem ipsum dolor sit bad, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
      "\n",
      "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n",
      "\n",
      "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
     ]
    }
   ],
   "source": [
    "# this print without the blanks between lines\n",
    "x = open(r\"D:\\python_content.txt\")\n",
    "print(x.readline(), end=\"\")\n",
    "print(x.readline(), end=\"\")\n",
    "print(x.readline(), end=\"\")\n",
    "print(x.readline(), end=\"\")\n",
    "print(x.readline(), end=\"\")\n",
    "x.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e0e969b5-d629-4371-a2ba-984a518608b0",
   "metadata": {},
   "source": [
    "### using a for loop "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "72d57b27-bfa9-47be-8c3d-3e908c40a1a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lorem ipsum dolor sit bad, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
      "\n",
      "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\n",
      "\n",
      "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
     ]
    }
   ],
   "source": [
    "x = open(r\"D:\\python_content.txt\")\n",
    "for line in x:\n",
    "    print(line.strip())\n",
    "x.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29e0a804-df24-4f0f-966c-f5a71ee5bbfe",
   "metadata": {},
   "source": [
    "### Reads the lines as a list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "735ea62f-8460-4001-89be-4fe41cf092f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Lorem ipsum dolor sit bad, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\\n', '\\n', 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\\n', '\\n', 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.']\n"
     ]
    }
   ],
   "source": [
    "x = open(r\"D:\\python_content.txt\")\n",
    "print(x.readlines()) "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca83a8f5-0eae-41a9-8b2a-25e6373a3f95",
   "metadata": {},
   "source": [
    "### Search line by keyword"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "3cfebf92-e4fc-4dac-8a44-23d646fac48f",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = open(r\"D:\\python_content.txt\")\n",
    "for line in x:\n",
    "    if line.startswith(\"Colombo\"): #prints nothing - does not start with Colombo \n",
    "        print(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "8cafb689-da53-484e-b0ff-03c28e35a741",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lorem ipsum dolor sit bad, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "x = open(r\"D:\\python_content.txt\")\n",
    "for line in x:\n",
    "    if line.startswith(\"Lorem\"): #prints lines - start with Lorem\n",
    "        print(line)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4bf2eac2-ba29-4f55-8584-d5c319e32d9b",
   "metadata": {},
   "source": [
    "### Write on text file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "a3747954-2238-4f52-a81a-1ac4dc1d6b72",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = open(r\"D:\\python_content.txt\", \"w\") # this override the current txt\n",
    "x.write(\"Python is fun 1\")\n",
    "x.write(\"Python is fun 2\")\n",
    "x.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "af2895da-687d-48e5-85ff-ab6061b3b7a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python is fun 1Python is fun 2\n"
     ]
    }
   ],
   "source": [
    "x = open(r\"D:\\python_content.txt\",\"r\")\n",
    "print(x.read())\n",
    "x.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "07000d47-134a-4f18-98da-6f54feb1b647",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = open(r\"D:\\python_content.txt\", \"w\") # this override the current txt\n",
    "x.write(\"Python is fun 1\\n\")\n",
    "x.write(\"Python is fun 2\\n\")\n",
    "x.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "c8ca008f-1a6b-4dc6-a40b-1ad556b91fbb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python is fun 1\n",
      "Python is fun 2\n",
      "\n"
     ]
    }
   ],
   "source": [
    "x = open(r\"D:\\python_content.txt\",\"r\")\n",
    "print(x.read())\n",
    "x.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5cc6cc02-d9ab-48c6-9151-28b28142b117",
   "metadata": {},
   "source": [
    "### Append"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "bacc97b8-e630-451f-b35c-27c8e9303fcb",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = open(r\"D:\\python_content.txt\", \"a\") \n",
    "x.write(\"Python is fun 3\")\n",
    "x.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "1d9362d3-f82a-4076-a821-db6b8d8f9fac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python is fun 1\n",
      "Python is fun 2\n",
      "Python is fun 3\n"
     ]
    }
   ],
   "source": [
    "x = open(r\"D:\\python_content.txt\",\"r\")\n",
    "print(x.read())\n",
    "x.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ebeb317-391b-4fec-9e70-040799aa7306",
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
