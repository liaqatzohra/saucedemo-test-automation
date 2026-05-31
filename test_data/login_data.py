# Valid credentials
VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"

# Invalid credentials test data
# Each tuple contains: (username, password, expected_error_message)
INVALID_LOGIN_DATA = [

    # Wrong password
    (
        "standard_user",
        "wrong_password",
        "Epic sadface"
    ),

    # Wrong username
    (
        "wrong_username",
        "secret_sauce",
        "Epic sadface"
    ),

    # Empty username
    (
        "",
        "secret_sauce",
        "Username is required"
    ),

    # Empty password
    (
        "standard_user",
        "",
        "Password is required"
    ),

    # Both empty
    (
        "",
        "",
        "Username is required"
    ),

    # Locked out user
    (
        "locked_out_user",
        "secret_sauce",
        "locked out"
    ),
]