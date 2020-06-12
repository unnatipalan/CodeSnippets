route = {'id': 271, 'title': 'Fast Apps'}
query = {'id': 1, 'render_fast': True}
post = {'email': 'hello@email.com','name':'Jeff'}

print('Individual Dictionaries: ')
print(f'route: {route}')
print(f'query: {query}')
print(f'post: {post}')

# Non pythonic procedural way
m1 = {}
for k in query:
    m1[k] = query[k]
for k in route:
    m1[k] = route[k]
for k in post:
    m1[k] = post[k]

print(f'm1: {m1}')

# Classic Pythonic way
m2 = query.copy()
m2.update(post)
m2.update(route)

print(f'm2 :{m2}')

# Use dictionary comprehensions

m3 = {k: v for d in [query, post, route] for k, v in d.items() }

print(f'm3 : {m3}')

# Pythonic 3.5
m4 = {**query,**post,**route}
print(f'm4 :{m4}')
