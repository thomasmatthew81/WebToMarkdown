# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:31.

## Converted Web Pages

### Pregel | LangChain Reference

**Source:** https://reference.langchain.com/python/langgraph/pregel/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langgraph/pregel.md "Edit this page")

# Pregel

##  `` langgraph.pregel.NodeBuilder ¶

METHOD | DESCRIPTION  
---|---  
`subscribe_only` |  Subscribe to a single channel.  
`subscribe_to` |  Add channels to subscribe to. Node will be invoked when any of these  
`read_from` |  Adds the specified channels to read from, without subscribing to them.  
`do` |  Adds the specified node.  
`write_to` |  Add channel writes.  
`meta` |  Add tags or metadata to the node.  
`build` |  Builds the node.  
  
###  `` subscribe_only ¶
    
    
    subscribe_only(channel: [str](https://docs.python.org/3/library/stdtypes.html#str)) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Subscribe to a single channel.

###  `` subscribe_to ¶
    
    
    subscribe_to(*channels: [str](https://docs.python.org/3/library/stdtypes.html#str), read: [bool](https://docs.python.org/3/library/functions.html#bool) = True) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Add channels to subscribe to. Node will be invoked when any of these channels are updated, with a dict of the channel values as input.

PARAMETER | DESCRIPTION  
---|---  
`channels` |  Channel name(s) to subscribe to **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)` **DEFAULT:** `()`  
`read` |  If `True`, the channels will be included in the input to the node. Otherwise, they will trigger the node without being sent in input. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
RETURNS | DESCRIPTION  
---|---  
`[Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")` |  Self for chaining  
  
###  `` read_from ¶
    
    
    read_from(*channels: [str](https://docs.python.org/3/library/stdtypes.html#str)) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Adds the specified channels to read from, without subscribing to them.

###  `` do ¶
    
    
    do(node: RunnableLike) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Adds the specified node.

###  `` write_to ¶
    
    
    write_to(*channels: [str](https://docs.python.org/3/library/stdtypes.html#str) | ChannelWriteEntry, **kwargs: _WriteValue) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Add channel writes.

PARAMETER | DESCRIPTION  
---|---  
`*channels` |  Channel names to write to **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | ChannelWriteEntry` **DEFAULT:** `()`  
`**kwargs` |  Channel name and value mappings **TYPE:** `_WriteValue` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")` |  Self for chaining  
  
###  `` meta ¶
    
    
    meta(*tags: [str](https://docs.python.org/3/library/stdtypes.html#str), **metadata: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Add tags or metadata to the node.

###  `` build ¶
    
    
    build() -> PregelNode
    

Builds the node.

##  `` langgraph.pregel.Pregel ¶

Bases: `PregelProtocol[StateT, ContextT, InputT, OutputT]`, `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "<code>typing.Generic</code>")[StateT, ContextT, InputT, OutputT]`

Pregel manages the runtime behavior for LangGraph applications.

#### Overview¶

Pregel combines [**actors**](https://en.wikipedia.org/wiki/Actor_model) and **channels** into a single application. **Actors** read data from channels and write data to channels. Pregel organizes the execution of the application into multiple steps, following the **Pregel Algorithm** /**Bulk Synchronous Parallel** model.

Each step consists of three phases:

  * **Plan** : Determine which **actors** to execute in this step. For example, in the first step, select the **actors** that subscribe to the special **input** channels; in subsequent steps, select the **actors** that subscribe to channels updated in the previous step.
  * **Execution** : Execute all selected **actors** in parallel, until all complete, or one fails, or a timeout is reached. During this phase, channel updates are invisible to actors until the next step.
  * **Update** : Update the channels with the values written by the **actors** in this step.



Repeat until no **actors** are selected for execution, or a maximum number of steps is reached.

#### Actors¶

An **actor** is a `PregelNode`. It subscribes to channels, reads data from them, and writes data to them. It can be thought of as an **actor** in the Pregel algorithm. `PregelNodes` implement LangChain's Runnable interface.

#### Channels¶

Channels are used to communicate between actors (`PregelNodes`). Each channel has a value type, an update type, and an update function – which takes a sequence of updates and modifies the stored value. Channels can be used to send data from one chain to another, or to send data from a chain to itself in a future step. LangGraph provides a number of built-in channels:

##### Basic channels: LastValue and Topic¶

  * `LastValue`: The default channel, stores the last value sent to the channel, useful for input and output values, or for sending data from one step to the next
  * `Topic`: A configurable PubSub Topic, useful for sending multiple values between _actors_ , or for accumulating output. Can be configured to deduplicate values, and/or to accumulate values over the course of multiple steps.



##### Advanced channels: Context and BinaryOperatorAggregate¶

  * `Context`: exposes the value of a context manager, managing its lifecycle. Useful for accessing external resources that require setup and/or teardown. eg. `client = Context(httpx.Client)`
  * `BinaryOperatorAggregate`: stores a persistent value, updated by applying a binary operator to the current value and each update sent to the channel, useful for computing aggregates over multiple steps. eg. `total = BinaryOperatorAggregate(int, operator.add)`



#### Examples¶

Most users will interact with Pregel via a [StateGraph (Graph API)](../graphs/#langgraph.graph.state.StateGraph "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.graph.state.StateGraph</span>") or via an [entrypoint (Functional API)](../func/#langgraph.func.entrypoint "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">entrypoint</span>").

However, for **advanced** use cases, Pregel can be used directly. If you're not sure whether you need to use Pregel directly, then the answer is probably no \- you should use the Graph API or Functional API instead. These are higher-level interfaces that will compile down to Pregel under the hood.

Here are some examples to give you a sense of how it works:

Single node application
    
    
    from langgraph.channels import EphemeralValue
    from langgraph.pregel import Pregel, NodeBuilder
    
    node1 = (
        NodeBuilder().subscribe_only("a")
        .do(lambda x: x + x)
        .write_to("b")
    )
    
    app = Pregel(
        nodes={"node1": node1},
        channels={
            "a": EphemeralValue(str),
            "b": EphemeralValue(str),
        },
        input_channels=["a"],
        output_channels=["b"],
    )
    
    app.invoke({"a": "foo"})
    
    
    
    {'b': 'foofoo'}
    

Using multiple nodes and multiple output channels
    
    
    from langgraph.channels import LastValue, EphemeralValue
    from langgraph.pregel import Pregel, NodeBuilder
    
    node1 = (
        NodeBuilder().subscribe_only("a")
        .do(lambda x: x + x)
        .write_to("b")
    )
    
    node2 = (
        NodeBuilder().subscribe_to("b")
        .do(lambda x: x["b"] + x["b"])
        .write_to("c")
    )
    
    
    app = Pregel(
        nodes={"node1": node1, "node2": node2},
        channels={
            "a": EphemeralValue(str),
            "b": LastValue(str),
            "c": EphemeralValue(str),
        },
        input_channels=["a"],
        output_channels=["b", "c"],
    )
    
    app.invoke({"a": "foo"})
    
    
    
    {'b': 'foofoo', 'c': 'foofoofoofoo'}
    

Using a Topic channel
    
    
    from langgraph.channels import LastValue, EphemeralValue, Topic
    from langgraph.pregel import Pregel, NodeBuilder
    
    node1 = (
        NodeBuilder().subscribe_only("a")
        .do(lambda x: x + x)
        .write_to("b", "c")
    )
    
    node2 = (
        NodeBuilder().subscribe_only("b")
        .do(lambda x: x + x)
        .write_to("c")
    )
    
    
    app = Pregel(
        nodes={"node1": node1, "node2": node2},
        channels={
            "a": EphemeralValue(str),
            "b": EphemeralValue(str),
            "c": Topic(str, accumulate=True),
        },
        input_channels=["a"],
        output_channels=["c"],
    )
    
    app.invoke({"a": "foo"})
    
    
    
    {"c": ["foofoo", "foofoofoofoo"]}
    

Using a BinaryOperatorAggregate channel
    
    
    from langgraph.channels import EphemeralValue, BinaryOperatorAggregate
    from langgraph.pregel import Pregel, NodeBuilder
    
    
    node1 = (
        NodeBuilder().subscribe_only("a")
        .do(lambda x: x + x)
        .write_to("b", "c")
    )
    
    node2 = (
        NodeBuilder().subscribe_only("b")
        .do(lambda x: x + x)
        .write_to("c")
    )
    
    
    def reducer(current, update):
        if current:
            return current + " | " + update
        else:
            return update
    
    
    app = Pregel(
        nodes={"node1": node1, "node2": node2},
        channels={
            "a": EphemeralValue(str),
            "b": EphemeralValue(str),
            "c": BinaryOperatorAggregate(str, operator=reducer),
        },
        input_channels=["a"],
        output_channels=["c"],
    )
    
    app.invoke({"a": "foo"})
    
    
    
    {'c': 'foofoo | foofoofoofoo'}
    

Introducing a cycle

This example demonstrates how to introduce a cycle in the graph, by having a chain write to a channel it subscribes to. Execution will continue until a None value is written to the channel.
    
    
    from langgraph.channels import EphemeralValue
    from langgraph.pregel import Pregel, NodeBuilder, ChannelWriteEntry
    
    example_node = (
        NodeBuilder()
        .subscribe_only("value")
        .do(lambda x: x + x if len(x) < 10 else None)
        .write_to(ChannelWriteEntry(channel="value", skip_none=True))
    )
    
    app = Pregel(
        nodes={"example_node": example_node},
        channels={
            "value": EphemeralValue(str),
        },
        input_channels=["value"],
        output_channels=["value"],
    )
    
    app.invoke({"value": "a"})
    
    
    
    {'value': 'aaaaaaaaaaaaaaaa'}
    

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

Back to top

---
