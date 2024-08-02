from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def highlight_lable_show(self, **event_args):
    """This method is called when the Label is shown on the screen"""
    pass

  def start_date_change(self, **event_args):
    """This method is called when the selected date changes"""
    pass

  def new_drive_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.new_dirve_panel.visible = True
