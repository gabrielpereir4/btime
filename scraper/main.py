from scraper.automation import Automation
from utils.csvmanager import CSVManager

def main():
    automation = Automation()
    noticias = automation.run()
    csv_manager = CSVManager()
    csv_manager.salvar(noticias, "noticias_scraper.csv")

main()