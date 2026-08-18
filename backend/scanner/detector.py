import re


def find_url_variables(code):
    """Find variables that contain API URLs."""

    variables = {}

    pattern = re.compile(
        r'\b([A-Za-z_][A-Za-z0-9_]*)\s*=\s*["\'](https?://[^"\']+)["\']'
    )

    for match in pattern.finditer(code):
        variable_name = match.group(1)
        url = match.group(2)

        variables[variable_name] = url

    return variables


def extract_body_fields(text):
    """Find simple request-body fields such as amount or name."""

    fields = []

    # Remove URLs so "https:" is not detected as a field.
    cleaned_text = re.sub(
        r'https?://[^\s"\']+',
        '',
        text
    )

    pattern = re.compile(
        r'["\']?([A-Za-z_][A-Za-z0-9_]*)["\']?\s*:'
    )

    for match in pattern.finditer(cleaned_text):

        field = match.group(1)

        if field not in fields:
            fields.append(field)

    return fields


def extract_query_parameters(text):
    """Find parameters inside params={...}."""

    fields = []

    params_match = re.search(
        r'params\s*=\s*\{(.*?)\}',
        text,
        re.DOTALL | re.IGNORECASE
    )

    if params_match:

        fields = extract_body_fields(
            params_match.group(1)
        )

    return fields


def detect_api_calls(code):

    results = []

    # =================================================
    # Find URL variables
    # =================================================

    url_variables = find_url_variables(code)

    # =================================================
    # PYTHON REQUESTS
    # =================================================

    requests_pattern = re.compile(
        r'requests\.(get|post|put|patch|delete)'
        r'\s*\((.*?)\)',
        re.IGNORECASE | re.DOTALL
    )

    for match in requests_pattern.finditer(code):

        method = match.group(1).upper()
        content = match.group(2)

        url = None

        # Direct URL
        url_match = re.search(
            r'["\'](https?://[^"\']+)["\']',
            content
        )

        if url_match:

            url = url_match.group(1)

        # URL variable
        if not url:

            variable_match = re.search(
                r'\b([A-Za-z_][A-Za-z0-9_]*)\b',
                content
            )

            if variable_match:

                variable_name = variable_match.group(1)

                url = url_variables.get(
                    variable_name
                )

        if url:

            line_number = (
                code[:match.start()].count("\n") + 1
            )

            parameters = extract_query_parameters(
                content
            )

            results.append({
                "method": method,
                "url": url,
                "line": line_number,
                "type": "REST_API",
                "parameters": parameters,
                "body": []
            })

    # =================================================
    # JAVASCRIPT FETCH
    # =================================================

    fetch_pattern = re.compile(
        r'fetch\s*\((.*?)\)',
        re.IGNORECASE | re.DOTALL
    )

    for match in fetch_pattern.finditer(code):

        content = match.group(1)

        url = None

        # Direct URL
        url_match = re.search(
            r'["\'](https?://[^"\']+)["\']',
            content
        )

        if url_match:

            url = url_match.group(1)

        # URL variable
        if not url:

            variable_match = re.search(
                r'\b([A-Za-z_][A-Za-z0-9_]*)\b',
                content
            )

            if variable_match:

                variable_name = variable_match.group(1)

                url = url_variables.get(
                    variable_name
                )

        if url:

            line_number = (
                code[:match.start()].count("\n") + 1
            )

            results.append({
                "method": "GET",
                "url": url,
                "line": line_number,
                "type": "REST_API",
                "parameters": [],
                "body": []
            })

    # =================================================
    # AXIOS
    # =================================================

    axios_pattern = re.compile(
        r'axios\.(get|post|put|patch|delete)'
        r'\s*\((.*?)\)',
        re.IGNORECASE | re.DOTALL
    )

    for match in axios_pattern.finditer(code):

        method = match.group(1).upper()
        content = match.group(2)

        url = None

        # Direct URL
        url_match = re.search(
            r'["\'](https?://[^"\']+)["\']',
            content
        )

        if url_match:

            url = url_match.group(1)

        # URL variable
        if not url:

            variable_match = re.search(
                r'\b([A-Za-z_][A-Za-z0-9_]*)\b',
                content
            )

            if variable_match:

                variable_name = variable_match.group(1)

                url = url_variables.get(
                    variable_name
                )

        if url:

            line_number = (
                code[:match.start()].count("\n") + 1
            )

            body = []

            # POST, PUT and PATCH can contain request bodies.
            if method in {"POST", "PUT", "PATCH"}:

                body = extract_body_fields(
                    content
                )

            results.append({
                "method": method,
                "url": url,
                "line": line_number,
                "type": "REST_API",
                "parameters": [],
                "body": body
            })

    return results