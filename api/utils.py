def check_request_has_required_parameters(request_data, parameter_list):
    """
    Function accept the data in api request and required parameter
    to return if any of the parameter is not in the request data/parameter.
    """

    missing_parameters = list()
    for parameter in parameter_list:
        if parameter not in request_data:
            missing_parameters.append(parameter)

    return missing_parameters
