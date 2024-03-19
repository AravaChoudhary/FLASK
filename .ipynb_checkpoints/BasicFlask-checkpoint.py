{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 23.3.2 -> 24.0\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in c:\\users\\dell\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (3.0.0)\n",
      "Requirement already satisfied: Werkzeug>=3.0.0 in c:\\users\\dell\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from flask) (3.0.1)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\dell\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from flask) (3.1.3)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\users\\dell\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from flask) (2.1.2)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\users\\dell\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from flask) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\users\\dell\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from flask) (1.7.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\dell\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from click>=8.1.3->flask) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\dell\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from Jinja2>=3.1.2->flask) (2.1.3)\n"
     ]
    }
   ],
   "source": [
    "!pip install flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Instantiate the Flask App\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\") #Home Directory\n",
    "def hello():\n",
    "    return \"Hello World , I am Starting my Journey with Flask and It's going great\"\n",
    "\n",
    "# For running this app , we have to call the run method \n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug = True)"
   ]
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
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
