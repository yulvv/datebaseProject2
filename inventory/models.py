from django.db import models
from django.utils.translation import gettext_lazy as _

# 定义产品库存表单
class Inventory(models.Model):
    # 继承models类

    class Meta:
        verbose_name = _("库存表")
        verbose_name_plural = _("库存表")

    # 产品号（CHAR PRIMARY KEY）√，
    # 产品名称(CHAR NOT NULL)
    # 产品尺码（default标码，也可以有S、M、L）√，
    # 产品库存数量（INT NOT NULL）√×，
    # 产品单价（INT NOT NULL）√，
    # 产品图片（看实现难度），存url，应该可以；×
    # 产品颜色 √，
    # 销售数量 ×
    # Create your models here.

    # 产品名称
    product_name = models.CharField(max_length=40, verbose_name=_("产品名称"), null=False, blank=False)

    # 产品号
    product_id = models.CharField(primary_key=True, verbose_name=_("产品号"),
                                  default="",max_length=40,unique=True)

    # 产品尺码的类型
    PRODUCT_SIZE_CHOICE = (
        ('均码', _('均码'))
        , ('S', _('S'))
        , ('M', _('M'))
        , ('L', _('L'))
    )

    # 产品尺码
    product_size = models.CharField(choices=PRODUCT_SIZE_CHOICE, verbose_name=_("产品尺码"), max_length=40, default="均码",
                                    null=False, blank=False)

    # 产品库存数量
    product_quantity = models.PositiveIntegerField(verbose_name=_("产品库存数量"), null=False)

    # 产品单价
    product_price = models.FloatField(verbose_name=_("产品单价"), null=False)

    # 产品颜色
    product_color = models.CharField(max_length=40, verbose_name=_("产品颜色"), null=False)

# 定义客户表单
class Client(models.Model):
    # 继承models类

    class Meta:
        verbose_name = _("客户单")
        verbose_name_plural = _("客户单")

    # 客户管理（客户号，客户名称，客户手机号，客户区域，客户地址）
    # 客户号（CHAR，PRIMARY KEY),√
    # 客户性别(CHAR)，√
    # 客户姓名(CHAR NOT NULL)，√
    # 客户手机号(CHAR NOT NULL)，√
    # 客户邮箱(CHAR)，√
    # 客户区域(CHAR NOT NULL)，（如表中所示，直接分为几个地区(例如中国的东北、华东华南，或者七大洲)，分别对应不同的物流公司） √
    # 客户地址(CHAR NOT NULL)；√

    # 客户名
    client_name = models.CharField(max_length=40, verbose_name=_("客户名"), null=False, blank=False)

    # 客户号
    client_id = models.CharField(primary_key=True, verbose_name=_("客户号"),
                                 default="", max_length=40, unique=True)

    # 客户性别的类型
    CLIENT_SEX_CHOICE = (
        ('man', _('男'))
        , ('women', _('女'))
    )

    # 客户性别
    client_sex = models.CharField(choices=CLIENT_SEX_CHOICE, max_length=127, default="",
                                  verbose_name=_("客户性别"))

    # 客户手机号
    client_phone_number = models.CharField(max_length=40, verbose_name=_("客户手机号"),
                                           null=False, blank=False)

    # 客户邮箱
    client_email = models.CharField(max_length=40, verbose_name=_("客户邮箱"), default="")

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
    client_region = models.CharField(choices=CLIENT_REGION_CHOICE, max_length=127, default="",
                                     verbose_name=_("客户区域"))

    # 客户地址
    client_address = models.CharField(max_length=40, verbose_name=_("客户地址"), null=False, blank=False)

# 定义订单表单
class Order(models.Model):
    # 继承models类

    class Meta:
        verbose_name = _("订单表")
        verbose_name_plural = _("订单表")

    # 订单号（CHAR，PRIMARY KEY)，√
    # 产品号（CHAR, Foreign KEY），√
    # 品牌号（CHAR, Foreign KEY），√
    # 运输号（CHAR, Foreign KEY），√
    # 评价号（CHAR, Foreign KEY），√
    # 客户号（CHAR, Foreign KEY），√
    # 订单状态（成功，　关闭，　进行中）（感觉这个跟物流约束有配合关系）√
    # 产品数量（INT NOT NULL），（限制其小于库存）√
    # 消费总金额（INT NOT NULL），（其等于单价和数量之积）√
    # 下单时间（自动读取当前时间）；×

    # 订单号
    order_id = models.CharField(primary_key=True, verbose_name=_("订单号"),
                                default="", max_length=40)

    # 产品号
    order_product_id = models.CharField(verbose_name=_("产品号"), max_length=40)

    # 品牌号
    order_brand_id = models.CharField(verbose_name=_("品牌号"), max_length=40)

    # 运输号
    order_transport_id = models.CharField(verbose_name=_("运输号"), max_length=40)

    # 评价号
    order_evaluate_id = models.CharField(verbose_name=_("评价号"), max_length=40)

    # 客户号
    order_client_id = models.CharField(verbose_name=_("客户号"), max_length=40)


    # 订单状态的类型

    ORDER_CONDITION_CHOICE = (
        ('achieved', _('已完成'))
        , ('closed', _('已关闭'))
        , ('be in progress', _('进行中'))
    )

    # 订单状态
    order_condition = models.CharField(choices=ORDER_CONDITION_CHOICE, max_length=127, default="",
                                       verbose_name=_("订单状态"))

    # 购买数量
    order_purchase_quantity = models.PositiveIntegerField(verbose_name=_("购买数量"), null=False)

    # 消费总金额
    order_aggregate_amount = models.FloatField(verbose_name=_("消费总金额"), null=False)

    # 下单时间

# 定义物流表单
class Distribution(models.Model):
    # 继承models类

    class Meta:
        verbose_name = _("物流表")
        verbose_name_plural = _("物流表")

    # 物流号（CHAR，PRIMARY KEY NOT NULL)， √
    # 物流公司名称(CHAR NOT NULL)， √
    # 物流区域(CHAR NOT NULL)，×
    # 邮费 √
    # 物流情况(CHAR NOT NULL)；（限制几种情况，如等待发货、运输中、待签收、已签收） √
    # 订单号（外键） √

    # 物流id
    distribution_id = models.CharField(primary_key=True, verbose_name=_("物流号"),
                                       default="", max_length=40)

    # 物流公司名称
    distribution_company_name = models.CharField(max_length=40, verbose_name=_("物流公司名称"),
                                                 null=False, blank=False)

    # 物流区域

    # 邮费
    distribution_fee = models.FloatField(verbose_name=_("邮费"), null=False)

    DISTRIBUTION_CONDITION_CHOICE = (
        ('waiting for delivery', _('等待发货'))
        , ('transporting', _('运输中'))
        , ('to be signed', _('待签收'))
        , ('signed', _('已签收'))
    )

    # 物流情况
    distribution_condition = models.CharField(choices=DISTRIBUTION_CONDITION_CHOICE, max_length=127,
                                              default="", verbose_name=_("物流情况"))

    # 订单id
    distribution_order_id = models.CharField(verbose_name=_("订单号"),default="", max_length=40, null=False)

# 定义评价表单
class Evaluation(models.Model):
    # 继承models类

    class Meta:
        verbose_name = _("评价表")
        verbose_name_plural = _("评价表")

    # 评价号（CHAR，PRIMARY KEY)，
    # 总评价星数（INT，1-5），
    # 产品评价星数（INT，1-5），
    # 物流评价星数（INT，1-5），
    # 评价文案(CHAR)，
    # 评价图片（看实现的难度），×
    # 订单号（外键）
    # 产品号（外键）×
    # 客户号（外键）×
    # 评价状态（未到货不可评价，已到货未评价，已评价）；

    # 评价号
    evaluation_id = models.CharField(primary_key=True, verbose_name=_("评价号"),
                                     default="", max_length=40)

    # 评价星数的类型
    EVALUATION_CHOICE = (
        ('一星评价', _('*'))
        , ('二星评价', _('**'))
        , ('三星评价', _('***'))
        , ('四星评价', _('****'))
        , ('五星评价', _('*****'))
    )

    # 总评价星数
    evaluation_sum = models.CharField(choices=EVALUATION_CHOICE, max_length=127,
                                      default="", verbose_name=_("总评价星数"))


    # 产品评价星数
    evaluation_product = models.CharField(choices=EVALUATION_CHOICE, max_length=127,
                                          default="", verbose_name=_("产品评价星数"))

    # 物流评价星数
    evaluation_distribution = models.CharField(choices=EVALUATION_CHOICE, max_length=127,
                                               default="", verbose_name=_("物流评价星数"))

    # 评价文案
    evaluation_description = models.CharField(max_length=40, verbose_name=_("评价文案"), default="")

    # 订单号
    evaluation_order_id = models.CharField(max_length=40, verbose_name=_("订单号"), default="")

    EVALUATION_CONDITION_CHOICE = (
        ('cannot evaluate', _('未到货不可评价'))
        , ('no evaluate', _('已到货未评价'))
        , ('have evaluated', _('已评价'))
    )

    evaluation_condition = models.CharField(choices=EVALUATION_CONDITION_CHOICE, max_length=127,
                                            default="", verbose_name=_("评价状态"))
# 定义入驻品牌表单
class Brand(models.Model):
    # 继承models类

    class Meta:
        verbose_name = _("入驻品牌表")
        verbose_name_plural = _("入驻品牌表")

    # 品牌号（CHAR，PRIMARY KEY)，
    # 品牌名称（CHAR，UNIQUE NOT NULL)，
    # 品牌等级（CHAR，NOT NULL);

    # 品牌号
    brand_id = models.CharField(primary_key=True, verbose_name=_("品牌号"), default="", max_length=40)

    brand_name = models.CharField(verbose_name=_("品牌名称"), default="", max_length=40, null=False)

    brand_grade = models.CharField(verbose_name=_("品牌等级"), default="", max_length=40,
                                   null=False)