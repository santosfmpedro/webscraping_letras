from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.letras.mus.br/estilos/emocore/artistas.html")
    time.sleep(3)
    #print(page.title())
    page.click("text=Ver todos os artistas do estilo Emocore")
    time.sleep(3)
    ul_artists = page.locator('ul[class="cnt-list cnt-list--col3"]')
    print(f"{ul_artists.count()} artists ul are found.")    
    print(ul_artists)

    artists = ul_artists.locator('a')
    n_artists = artists.count()
    print(f"{n_artists} artists ul are found.")   

    time.sleep(3)
    for i in range(n_artists):
        print(artists.nth(i).get_attribute('href'))
        time.sleep(2)
        time.sleep(2)




    time.sleep(3)
    time.sleep(3)
    #browser.close()
    

    