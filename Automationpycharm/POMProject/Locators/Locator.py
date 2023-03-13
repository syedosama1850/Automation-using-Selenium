
class pageLocator():

    #Login Page Locators
    username_textbox_name = 'username'
    password_textbox_name = 'password'
    login_btn_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    invalidUsernameXpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]'
    emptyUsernameXpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span'
    emptyPasswordXpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span'
    emptyUsernamePasswordXpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span'

    #HomePage Locators
    dropdown_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i'
    logout_link_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'
    myinfo_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a'

    #myInfo Page Locators
    add_btn_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div/button'
    browse_btn_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[1]/div/div/div/div[2]/input'
    save_btn_Xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[3]/button[2]'
    largefilemessage_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[1]/div/div/div/span'
    emptyfilemessage_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[1]/div/div/div/span'
    maleradio_btn_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
    radio_save_btn_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    smoker_radiobtn_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label/span/i'
    maritalstatus_dropdown_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i'
    marriedstatus_btn_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
