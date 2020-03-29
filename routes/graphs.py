
from flask import render_template, jsonify
from . import routes
import requests
import json
from operator import itemgetter
import plotly.express as px
import plotly.io as pio
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.graph_objects as go
import plotly

from flask import Markup



import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


@routes.route('/Graph')
def Graph():

    points = show()

    print(points)
    return render_template('graph.html', a= points )







# Data for plotting

# @show.route("/graph")
def show():
    

    data = search.get_data()
    sortedDic = search.get_all_data(data)


    send_json = search.get_top_five(sortedDic)


    return send_json







class search():
    @staticmethod
    def Sort_from_highest(sortedDic, value):

        print(type(sortedDic))
        List= sorted(sortedDic.items(), key=lambda x: x[1][value], reverse = True)
        return List

    @staticmethod
    def get_data():
            #using the API to get data about COVID19
        url ="https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php"

        headers = {
        'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
        'x-rapidapi-key': "51274aee9amsh6c7865b0aa6ae6cp1fa37cjsnc5109b42003f"
        }

        response = requests.request("GET", url, headers=headers)
    
        
        data = json.loads(response.text)
        return data

    @staticmethod
    def get_all_data(data):
            
        #This is getting the data.
        sortedDic = {}
        sortlist = {}
        
    
        #Looping throu the Data by country_stat
        for i in data['countries_stat']:
            
            value = int( i['cases'].replace(',', ''))    #['countries_stat']:
            death_value = int( i['deaths'].replace(',', ''))   # Converting the str into Int
            total_recovered_value = int( i['total_recovered'].replace(',', '')) # Converting the str into Int
            new_death=int( i['new_deaths'].replace(',', ''))
            new_cases=int( i['new_cases'].replace(',', ''))
            serious_critical=int( i['serious_critical'].replace(',', ''))
            active_cases=int( i['active_cases'].replace(',', ''))
            total_case_per_1m_population=float( i['total_cases_per_1m_population'].replace(',', ''))


                
            sortedDic[i['country_name']] ={
                'cases': value, 
                'deaths': death_value, 
                'total_recovered': total_recovered_value , 
                'new_death':new_death,
                'new_cases': new_cases,
                'serious_critical':serious_critical,
                'active_cases': active_cases,
                "total_case_per_1m_population":total_case_per_1m_population
            
            }  # Adding this Data into a New Dictionary.
        

        return sortedDic






    def get_top_five(sortedDic):
        
 
        newlist = search.Sort_from_highest(sortedDic, "cases")
        cases_data = []
        recover_data = []
        labels =[]
        

    
    
        for i in newlist:
            size = len(cases_data) +1
            if size <=5:
                    labels.insert(size, i[0]) # Country (name)
                    cases_data.insert(size,i[1]['cases'] ) # List of Cases for graph
                    recover_data.insert(size,i[1]['total_recovered'] ) # list of recover
        

        points = {
                'country': labels,
                'cases': cases_data,
                'recover': recover_data

            }

        send_json =json.dumps(points)
        send_json = json.loads(send_json)
        return send_json

    @staticmethod
    def get_json_all_data():
      
        data = search.get_data()
       
        sortedDic = search.get_all_data(data)
        
        newlist = search.Sort_from_highest(sortedDic, "cases")
        
        
        cases_data = []
        recover_data = []
        labels =[]
        cases_data = []
        recover_data = []
        labels =[]
        value=[] 
        death_value=[] 
        total_recovered_value =[]
        new_death=[]
        new_cases=[]
        serious_critical=[]
        active_cases=[]
        total_case_per_1m_population=[]

    
    
        for i in newlist:
           
            size = len(cases_data) +1
           
            labels.insert(size, i[0]) # Country (name)
            cases_data.insert(size,i[1]['cases'] ) # List of Cases for graph
            recover_data.insert(size,i[1]['total_recovered'] ) # list of recover 
            death_value.insert(size,i[1]['deaths'] ) 
            total_recovered_value.insert(size,i[1]['total_recovered'] ) 
            new_death.insert(size,i[1]['new_death'] ) 
            new_cases.insert(size,i[1]['new_cases'] ) 
            serious_critical.insert(size,i[1]['serious_critical'] ) 
            active_cases.insert(size,i[1]['active_cases'] ) 
            total_case_per_1m_population.insert(size,i[1]['total_case_per_1m_population'] ) 
    
            points = {
                'country': labels,
                'cases': cases_data,
                'recover': recover_data,
                'death': death_value,
                'total':total_recovered_value,
                'new_death':new_death,
                'new_cases':new_cases,
                'serious_critical':serious_critical,
                'active_cases':active_cases,
                'total_case_per_1m_population':total_case_per_1m_population
            }
        

        send_json =json.dumps(points)
        send_json = json.loads(send_json)

        
        return send_json