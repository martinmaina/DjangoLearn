from django.db import models


# A many to many relationship.Products can have different promotions 
# and promotions can have different products

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # Since we have defined a many to many relationship in the Product class
    # in this class, Django will automatically create for us product_set field
    # If you are not content with this name, we can add a related_name=favorite_name
    # argument in the manytomany relationship declaration in the product class.
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL,null=True,related_name='+')
    # We are in a situation where collection class depends on the Product class and
    # Product class depends on the collection class. This is called circular dependency.
    # We use the quotes in the Product name class since it is defined after the collection class.
    # Since Django will try to create reverse relationship, there will be a clash
    # since we already have collection field in the Product model.
    # To avoid this, we tell the django not to create the reverse rship
    # by setting the related_name to '+'

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Item(models.Model):
    title = models.CharField(max_length=255)

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD   =  'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD,   'Gold')
    ]
    given_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)


 
        
class Order(models.Model):
    PAYMENT_STATUS_PENDING  = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED   = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
     # on_delete=models.CASCADE This means when we delete the customer, the associated address will also be deleted
    #Alternatively, if this field accepts null values, we can se tthe field to null when the customer is deleted
    # on_delete=models.SET_NULL. That is, when the parent will be deleted, (Customer)
    # the associated address, will not be deleted, but it will the customer
    # field will be set to null. That is, if the field accepts null values.
    # We have also models.SET_DEFAULT which sets the field to the default value, 
    # We have also models.PROTECT which means that the parent cannot be delete the parent associated with this child(address). First,w e have to delete the child.

    # If the customer can have multiple addresses, then the relationship will be one-to-many
    # customer_a = models.ForeignKey(Customer,on_delete=models.CASCADE)
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # zip = models.CharField(max_length=255)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()