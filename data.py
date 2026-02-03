class URL:
    base_url = "https://www.saucedemo.com/"
    main_url = "https://www.saucedemo.com/inventory.html"


class TestData:
    successful_username = "standard_user"
    password = "secret_sauce"
    wrong_password = '1111111'
    locked_out_user = "locked_out_user"
    performance_glitch_user = "performance_glitch_user"

class ErrorMessages:
    wrong_data_msg = 'Epic sadface: Username and password do not match any user in this service'
    locked_out_user_msg = 'Epic sadface: Sorry, this user has been locked out.'
    username_is_required_msg = 'Epic sadface: Username is required'

class Styles:
    red_border_color = 'rgba(226, 35, 26, 1)'