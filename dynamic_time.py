{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "bad4cc32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n",
      "['1', '2']\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-13-63c3d4ce8078>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmy\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m \u001b[0mT1\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmy\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m11\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0mmy\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m12\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     12\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[0mT2\u001b[0m  \u001b[1;33m=\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmy\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m14\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0mmy\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m15\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "import time;\n",
    "\n",
    "\n",
    "print (\"Local current time :\", localtime)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "87cdb0b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def test(I1 , I2, I3, I4):\n",
    "    M1 = int(my[0]+my[1])\n",
    "    M2 = int(my[2]+my[3])\n",
    "    T1 = int(my[11_l]+my_l[12])\n",
    "    T2 = int(my_l[14]+my_l[15])\n",
    "    if ()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edce471a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    my = list(input()) \n",
    "    get_local = time.asctime( time.localtime(time.time()) )\n",
    "    my_l = list(get_local)\n",
    "    test(my,my_l)   \n",
    "    \n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
