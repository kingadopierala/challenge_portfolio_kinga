from pages.base_page import BasePage


class Dashboard(BasePage)

    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"
    youtube_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[19]/button/span[1]"
    add_language_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[15]/button/span[1]"
    name_form_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    surname_form_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    age_form_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    main_position_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    leg_xpath = "//*[@id="mui-component-select-leg"]"
    district_xpath = "//*[@id="mui-component-select-district"]"

    pass