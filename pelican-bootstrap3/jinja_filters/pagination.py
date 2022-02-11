from math import floor

#
# Based on https://github.com/dyve/django-bootstrap3
#

def pagination(page, action):
    pages_to_show = page.settings.get('PAGINATION_BOOTSTRAP3_PAGES_TO_SHOW', 11)
    num_pages = page.paginator.num_pages
    current_page = page.number

    half_page_num = int(floor(pages_to_show / 2))
    if half_page_num < 0:
        half_page_num = 0
    first_page = current_page - half_page_num
    if first_page <= 1:
        first_page = 1
    if first_page > 1:
        pages_back = first_page - half_page_num
        if pages_back < 1:
            pages_back = 1
    else:
        pages_back = None
    last_page = first_page + pages_to_show - 1
    if pages_back is None:
        last_page += 1
    if last_page > num_pages:
        last_page = num_pages
    if last_page < num_pages:
        pages_forward = last_page + half_page_num
        if pages_forward > num_pages:
            pages_forward = num_pages
    else:
        pages_forward = None
        if first_page > 1:
            first_page -= 1
        if pages_back is not None and pages_back > 1:
            pages_back -= 1
        else:
            pages_back = None
    pages_shown = []
    for i in range(first_page, last_page + 1):
        pages_shown.append(i)

    if action == 'pages_back':
        return pages_back
    if action == 'pages_forward':
        return pages_forward
    if action == 'first_page':
        return first_page
    if action == 'last_page':
        return last_page
    if action == 'pages_shown':
        return pages_shown
