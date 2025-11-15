# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:30.

## Converted Web Pages

### Graphs | LangChain Reference

**Source:** https://reference.langchain.com/python/langgraph/graphs/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langgraph/graphs.md "Edit this page")

# Graphs

##  `` langgraph.graph.state.StateGraph ¶

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "<code>typing.Generic</code>")[StateT, ContextT, InputT, OutputT]`

A graph whose nodes communicate by reading and writing to a shared state.

The signature of each node is `State -> Partial<State>`.

Each state key can optionally be annotated with a reducer function that will be used to aggregate the values of that key received from multiple nodes. The signature of a reducer function is `(Value, Value) -> Value`.

Warning

`StateGraph` is a builder class and cannot be used directly for execution. You must first call `.compile()` to create an executable graph that supports methods like `invoke()`, `stream()`, `astream()`, and `ainvoke()`. See the `CompiledStateGraph` documentation for more details.

PARAMETER | DESCRIPTION  
---|---  
`state_schema` |  The schema class that defines the state. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[StateT]`  
`context_schema` |  The schema class that defines the runtime context. Use this to expose immutable context data to your nodes, like `user_id`, `db_conn`, etc. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[ContextT] | None` **DEFAULT:** `None`  
`input_schema` |  The schema class that defines the input to the graph. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[InputT] | None` **DEFAULT:** `None`  
`output_schema` |  The schema class that defines the output from the graph. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[OutputT] | None` **DEFAULT:** `None`  
  
`config_schema` Deprecated

The `config_schema` parameter is deprecated in v0.6.0 and support will be removed in v2.0.0. Please use `context_schema` instead to specify the schema for run-scoped context.

Example
    
    
    from langchain_core.runnables import RunnableConfig
    from typing_extensions import Annotated, TypedDict
    from langgraph.checkpoint.memory import InMemorySaver
    from langgraph.graph import StateGraph
    from langgraph.runtime import Runtime
    
    
    def reducer(a: list, b: int | None) -> list:
        if b is not None:
            return a + [b]
        return a
    
    
    class State(TypedDict):
        x: Annotated[list, reducer]
    
    
    class Context(TypedDict):
        r: float
    
    
    graph = StateGraph(state_schema=State, context_schema=Context)
    
    
    def node(state: State, runtime: Runtime[Context]) -> dict:
        r = runtime.context.get("r", 1.0)
        x = state["x"][-1]
        next_value = x * r * (1 - x)
        return {"x": next_value}
    
    
    graph.add_node("A", node)
    graph.set_entry_point("A")
    graph.set_finish_point("A")
    compiled = graph.compile()
    
    step1 = compiled.invoke({"x": 0.5}, context={"r": 3.0})
    # {'x': [0.5, 0.75]}
    

METHOD | DESCRIPTION  
---|---  
`add_node` |  Add a new node to the `StateGraph`.  
`add_edge` |  Add a directed edge from the start node (or list of start nodes) to the end node.  
`add_conditional_edges` |  Add a conditional edge from the starting node to any number of destination nodes.  
`add_sequence` |  Add a sequence of nodes that will be executed in the provided order.  
`compile` |  Compiles the `StateGraph` into a `CompiledStateGraph` object.  
  
###  `` add_node ¶
    
    
    add_node(
        node: [str](https://docs.python.org/3/library/stdtypes.html#str) | StateNode[NodeInputT, ContextT],
        action: StateNode[NodeInputT, ContextT] | None = None,
        *,
        defer: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        input_schema: [type](https://docs.python.org/3/library/functions.html#type)[NodeInputT] | None = None,
        retry_policy: [RetryPolicy](../types/#langgraph.types.RetryPolicy "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">RetryPolicy</span> \(<code>langgraph.types.RetryPolicy</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[RetryPolicy](../types/#langgraph.types.RetryPolicy "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">RetryPolicy</span> \(<code>langgraph.types.RetryPolicy</code>\)")] | None = None,
        cache_policy: [CachePolicy](../types/#langgraph.types.CachePolicy "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">CachePolicy</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.CachePolicy</code>\)") | None = None,
        destinations: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...] | None = None,
        **kwargs: [Unpack](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack "<code>typing_extensions.Unpack</code>")[DeprecatedKwargs],
    ) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Add a new node to the `StateGraph`.

PARAMETER | DESCRIPTION  
---|---  
`node` |  The function or runnable this node will run. If a string is provided, it will be used as the node name, and action will be used as the function or runnable. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | StateNode[NodeInputT, ContextT]`  
`action` |  The action associated with the node. Will be used as the node function or runnable if `node` is a string (node name). **TYPE:** `StateNode[NodeInputT, ContextT] | None` **DEFAULT:** `None`  
`defer` |  Whether to defer the execution of the node until the run is about to end. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`metadata` |  The metadata associated with the node. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`input_schema` |  The input schema for the node. (default: the graph's state schema) **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[NodeInputT] | None` **DEFAULT:** `None`  
`retry_policy` |  The retry policy for the node. If a sequence is provided, the first matching policy will be applied. **TYPE:** `[RetryPolicy](../types/#langgraph.types.RetryPolicy "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">RetryPolicy</span> \(<code>langgraph.types.RetryPolicy</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[RetryPolicy](../types/#langgraph.types.RetryPolicy "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">RetryPolicy</span> \(<code>langgraph.types.RetryPolicy</code>\)")] | None` **DEFAULT:** `None`  
`cache_policy` |  The cache policy for the node. **TYPE:** `[CachePolicy](../types/#langgraph.types.CachePolicy "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">CachePolicy</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.CachePolicy</code>\)") | None` **DEFAULT:** `None`  
`destinations` |  Destinations that indicate where a node can route to. This is useful for edgeless graphs with nodes that return `Command` objects. If a `dict` is provided, the keys will be used as the target node names and the values will be used as the labels for the edges. If a `tuple` is provided, the values will be used as the target node names. Note This is only used for graph rendering and doesn't have any effect on the graph execution. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...] | None` **DEFAULT:** `None`  
Example
    
    
    from typing_extensions import TypedDict
    
    from langchain_core.runnables import RunnableConfig
    from langgraph.graph import START, StateGraph
    
    
    class State(TypedDict):
        x: int
    
    
    def my_node(state: State, config: RunnableConfig) -> State:
        return {"x": state["x"] + 1}
    
    
    builder = StateGraph(State)
    builder.add_node(my_node)  # node name will be 'my_node'
    builder.add_edge(START, "my_node")
    graph = builder.compile()
    graph.invoke({"x": 1})
    # {'x': 2}
    

Customize the name:
    
    
    builder = StateGraph(State)
    builder.add_node("my_fair_node", my_node)
    builder.add_edge(START, "my_fair_node")
    graph = builder.compile()
    graph.invoke({"x": 1})
    # {'x': 2}
    

RETURNS | DESCRIPTION  
---|---  
`Self` |  The instance of the `StateGraph`, allowing for method chaining. **TYPE:** `[Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")`  
  
###  `` add_edge ¶
    
    
    add_edge(start_key: [str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)], end_key: [str](https://docs.python.org/3/library/stdtypes.html#str)) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Add a directed edge from the start node (or list of start nodes) to the end node.

When a single start node is provided, the graph will wait for that node to complete before executing the end node. When multiple start nodes are provided, the graph will wait for ALL of the start nodes to complete before executing the end node.

PARAMETER | DESCRIPTION  
---|---  
`start_key` |  The key(s) of the start node(s) of the edge. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`end_key` |  The key of the end node of the edge. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If the start key is `'END'` or if the start key or end key is not present in the graph.  
RETURNS | DESCRIPTION  
---|---  
`Self` |  The instance of the `StateGraph`, allowing for method chaining. **TYPE:** `[Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")`  
  
###  `` add_conditional_edges ¶
    
    
    add_conditional_edges(
        source: [str](https://docs.python.org/3/library/stdtypes.html#str),
        path: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[..., [Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>")]]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[..., [Awaitable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "<code>collections.abc.Awaitable</code>")[[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>")]]]
        | [Runnable](../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span> \(<code>langchain_core.runnables.Runnable</code>\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), [Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>")]],
        path_map: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>"), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
    ) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Add a conditional edge from the starting node to any number of destination nodes.

PARAMETER | DESCRIPTION  
---|---  
`source` |  The starting node. This conditional edge will run when exiting this node. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`path` |  The callable that determines the next node or nodes. If not specifying `path_map` it should return one or more nodes. If it returns `'END'`, the graph will stop execution. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[..., [Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>")]] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[..., [Awaitable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "<code>collections.abc.Awaitable</code>")[[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>")]]] | [Runnable](../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span> \(<code>langchain_core.runnables.Runnable</code>\)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), [Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>")]]`  
`path_map` |  Optional mapping of paths to node names. If omitted the paths returned by `path` should be node names. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "<code>collections.abc.Hashable</code>"), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`Self` |  The instance of the graph, allowing for method chaining. **TYPE:** `[Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")`  
  
Warning

Without type hints on the `path` function's return value (e.g., `-> Literal["foo", "__end__"]:`) or a path_map, the graph visualization assumes the edge could transition to any node in the graph.

###  `` add_sequence ¶
    
    
    add_sequence(
        nodes: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[
            StateNode[NodeInputT, ContextT] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), StateNode[NodeInputT, ContextT]]
        ],
    ) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Add a sequence of nodes that will be executed in the provided order.

PARAMETER | DESCRIPTION  
---|---  
`nodes` |  A sequence of `StateNode` (callables that accept a `state` arg) or `(name, StateNode)` tuples. If no names are provided, the name will be inferred from the node object (e.g. a `Runnable` or a `Callable` name). Each node will be executed in the order provided. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[StateNode[NodeInputT, ContextT] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), StateNode[NodeInputT, ContextT]]]`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If the sequence is empty.  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If the sequence contains duplicate node names.  
RETURNS | DESCRIPTION  
---|---  
`Self` |  The instance of the `StateGraph`, allowing for method chaining. **TYPE:** `[Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")`  
  
###  `` compile ¶
    
    
    compile(
        checkpointer: Checkpointer = None,
        *,
        cache: [BaseCache](../cache/#langgraph.cache.base.BaseCache "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseCache</span> \(<code>langgraph.cache.base.BaseCache</code>\)") | None = None,
        store: [BaseStore](../store/#langgraph.store.base.BaseStore "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseStore</span> \(<code>langgraph.store.base.BaseStore</code>\)") | None = None,
        interrupt_before: [All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.All</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        interrupt_after: [All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.All</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        debug: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    ) -> CompiledStateGraph[StateT, ContextT, InputT, OutputT]
    

Compiles the `StateGraph` into a `CompiledStateGraph` object.

The compiled graph implements the `Runnable` interface and can be invoked, streamed, batched, and run asynchronously.

PARAMETER | DESCRIPTION  
---|---  
`checkpointer` |  A checkpoint saver object or flag. If provided, this `Checkpointer` serves as a fully versioned "short-term memory" for the graph, allowing it to be paused, resumed, and replayed from any point. If `None`, it may inherit the parent graph's checkpointer when used as a subgraph. If `False`, it will not use or inherit any checkpointer. **TYPE:** `Checkpointer` **DEFAULT:** `None`  
`interrupt_before` |  An optional list of node names to interrupt before. **TYPE:** `[All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.All</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`interrupt_after` |  An optional list of node names to interrupt after. **TYPE:** `[All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.All</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`debug` |  A flag indicating whether to enable debug mode. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`name` |  The name to use for the compiled graph. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`CompiledStateGraph` |  The compiled `StateGraph`. **TYPE:** `CompiledStateGraph[StateT, ContextT, InputT, OutputT]`  
  
##  `` langgraph.graph.state.CompiledStateGraph ¶

Bases: `[Pregel](../pregel/#langgraph.pregel.Pregel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.pregel.Pregel</span>")[StateT, ContextT, InputT, OutputT]`, `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "<code>typing.Generic</code>")[StateT, ContextT, InputT, OutputT]`

METHOD | DESCRIPTION  
---|---  
`stream` |  Stream graph steps for a single input.  
`astream` |  Asynchronously stream graph steps for a single input.  
`invoke` |  Run the graph with a single input and config.  
`ainvoke` |  Asynchronously run the graph with a single input and config.  
`get_state` |  Get the current state of the graph.  
`aget_state` |  Get the current state of the graph.  
`get_state_history` |  Get the history of the state of the graph.  
`aget_state_history` |  Asynchronously get the history of the state of the graph.  
`update_state` |  Update the state of the graph with the given values, as if they came from  
`aupdate_state` |  Asynchronously update the state of the graph with the given values, as if they came from  
`bulk_update_state` |  Apply updates to the graph state in bulk. Requires a checkpointer to be set.  
`abulk_update_state` |  Asynchronously apply updates to the graph state in bulk. Requires a checkpointer to be set.  
`get_graph` |  Return a drawable representation of the computation graph.  
`aget_graph` |  Return a drawable representation of the computation graph.  
`get_subgraphs` |  Get the subgraphs of the graph.  
`aget_subgraphs` |  Get the subgraphs of the graph.  
`with_config` |  Create a copy of the Pregel object with an updated config.  
  
###  `` stream ¶
    
    
    stream(
        input: InputT | [Command](../types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.Command</code>\)") | None,
        config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None,
        *,
        context: ContextT | None = None,
        stream_mode: [StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)")] | None = None,
        print_mode: [StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)")] = (),
        output_keys: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        interrupt_before: [All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        interrupt_after: [All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        durability: Durability | None = None,
        subgraphs: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        debug: [bool](https://docs.python.org/3/library/functions.html#bool) | None = None,
        **kwargs: [Unpack](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack "<code>typing_extensions.Unpack</code>")[DeprecatedKwargs],
    ) -> [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Stream graph steps for a single input.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input to the graph. **TYPE:** `InputT | [Command](../types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.Command</code>\)") | None`  
`config` |  The configuration to use for the run. **TYPE:** `[RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`context` |  The static context to use for the run. Added in version 0.6.0 **TYPE:** `ContextT | None` **DEFAULT:** `None`  
`stream_mode` |  The mode to stream output, defaults to `self.stream_mode`. Options are:

  * `"values"`: Emit all values in the state after each step, including interrupts. When used with functional API, values are emitted once at the end of the workflow.
  * `"updates"`: Emit only the node or task names and updates returned by the nodes or tasks after each step. If multiple updates are made in the same step (e.g. multiple nodes are run) then those updates are emitted separately.
  * `"custom"`: Emit custom data from inside nodes or tasks using `StreamWriter`.
  * `"messages"`: Emit LLM messages token-by-token together with metadata for any LLM invocations inside nodes or tasks. Will be emitted as 2-tuples `(LLM token, metadata)`.
  * `"checkpoints"`: Emit an event when a checkpoint is created, in the same format as returned by `get_state()`.
  * `"tasks"`: Emit events when tasks start and finish, including their results and errors.
  * `"debug"`: Emit debug events with as much information as possible for each step.

You can pass a list as the `stream_mode` parameter to stream multiple modes at once. The streamed outputs will be tuples of `(mode, data)`. See [LangGraph streaming guide](https://docs.langchain.com/oss/python/langgraph/streaming) for more details. **TYPE:** `[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)")] | None` **DEFAULT:** `None`  
`print_mode` |  Accepts the same values as `stream_mode`, but only prints the output to the console, for debugging purposes. Does not affect the output of the graph in any way. **TYPE:** `[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)")]` **DEFAULT:** `()`  
`output_keys` |  The keys to stream, defaults to all non-context channels. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`interrupt_before` |  Nodes to interrupt before, defaults to all nodes in the graph. **TYPE:** `[All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`interrupt_after` |  Nodes to interrupt after, defaults to all nodes in the graph. **TYPE:** `[All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`durability` |  The durability mode for the graph execution, defaults to `"async"`. Options are:

  * `"sync"`: Changes are persisted synchronously before the next step starts.
  * `"async"`: Changes are persisted asynchronously while the next step executes.
  * `"exit"`: Changes are persisted only when the graph exits.

**TYPE:** `Durability | None` **DEFAULT:** `None`  
`subgraphs` |  Whether to stream events from inside subgraphs, defaults to False. If `True`, the events will be emitted as tuples `(namespace, data)`, or `(namespace, mode, data)` if `stream_mode` is a list, where `namespace` is a tuple with the path to the node where a subgraph is invoked, e.g. `("parent_node:<task_id>", "child_node:<task_id>")`. See [LangGraph streaming guide](https://docs.langchain.com/oss/python/langgraph/streaming) for more details. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
YIELDS | DESCRIPTION  
---|---  
`[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` |  The output of each step in the graph. The output shape depends on the `stream_mode`.  
  
###  `` astream `async` ¶
    
    
    astream(
        input: InputT | [Command](../types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.Command</code>\)") | None,
        config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None,
        *,
        context: ContextT | None = None,
        stream_mode: [StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)")] | None = None,
        print_mode: [StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)")] = (),
        output_keys: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        interrupt_before: [All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        interrupt_after: [All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        durability: Durability | None = None,
        subgraphs: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        debug: [bool](https://docs.python.org/3/library/functions.html#bool) | None = None,
        **kwargs: [Unpack](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Unpack "<code>typing_extensions.Unpack</code>")[DeprecatedKwargs],
    ) -> [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Asynchronously stream graph steps for a single input.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input to the graph. **TYPE:** `InputT | [Command](../types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.Command</code>\)") | None`  
`config` |  The configuration to use for the run. **TYPE:** `[RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`context` |  The static context to use for the run. Added in version 0.6.0 **TYPE:** `ContextT | None` **DEFAULT:** `None`  
`stream_mode` |  The mode to stream output, defaults to `self.stream_mode`. Options are:

  * `"values"`: Emit all values in the state after each step, including interrupts. When used with functional API, values are emitted once at the end of the workflow.
  * `"updates"`: Emit only the node or task names and updates returned by the nodes or tasks after each step. If multiple updates are made in the same step (e.g. multiple nodes are run) then those updates are emitted separately.
  * `"custom"`: Emit custom data from inside nodes or tasks using `StreamWriter`.
  * `"messages"`: Emit LLM messages token-by-token together with metadata for any LLM invocations inside nodes or tasks. Will be emitted as 2-tuples `(LLM token, metadata)`.
  * `"checkpoints"`: Emit an event when a checkpoint is created, in the same format as returned by `get_state()`.
  * `"tasks"`: Emit events when tasks start and finish, including their results and errors.
  * `"debug"`: Emit debug events with as much information as possible for each step.

You can pass a list as the `stream_mode` parameter to stream multiple modes at once. The streamed outputs will be tuples of `(mode, data)`. See [LangGraph streaming guide](https://docs.langchain.com/oss/python/langgraph/streaming) for more details. **TYPE:** `[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)")] | None` **DEFAULT:** `None`  
`print_mode` |  Accepts the same values as `stream_mode`, but only prints the output to the console, for debugging purposes. Does not affect the output of the graph in any way. **TYPE:** `[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)")]` **DEFAULT:** `()`  
`output_keys` |  The keys to stream, defaults to all non-context channels. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`interrupt_before` |  Nodes to interrupt before, defaults to all nodes in the graph. **TYPE:** `[All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`interrupt_after` |  Nodes to interrupt after, defaults to all nodes in the graph. **TYPE:** `[All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`durability` |  The durability mode for the graph execution, defaults to `"async"`. Options are:

  * `"sync"`: Changes are persisted synchronously before the next step starts.
  * `"async"`: Changes are persisted asynchronously while the next step executes.
  * `"exit"`: Changes are persisted only when the graph exits.

**TYPE:** `Durability | None` **DEFAULT:** `None`  
`subgraphs` |  Whether to stream events from inside subgraphs, defaults to False. If `True`, the events will be emitted as tuples `(namespace, data)`, or `(namespace, mode, data)` if `stream_mode` is a list, where `namespace` is a tuple with the path to the node where a subgraph is invoked, e.g. `("parent_node:<task_id>", "child_node:<task_id>")`. See [LangGraph streaming guide](https://docs.langchain.com/oss/python/langgraph/streaming) for more details. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
YIELDS | DESCRIPTION  
---|---  
`[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]` |  The output of each step in the graph. The output shape depends on the `stream_mode`.  
  
###  `` invoke ¶
    
    
    invoke(
        input: InputT | [Command](../types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.Command</code>\)") | None,
        config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None,
        *,
        context: ContextT | None = None,
        stream_mode: [StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)") = "values",
        print_mode: [StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)")] = (),
        output_keys: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        interrupt_before: [All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        interrupt_after: [All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        durability: Durability | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run the graph with a single input and config.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input data for the graph. It can be a dictionary or any other type. **TYPE:** `InputT | [Command](../types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.Command</code>\)") | None`  
`config` |  The configuration for the graph run. **TYPE:** `[RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`context` |  The static context to use for the run. Added in version 0.6.0 **TYPE:** `ContextT | None` **DEFAULT:** `None`  
`stream_mode` |  The stream mode for the graph run. **TYPE:** `[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)")` **DEFAULT:** `'values'`  
`print_mode` |  Accepts the same values as `stream_mode`, but only prints the output to the console, for debugging purposes. Does not affect the output of the graph in any way. **TYPE:** `[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)")]` **DEFAULT:** `()`  
`output_keys` |  The output keys to retrieve from the graph run. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`interrupt_before` |  The nodes to interrupt the graph run before. **TYPE:** `[All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`interrupt_after` |  The nodes to interrupt the graph run after. **TYPE:** `[All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`durability` |  The durability mode for the graph execution, defaults to `"async"`. Options are:

  * `"sync"`: Changes are persisted synchronously before the next step starts.
  * `"async"`: Changes are persisted asynchronously while the next step executes.
  * `"exit"`: Changes are persisted only when the graph exits.

**TYPE:** `Durability | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the graph run. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` |  The output of the graph run. If `stream_mode` is `"values"`, it returns the latest output.  
`[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` |  If `stream_mode` is not `"values"`, it returns a list of output chunks.  
  
###  `` ainvoke `async` ¶
    
    
    ainvoke(
        input: InputT | [Command](../types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.Command</code>\)") | None,
        config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None,
        *,
        context: ContextT | None = None,
        stream_mode: [StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)") = "values",
        print_mode: [StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamMode</code>\)")] = (),
        output_keys: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        interrupt_before: [All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        interrupt_after: [All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        durability: Durability | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Asynchronously run the graph with a single input and config.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input data for the graph. It can be a dictionary or any other type. **TYPE:** `InputT | [Command](../types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.Command</code>\)") | None`  
`config` |  The configuration for the graph run. **TYPE:** `[RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`context` |  The static context to use for the run. Added in version 0.6.0 **TYPE:** `ContextT | None` **DEFAULT:** `None`  
`stream_mode` |  The stream mode for the graph run. **TYPE:** `[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)")` **DEFAULT:** `'values'`  
`print_mode` |  Accepts the same values as `stream_mode`, but only prints the output to the console, for debugging purposes. Does not affect the output of the graph in any way. **TYPE:** `[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[StreamMode](../types/#langgraph.types.StreamMode "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamMode</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.StreamMode</code>\)")]` **DEFAULT:** `()`  
`output_keys` |  The output keys to retrieve from the graph run. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`interrupt_before` |  The nodes to interrupt the graph run before. **TYPE:** `[All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`interrupt_after` |  The nodes to interrupt the graph run after. **TYPE:** `[All](../types/#langgraph.types.All "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">All</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langgraph.types.All</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`durability` |  The durability mode for the graph execution, defaults to `"async"`. Options are:

  * `"sync"`: Changes are persisted synchronously before the next step starts.
  * `"async"`: Changes are persisted asynchronously while the next step executes.
  * `"exit"`: Changes are persisted only when the graph exits.

**TYPE:** `Durability | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the graph run. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` |  The output of the graph run. If `stream_mode` is `"values"`, it returns the latest output.  
`[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` |  If `stream_mode` is not `"values"`, it returns a list of output chunks.  
  
###  `` get_state ¶
    
    
    get_state(config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)"), *, subgraphs: [bool](https://docs.python.org/3/library/functions.html#bool) = False) -> [StateSnapshot](../types/#langgraph.types.StateSnapshot "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">StateSnapshot</span> \(<code>langgraph.types.StateSnapshot</code>\)")
    

Get the current state of the graph.

###  `` aget_state `async` ¶
    
    
    aget_state(config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)"), *, subgraphs: [bool](https://docs.python.org/3/library/functions.html#bool) = False) -> [StateSnapshot](../types/#langgraph.types.StateSnapshot "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">StateSnapshot</span> \(<code>langgraph.types.StateSnapshot</code>\)")
    

Get the current state of the graph.

###  `` get_state_history ¶
    
    
    get_state_history(
        config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)"),
        *,
        filter: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        before: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None,
        limit: [int](https://docs.python.org/3/library/functions.html#int) | None = None,
    ) -> [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[StateSnapshot](../types/#langgraph.types.StateSnapshot "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">StateSnapshot</span> \(<code>langgraph.types.StateSnapshot</code>\)")]
    

Get the history of the state of the graph.

###  `` aget_state_history `async` ¶
    
    
    aget_state_history(
        config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)"),
        *,
        filter: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        before: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None,
        limit: [int](https://docs.python.org/3/library/functions.html#int) | None = None,
    ) -> [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[StateSnapshot](../types/#langgraph.types.StateSnapshot "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">StateSnapshot</span> \(<code>langgraph.types.StateSnapshot</code>\)")]
    

Asynchronously get the history of the state of the graph.

###  `` update_state ¶
    
    
    update_state(
        config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)"),
        values: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None,
        as_node: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        task_id: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    ) -> [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")
    

Update the state of the graph with the given values, as if they came from node `as_node`. If `as_node` is not provided, it will be set to the last node that updated the state, if not ambiguous.

###  `` aupdate_state `async` ¶
    
    
    aupdate_state(
        config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)"),
        values: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
        as_node: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        task_id: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    ) -> [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")
    

Asynchronously update the state of the graph with the given values, as if they came from node `as_node`. If `as_node` is not provided, it will be set to the last node that updated the state, if not ambiguous.

###  `` bulk_update_state ¶
    
    
    bulk_update_state(
        config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)"), supersteps: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[StateUpdate]]
    ) -> [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")
    

Apply updates to the graph state in bulk. Requires a checkpointer to be set.

PARAMETER | DESCRIPTION  
---|---  
`config` |  The config to apply the updates to. **TYPE:** `[RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")`  
`supersteps` |  A list of supersteps, each including a list of updates to apply sequentially to a graph state. Each update is a tuple of the form `(values, as_node, task_id)` where `task_id` is optional. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[StateUpdate]]`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If no checkpointer is set or no updates are provided.  
`[InvalidUpdateError](../errors/#langgraph.errors.InvalidUpdateError "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">InvalidUpdateError</span> \(<code>langgraph.errors.InvalidUpdateError</code>\)")` |  If an invalid update is provided.  
RETURNS | DESCRIPTION  
---|---  
`RunnableConfig` |  The updated config. **TYPE:** `[RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")`  
  
###  `` abulk_update_state `async` ¶
    
    
    abulk_update_state(
        config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)"), supersteps: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[StateUpdate]]
    ) -> [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")
    

Asynchronously apply updates to the graph state in bulk. Requires a checkpointer to be set.

PARAMETER | DESCRIPTION  
---|---  
`config` |  The config to apply the updates to. **TYPE:** `[RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")`  
`supersteps` |  A list of supersteps, each including a list of updates to apply sequentially to a graph state. Each update is a tuple of the form `(values, as_node, task_id)` where `task_id` is optional. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[StateUpdate]]`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If no checkpointer is set or no updates are provided.  
`[InvalidUpdateError](../errors/#langgraph.errors.InvalidUpdateError "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">InvalidUpdateError</span> \(<code>langgraph.errors.InvalidUpdateError</code>\)")` |  If an invalid update is provided.  
RETURNS | DESCRIPTION  
---|---  
`RunnableConfig` |  The updated config. **TYPE:** `[RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")`  
  
###  `` get_graph ¶
    
    
    get_graph(config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None, *, xray: [int](https://docs.python.org/3/library/functions.html#int) | [bool](https://docs.python.org/3/library/functions.html#bool) = False) -> Graph
    

Return a drawable representation of the computation graph.

###  `` aget_graph `async` ¶
    
    
    aget_graph(config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None, *, xray: [int](https://docs.python.org/3/library/functions.html#int) | [bool](https://docs.python.org/3/library/functions.html#bool) = False) -> Graph
    

Return a drawable representation of the computation graph.

###  `` get_subgraphs ¶
    
    
    get_subgraphs(
        *, namespace: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None, recurse: [bool](https://docs.python.org/3/library/functions.html#bool) = False
    ) -> [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), PregelProtocol]]
    

Get the subgraphs of the graph.

PARAMETER | DESCRIPTION  
---|---  
`namespace` |  The namespace to filter the subgraphs by. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`recurse` |  Whether to recurse into the subgraphs. If `False`, only the immediate subgraphs will be returned. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
RETURNS | DESCRIPTION  
---|---  
`[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), PregelProtocol]]` |  An iterator of the `(namespace, subgraph)` pairs.  
  
###  `` aget_subgraphs `async` ¶
    
    
    aget_subgraphs(
        *, namespace: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None, recurse: [bool](https://docs.python.org/3/library/functions.html#bool) = False
    ) -> [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), PregelProtocol]]
    

Get the subgraphs of the graph.

PARAMETER | DESCRIPTION  
---|---  
`namespace` |  The namespace to filter the subgraphs by. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`recurse` |  Whether to recurse into the subgraphs. If `False`, only the immediate subgraphs will be returned. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
RETURNS | DESCRIPTION  
---|---  
`[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), PregelProtocol]]` |  An iterator of the `(namespace, subgraph)` pairs.  
  
###  `` with_config ¶
    
    
    with_config(config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Create a copy of the Pregel object with an updated config.

##  `` langgraph.graph.message ¶

FUNCTION | DESCRIPTION  
---|---  
`add_messages` |  Merges two lists of messages, updating existing messages by ID.  
  
###  `` add_messages ¶
    
    
    add_messages(
        left: Messages,
        right: Messages,
        *,
        format: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")["langchain-openai"] | None = None,
    ) -> Messages
    

Merges two lists of messages, updating existing messages by ID.

By default, this ensures the state is "append-only", unless the new message has the same ID as an existing message.

PARAMETER | DESCRIPTION  
---|---  
`left` |  The base list of `Messages`. **TYPE:** `Messages`  
`right` |  The list of `Messages` (or single `Message`) to merge into the base list. **TYPE:** `Messages`  
`format` |  The format to return messages in. If `None` then `Messages` will be returned as is. If `langchain-openai` then `Messages` will be returned as `BaseMessage` objects with their contents formatted to match OpenAI message format, meaning contents can be string, `'text'` blocks, or `'image_url'` blocks and tool responses are returned as their own `ToolMessage` objects. Requirement Must have `langchain-core>=0.3.11` installed to use this feature. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['langchain-openai'] | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`Messages` |  A new list of messages with the messages from `right` merged into `left`.  
`Messages` |  If a message in `right` has the same ID as a message in `left`, the message from `right` will replace the message from `left`.  
Example

Basic usage
    
    
    from langchain_core.messages import AIMessage, HumanMessage
    
    msgs1 = [HumanMessage(content="Hello", id="1")]
    msgs2 = [AIMessage(content="Hi there!", id="2")]
    add_messages(msgs1, msgs2)
    # [HumanMessage(content='Hello', id='1'), AIMessage(content='Hi there!', id='2')]
    

Overwrite existing message
    
    
    msgs1 = [HumanMessage(content="Hello", id="1")]
    msgs2 = [HumanMessage(content="Hello again", id="1")]
    add_messages(msgs1, msgs2)
    # [HumanMessage(content='Hello again', id='1')]
    

Use in a StateGraph
    
    
    from typing import Annotated
    from typing_extensions import TypedDict
    from langgraph.graph import StateGraph
    
    
    class State(TypedDict):
        messages: Annotated[list, add_messages]
    
    
    builder = StateGraph(State)
    builder.add_node("chatbot", lambda state: {"messages": [("assistant", "Hello")]})
    builder.set_entry_point("chatbot")
    builder.set_finish_point("chatbot")
    graph = builder.compile()
    graph.invoke({})
    # {'messages': [AIMessage(content='Hello', id=...)]}
    

Use OpenAI message format
    
    
    from typing import Annotated
    from typing_extensions import TypedDict
    from langgraph.graph import StateGraph, add_messages
    
    
    class State(TypedDict):
        messages: Annotated[list, add_messages(format="langchain-openai")]
    
    
    def chatbot_node(state: State) -> list:
        return {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Here's an image:",
                            "cache_control": {"type": "ephemeral"},
                        },
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": "image/jpeg",
                                "data": "1234",
                            },
                        },
                    ],
                },
            ]
        }
    
    
    builder = StateGraph(State)
    builder.add_node("chatbot", chatbot_node)
    builder.set_entry_point("chatbot")
    builder.set_finish_point("chatbot")
    graph = builder.compile()
    graph.invoke({"messages": []})
    # {
    #     'messages': [
    #         HumanMessage(
    #             content=[
    #                 {"type": "text", "text": "Here's an image:"},
    #                 {
    #                     "type": "image_url",
    #                     "image_url": {"url": "data:image/jpeg;base64,1234"},
    #                 },
    #             ],
    #         ),
    #     ]
    # }
    

Back to top

---
