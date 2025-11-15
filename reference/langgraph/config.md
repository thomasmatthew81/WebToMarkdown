# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:33.

## Converted Web Pages

### Config | LangChain Reference

**Source:** https://reference.langchain.com/python/langgraph/config/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langgraph/config.md "Edit this page")

# Config

##  `` langgraph.config ¶

FUNCTION | DESCRIPTION  
---|---  
`get_store` |  Access LangGraph store from inside a graph node or entrypoint task at runtime.  
`get_stream_writer` |  Access LangGraph [StreamWriter](../types/#langgraph.types.StreamWriter "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamWriter</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>") from inside a graph node or entrypoint task at runtime.  
  
###  `` get_store ¶
    
    
    get_store() -> [BaseStore](../store/#langgraph.store.base.BaseStore "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseStore</span> \(<code>langgraph.store.base.BaseStore</code>\)")
    

Access LangGraph store from inside a graph node or entrypoint task at runtime.

Can be called from inside any [StateGraph](../graphs/#langgraph.graph.state.StateGraph "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.graph.state.StateGraph</span>") node or functional API [task](../func/#langgraph.func.task "<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code>            <span class="doc doc-object-name doc-function-name">task</span>"), as long as the StateGraph or the [entrypoint](../func/#langgraph.func.entrypoint "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">entrypoint</span>") was initialized with a store, e.g.:
    
    
    # with StateGraph
    graph = (
        StateGraph(...)
        ...
        .compile(store=store)
    )
    
    # or with entrypoint
    @entrypoint(store=store)
    def workflow(inputs):
        ...
    

Async with Python < 3.11

If you are using Python < 3.11 and are running LangGraph asynchronously, `get_store()` won't work since it uses [contextvar](https://docs.python.org/3/library/contextvars.html) propagation (only available in [Python >= 3.11](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task)).

Using with StateGraph
    
    
    from typing_extensions import TypedDict
    from langgraph.graph import StateGraph, START
    from langgraph.store.memory import InMemoryStore
    from langgraph.config import get_store
    
    store = InMemoryStore()
    store.put(("values",), "foo", {"bar": 2})
    
    
    class State(TypedDict):
        foo: int
    
    
    def my_node(state: State):
        my_store = get_store()
        stored_value = my_store.get(("values",), "foo").value["bar"]
        return {"foo": stored_value + 1}
    
    
    graph = (
        StateGraph(State)
        .add_node(my_node)
        .add_edge(START, "my_node")
        .compile(store=store)
    )
    
    graph.invoke({"foo": 1})
    
    
    
    {"foo": 3}
    

Using with functional API
    
    
    from langgraph.func import entrypoint, task
    from langgraph.store.memory import InMemoryStore
    from langgraph.config import get_store
    
    store = InMemoryStore()
    store.put(("values",), "foo", {"bar": 2})
    
    
    @task
    def my_task(value: int):
        my_store = get_store()
        stored_value = my_store.get(("values",), "foo").value["bar"]
        return stored_value + 1
    
    
    @entrypoint(store=store)
    def workflow(value: int):
        return my_task(value).result()
    
    
    workflow.invoke(1)
    
    
    
    3
    

###  `` get_stream_writer ¶
    
    
    get_stream_writer() -> [StreamWriter](../types/#langgraph.types.StreamWriter "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamWriter</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamWriter</code>\)")
    

Access LangGraph [StreamWriter](../types/#langgraph.types.StreamWriter "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamWriter</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>") from inside a graph node or entrypoint task at runtime.

Can be called from inside any [StateGraph](../graphs/#langgraph.graph.state.StateGraph "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.graph.state.StateGraph</span>") node or functional API [task](../func/#langgraph.func.task "<code class="doc-symbol doc-symbol-heading doc-symbol-function"></code>            <span class="doc doc-object-name doc-function-name">task</span>").

Async with Python < 3.11

If you are using Python < 3.11 and are running LangGraph asynchronously, `get_stream_writer()` won't work since it uses [contextvar](https://docs.python.org/3/library/contextvars.html) propagation (only available in [Python >= 3.11](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task)).

Using with StateGraph
    
    
    from typing_extensions import TypedDict
    from langgraph.graph import StateGraph, START
    from langgraph.config import get_stream_writer
    
    
    class State(TypedDict):
        foo: int
    
    
    def my_node(state: State):
        my_stream_writer = get_stream_writer()
        my_stream_writer({"custom_data": "Hello!"})
        return {"foo": state["foo"] + 1}
    
    
    graph = (
        StateGraph(State)
        .add_node(my_node)
        .add_edge(START, "my_node")
        .compile(store=store)
    )
    
    for chunk in graph.stream({"foo": 1}, stream_mode="custom"):
        print(chunk)
    
    
    
    {"custom_data": "Hello!"}
    

Using with functional API
    
    
    from langgraph.func import entrypoint, task
    from langgraph.config import get_stream_writer
    
    
    @task
    def my_task(value: int):
        my_stream_writer = get_stream_writer()
        my_stream_writer({"custom_data": "Hello!"})
        return value + 1
    
    
    @entrypoint(store=store)
    def workflow(value: int):
        return my_task(value).result()
    
    
    for chunk in workflow.stream(1, stream_mode="custom"):
        print(chunk)
    
    
    
    {"custom_data": "Hello!"}
    

Back to top

---
