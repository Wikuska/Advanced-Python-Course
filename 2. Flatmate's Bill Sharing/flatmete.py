class Flatmate:
    """
    Object representing person sharing a bill, 
    contains person name and number of days they spent in house
    """
    
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        
    def pays(self, bill):
        pass
