# Valid data
VALID_FIRSTNAME = "zoo"
VALID_LASTNAME  = "zee"
VALID_ZIPCODE   = "9526"

# Invalid data for parametrize
# Each tuple: (firstname, lastname, zipcode, expected_error)
INVALID_CHECKOUT_DATA = [
    (
        "",
        "zee",
        "9526",
        "Error: First Name is required"
    ),
    (
        "zoo",
        "",
        "9526",
        "Error: Last Name is required"
    ),
    (
        "zoo",
        "zee",
        "",
        "Error: Postal Code is required"
    ),
    (
        "",
        "",
        "",
        "Error: First Name is required"
    ),
]