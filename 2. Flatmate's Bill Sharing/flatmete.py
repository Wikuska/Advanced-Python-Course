class Flatmate:
    """
    Object representing person sharing a bill, 
    contains person name and number of days they spent in house
    """
    
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        
    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return round((bill.amount * weight), 2)
