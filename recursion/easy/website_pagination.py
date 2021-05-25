# urls[page-*pagesize]からpagesize分のpageを取り出して返却する
def websitePagination(urls, pageSize, page):
    base = page - 1
    startIndex = base * pageSize
    lastIndex = startIndex + pageSize

    return urls[startIndex:lastIndex]
