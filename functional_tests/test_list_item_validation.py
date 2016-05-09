from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Carlos goes to the home page and accidentally tries to submit an empty list item

        # The home page refreshes and there is an error message saying that list items cannot be blank

        # He tries again with some text for the item. It now works

        # He tries again to submit a blank list item

        # The list display page shows the same error message

        # Finally, Carlos adds some text and enters another item
        self.fail('Write this test case')
