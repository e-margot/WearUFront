from fastapi import FastAPI, File
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles
from typing import List, Annotated

from fastapi.middleware.cors import CORSMiddleware



class TextQuery(BaseModel):
    text: str


class Item(BaseModel):
    item_id: int
    image_path: str
    product_name: str
    product_type_name: str
    product_group_name: str
    colour_group_name: str
    perceived_colour_value_name: str
    perceived_colour_master_name: str
    department_name: str
    index_name: str
    index_group_name: str
    section_name: str
    garment_group_name: str
    description: str


fixtures = [
    {
        'item_id': 866,
        'image_path': '/static/030/0300024042.jpg',
        'product_name': 'Superskinny',
        'product_type_name': 'Trousers',
        'product_group_name': 'Garment Lower body',
        'colour_group_name': 'Dark Blue',
        'perceived_colour_value_name': 'Dark',
        'perceived_colour_master_name': 'Turquoise',
        'department_name': 'Woven bottoms',
        'index_name': 'Ladieswear',
        'index_group_name': 'Ladieswear',
        'section_name': 'Mama',
        'garment_group_name': 'Trousers',
        'description': 'Jeans in washed stretch denim with fake front pockets, real back pockets and skinny legs. Wide ribbing at the waist for optimum comfort.',
    },
    {
        'item_id': 864,
        'image_path': '/static/030/0300024017.jpg',
        'product_name': 'Super skinny denim',
        'product_type_name': 'Trousers',
        'product_group_name': 'Garment Lower body',
        'colour_group_name': 'Light Blue',
        'perceived_colour_value_name': 'Dusty Light',
        'perceived_colour_master_name': 'Blue',
        'department_name': 'Woven bottoms',
        'index_name': 'Ladieswear',
        'index_group_name': 'Ladieswear',
        'section_name': 'Mama',
        'garment_group_name': 'Trousers',
        'description': 'Jeans in washed stretch denim with fake front pockets, real back pockets and skinny legs. Wide ribbing at the waist for optimum comfort.',
    },
    {
        'item_id': 872,
        'image_path': '/static/030/0300024063.jpg',
        'product_name': 'Superskinny',
        'product_type_name': 'Trousers',
        'product_group_name': 'Garment Lower body',
        'colour_group_name': 'Blue',
        'perceived_colour_value_name': 'Medium Dusty',
        'perceived_colour_master_name': 'Blue',
        'department_name': 'Woven bottoms',
        'index_name': 'Ladieswear',
        'index_group_name': 'Ladieswear',
        'section_name': 'Mama',
        'garment_group_name': 'Trousers',
        'description': 'Jeans in washed stretch denim with fake front pockets, real back pockets and skinny legs. Wide ribbing at the waist for optimum comfort.',
    },
    {
        'item_id': 863,
        'image_path': '/static/030/0300024016.jpg',
        'product_name': 'Superskinny',
        'product_type_name': 'Trousers',
        'product_group_name': 'Garment Lower body',
        'colour_group_name': 'Dark Blue',
        'perceived_colour_value_name': 'Medium Dusty',
        'perceived_colour_master_name': 'Blue',
        'department_name': 'Woven bottoms',
        'index_name': 'Ladieswear',
        'index_group_name': 'Ladieswear',
        'section_name': 'Mama',
        'garment_group_name': 'Trousers',
        'description': 'Jeans in washed stretch denim with fake front pockets, real back pockets and skinny legs. Wide ribbing at the waist for optimum comfort.',
    },
    {
        'item_id': 870,
        'image_path': '/static/030/0300024056.jpg',
        'product_name': 'Super skinny denim',
        'product_type_name': 'Trousers',
        'product_group_name': 'Garment Lower body',
        'colour_group_name': 'Light Blue',
        'perceived_colour_value_name': 'Dusty Light',
        'perceived_colour_master_name': 'Blue',
        'department_name': 'Woven bottoms',
        'index_name': 'Ladieswear',
        'index_group_name': 'Ladieswear',
        'section_name': 'Mama',
        'garment_group_name': 'Trousers',
        'description': 'Jeans in washed stretch denim with fake front pockets, real back pockets and skinny legs. Wide ribbing at the waist for optimum comfort.',
    },

]

items = [Item.model_validate(fixture) for fixture in fixtures]


mock_service = FastAPI()
mock_service.mount(
    '/static', StaticFiles(directory='static'), name='static',
)

mock_service.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники (в реальном приложении лучше уточнить)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы
    allow_headers=["*"],  # Разрешить все заголовки
)


@mock_service.get('/items/{item_id}')
async def get_item(item_id: int) -> Item:
    return items[0]


@mock_service.post('/search_text')
async def search_text(
    limit: int,
    offset: int,
    query: TextQuery,
) -> list[Item]:
    return items


@mock_service.post('/search_image')
async def search_image(
    limit: int,
    offset: int,
    query: Annotated[bytes, File()],
) -> list[Item]:
    return items
