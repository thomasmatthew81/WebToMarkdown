# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:33.

## Converted Web Pages

### Channels | LangChain Reference

**Source:** https://reference.langchain.com/python/langgraph/channels/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langgraph/channels.md "Edit this page")

# Channels

##  `` langgraph.channels.base ¶

###  `` BaseChannel ¶

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "<code>typing.Generic</code>")[Value, Update, Checkpoint]`, `[ABC](https://docs.python.org/3/library/abc.html#abc.ABC "<code>abc.ABC</code>")`

Base class for all channels.

METHOD | DESCRIPTION  
---|---  
`copy` |  Return a copy of the channel.  
`checkpoint` |  Return a serializable representation of the channel's current state.  
`from_checkpoint` |  Return a new identical channel, optionally initialized from a checkpoint.  
`get` |  Return the current value of the channel.  
`is_available` |  Return `True` if the channel is available (not empty), `False` otherwise.  
`update` |  Update the channel's value with the given sequence of updates.  
`consume` |  Notify the channel that a subscribed task ran. By default, no-op.  
`finish` |  Notify the channel that the Pregel run is finishing. By default, no-op.  
  
####  `` ValueType `abstractmethod` `property` ¶
    
    
    ValueType: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

The type of the value stored in the channel.

####  `` UpdateType `abstractmethod` `property` ¶
    
    
    UpdateType: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

The type of the update received by the channel.

####  `` copy ¶
    
    
    copy() -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a copy of the channel. By default, delegates to `checkpoint()` and `from_checkpoint()`. Subclasses can override this method with a more efficient implementation.

####  `` checkpoint ¶
    
    
    checkpoint() -> Checkpoint | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Return a serializable representation of the channel's current state. Raises `EmptyChannelError` if the channel is empty (never updated yet), or doesn't support checkpoints.

####  `` from_checkpoint `abstractmethod` ¶
    
    
    from_checkpoint(checkpoint: Checkpoint | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a new identical channel, optionally initialized from a checkpoint. If the checkpoint contains complex data structures, they should be copied.

####  `` get `abstractmethod` ¶
    
    
    get() -> Value
    

Return the current value of the channel.

Raises `EmptyChannelError` if the channel is empty (never updated yet).

####  `` is_available ¶
    
    
    is_available() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Return `True` if the channel is available (not empty), `False` otherwise. Subclasses should override this method to provide a more efficient implementation than calling `get()` and catching `EmptyChannelError`.

####  `` update `abstractmethod` ¶
    
    
    update(values: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Update]) -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Update the channel's value with the given sequence of updates. The order of the updates in the sequence is arbitrary. This method is called by Pregel for all channels at the end of each step. If there are no updates, it is called with an empty sequence. Raises `InvalidUpdateError` if the sequence of updates is invalid. Returns `True` if the channel was updated, `False` otherwise.

####  `` consume ¶
    
    
    consume() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Notify the channel that a subscribed task ran. By default, no-op. A channel can use this method to modify its state, preventing the value from being consumed again.

Returns `True` if the channel was updated, `False` otherwise.

####  `` finish ¶
    
    
    finish() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Notify the channel that the Pregel run is finishing. By default, no-op. A channel can use this method to modify its state, preventing finish.

Returns `True` if the channel was updated, `False` otherwise.

##  `` langgraph.channels ¶

###  `` Topic ¶

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "<code>typing.Generic</code>")[Value]`, `BaseChannel[[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Value], Value | [list](https://docs.python.org/3/library/stdtypes.html#list)[Value], [list](https://docs.python.org/3/library/stdtypes.html#list)[Value]]`

A configurable PubSub Topic.

PARAMETER | DESCRIPTION  
---|---  
`typ` |  The type of the value stored in the channel. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[Value]`  
`accumulate` |  Whether to accumulate values across steps. If `False`, the channel will be emptied after each step. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
METHOD | DESCRIPTION  
---|---  
`consume` |  Notify the channel that a subscribed task ran. By default, no-op.  
`finish` |  Notify the channel that the Pregel run is finishing. By default, no-op.  
`copy` |  Return a copy of the channel.  
`checkpoint` |  Return a serializable representation of the channel's current state.  
`from_checkpoint` |  Return a new identical channel, optionally initialized from a checkpoint.  
`update` |  Update the channel's value with the given sequence of updates.  
`get` |  Return the current value of the channel.  
`is_available` |  Return `True` if the channel is available (not empty), `False` otherwise.  
  
####  `` ValueType `property` ¶
    
    
    ValueType: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

The type of the value stored in the channel.

####  `` UpdateType `property` ¶
    
    
    UpdateType: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

The type of the update received by the channel.

####  `` consume ¶
    
    
    consume() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Notify the channel that a subscribed task ran. By default, no-op. A channel can use this method to modify its state, preventing the value from being consumed again.

Returns `True` if the channel was updated, `False` otherwise.

####  `` finish ¶
    
    
    finish() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Notify the channel that the Pregel run is finishing. By default, no-op. A channel can use this method to modify its state, preventing finish.

Returns `True` if the channel was updated, `False` otherwise.

####  `` copy ¶
    
    
    copy() -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a copy of the channel.

####  `` checkpoint ¶
    
    
    checkpoint() -> [list](https://docs.python.org/3/library/stdtypes.html#list)[Value]
    

Return a serializable representation of the channel's current state. Raises `EmptyChannelError` if the channel is empty (never updated yet), or doesn't support checkpoints.

####  `` from_checkpoint ¶
    
    
    from_checkpoint(checkpoint: [list](https://docs.python.org/3/library/stdtypes.html#list)[Value]) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a new identical channel, optionally initialized from a checkpoint. If the checkpoint contains complex data structures, they should be copied.

####  `` update ¶
    
    
    update(values: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Value | [list](https://docs.python.org/3/library/stdtypes.html#list)[Value]]) -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Update the channel's value with the given sequence of updates. The order of the updates in the sequence is arbitrary. This method is called by Pregel for all channels at the end of each step. If there are no updates, it is called with an empty sequence. Raises `InvalidUpdateError` if the sequence of updates is invalid. Returns `True` if the channel was updated, `False` otherwise.

####  `` get ¶
    
    
    get() -> [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Value]
    

Return the current value of the channel.

Raises `EmptyChannelError` if the channel is empty (never updated yet).

####  `` is_available ¶
    
    
    is_available() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Return `True` if the channel is available (not empty), `False` otherwise. Subclasses should override this method to provide a more efficient implementation than calling `get()` and catching `EmptyChannelError`.

###  `` LastValue ¶

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "<code>typing.Generic</code>")[Value]`, `BaseChannel[Value, Value, Value]`

Stores the last value received, can receive at most one value per step.

METHOD | DESCRIPTION  
---|---  
`consume` |  Notify the channel that a subscribed task ran. By default, no-op.  
`finish` |  Notify the channel that the Pregel run is finishing. By default, no-op.  
`copy` |  Return a copy of the channel.  
`from_checkpoint` |  Return a new identical channel, optionally initialized from a checkpoint.  
`update` |  Update the channel's value with the given sequence of updates.  
`get` |  Return the current value of the channel.  
`is_available` |  Return `True` if the channel is available (not empty), `False` otherwise.  
`checkpoint` |  Return a serializable representation of the channel's current state.  
  
####  `` ValueType `property` ¶
    
    
    ValueType: [type](https://docs.python.org/3/library/functions.html#type)[Value]
    

The type of the value stored in the channel.

####  `` UpdateType `property` ¶
    
    
    UpdateType: [type](https://docs.python.org/3/library/functions.html#type)[Value]
    

The type of the update received by the channel.

####  `` consume ¶
    
    
    consume() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Notify the channel that a subscribed task ran. By default, no-op. A channel can use this method to modify its state, preventing the value from being consumed again.

Returns `True` if the channel was updated, `False` otherwise.

####  `` finish ¶
    
    
    finish() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Notify the channel that the Pregel run is finishing. By default, no-op. A channel can use this method to modify its state, preventing finish.

Returns `True` if the channel was updated, `False` otherwise.

####  `` copy ¶
    
    
    copy() -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a copy of the channel.

####  `` from_checkpoint ¶
    
    
    from_checkpoint(checkpoint: Value) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a new identical channel, optionally initialized from a checkpoint. If the checkpoint contains complex data structures, they should be copied.

####  `` update ¶
    
    
    update(values: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Value]) -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Update the channel's value with the given sequence of updates. The order of the updates in the sequence is arbitrary. This method is called by Pregel for all channels at the end of each step. If there are no updates, it is called with an empty sequence. Raises `InvalidUpdateError` if the sequence of updates is invalid. Returns `True` if the channel was updated, `False` otherwise.

####  `` get ¶
    
    
    get() -> Value
    

Return the current value of the channel.

Raises `EmptyChannelError` if the channel is empty (never updated yet).

####  `` is_available ¶
    
    
    is_available() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Return `True` if the channel is available (not empty), `False` otherwise. Subclasses should override this method to provide a more efficient implementation than calling `get()` and catching `EmptyChannelError`.

####  `` checkpoint ¶
    
    
    checkpoint() -> Value
    

Return a serializable representation of the channel's current state. Raises `EmptyChannelError` if the channel is empty (never updated yet), or doesn't support checkpoints.

###  `` EphemeralValue ¶

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "<code>typing.Generic</code>")[Value]`, `BaseChannel[Value, Value, Value]`

Stores the value received in the step immediately preceding, clears after.

METHOD | DESCRIPTION  
---|---  
`consume` |  Notify the channel that a subscribed task ran. By default, no-op.  
`finish` |  Notify the channel that the Pregel run is finishing. By default, no-op.  
`copy` |  Return a copy of the channel.  
`from_checkpoint` |  Return a new identical channel, optionally initialized from a checkpoint.  
`update` |  Update the channel's value with the given sequence of updates.  
`get` |  Return the current value of the channel.  
`is_available` |  Return `True` if the channel is available (not empty), `False` otherwise.  
`checkpoint` |  Return a serializable representation of the channel's current state.  
  
####  `` ValueType `property` ¶
    
    
    ValueType: [type](https://docs.python.org/3/library/functions.html#type)[Value]
    

The type of the value stored in the channel.

####  `` UpdateType `property` ¶
    
    
    UpdateType: [type](https://docs.python.org/3/library/functions.html#type)[Value]
    

The type of the update received by the channel.

####  `` consume ¶
    
    
    consume() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Notify the channel that a subscribed task ran. By default, no-op. A channel can use this method to modify its state, preventing the value from being consumed again.

Returns `True` if the channel was updated, `False` otherwise.

####  `` finish ¶
    
    
    finish() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Notify the channel that the Pregel run is finishing. By default, no-op. A channel can use this method to modify its state, preventing finish.

Returns `True` if the channel was updated, `False` otherwise.

####  `` copy ¶
    
    
    copy() -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a copy of the channel.

####  `` from_checkpoint ¶
    
    
    from_checkpoint(checkpoint: Value) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a new identical channel, optionally initialized from a checkpoint. If the checkpoint contains complex data structures, they should be copied.

####  `` update ¶
    
    
    update(values: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Value]) -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Update the channel's value with the given sequence of updates. The order of the updates in the sequence is arbitrary. This method is called by Pregel for all channels at the end of each step. If there are no updates, it is called with an empty sequence. Raises `InvalidUpdateError` if the sequence of updates is invalid. Returns `True` if the channel was updated, `False` otherwise.

####  `` get ¶
    
    
    get() -> Value
    

Return the current value of the channel.

Raises `EmptyChannelError` if the channel is empty (never updated yet).

####  `` is_available ¶
    
    
    is_available() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Return `True` if the channel is available (not empty), `False` otherwise. Subclasses should override this method to provide a more efficient implementation than calling `get()` and catching `EmptyChannelError`.

####  `` checkpoint ¶
    
    
    checkpoint() -> Value
    

Return a serializable representation of the channel's current state. Raises `EmptyChannelError` if the channel is empty (never updated yet), or doesn't support checkpoints.

###  `` BinaryOperatorAggregate ¶

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "<code>typing.Generic</code>")[Value]`, `BaseChannel[Value, Value, Value]`

Stores the result of applying a binary operator to the current value and each new value.
    
    
    import operator
    
    total = Channels.BinaryOperatorAggregate(int, operator.add)
    

METHOD | DESCRIPTION  
---|---  
`consume` |  Notify the channel that a subscribed task ran. By default, no-op.  
`finish` |  Notify the channel that the Pregel run is finishing. By default, no-op.  
`copy` |  Return a copy of the channel.  
`from_checkpoint` |  Return a new identical channel, optionally initialized from a checkpoint.  
`update` |  Update the channel's value with the given sequence of updates.  
`get` |  Return the current value of the channel.  
`is_available` |  Return `True` if the channel is available (not empty), `False` otherwise.  
`checkpoint` |  Return a serializable representation of the channel's current state.  
  
####  `` ValueType `property` ¶
    
    
    ValueType: [type](https://docs.python.org/3/library/functions.html#type)[Value]
    

The type of the value stored in the channel.

####  `` UpdateType `property` ¶
    
    
    UpdateType: [type](https://docs.python.org/3/library/functions.html#type)[Value]
    

The type of the update received by the channel.

####  `` consume ¶
    
    
    consume() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Notify the channel that a subscribed task ran. By default, no-op. A channel can use this method to modify its state, preventing the value from being consumed again.

Returns `True` if the channel was updated, `False` otherwise.

####  `` finish ¶
    
    
    finish() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Notify the channel that the Pregel run is finishing. By default, no-op. A channel can use this method to modify its state, preventing finish.

Returns `True` if the channel was updated, `False` otherwise.

####  `` copy ¶
    
    
    copy() -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a copy of the channel.

####  `` from_checkpoint ¶
    
    
    from_checkpoint(checkpoint: Value) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a new identical channel, optionally initialized from a checkpoint. If the checkpoint contains complex data structures, they should be copied.

####  `` update ¶
    
    
    update(values: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Value]) -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Update the channel's value with the given sequence of updates. The order of the updates in the sequence is arbitrary. This method is called by Pregel for all channels at the end of each step. If there are no updates, it is called with an empty sequence. Raises `InvalidUpdateError` if the sequence of updates is invalid. Returns `True` if the channel was updated, `False` otherwise.

####  `` get ¶
    
    
    get() -> Value
    

Return the current value of the channel.

Raises `EmptyChannelError` if the channel is empty (never updated yet).

####  `` is_available ¶
    
    
    is_available() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Return `True` if the channel is available (not empty), `False` otherwise. Subclasses should override this method to provide a more efficient implementation than calling `get()` and catching `EmptyChannelError`.

####  `` checkpoint ¶
    
    
    checkpoint() -> Value
    

Return a serializable representation of the channel's current state. Raises `EmptyChannelError` if the channel is empty (never updated yet), or doesn't support checkpoints.

###  `` AnyValue ¶

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "<code>typing.Generic</code>")[Value]`, `BaseChannel[Value, Value, Value]`

Stores the last value received, assumes that if multiple values are received, they are all equal.

METHOD | DESCRIPTION  
---|---  
`consume` |  Notify the channel that a subscribed task ran. By default, no-op.  
`finish` |  Notify the channel that the Pregel run is finishing. By default, no-op.  
`copy` |  Return a copy of the channel.  
`from_checkpoint` |  Return a new identical channel, optionally initialized from a checkpoint.  
`update` |  Update the channel's value with the given sequence of updates.  
`get` |  Return the current value of the channel.  
`is_available` |  Return `True` if the channel is available (not empty), `False` otherwise.  
`checkpoint` |  Return a serializable representation of the channel's current state.  
  
####  `` ValueType `property` ¶
    
    
    ValueType: [type](https://docs.python.org/3/library/functions.html#type)[Value]
    

The type of the value stored in the channel.

####  `` UpdateType `property` ¶
    
    
    UpdateType: [type](https://docs.python.org/3/library/functions.html#type)[Value]
    

The type of the update received by the channel.

####  `` consume ¶
    
    
    consume() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Notify the channel that a subscribed task ran. By default, no-op. A channel can use this method to modify its state, preventing the value from being consumed again.

Returns `True` if the channel was updated, `False` otherwise.

####  `` finish ¶
    
    
    finish() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Notify the channel that the Pregel run is finishing. By default, no-op. A channel can use this method to modify its state, preventing finish.

Returns `True` if the channel was updated, `False` otherwise.

####  `` copy ¶
    
    
    copy() -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a copy of the channel.

####  `` from_checkpoint ¶
    
    
    from_checkpoint(checkpoint: Value) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a new identical channel, optionally initialized from a checkpoint. If the checkpoint contains complex data structures, they should be copied.

####  `` update ¶
    
    
    update(values: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Value]) -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Update the channel's value with the given sequence of updates. The order of the updates in the sequence is arbitrary. This method is called by Pregel for all channels at the end of each step. If there are no updates, it is called with an empty sequence. Raises `InvalidUpdateError` if the sequence of updates is invalid. Returns `True` if the channel was updated, `False` otherwise.

####  `` get ¶
    
    
    get() -> Value
    

Return the current value of the channel.

Raises `EmptyChannelError` if the channel is empty (never updated yet).

####  `` is_available ¶
    
    
    is_available() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Return `True` if the channel is available (not empty), `False` otherwise. Subclasses should override this method to provide a more efficient implementation than calling `get()` and catching `EmptyChannelError`.

####  `` checkpoint ¶
    
    
    checkpoint() -> Value
    

Return a serializable representation of the channel's current state. Raises `EmptyChannelError` if the channel is empty (never updated yet), or doesn't support checkpoints.

Back to top

---
