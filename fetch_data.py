import requests
import lxml.etree as et
import pandas as pd
import os
from tqdm import tqdm, trange

modes = {
    0: "osu",
    1: "taiko",
    2: "fruits",
    3: "mania"
}


def get_data(mode: int, start: int, end: int):
    data = pd.DataFrame([], columns=["pc", "pp"])
    print("Collecting data...")
    for i in trange((start - 1) // 50 + 1, (end - 1) // 50 + 2):
        url = f'https://osu.ppy.sh/rankings/{modes[mode]}/performance?page={i}#scores'
        try:
            r = requests.get(url)
            r.raise_for_status()
            text = r.text
            html = et.HTML(text)
            for j in range(1, 51):
                pc: str = html.xpath(f'//body//tbody//tr[{j}]/td[@class="ranking-page-table__column '
                                     f'ranking-page-table__column--dimmed"][2]/text()')[0].strip().replace(',', '')
                pp: str = html.xpath(f'//body//tbody//tr[{j}]/td[@class="ranking-page-table__column '
                                     f'ranking-page-table__column--focused"]/text()')[0].strip().replace(',', '')
                data = data.append(pd.DataFrame({"pc": [pc], "pp": [pp]}), ignore_index=True)
        except:
            print("failed")
            return 0

    data.to_csv("data.csv")
    return 1
