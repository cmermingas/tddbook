from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Carlos goes to the home page and accidentally tries to submit an empty list item
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # The home page refreshes and there is an error message saying that list items cannot be blank
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # He tries again with some text for the item. It now works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # He tries again to submit a blank list item
        self.get_item_input_box().send_keys('\n')

        # The list display page shows the same error message
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # Finally, Carlos adds some text and enters another item
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_duplicate_items(self):
        # Carlos goes to the home page and starts a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # He enters the same item
        self.get_item_input_box().send_keys('Buy wellies\n')

        # The page displays a helpful error message
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")

    def test_error_messages_are_cleared_on_input(self):
        # Carlos starts a new list in a way that causes a validation error:
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # Start typing in the input box to clear the error
        self.get_item_input_box().send_keys('a')

        # The error disappears
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())