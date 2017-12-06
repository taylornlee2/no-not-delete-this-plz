def words(essay):
    ans = 0
    if '!' in essay:
        ans = ans + 1
    if '?' in essay:
        ans = ans + 1
    if '.' in essay:
        ans = ans + 1
    print ans 