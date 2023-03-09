"""Classes for melon orders."""
class AbstractMelonOrder:
    """ Generic melon superclass"""
    shipped = False

    def __init__(self, species, qty):

        self.species = species
        self.qty = qty

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        flat_fee = 0

        # Now, Christmas melons will cost 1.5 times as much as the base price.
        #Also, a flat fee of $3 will be added to all international orders with less than 10 melons.

        if self.species == 'Christmas melons':
            base_price = base_price * 1.5

        if self.order_type == "international":
            if self.qty < 10:
                flat_fee = 3

        total = ((1 + self.tax) * self.qty * base_price) + flat_fee

        return total
    

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    order_type = "domestic"
    tax = 0.08

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""
    #     super().__init__(species, qty)

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.order_type = "domestic"
        # self.tax = 0.08
        
        

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        
        self.country_code = country_code
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
