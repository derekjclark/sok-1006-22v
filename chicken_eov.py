

#Importerer nødvendige pakker.

import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
import numpy as np
import matplotlib.font_manager as font_manager


#Likning 14

def demand_curve(c,Q,y,pb):
    demand = (c.log(Q)-(-4.597 + 0.841*y + 0.2775*pb)) / (-0.397)
    return demand


#Likning 15

def supply_curve_long_run(c,Q,N,X,pf,t):
    supply = ((1-0.631)*c.log(N*Q+X)-(2.030-0.146*pf+0.0184*t)) / (0.221) 
    return supply


#Likning 16

def supply_curve_short_run(c,Q,N,X,pf,t,Q_fitted):
    supply = (c.log(N*Q+X)-(2.030-0.146*pf + 0.0184*t + 0.631*c.log(N*Q_fitted+X))) / (0.221)
    return supply


#Likevekt

def equate_q(y,pb,N,X,pf,t):
    Q = sp.symbols("Q")
    eqDS = sp.Eq(demand_curve(sp,Q,y,pb),supply_curve_long_run(sp,Q,N,X,pf,t))
    sol=sp.nsolve(eqDS, 40)
    return float(sol)



#############Plot av 1995################


def plot_year(df,year):

##Denne delen var ferdig i oppgavetekst
    d=df[df['YEAR']==year].to_dict(orient='records')[0]
    
    cpi=d['CPI']
    y=np.log(d['Y'])
    pb=np.log(d['PBEEF']/cpi)
    N=d['POP']
    X=d['QPRODA']/1439-d['Q']*d['POP']
    pf=np.log(d['PF']/cpi)
    t=d['TIME']
    
    #henter likevektskvantum:
    Q_fitted = equate_q(y,pb,N,X,pf,t)
#######################################    
    #plotter funksjoner:
    Q_num = np.linspace(0.1,100,100)
    
    #sørger for å multiplisere med "cpi"
    D_C = np.exp(demand_curve(np,Q_num,y,pb)) * cpi
    L_S_C = np.exp(supply_curve_long_run(np,Q_num,N,X,pf,t)) * cpi
    S_S_C = np.exp(supply_curve_short_run(np,Q_num,N,X,pf,t,Q_fitted)) * cpi
    
    #Estetiske justeringer for plot, type font, tittel osv.
    plt.subplots(1, figsize=(10, 8))
    plt.title("Etterspørsel og Tilbud\n1995", size=18, color ="darkslategray", family = "Times New Roman")
    plt.rc("axes" ,edgecolor="lavender")
    plt.rcParams["font.family"] = "Sans Serif"
    font = font_manager.FontProperties(family="Times New Roman",
                                       style='normal',size=12)
    #
    plt.plot(Q_num, D_C, label='Etterspørsel', color = "mediumaquamarine")
    plt.plot(Q_num, L_S_C, label = 'Tilbud, lang sikt', color = "lightskyblue")
    plt.plot(Q_num ,S_S_C, label = 'Tilbud, kort sikt', color = "cornflowerblue")
    #Plasserer legend
    plt.legend(loc='upper left', fontsize= "medium", 
               prop=font, frameon=False, labelcolor="darkslategray")
    #Setter y=P, x=Q
    plt.ylabel('P', color ="dimgray", size = 14, family = "Times New Roman")
    plt.xlabel('Q', color = "dimgray", size = 14,family = "Times New Roman")
    
    
    plt.ylim(0,400)
    plt.xlim(0,80,10)
    #Estetiske justeringer for grid og ticks
    plt.grid(visible=True, which='major', color='lavender', linestyle='-')
    plt.tick_params(axis="x", colors='slategray')
    plt.tick_params(axis="y", colors='slategray')
    
    
    plt.show()
    

import pandas as pd
df=pd.read_csv("https://uit-sok-1006-v22.github.io/innleveringer/chickendata.csv",delimiter=";")

plot_year(df,1995) 

##############Plot av 1960###############

# Sjekker hvordan tilbud og etterspørsel var for 1960.

def plot_oppg(df,year):

##Denne delen var ferdig i oppgavetekst
    d=df[df['YEAR']==year].to_dict(orient='records')[0]
    
    cpi=d['CPI']
    y=np.log(d['Y'])
    pb=np.log(d['PBEEF']/cpi)
    N=d['POP']
    X=d['QPRODA']/1439-d['Q']*d['POP']
    pf=np.log(d['PF']/cpi)
    t=d['TIME']
    
    #henter likevektskvantum:
    Q_fitted = equate_q(y,pb,N,X,pf,t)
#######################################    
    #plotter funksjoner:
    Q_num = np.linspace(0.1,100,100)
    
    #sørger for å multiplisere med "cpi"
    D_C = np.exp(demand_curve(np,Q_num,y,pb)) * cpi
    L_S_C = np.exp(supply_curve_long_run(np,Q_num,N,X,pf,t)) * cpi
    S_S_C = np.exp(supply_curve_short_run(np,Q_num,N,X,pf,t,Q_fitted)) * cpi
    
    #Estetiske justeringer for plot, type font, tittel osv.
    plt.subplots(1, figsize=(8, 6))
    plt.title("Etterspørsel og Tilbud\n1960", size=18, color ="darkslategray", family = "Times New Roman")
    plt.rc("axes" ,edgecolor="lavender")
    plt.rcParams["font.family"] = "Sans Serif"
    font = font_manager.FontProperties(family="Times New Roman",
                                       style='normal',size=12)
    #
    plt.plot(Q_num, D_C, label='Etterspørsel', color = "mediumaquamarine")
    plt.plot(Q_num, L_S_C, label = 'Tilbud, lang sikt', color = "lightskyblue")
    plt.plot(Q_num ,S_S_C, label = 'Tilbud, kort sikt', color = "cornflowerblue")
    #Plasserer legend
    plt.legend(loc='lower right', fontsize= "medium", 
               prop=font, frameon=False, labelcolor="darkslategray")
    #Setter y=P, x=Q
    plt.ylabel('P', color ="dimgray", size = 14,family = "Times New Roman")
    plt.xlabel('Q', color = "dimgray", size = 14,family = "Times New Roman")
    
    plt.ylim(0,400)
    plt.xlim(0,80,10)
    #Estetiske justeringer for grid og ticks
    plt.grid(visible=True, which='major', color='lavender', linestyle='-')
    plt.tick_params(axis="x", colors='slategray')
    plt.tick_params(axis="y", colors='slategray')
    
    plt.show()

plot_oppg(df,1960)

############Plot av 1960 & 1995#############

def plot1960_1995(df,year,year1):
  ##Kopi av figur 2, 1960  
######################################
    d=df[df['YEAR']==year].to_dict(orient='records')[0]
    
    cpi=d['CPI']
    y=np.log(d['Y'])
    pb=np.log(d['PBEEF']/cpi)
    N=d['POP']
    X=d['QPRODA']/1439-d['Q']*d['POP']
    pf=np.log(d['PF']/cpi)
    t=d['TIME']
    
    #henter likevektskvantum:
    Q_fitted = equate_q(y,pb,N,X,pf,t)
#######################################    
    #plotter funksjoner:
    Q_num = np.linspace(0.1,100,100)
    
    D_C = np.exp(demand_curve(np,Q_num,y,pb)) * cpi
    L_S_C = np.exp(supply_curve_long_run(np,Q_num,N,X,pf,t)) * cpi
    S_S_C = np.exp(supply_curve_short_run(np,Q_num,N,X,pf,t,Q_fitted)) * cpi
    
    #Estetiske justeringer for subplots, type font, tittel osv.
    fig, ax = plt.subplots(1,2, figsize = (7,5))
    ax[0].set_title("Etterspørsel og Tilbud\n1960", size=14, color ="darkslategray",family="Times New Roman")
    plt.rc("axes" ,edgecolor="lavender")
    plt.rcParams["font.family"] = "Sans Serif"
    font = font_manager.FontProperties(family="Times New Roman",
                                       style='normal',size=12)
    #
    ax[0].plot(Q_num, D_C, label='Etterspørsel', color = "mediumaquamarine")
    ax[0].plot(Q_num, L_S_C, label = 'Tilbud, lang sikt', color = "lightskyblue")
    ax[0].plot(Q_num ,S_S_C, label = 'Tilbud, kort sikt', color = "cornflowerblue")
    #Plasserer legend på utesiden av figuren.
    ax[0].legend(loc="lower right", fontsize= "small", 
               prop=font, frameon=False, labelcolor="darkslategray")
    
    #Setter y=P, x=Q
    ax[0].set_ylabel('P', color ="dimgray", size = 14,family="Times New Roman")
    ax[0].set_xlabel('Q', color = "dimgray", size = 14,family="Times New Roman")
    
    ax[0].set_ylim(0,400)
    ax[0].set_xlim(0,80,10)
    #Estetiske justeringer for grid og ticks
    ax[0].grid(visible=True, which='major', color='lavender', linestyle='-')
    ax[0].tick_params(axis="x", colors='slategray')
    ax[0].tick_params(axis="y", colors='slategray')
    
    ##Denne delen er justert kopi av Figur 1, 1995
    d1=df[df['YEAR']==year1].to_dict(orient='records')[0]
    
    cpi1=d1['CPI']
    y1=np.log(d1['Y'])
    pb1=np.log(d1['PBEEF']/cpi1)
    N1=d1['POP']
    X1=d1['QPRODA']/1439-d1['Q']*d1['POP']
    pf1=np.log(d1['PF']/cpi1)
    t1=d1['TIME']
    
    #henter likevektskvantum:
    Q_fitted1 = equate_q(y1,pb1,N1,X1,pf1,t1)
#######################################    
    #plotter funksjoner:
    Q_num1 = np.linspace(0.1,100,100)
    
    D_C1 = np.exp(demand_curve(np,Q_num1,y1,pb1)) * cpi1
    L_S_C1 = np.exp(supply_curve_long_run(np,Q_num1,N1,X1,pf1,t1)) * cpi1
    S_S_C1 = np.exp(supply_curve_short_run(np,Q_num1,N1,X1,pf1,t1,Q_fitted1)) * cpi1
    
    #Estetiske justeringer for plot, type font, tittel osv.
    plt.title("Etterspørsel og Tilbud\n1995", size=14, color ="darkslategray", family="Times New Roman")
    plt.rc("axes" ,edgecolor="lavender")
    plt.rcParams["font.family"] = "Sans Serif"
    font = font_manager.FontProperties(family="Times New Roman",
                                       style='normal',size=12)
    #
    ax[1].plot(Q_num1, D_C1, label='Etterspørsel', color = "mediumaquamarine")
    ax[1].plot(Q_num1, L_S_C1, label = 'Tilbud, lang sikt', color = "lightskyblue")
    ax[1].plot(Q_num1, S_S_C1, label = 'Tilbud, kort sikt', color = "cornflowerblue")
    
    #Setter y=P, x=Q
    ax[1].set_ylabel('', color ="dimgray", size = 14)
    ax[1].set_xlabel('Q', color = "dimgray", size = 14,family="Times New Roman")
    
    ax[1].set_ylim(0,400)
    ax[1].set_xlim(0,80,10)
    #Estetiske justeringer for grid og ticks
    ax[1].grid(visible=True, which='major', color='lavender', linestyle='-')
    ax[1].tick_params(axis="x", colors='slategray')
    ax[1].tick_params(axis="y", colors='slategray')
    
    plt.show()
    
plot1960_1995(df,1960,1995)

#######Plot Scenario########

def plot_scenario(df,year):

##Denne delen var ferdig i oppgavetekst
    d=df[df['YEAR']==year].to_dict(orient='records')[0]
    
    cpi=d['CPI']
    y=np.log(d['Y'])
    pb=np.log(d['PBEEF']/cpi)
    N=d['POP']
    X=d['QPRODA']/1439-d['Q']*d['POP']
    pf=np.log(d['PF']/cpi)
    t=d['TIME']
    
    ##her legges 0.5 til på inntekt y, og kjøtt pb.
    y1=np.log(d['Y'])+0.5
    pb1=np.log(d['PBEEF']/cpi)+0.5
    #henter likevektskvantum:
    Q_fitted = equate_q(y,pb,N,X,pf,t)
#######################################    
    #plotter funksjoner:
    Q_num = np.linspace(0.1,100,100)
    ##her legges 0.5 til på kvantum Q.
    Q_num1 =Q_num+0.5
    
    #sørger for å multiplisere med "cpi"
    D_C = np.exp(demand_curve(np,Q_num,y,pb)) * cpi
    L_S_C = np.exp(supply_curve_long_run(np,Q_num,N,X,pf,t)) * cpi
    S_S_C = np.exp(supply_curve_short_run(np,Q_num,N,X,pf,t,Q_fitted)) * cpi
    #Endringen på 0.5 legges inn i funksjonene
    Demand_y = np.exp(demand_curve(np,Q_num,y1,pb)) * cpi
    Demand_pb = np.exp(demand_curve(np,Q_num,y,pb1)) * cpi
    Demand_Q = np.exp(demand_curve(np,Q_num1,y,pb)) * cpi
    #Estetiske justeringer for plot, type font, tittel osv.
    plt.subplots(1, figsize=(8, 6))
    plt.title("Scenarioanalyse\n1995", size=18, color ="darkslategray", family="Times New Roman")
    plt.rc("axes" ,edgecolor="lavender")
    plt.rcParams["font.family"] = "Sans Serif"
    font = font_manager.FontProperties(family="Times New Roman",
                                       style='normal',size=12)
    #
    plt.plot(Q_num, D_C, label='Etterspørsel', color = "mediumaquamarine")
    plt.plot(Q_num, L_S_C, label = 'Tilbud, lang sikt', color = "lightskyblue")
    plt.plot(Q_num ,S_S_C, label = 'Tilbud, kort sikt', color = "cornflowerblue")
    #de nye scenariovariablene
    plt.plot(Q_num, Demand_y, label='Etterspørsel, y', color = "palevioletred")
    plt.plot(Q_num, Demand_pb, label='Etterspørsel, pb', color = "mediumvioletred")
    plt.plot(Q_num, Demand_Q, label='Etterspørsel, Q', color = "darkmagenta")
    #Plasserer legend
    plt.legend(loc='upper left', fontsize= "medium", 
               prop=font, frameon=False, labelcolor="darkslategray")
    #Setter y=P, x=Q
    plt.ylabel('P', color ="dimgray", size = 14, family="Times New Roman")
    plt.xlabel('Q', color = "dimgray", size = 14, family="Times New Roman")
    
    plt.ylim(0,400)
    plt.xlim(0,80,10)
    #Estetiske justeringer for grid og ticks
    plt.grid(visible=True, which='major', color='lavender', linestyle='-')
    plt.tick_params(axis="x", colors='slategray')
    plt.tick_params(axis="y", colors='slategray')
    
    plt.show()
    
plot_scenario(df,1995)
    
    
    

