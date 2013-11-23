Overkill-notify
===============

This tiny package contains a Notify mix-in class and that's it. It's in a
separate package so it can be used by multiple sinks (although, as of writing
this, it is inly used by Overkill-mail).

Using
-----

```python
class MySink(SimpleSink, Notify):
    summary = "New Mail"
    subscription = "my_source_sub"

    def handle_update(self, update):
        self.summary = "Some Title"
        self.message = "Some update: %s" % update
        self.show()
```


