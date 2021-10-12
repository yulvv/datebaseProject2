from django.contrib import admin
from .models import Inventory, Client, Order, Distribution, Evaluation, Brand


# Register your models here.

@admin.register(Inventory)
class Inventory(admin.ModelAdmin):
    list_display = ["product_id", "product_name","product_quantity", "product_price", "product_size", "product_color"]
    # list_editable = ["product_price"] #可编辑单价
    # list_display_links = ["product_name"] #点击类名跳转
    # filter_vertical = ["product_name"] #垂直筛选
    # raw_id_fields = ["product_name"] #顶端搜索框优化
    # list_filter = ["product_name"] #右侧可以按类名筛选
    # search_fields = ["product_name"] #主界面模糊搜索

@admin.register(Client)
class Client(admin.ModelAdmin):
        list_display = ["client_id", "client_name", "client_sex", "client_phone_number",
                        "client_email", "client_region", "client_address"]

@admin.register(Order)
class Order(admin.ModelAdmin):
        list_display = ["order_id", "order_product_id", "order_brand_id", "order_transport_id", "order_evaluate_id",
                        "order_client_id", "order_condition", "order_purchase_quantity","order_aggregate_amount"]

@admin.register(Distribution)
class Distribution(admin.ModelAdmin):
        list_display = ["distribution_id", "distribution_company_name", "distribution_fee", "distribution_condition",
                        "distribution_order_id"]

@admin.register(Evaluation)
class Evaluation(admin.ModelAdmin):
        list_display = ["evaluation_id", "evaluation_sum", "evaluation_product", "evaluation_distribution",
                        "evaluation_description", "evaluation_order_id", "evaluation_condition"]

@admin.register(Brand)
class Evaluation(admin.ModelAdmin):
        list_display = ["brand_id", "brand_name", "brand_grade"]