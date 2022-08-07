http_status = 501

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad Request")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown")