from extractor import *
import json
import csv
import pdb

if __name__ == "__main__":
    try:
        driver = CrawlBrowser()
        
        driver.login()

        driver.get_list()

        for i in driver.data:
            driver.get_detail(i)

        my_dict = driver.data
        
        with open('total.csv', 'w', encoding='utf-8') as f:  # Just use 'w' mode in 3.x
            w = csv.DictWriter(f, my_dict[0].keys())
            w.writeheader()
            for key, value in my_dict.items():
                w.writerow(value)
        

    except:
        print("error")
    finally:

        print("end")
