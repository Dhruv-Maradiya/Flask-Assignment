from typing import List

from pydantic import BaseModel, Field


class ProductSchema(BaseModel):
    name: str = Field(..., title="Product Name", max_length=100)
    description: str = Field(..., title="Product Description", max_length=500)
    price: float = Field(..., gt=0, title="Product Price")
    category: str = Field(..., title="Product Category", max_length=50)
    images: List[str] = Field(..., title="Product Images")
    stock_quantity: int = Field(..., ge=0, title="Stock Quantity")
