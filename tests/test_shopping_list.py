from list.Shopping_list_oop import Item
import pytest

class TestShop:
    @pytest.mark.slow
    def test_items_in_list(self):
        item = Item()
        assert item.items_in_list =={}
        with pytest.raises(BaseException):
            item.items_in_list.pop()
    def test_add_item(self):
        item=Item()
        with pytest.raises(BaseException):
            item.add_item(12,13)
        item.add_item('ali',12)
        item.add_item('ali',12)
        assert len(item.items_in_list)==2