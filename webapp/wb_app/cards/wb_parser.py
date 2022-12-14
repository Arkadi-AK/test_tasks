import asyncio
import json
from io import BytesIO

import aiohttp
import openpyxl

from cards.models import CardModel
from wb_app.settings import URL_WB


def xlsx_to_list(request):
    file_uploaded = request.FILES.get("file")
    file_name = file_uploaded.name
    if not file_name.endswith(".xlsx"):
        return f"Error. The file must have the xlsx extension. You have uploaded {file_name}"

    try:
        file_data_binary = file_uploaded.read()
        book = openpyxl.open(filename=BytesIO(file_data_binary))
        sheet = book.active
        rows_count = sheet.max_row
        articles = []
        for row_index in range(1, rows_count + 1):
            cell_value = sheet[row_index][0].value
            if isinstance(cell_value, int):
                articles.append(cell_value)
    except Exception:
        return "File data is not valid"
    return articles


async def parse_data_from_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            if resp.status == 200:
                product_data = await resp.text()
                return product_data


def parser(list_of_articles):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    cards_list = []
    for article in list_of_articles:
        task = parse_data_from_url(f"{str(URL_WB)}{article}")
        cards_list.append(task)
    results = loop.run_until_complete(asyncio.gather(*cards_list))
    result = []
    for i in results:
        card = CardModel.parse_raw(i)
        card_json = json.loads(card.json(ensure_ascii=False, ))
        result.append(card_json)
    return result
