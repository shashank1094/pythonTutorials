from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

# Ensure a path, create if necessary
zk.ensure_path("/test_znode/child/grandchild")

@zk.ChildrenWatch("/test_znode/child/")
def watch_children(children):
    print("[WATCHER] Children are now: %s" % children)
# Above function called immediately, and from then on

@zk.DataWatch("/test_znode/child")
def watch_node(data, stat):
    print("[WATCHER] Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

def my_func(event):
    # check to see what the children are now
    print(event)

zk.get("/test_znode/child/grandchild", watch=my_func)
# List the children
children = zk.get_children("/test_znode/child/grandchild", watch=my_func)
print("There are %s children with names %s" % (len(children), children))


if not zk.exists("/test_znode/child/grandchild/1"):
    # Create a node with data
    zk.create("/test_znode/child/grandchild/1", b"this is data 1")

zk.set("/test_znode/child", b"testing watcher")

# Print the version of a node and its data
data, stat = zk.get("/test_znode/child/grandchild/1")
print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

# List the children
children = zk.get_children("/test_znode/child/grandchild", watch=my_func)
print("There are %s children with names %s" % (len(children), children))


zk.set("/test_znode/child/grandchild/1", b"NEW this is somedata",
       # version=1
       )

# Print the version of a node and its data
data, stat = zk.get("/test_znode/child/grandchild/1")
print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))


zk.delete("/test_znode/child/grandchild", recursive=True)

# List the children
children = zk.get_children("/test_znode/child/")
print("There are %s children with names %s" % (len(children), children))

zk.set("/test_znode/child", b"testing watcher AGAIN")

