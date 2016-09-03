python工程

com.wt.practice 练习目录
com.wt.workdlow alfred-workflow目录

遗留问题：
1、workflow中引入模块目录
from workflow import Workflow, ICON_WEB, web
必须改写成
import web
from workflow import Workflow, ICON_WEB
否则eclipse会报错



