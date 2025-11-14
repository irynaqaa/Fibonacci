*** Keywords ***
Login
    Input Text    username_field    demo_user
    Input Text    password_field    password123
    Click Button    login_button

Create Product
    Input Text    product_name_field    Test Product
    Input Text    product_description_field    This is a test product
    Click Button    create_product_button