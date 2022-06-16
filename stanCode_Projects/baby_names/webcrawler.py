"""
File: webcrawler.py
Name: 林志叡
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup

def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        # tags = soup.findAll('table', {'class', 't-stripe'})
        tags = soup.findAll('tbody')
        # find all the tags in tbody
        male_count = 0
        female_count = 0
        for tag in tags:
            y = tag.text.split("\n")
            # split the text with \n to distinguish the desired data in same position of list
            for line in y:
                g = line.split()
                # split desired data into list structure
                if len(g) == 4:
                    """
                    through observation, if data contains male name ,name num, female name , name num 
                    then lens of list equals to 4
                    """
                    num1 = int(g[1].replace(',', ''))
                    num2 = int(g[3].replace(',', ''))
                    male_count += num1
                    female_count += num2
        print('Male Number: '+str(male_count))
        print('Female Number: '+str(female_count))





if __name__ == "__main__":
    main()
