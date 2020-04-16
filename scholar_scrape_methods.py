"""
This module contains methods for scraping publication information
from Google Scholar using the Python wrapper for Selenium web
automation framework.

created April 15, 2020

"""

import os
import time
import pandas as pd


def results_to_file(df, topic):
    """Save search results in a dataframe to tab-separated text file"""
    current_time = time.strftime('%Y-%m-%d_%H-%M')
    export_filepath = os.path.join(
        os.getcwd(),
        topic.replace(':', '_')+'_gscholar_'+current_time+'.txt')
    df.to_csv(export_filepath, sep='\t', index=False)

    
def get_total_search_results(browser):
    """Get total number of Google Scholar search results using
    Selenium browser object"""
    page_summary = browser.find_elements_by_class_name('gs_ab_mdw')
    tot_results = page_summary[1].text.split(' results')[0]
    # check of word 'about' preceeds the total number of results
    if 'bout' in tot_results:
        tot_results = tot_results.split(' ')[1]
    tot_results = int(tot_results.replace(',', ''))
    return tot_results

def get_titles(browser):
    """Get all titles on a page of Google Scholar search results
    using Selenium browser object"""
    titles = [a.text for a in browser.find_elements_by_xpath('//h3')]
    return titles

def get_abstract_previews(browser):
    """Get all abstract previews on a page of Google Scholar search results
    using Selenium browser object"""
    abstract_previews = [a.text for a in browser.find_elements_by_class_name('gs_rs')]
    return abstract_previews

def preview_paper_info(browser):
    """Get all paper info previews (authors, journal, etc.)on a page of
    Google Scholar search results using Selenium browser object"""
    info = [a.text for a in browser.find_elements_by_class_name('gs_a')]
    return info

def move_to_next_page(browser):
    """Move the search results to the next page"""
    next_button = browser.find_element_by_class_name('gs_ico_nav_next')
    next_button.click()

def get_citations(browser):
    """Returns a list of the citations shown on a Google Scholar
    search results page using Selenium browser object"""
    
    # get current_results page
    current_results_page = browser.current_url
    
    # get the buttons which create popup windows of citations
    # these are every 4th button of the 'gs_or_svg' class
    cite_buttons = browser.find_elements_by_class_name('gs_or_svg')[1::4]
    
    citations = []
    cite_button_counter = 0
    
    # loop over each cite button on the page
    for _ in range(len(cite_buttons)):
        
        # re-instantiate the cite button
        cite_buttons = browser.find_elements_by_class_name('gs_or_svg')[1::4]
        cb = cite_buttons[cite_button_counter]

        # click on the cite button
        time.sleep(0.2)
        cb.click()
        time.sleep(1)

        # get text of the third citation (Chicago style) in the citation popup window
        # Chicago sytle is used because it contains full author names
        citation = browser.find_elements_by_class_name('gs_citr')[2].text
        citations.append(citation)

        # exit citation popup window and return to results page
        browser.get(current_results_page)
        time.sleep(1)
        cite_button_counter += 1

    print('acquired {} citations'.format(len(citations)))
    return citations
