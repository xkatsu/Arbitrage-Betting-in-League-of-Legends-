from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import string

datee = pd.read_csv('durabilidade.csv', low_memory=False)
date = datee[datee.patch >= '13.01']
driver = webdriver.Chrome(r'C:\Program Files\chromedriver')
driver.maximize_window()

url_dict = {
    'LLA' :  'https://22bet.com/br/line/esports/1940546-league-of-legends-lla',
    'LPL' :  'https://22bet.com/br/line/esports/1852934-league-of-legends-lpl-spring',
    'LCKCL' : 'https://22bet.com/br/line/esports/2173122-league-of-legends-lck-challengers/164331349-hanwha-life-challengers-t1-challengers', 
    'LVP'  :  'https://22bet.com/br/line/esports/2076227-league-of-legends-lvp-superliga-spring-playoffs',
    'NLC'  :  'https://22bet.com/br/line/esports/2057368-league-of-legends-prime-league-spring'
}   

n=1

def get_liga(nome, mercado=False):
    print(nome)
    driver.get(url_dict[nome])

    def goto_game(n):      
        driver.find_element(By.XPATH,f'/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div[4]/div[2]/div/div/div/div[2]/a[{n}]/span[6]').click()
        sleep(5)   

        driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[2]/select/option[2]').click()
        sleep(5)    


    def get_odds():
        team_1 = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]')
        team_2 = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div[3]/div/div[1]/div[1]/div/div/div[2]/div[3]/div[2]')
        time_A = team_1.text
        time_B = team_2.text

        all = driver.find_elements(By.XPATH,'//*[@id="allBetsTable"]')
        lista_odds = all[0].text

        print(f'----{team_1.text}  x  {team_2.text}')


        od_text = 'Total de Dragões Derrotados Acima de'
        od_linha = float(lista_odds[lista_odds.find(od_text) + len(od_text) +1 : lista_odds.find(od_text) + len(od_text) + 4] )
        over_drake = float(lista_odds[lista_odds.find(od_text) + len(od_text) +4 : lista_odds.find(od_text) + len(od_text) +8])
        print(f'Over {od_linha} Drakes: {over_drake}')
        
        ud_text = 'Total de Dragões Derrotados Abaixo de'
        ud_linha = float(lista_odds[lista_odds.find(ud_text) + len(ud_text) +1: lista_odds.find(ud_text) + len(ud_text) + 4])
        under_drake = float(lista_odds[lista_odds.find(ud_text) + len(ud_text) +4 : lista_odds.find(ud_text) + len(ud_text) + 7])
        print(f'Under {ud_linha} Drakes: {under_drake}')

        
        ot_text = 'Total de Torres Destruídas Acima de'
        ot_linha = float(lista_odds[lista_odds.find(ot_text) + len(ot_text) +1 : lista_odds.find(ot_text) + len(ot_text) + 4].strip(string.ascii_letters))
        over_tower = float(lista_odds[lista_odds.find(ot_text) + len(ot_text) +5: lista_odds.find(ot_text) + len(ot_text) + 10].strip(string.ascii_letters))
        print(f'Over {ot_linha} Tower: {over_tower}')

        ut_text = 'Total de Torres Destruídas Abaixo de'
        ut_linha = float(lista_odds[lista_odds.find(ut_text) + len(ut_text) +1: lista_odds.find(ut_text) + len(ut_text) + 4].strip(string.ascii_letters))
        under_tower = float(lista_odds[lista_odds.find(ut_text) + len(ut_text) +5 : lista_odds.find(ut_text) + len(ut_text) + 10].strip(string.ascii_letters))
        print(f'Under {ut_linha} Tower: {under_tower}')

        '''otime_text = 'Duração do Mapa Acima de'
        otime_linha = float(lista_odds[lista_odds.find(otime_text) + len(otime_text) : lista_odds.find(otime_text) + len(otime_text) + 2].strip(string.ascii_letters))
        over_time = float(lista_odds[lista_odds.find(otime_text) + len(otime_text) +2  : lista_odds.find(otime_text) + len(otime_text) + 6].strip(string.ascii_letters))
        print(f'Over {otime_linha} Mins: {over_time}')

        utime_text = 'Duração do Mapa Abaixo de'
        utime_linha = float(lista_odds[lista_odds.find(utime_text) + len(utime_text) : lista_odds.find(utime_text) + len(utime_text) + 3].strip(string.ascii_letters))
        under_time = float(lista_odds[lista_odds.find(utime_text) + len(utime_text) +3 : lista_odds.find(utime_text) + len(utime_text) + 7].strip(string.ascii_letters))
        print(f'Under {utime_linha} Mins: {under_time}')'''

        '''ob_text = 'Total de Nashors Derrotados Acima de'
        ob_linha = float(lista_odds[lista_odds.find(ob_text) + len(ob_text) : lista_odds.find(ob_text) + len(ob_text) + 2].strip(string.ascii_letters))
        over_baron = float(lista_odds[lista_odds.find(ob_text) + len(ob_text) +2 : lista_odds.find(ob_text) + len(ob_text) + 6].strip(string.ascii_letters))
        print(f'Over {ob_linha} Barons: {over_baron}')

        ub_text = 'Total de Nashors Derrotados Abaixo de'
        ub_linha = float(lista_odds[lista_odds.find(ub_text) + len(ub_text) : lista_odds.find(ub_text) + len(ub_text) + 2].strip(string.ascii_letters))
        under_baron = float(lista_odds[lista_odds.find(ub_text) + len(ub_text) +2 : lista_odds.find(ub_text) + len(ub_text) + 6].strip(string.ascii_letters))
        print(f'Under {ub_linha} Barons: {under_baron}')'''
        
        return time_A, time_B
    
    goto_game(n) 
    time_A, time_B = get_odds()
    print()
  

        

    def analise_ev(time, pos,escolha):
        player = date[date.position == pos]
        tim = player[player.teamname == time]

        aliado_drakes = tim[tim.dragons >= "0"]
        opp_drakes = aliado_drakes[aliado_drakes.opp_dragons >= "0"]

        aliado_torres = tim[tim.towers >= "0"]
        opp_torres = aliado_torres[aliado_torres.opp_towers >= "0"]

        num_games = len(opp_torres)

        atorres = aliado_torres['towers'].tolist()
        btorres = opp_torres['opp_towers'].tolist()

        adrakes = aliado_drakes['dragons'].tolist()
        bdrakes = opp_drakes['opp_dragons'].tolist()

        lista_torres = atorres + btorres
        lis_torre = [int(x) for x in lista_torres]
        soma_lista_torre = sum(lis_torre)

        lista_drakes = adrakes + bdrakes
        lis_drake = [int(x) for x in lista_drakes]
        soma_lista_drake = sum(lis_drake)

        

        lis_div_torre = (soma_lista_torre/num_games)
        lis_div_drake = (soma_lista_drake/num_games)

        
        #print(torres_list)
        def soma_items(num, obj, tipo_lista, tipoa, tipob):
            soma_over= []
            soma_under =[]
            for x in range(len(tipoa)):
                if float(tipoa[x]) + float(tipob[x]) > num:
                    soma_over.append(1)
                if float(tipoa[x]) + float(tipob[x]) < num:
                    soma_under.append(1)
        
            print(obj)
            print(f'{escolha} obtem uma média de{obj} {tipo_lista:.1f} por jogo')    

            print(f'dando uma probabilidade de OVER {num}  {obj}  {(len(soma_over)/num_games*100):.2f}%  ')           
            print(f'dando uma probabilidade de UNDER {num}  {obj}  {(len(soma_under)/num_games*100):.2f}%  ')
            print()
        soma_items(4.5,'dragons', lis_div_drake, adrakes, bdrakes )
        soma_items(12.5,'towers', lis_div_torre, atorres, btorres )


    analise_ev(time_A, 'team', time_A)
    analise_ev(time_B, 'team', time_B)    


get_liga('LLA')






