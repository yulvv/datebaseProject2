from django.db import models
from django.utils.translation import gettext_lazy as _

# 定义入驻品牌表单
class Brand(models.Model):
    # 继承models类

    class Meta:
        verbose_name = _("入驻品牌信息表")
        verbose_name_plural = _("入驻品牌信息表")

    # 品牌号
    brand_id = models.CharField(primary_key=True, verbose_name=_("品牌号"), max_length=40, default="")

    # 品牌名称
    brand_name = models.CharField(verbose_name=_("品牌名称"), max_length=40, unique=True, default="")

    # 品牌等级的类型
    BRAND_GRADE_CHOICE = (
        ('一星品牌', _('*'))
        , ('二星品牌', _('**'))
        , ('三星品牌', _('***'))
        , ('四星品牌', _('****'))
        , ('五星品牌', _('*****'))
    )

    # 品牌等级
    brand_grade = models.CharField(choices=BRAND_GRADE_CHOICE, verbose_name=_("品牌等级"), max_length=10, default="")

    def __str__(self):
        return str(self.brand_name)

# 定义商品类别表
class ProductType(models.Model):

    class Meta:
        verbose_name = _("商品类别表")
        verbose_name_plural = _("商品类别表")

    # 商品类别编号
    type_id = models.CharField(verbose_name=_("商品类别编号"), primary_key=True, max_length=40, default="")

    # 商品类别名称
    type_name = models.CharField(verbose_name=_("商品类别名称"), max_length=40, null="")

    def __str__(self):
        return str(self.type_name)

# 定义产品库存表单
class ProductInventory(models.Model):

    class Meta:
        verbose_name = _("产品库存表")
        verbose_name_plural = _("产品库存表")

    # 产品号
    product_id = models.CharField(verbose_name=_("产品号"), primary_key=True, max_length=40, default="")

    # 品牌名称
    product_brand = models.ForeignKey(to=Brand, related_name="product_brand_brand", on_delete=models.CASCADE,
                                      verbose_name=_("品牌名称"), max_length=40, default="")

    # 产品类别
    product_type = models.ForeignKey(to=ProductType, related_name="product_type_product_type", on_delete=models.CASCADE,
                                     verbose_name=_("产品类别"), max_length=40, default="")

    # 产品名称
    product_name = models.CharField(verbose_name=_("产品名称"), max_length=40, default="")

    # 产品图片
    # product_photo = LimitSizeImageField(upload_to=user_directory_path, verbose_name=_("Proof Image"),
    # blank=True, null=True)

    # 产品尺码的类型
    PRODUCT_SIZE_CHOICE = (
        ('均码', _('均码'))
        , ('S', _('S'))
        , ('M', _('M'))
        , ('L', _('L'))
    )

    # 产品尺码
    product_size = models.CharField(choices=PRODUCT_SIZE_CHOICE, verbose_name=_("产品尺码"), max_length=40, default="均码")

    # 产品库存数量
    product_quantity = models.PositiveIntegerField(verbose_name=_("产品库存数量"))

    # 产品单价
    product_price = models.FloatField(verbose_name=_("产品单价"))

    # 产品颜色
    product_color = models.CharField(verbose_name=_("产品颜色"), max_length=40, default="")

    # 销售数量
    product_sold_quantity = models.PositiveIntegerField(verbose_name=_("销售数量"))

    def __str__(self):
        return str(self.product_name) + "  "+str(self.product_color) + "  " + str(self.product_size)

# 定义用户登陆表
class User(models.Model):

    class Meta:
        verbose_name = _("用户登陆表")
        verbose_name_plural = _("用户登陆表")

    # 用户号
    user_id = models.CharField(primary_key=True, verbose_name=_("用户号"), max_length=40, unique=True, default="")

    # 用户密码
    user_pwd = models.CharField(verbose_name=_("用户密码"), max_length=40, default="")

    # 用户昵称
    user_nickname = models.CharField(verbose_name=_("用户昵称"), max_length=40, unique=True, default="")

    def __str__(self):
        return str(self.user_id)

# 定义客户表单
class Client(models.Model):
    class Meta:
       verbose_name = _("客户信息表")
       verbose_name_plural = _("客户信息表")

    # 身份证号
    client_identity_card = models.CharField(primary_key=True, verbose_name=_("身份证号"), max_length=40, default="")

    # 客户姓名
    client_name = models.CharField(verbose_name=_("客户名"), max_length=40, default="")

    # 客户性别的类型
    CLIENT_SEX_CHOICE = (
        ('man', _('男'))
        , ('women', _('女'))
    )

    # 客户性别
    client_sex = models.CharField(choices=CLIENT_SEX_CHOICE, verbose_name=_("客户性别"), max_length=10, default="")

    # 客户手机号
    client_phone_number = models.CharField(verbose_name=_("客户手机号"), max_length=40, unique=True, default="")

    # 客户邮箱
    client_email = models.CharField(verbose_name=_("客户邮箱"), max_length=40, default="")

    # 客户区域的类型
    CLIENT_REGION_CHOICE = (
        ('奥地利', _('AT'))
        , ('中国', _('CN'))
        , ('英国', _('GB'))
        , ('新加坡', _('SG'))
        , ('美国', _('US'))
        , ('委内瑞拉', _('VE'))
    )

    # 客户区域
    client_region = models.CharField(choices=CLIENT_REGION_CHOICE, verbose_name=_("客户区域"), max_length=40,
                                     default="")

    # 客户地址
    client_address = models.CharField(verbose_name=_("客户地址"), max_length=40, default="")

    # 用户号
    client_user_id = models.ForeignKey(to=User, related_name="client_user_id_user", on_delete=models.CASCADE,
                                       verbose_name=_("用户号"), max_length=40, default="")

    def __str__(self):
        return str(self.client_name + " " + str(self.client_phone_number) + " " + str(self.client_address))


# 定义物流公司信息表
class Logistics(models.Model):

    class Meta:
        verbose_name = _("物流公司信息表")
        verbose_name_plural = _("物流公司信息表")

    # 物流公司号
    logistics_id = models.CharField(primary_key=True, verbose_name=_("物流公司号"), max_length=40, default="")

    # 物流公司名
    logistics_name = models.CharField(verbose_name=_("物流公司名"), max_length=40, default="")

    # 联系人
    logistics_person = models.CharField(verbose_name=_("联系人"), max_length=40, default="")

    # 电话号码
    logistics_phone = models.CharField(verbose_name=_("电话号码"), max_length=40, default="")

    # 客户区域的类型
    REGION_CHOICE = (
        ('奥地利', _('AT'))
        , ('中国', _('CN'))
        , ('英国', _('GB'))
        , ('新加坡', _('SG'))
        , ('美国', _('US'))
        , ('委内瑞拉', _('VE'))
    )
    # 所在国家
    logistics_country = models.CharField(choices=REGION_CHOICE, verbose_name=_("所在国家"), max_length=40, default="")

    def __str__(self):
        return str(self.logistics_country) + "  " + str(self.logistics_name)

# 定义购物车情况表单
class ShoppingCart(models.Model):
    # 继承models类

    class Meta:
        verbose_name = _("购物车情况表")
        verbose_name_plural = _("购物车情况表")

    unique_together = (("cart_id", "cart_product"),)

    # 购物车号
    cart_id = models.CharField(verbose_name=_("购物车号"), max_length=40, default="")

    # 用户信息
    cart_user = models.ForeignKey(to=Client, related_name="cart_user_client", verbose_name=_("用户名称"), max_length=40,
                                  on_delete=models.CASCADE, default="")

    # 产品名称
    cart_product = models.ForeignKey(to=ProductInventory, related_name="product_name_product_inventory",
                                     verbose_name=_("商品名称"), on_delete=models.CASCADE, max_length=40, default="")

    # 产品数量
    cart_product_quantity = models.PositiveIntegerField(verbose_name=_("产品数量"))

    # 添加时间
    cart_add_time = models.DateField(auto_now=True, verbose_name=_("添加时间"))

    def __str__(self):
        return str(self.cart_user) + "  " + str(self.cart_product) + "  " + str(self.cart_product_quantity)

# 定义订单信息表单
class Order(models.Model):

    class Meta:
        verbose_name = _("订单信息表")
        verbose_name_plural = _("订单信息表")

    # 订单号
    order_id = models.CharField(primary_key=True, verbose_name=_("订单号"), max_length=40, default="")

    # 订单状态的类型

    ORDER_CONDITION_CHOICE = (
        ('achieved', _('已完成'))
        , ('closed', _('已关闭'))
        , ('be in progress', _('进行中'))
    )

    # 订单状态
    order_condition = models.CharField(choices=ORDER_CONDITION_CHOICE, verbose_name=_("订单状态"), max_length=40, default="")

    # 消费总金额
    order_aggregate_amount = models.FloatField(verbose_name=_("消费总金额"))

    # 下单时间
    order_purchase_time = models.DateTimeField(auto_now=True, verbose_name=_("下单时间"))

    def __str__(self):
        return str(self.order_id)

# 定义物流表单
class Transportation(models.Model):
    class Meta:
        verbose_name = _("物流信息表")
        verbose_name_plural = _("物流信息表")

    # 物流id
    transportation_id = models.CharField(primary_key=True, verbose_name=_("物流号"), max_length=40, default="")

    # 物流公司名称
    transportation_company_name = models.ForeignKey(to=Logistics, related_name="transportation_company_name_Logistics",
                                                    verbose_name=_("物流公司名称"), on_delete=models.CASCADE, max_length=40,
                                                    default="")

    # 邮费
    transportation_fee = models.FloatField(verbose_name=_("邮费"))

    TRANSPORTATION_CONDITION_CHOICE = (
        ('waiting for delivery', _('等待发货'))
        , ('transporting', _('运输中'))
        , ('to be signed', _('待签收'))
        , ('signed', _('已签收'))
    )

    # 物流情况
    transportation_condition = models.CharField(choices=TRANSPORTATION_CONDITION_CHOICE, verbose_name=_("物流情况"),
                                                max_length=40, default="")

    # 订单id
    transportation_order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name=_("订单号"),
                                             related_name="transportation_order_order", max_length=40, default="")

# 定义产品购买信息表
class ProductPurchase(models.Model):
    class Meta:
        verbose_name = _("产品购买信息表")
        verbose_name_plural = _("产品购买信息表")

    unique_together = (("purchase_order_id", "purchase_cart"),)

    # 订单号
    purchase_order_id = models.CharField(verbose_name=_("订单号"), max_length=40, default="")

    # 订单信息
    purchase_cart = models.ForeignKey(to=ShoppingCart, related_name="order_cart_shopping_cart", verbose_name=_("具体信息"),
                                      on_delete=models.CASCADE, max_length=40, default="")

    # 产品总价
    purchase_aggregate_amount = models.FloatField(verbose_name=_("产品总价"))

# 定义订单评价表单
class Rate(models.Model):
    class Meta:
        verbose_name = _("订单评价表")
        verbose_name_plural = _("订单评价表")

    # 评价号
    rate_id = models.CharField(primary_key=True, verbose_name=_("评价号"), max_length=40, default="")

    # 评价星数的类型
    RATE_CHOICE = (
        ('一星评价', _('*'))
        , ('二星评价', _('**'))
        , ('三星评价', _('***'))
        , ('四星评价', _('****'))
        , ('五星评价', _('*****'))
    )

    # 总评价星数
    rate_total = models.CharField(choices=RATE_CHOICE, verbose_name=_("总评价星数"), max_length=40, default="*****")

    # 产品评价星数
    rate_product = models.CharField(choices=RATE_CHOICE, verbose_name=_("产品评价星数"), max_length=40, default="*****")

    # 物流评价星数
    rate_transport = models.CharField(choices=RATE_CHOICE, verbose_name=_("物流评价星数"), max_length=40, default="*****")

    # 评价文案
    rate_content = models.CharField(verbose_name=_("评价文案"), max_length=200, default="")

    # 订单号
    rate_order = models.ForeignKey(to=Order, related_name="rate_order_order", verbose_name=_("订单号"), max_length=40,
                                   on_delete=models.CASCADE, default="")

    RATE_CONDITION_CHOICE = (
        ('cannot evaluate', _('未到货不可评价'))
        , ('no evaluate', _('已到货未评价'))
        , ('have evaluated', _('已评价'))
    )

    # 评价状态
    rate_status = models.CharField(choices=RATE_CONDITION_CHOICE, verbose_name=_("评价状态"), max_length=40, default="")

    # 评价时间
    rate_time = models.DateTimeField(auto_now_add=True, verbose_name=_("评价时间"))

    def __str__(self):
        return str(self.rate_id)

# 定义系统管理员表
class Manager(models.Model):

    class Meta:
        verbose_name = _("系统管理员表")
        verbose_name_plural = _("系统管理员表")

    # 管理员编号
    manager_id = models.CharField(primary_key=True, verbose_name=_("管理员编号"), max_length=40, default="")

    # 管理员姓
    manager_name = models.CharField(verbose_name=_("管理员姓名"), max_length=40, default="")

    # 管理员密码
    manager_pwd = models.CharField(verbose_name=_("管理员密码"), max_length=40, default="")

    def __str__(self):
        return str(self.manager_id) + "  " + str(self.manager_name)

# 定义管理员回复留言表
class ManagerReply(models.Model):

    class Meta:
        verbose_name = _("管理员回复")
        verbose_name_plural = _("管理员回复")

    # 回复编号
    reply_id = models.CharField(primary_key=True, verbose_name=_("回复编号"), max_length=20, default="")

    # 管理员编号
    reply_manager_id = models.ForeignKey(to=Manager, related_name="reply_manager_id_manager", on_delete=models.CASCADE,
                                         verbose_name=_("管理员编号"), max_length=40, default="")

    # 评价号
    reply_rate_id = models.ForeignKey(to=Rate, on_delete=models.CASCADE, verbose_name=_("评价号"),
                                      related_name="reply_rate_id_rate", max_length=40, default="")

    # 回复时间
    reply_time = models.DateTimeField(auto_now_add=True, verbose_name=_("回复时间"))


    # 回复内容
    reply_content = models.CharField(verbose_name=_("回复内容"), max_length=200, default="")