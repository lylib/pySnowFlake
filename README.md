## goSnowFlake

A threadsafe unique ID generator inspired by Twitter SnowFlake theory

Feature
--------

* ThreadSafe unique id generator
* Green pluggable, without external storage like Redis or MySQL
* Suitable for distributed systems
* Implement Twitter's SnowFlake theory


Description
-----------

```
+---------------+----------------+----------------+
|timestamp(ms)42  | worker id(10) | sequence(12)  |
+---------------+----------------+----------------+

id  = timestamp | workerid | sequence (eg. 781910964961284113)

```

An unique ID contains 3 parts:

* a timestamp in nanosecond
* a worker ID
* a sequence number


Example
-------

```go
import pySnowFlake

iw = pySnowFlake.IdWorker(1)
for i in range(10):
    print(iw.NextId())

```

Documentation
-------------

- [Twitter Blog Reference](https://blog.twitter.com/2010/announcing-snowflake)
- [Reddit Discuss](https://www.reddit.com/comments/cajap/twitter_announces_snowflake_a_distributed_unique/)

License
-------

Copyright (c) 2022 by yu-liang released under MIT License.

