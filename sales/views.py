from django.shortcuts import render
import pandas as pd
import json
from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict



# Create your views here.

def rh(request): # code de graphique RH 


    df = pd.read_csv("rh/BU.csv")
    dfs = pd.read_csv("rh/Date1.csv")
    dfs1 = pd.read_csv("rh/gender.csv")
    df2 = pd.read_csv("rh/employee.csv")
    df3 = pd.read_csv("rh/AgeGroup.csv")
  


    rs = df.groupby("RegionSeq")["BU"].agg("sum")
    rs_pie = df.groupby("Region")["BU"].agg("sum")
    rs_months = dfs.groupby("Month")["Qtr"].agg("mean")
    rs_gender = dfs1.groupby("Gender")["Sort"].agg("mean")
    rs_age = df3.groupby("AgeGroup")["AgeGroupID"].agg("sum")
    rs_empl = df2.groupby("Gender")["Age"].agg("mean")

    
    #***********************
    categories = list(rs.index)
    values = list(rs.values)
    
    #**********************
    
    months_months = list(rs_months.index)
    values_months = list(rs_months.values)

    #***********************
    categoriespie = list(rs_pie.index)
    valuespie = list(rs_pie.values)

    #***********************
    gender_gd = list(rs_gender.index)
    values_gender = list(rs_gender.values)
    
    
    #***************************
    
    categories_age = list(rs_age.index)
    values_age = list(rs_age.values)
    
    #*********************************
    
    categories_emply = list(rs_empl.index)
    values_emply = list(rs_empl.values)
    
    data = []
    for index in range(0, len(rs_pie.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_pie.index[index], 'y': rs_pie.values[index]  }
        data.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories, 'values': values,'months_months':months_months,
               'values_months':values_months,'gender_gd':gender_gd,'categories_age':categories_age,"values_age":values_age,
               'values_gender':values_gender, 'data': data,'categories_emply':categories_emply,'values_emply':values_emply,
               'table_data':table_content}
    return render(request, 'rh.html', context=context)



def customr(request):

    # importation de fichier CSV 
    df = pd.read_csv("customr/Date.csv")
    df1 = pd.read_csv("customr/product.csv")
    df2 = pd.read_csv("customr/BU.csv")
    df3 = pd.read_csv("customr/State.csv")
    df4 = pd.read_csv("customr/Fact.csv")
    
    
    
    
    rs_region = df.groupby("Year")["Qtr"].agg("count")  # Date.csv  #ok   

    
    rs_cu = df1.groupby("Product")["Product Key"].agg("mean") #product.csv   #ok
    
    
    rs_indy = df2.groupby("Division")["Executive_id"].agg("max") # Scenario.csv  #ok  *****  
    
    
    rs_state = df3.groupby("Region")["State"].agg("count") # State.csv  #ok 
    
    
    rs_fact = df4.groupby("YearPeriod")["Subscription Revenue"].agg("count") # Fact.csv  #ok

    
    
    ################################
    categories = list(rs_cu.index)
    values = list(rs_cu.values)
    ##############################
    
    categories_region = list(rs_region.index)
    values_region = list(rs_region.values)
    ##############################
    
    categories_rs_indy = list(rs_indy.index)
    values_rs_indy = list(rs_indy.values)
    ##############################
    
    
    categories_state = list(rs_state.index)
    values_state = list(rs_state.values)
    ##############################
    

        
    categories_fact = list(rs_fact.index)
    values_fact = list(rs_fact.values)
    
    ##############################
    
    
  
    data = []
    for index in range(0, len(rs_region.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_region.index[index], 'y': rs_region.values[index]  }
        data.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"',"")
	
    context = {'categories_region':categories_region,'values_region':values_region,'categories_rs_indy':categories_rs_indy,'values_rs_indy':values_rs_indy,
               'data': data, 'table_data':table_content,'categories':categories,"values":values,'categories_state':categories_state,'values_state':values_state,
               "categories_fact":categories_fact,"values_fact":values_fact
               
               }
    return render(request, 'customr.html', context=context)







def procurement(request):

    # importation de fichier CSV 
    ####################################
    df = pd.read_csv("pro/Currency.csv")
    df1 = pd.read_csv("pro/Item.csv")
    df2 = pd.read_csv("pro/location.csv")
    df3 = pd.read_csv("pro/Vendor.csv")
    df4 = pd.read_csv("pro/Invoiceitem.csv")
   
    
    
    ####################################
    
    rs = df.groupby("Currency Abbr")["CurrencyID"].agg("mean") # currency.csv  #ok
    
    rs_invoc = df1.groupby("Sub Category")["Commodity"].agg("count") #Item.csv #ok
    
    rs_loc = df2.groupby("City")["Location Number"].agg("count") #location.csv #ok
    
    rs_date = df3.groupby("Total Spend")["Tier"].agg("sum") #vendor.csv #ok
    
    rs_item = df4.groupby("Invoice LOC Amount")["ItemID"].agg("count") #invoice item line.csv 

    
    
    
    

    
    
    
    #######################################
    categories = list(rs.index)
    values = list(rs.values)
    ######################################
    categories_date = list(rs_invoc.index)
    values_date = list(rs_invoc.values)
    ####################################
    categories_loc = list(rs_date.index)
    values_loc = list(rs_date.values)
    ###################################
    categories_palc = list(rs_loc.index)
    values_palc = list(rs_loc.values)
    ###################################
    categories_invoice = list(rs_item.index)
    values_invoice = list(rs_item.values)
    
    
  # code pour table 
    data = []
    for index in range(0, len(rs_invoc.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_invoc.index[index], 'y': rs_invoc.values[index]  }
        data.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"',"")
	####################################################################################
 
 
    context = {
               'data': data, 'table_data':table_content,'categories':categories,"values":values,
               'categories_date':categories_date,'values_date':values_date,"categories_loc":categories_loc,"values_loc":values_loc,
               "categories_palc":categories_palc,"values_palc":values_palc,"categories_invoice":categories_invoice,"values_invoice":values_invoice
               
               }
    return render(request, 'procurement.html', context=context)





def opportunity(request):

    # importation de fichier CSV 
    ####################################
    df = pd.read_csv("opportunity/Account.csv") #ok
    df1 = pd.read_csv("opportunity/product.csv") #ok 
    df2 = pd.read_csv("opportunity/opportunity.csv") #ok 
    df3 = pd.read_csv('opportunity/salesstage.csv') #ok
    df4 = pd.read_csv('opportunity/Fact.csv') #----------
   
    
    
    ####################################
    
    rs = df.groupby("Region")["Account ID"].agg("mean") # Account.csv  #ok
    
    rs_invoc = df1.groupby("Product Code")["Product ID"].agg("sum") #Product.csv #ok
    
    rs_opp = df2.groupby("Opportunity Size")["SizeID"].agg("count") #opportunity.csv #ok 

    rs_stage = df3.groupby("Sales Stage")["Probability"].agg("count") #salessatage.csv #ok


    rs_fact = df4.groupby("Month")["ProductRevenue"].agg("count") #fact.csv #--------



    
    
    
    

    
    
    
    #######################################
    categories = list(rs.index)
    values = list(rs.values)
    ######################################
    categories_product = list(rs_invoc.index)
    values_product = list(rs_invoc.values)
    ####################################

    categories_opportunity = list(rs_opp.index)
    values_opportunity = list(rs_opp.values)
    ###################################
    categories_stage = list(rs_stage.index)
    values_stage = list(rs_stage.values)
    ###################################

    categories_factt = list(rs_fact.index)
    values_factt = list(rs_fact.values)
    ###################################

    
  
    
  # code pour table 
    data = []
    for index in range(0, len(rs_invoc.index)):
        # print(rs_pie.index[index])
        value = {'name': rs_invoc.index[index], 'y': rs_invoc.values[index]  }
        data.append(value)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"id='big_tables' class='table table-striped table-bordered'")
    table_content = table_content.replace('border="1"',"")
	####################################################################################
 
 
    context = {
               'data': data, 'table_data':table_content,'categories':categories,"values":values,
               'categories_product':categories_product,'values_product':values_product,"categories_opportunity":categories_opportunity,"values_opportunity":values_opportunity,
               "categories_stage":categories_stage,"values_stage":values_stage, 'categories_factt':categories_factt,'values_factt':values_factt
               
               }
    return render(request, 'opportunity.html', context=context)





def index(request):
    return render(request, 'index.html')






