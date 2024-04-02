from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Predict_click(self, **event_args):
    """This method is called when the button is clicked"""
    prediction = anvil.server.call('House_Prediction',
                                  self.MedInc.text,self.HouseAge.text,
                                  self.AveRooms.text,self.AveBedrms.text,
                                  self.Population.text,self.AveOccup.text,
                                  self.Latitude.text,self.Longitude.text)
    if prediction:
      self.Prediction.visible = True
      self.Prediction.text = 'The predicted house price is {}'.format(round(prediction,2))
