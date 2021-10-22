from django.contrib import admin
from .models import Brand, ProductType, ProductInventory, User, Client, Logistics, ShoppingCart, Order, ProductPurchase
from .models import Transportation, Rate, Manager, ManagerReply


# Register your models here.
@admin.register(Brand)
class Brand(admin.ModelAdmin):
    list_display = ["brand_id", "brand_name", "brand_grade"]

    # list_editable = ["product_price"] #可编辑单价
    # list_display_links = ["product_name"] #点击类名跳转
    # filter_vertical = ["product_name"] #垂直筛选
    # raw_id_fields = ["product_name"] #顶端搜索框优化
    # list_filter = ["product_name"] #右侧可以按类名筛选
    # search_fields = ["product_name"] #主界面模糊搜索

@admin.register(ProductType)
class ProductType(admin.ModelAdmin):
    list_display = ["type_id", "type_name"]

@admin.register(ProductInventory)
class ProductInventory(admin.ModelAdmin):
    list_display = ["product_id", "product_brand", "product_type", "product_name", "product_size", "product_quantity",
                    "product_price", "product_color", "product_sold_quantity"]

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ["user_id", "user_pwd", "user_nickname"]

@admin.register(Client)
class Client(admin.ModelAdmin):
    list_display = ["client_identity_card", "client_name", "client_sex", "client_phone_number", "client_email",
                    "client_region", "client_address", "client_user_id"]

@admin.register(Logistics)
class Logistics(admin.ModelAdmin):
    list_display = ["logistics_id", "logistics_name", "logistics_person", "logistics_phone", "logistics_country"]


@admin.register(ShoppingCart)
class ShoppingCart(admin.ModelAdmin):
    list_display = ["cart_id", "cart_product", "cart_user", "cart_product_quantity", "cart_add_time"]

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ["order_id", "order_condition", "order_aggregate_amount", "order_purchase_time"]

@admin.register(ProductPurchase)
class ProductPurchase(admin.ModelAdmin):
    list_display = ["purchase_order_id", "purchase_cart", "purchase_aggregate_amount"]

@admin.register(Transportation)
class Transportation(admin.ModelAdmin):
    list_display = ["transportation_id", "transportation_company_name", "transportation_fee",
                    "transportation_condition", "transportation_order"]

@admin.register(Rate)
class Rate(admin.ModelAdmin):
    list_display = ["rate_id", "rate_total", "rate_product", "rate_transport", "rate_content", "rate_order", "rate_status",
                    "rate_time"]

@admin.register(Manager)
class Manager(admin.ModelAdmin):
    list_display = ["manager_id", "manager_name", "manager_pwd"]
    
@admin.register(ManagerReply)
class ManagerReply(admin.ModelAdmin):
    list_display = ["reply_id", "reply_manager_id", "reply_rate_id", "reply_time", "reply_content"]


