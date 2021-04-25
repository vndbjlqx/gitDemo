1. 查看log，找到app的包名和应用名
# 打开模拟器，启动需要查看的app
# 让 adb 链接到指定的模拟器：
$ adb connect 127.0.0.1:7555
# 然后查看app的包和应用名
$ adb logcat |grep -i displayed
{企业微信：com.tencent.wework/.launch.WwMainActivity}

---------------------------------------------------------------
2. 开始准备作业
# 手动操作熟悉作业要求的操作过程，记录pageObject和操作。
# plantUML 画时序图，代码建模
课后练习：
    实现添加联系人功能的PO封装
    实现删除联系人功能的PO封装

任务一：实现添加联系人功能的PO封装
1, 主页面 main_page, 点击，通讯录， 转向 通讯录页面 contact_list_page
2, 通讯录页面 contact_list_page, 点击 添加成员 按钮， 转向 添加成员页面 add_friend_page
3, 添加成员页面 add_friend_page, 点击 手动输入添加 按钮，转向 录入成员信息页面 input_friend_info_page
4, 录入成员信息页面 input_friend_info_page,
   录入：姓名，手机号，点击 保存 按钮，转向 添加成员页面 add_friend_page
5, 添加成员页面 add_friend_page, 点击 返回 按钮，返回  通讯录页面 contact_list_page
6, 通讯录页面 contact_list_page, assert 新成员在列表中

任务二：实现删除联系人功能的PO封装
1, 主页面 main_page, 点击，通讯录， 转向 通讯录页面 contact_list_page
2, 通讯录页面 contact_list_page, 点击 搜索 按钮，转向 搜索页面 search_page
3, 搜索页面 search_page 搜索 姓名 ，从列表中选择 用户，转向 个人信息页面 person_info_page
4, 个人信息页面 person_info_page, 点击 编辑， 点击 编辑成员 链接，转向 编辑成员页面 edit_person_info_page
5, 编辑成员页面 edit_person_info_page, (向下滑动页面)点击 删除成员 按钮， 弹出框，点击 确定， 返回 搜索页面 search_page
6, 搜索页面 search_page, 搜索 姓名，assert 没有返回结果

@startuml
participant main_page as "主页面"
participant contact_list_page as "通讯录页面"
participant add_friend_page as "添加成员页面"
participant input_friend_info_page as "录入成员信息页面"
participant search_page as "搜索页面"
participant person_info_page as "个人信息页面"
participant edit_person_info_page as "编辑成员页面"

main_page -> contact_list_page : goto_contact_list_page
contact_list_page -> add_friend_page : goto_add_friend_page
add_friend_page -> input_friend_info_page : goto_manual_add_friend_page
input_friend_info_page --> add_friend_page : save
add_friend_page --> contact_list_page : back
contact_list_page -> contact_list_page : check

contact_list_page -> search_page : search
search_page -> person_info_page : search_and_select_person_by_name
person_info_page -> edit_person_info_page : edit_person_info
edit_person_info_page --> search_page : delete_person
search_page ->  search_page : search_person

@enduml

-----------------------------------------------------------------
3. 设置base_page, app_page，创建driver，以及封装常用方法
# 理解一下：AppPage 是应用的第一步，负责提供driver信息，创建driver，以及提供入口对象MainPage()
# 理解一下：BasePage 才是所有页面的基础，提供通用页面操作方法
(1) 配置好 BasePage，AppPage，尝试运行测试，看看是否能正确打开app
启动 appium server -> 运行
$ adb connect 127.0.0.1:7555
$ adb devices
(2) 开始逐个页面的定义方法，完善BasePage中的公共方法
    定义任务一所需要的方法，并完成测试；
    定义任务二所需要的方法，并完成测试；
        删除时加入滑动点击；

4. 改进
(1)加入fixture改进中文处理
(2)数据文件读取

