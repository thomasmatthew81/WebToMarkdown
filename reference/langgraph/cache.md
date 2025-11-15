# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:32.

## Converted Web Pages

### Caching (LangGraph) | LangChain Reference

**Source:** https://reference.langchain.com/python/langgraph/cache/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langgraph/cache.md "Edit this page")

# Caching

##  `` langgraph.cache.base ¶

###  `` BaseCache ¶

Bases: `[ABC](https://docs.python.org/3/library/abc.html#abc.ABC "<code>abc.ABC</code>")`, `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "<code>typing.Generic</code>")[ValueT]`

Base class for a cache.

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the cache with a serializer.  
`get` |  Get the cached values for the given keys.  
`aget` |  Asynchronously get the cached values for the given keys.  
`set` |  Set the cached values for the given keys and TTLs.  
`aset` |  Asynchronously set the cached values for the given keys and TTLs.  
`clear` |  Delete the cached values for the given namespaces.  
`aclear` |  Asynchronously delete the cached values for the given namespaces.  
  
####  `` __init__ ¶
    
    
    __init__(*, serde: [SerializerProtocol](../checkpoints/#langgraph.checkpoint.serde.base.SerializerProtocol "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">SerializerProtocol</span> \(<code>langgraph.checkpoint.serde.base.SerializerProtocol</code>\)") | None = None) -> None
    

Initialize the cache with a serializer.

####  `` get `abstractmethod` ¶
    
    
    get(keys: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[FullKey]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[FullKey, ValueT]
    

Get the cached values for the given keys.

####  `` aget `abstractmethod` `async` ¶
    
    
    aget(keys: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[FullKey]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[FullKey, ValueT]
    

Asynchronously get the cached values for the given keys.

####  `` set `abstractmethod` ¶
    
    
    set(pairs: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[FullKey, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[ValueT, [int](https://docs.python.org/3/library/functions.html#int) | None]]) -> None
    

Set the cached values for the given keys and TTLs.

####  `` aset `abstractmethod` `async` ¶
    
    
    aset(pairs: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[FullKey, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[ValueT, [int](https://docs.python.org/3/library/functions.html#int) | None]]) -> None
    

Asynchronously set the cached values for the given keys and TTLs.

####  `` clear `abstractmethod` ¶
    
    
    clear(namespaces: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Namespace] | None = None) -> None
    

Delete the cached values for the given namespaces. If no namespaces are provided, clear all cached values.

####  `` aclear `abstractmethod` `async` ¶
    
    
    aclear(namespaces: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Namespace] | None = None) -> None
    

Asynchronously delete the cached values for the given namespaces. If no namespaces are provided, clear all cached values.

##  `` langgraph.cache.memory ¶

###  `` InMemoryCache ¶

Bases: `BaseCache[ValueT]`

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the cache with a serializer.  
`get` |  Get the cached values for the given keys.  
`aget` |  Asynchronously get the cached values for the given keys.  
`set` |  Set the cached values for the given keys.  
`aset` |  Asynchronously set the cached values for the given keys.  
`clear` |  Delete the cached values for the given namespaces.  
`aclear` |  Asynchronously delete the cached values for the given namespaces.  
  
####  `` __init__ ¶
    
    
    __init__(*, serde: [SerializerProtocol](../checkpoints/#langgraph.checkpoint.serde.base.SerializerProtocol "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">SerializerProtocol</span> \(<code>langgraph.checkpoint.serde.base.SerializerProtocol</code>\)") | None = None)
    

Initialize the cache with a serializer.

####  `` get ¶
    
    
    get(keys: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[FullKey]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[FullKey, ValueT]
    

Get the cached values for the given keys.

####  `` aget `async` ¶
    
    
    aget(keys: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[FullKey]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[FullKey, ValueT]
    

Asynchronously get the cached values for the given keys.

####  `` set ¶
    
    
    set(keys: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[FullKey, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[ValueT, [int](https://docs.python.org/3/library/functions.html#int) | None]]) -> None
    

Set the cached values for the given keys.

####  `` aset `async` ¶
    
    
    aset(keys: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[FullKey, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[ValueT, [int](https://docs.python.org/3/library/functions.html#int) | None]]) -> None
    

Asynchronously set the cached values for the given keys.

####  `` clear ¶
    
    
    clear(namespaces: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Namespace] | None = None) -> None
    

Delete the cached values for the given namespaces. If no namespaces are provided, clear all cached values.

####  `` aclear `async` ¶
    
    
    aclear(namespaces: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Namespace] | None = None) -> None
    

Asynchronously delete the cached values for the given namespaces. If no namespaces are provided, clear all cached values.

##  `` langgraph.cache.sqlite ¶

###  `` SqliteCache ¶

Bases: `BaseCache[ValueT]`

File-based cache using SQLite.

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the cache with a file path.  
`get` |  Get the cached values for the given keys.  
`aget` |  Asynchronously get the cached values for the given keys.  
`set` |  Set the cached values for the given keys and TTLs.  
`aset` |  Asynchronously set the cached values for the given keys and TTLs.  
`clear` |  Delete the cached values for the given namespaces.  
`aclear` |  Asynchronously delete the cached values for the given namespaces.  
  
####  `` __init__ ¶
    
    
    __init__(*, path: [str](https://docs.python.org/3/library/stdtypes.html#str), serde: [SerializerProtocol](../checkpoints/#langgraph.checkpoint.serde.base.SerializerProtocol "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">SerializerProtocol</span> \(<code>langgraph.checkpoint.serde.base.SerializerProtocol</code>\)") | None = None) -> None
    

Initialize the cache with a file path.

####  `` get ¶
    
    
    get(keys: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[FullKey]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[FullKey, ValueT]
    

Get the cached values for the given keys.

####  `` aget `async` ¶
    
    
    aget(keys: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[FullKey]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[FullKey, ValueT]
    

Asynchronously get the cached values for the given keys.

####  `` set ¶
    
    
    set(mapping: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[FullKey, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[ValueT, [int](https://docs.python.org/3/library/functions.html#int) | None]]) -> None
    

Set the cached values for the given keys and TTLs.

####  `` aset `async` ¶
    
    
    aset(mapping: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[FullKey, [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[ValueT, [int](https://docs.python.org/3/library/functions.html#int) | None]]) -> None
    

Asynchronously set the cached values for the given keys and TTLs.

####  `` clear ¶
    
    
    clear(namespaces: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Namespace] | None = None) -> None
    

Delete the cached values for the given namespaces. If no namespaces are provided, clear all cached values.

####  `` aclear `async` ¶
    
    
    aclear(namespaces: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Namespace] | None = None) -> None
    

Asynchronously delete the cached values for the given namespaces. If no namespaces are provided, clear all cached values.

Back to top

---
