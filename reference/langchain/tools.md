# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:27.

## Converted Web Pages

### Tools | LangChain Reference

**Source:** https://reference.langchain.com/python/langchain/tools/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langchain/tools.md "Edit this page")

# Tools

Reference docs

This page contains **reference documentation** for Tools. See [the docs](https://docs.langchain.com/oss/python/langchain/tools) for conceptual guides, tutorials, and examples on using Tools.

##  `` langchain.tools.tool ¶
    
    
    tool(
        name_or_callable: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | None = None,
        runnable: [Runnable](../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span> \(<code>langchain_core.runnables.Runnable</code>\)") | None = None,
        *args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
        description: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        return_direct: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        args_schema: ArgsSchema | None = None,
        infer_schema: [bool](https://docs.python.org/3/library/functions.html#bool) = True,
        response_format: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")["content", "content_and_artifact"] = "content",
        parse_docstring: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        error_on_invalid_docstring: [bool](https://docs.python.org/3/library/functions.html#bool) = True,
    ) -> BaseTool | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [Runnable](../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span> \(<code>langchain_core.runnables.Runnable</code>\)")], BaseTool]
    

Convert Python functions and `Runnables` to LangChain tools.

Can be used as a decorator with or without arguments to create tools from functions.

Functions can have any signature - the tool will automatically infer input schemas unless disabled.

Requirements

  * Functions must have type hints for proper schema inference
  * When `infer_schema=False`, functions must be `(str) -> str` and have docstrings
  * When using with `Runnable`, a string name must be provided



PARAMETER | DESCRIPTION  
---|---  
`name_or_callable` |  Optional name of the tool or the `Callable` to be converted to a tool. Overrides the function's name. Must be provided as a positional argument. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | None` **DEFAULT:** `None`  
`runnable` |  Optional `Runnable` to convert to a tool. Must be provided as a positional argument. **TYPE:** `[Runnable](../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span> \(<code>langchain_core.runnables.Runnable</code>\)") | None` **DEFAULT:** `None`  
`description` |  Optional description for the tool. Precedence for the tool description value is as follows:

  * This `description` argument (used even if docstring and/or `args_schema` are provided)
  * Tool function docstring (used even if `args_schema` is provided)
  * `args_schema` description (used only if `description` and docstring are not provided)

**TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`*args` |  Extra positional arguments. Must be empty. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `()`  
`return_direct` |  Whether to return directly from the tool rather than continuing the agent loop. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`args_schema` |  Optional argument schema for user to specify. **TYPE:** `ArgsSchema | None` **DEFAULT:** `None`  
`infer_schema` |  Whether to infer the schema of the arguments from the function's signature. This also makes the resultant tool accept a dictionary input to its `run()` function. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
`response_format` |  The tool response format. If `'content'`, then the output of the tool is interpreted as the contents of a `ToolMessage`. If `'content_and_artifact'`, then the output is expected to be a two-tuple corresponding to the `(content, artifact)` of a `ToolMessage`. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['content', 'content_and_artifact']` **DEFAULT:** `'content'`  
`parse_docstring` |  If `infer_schema` and `parse_docstring`, will attempt to parse parameter descriptions from Google Style function docstrings. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`error_on_invalid_docstring` |  If `parse_docstring` is provided, configure whether to raise `ValueError` on invalid Google Style docstrings. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If too many positional arguments are provided (e.g. violating the `*args` constraint).  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If a `Runnable` is provided without a string name. When using `tool` with a `Runnable`, a `str` name must be provided as the `name_or_callable`.  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If the first argument is not a string or callable with a `__name__` attribute.  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If the function does not have a docstring and description is not provided and `infer_schema` is `False`.  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If `parse_docstring` is `True` and the function has an invalid Google-style docstring and `error_on_invalid_docstring` is True.  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If a `Runnable` is provided that does not have an object schema.  
RETURNS | DESCRIPTION  
---|---  
`BaseTool | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [Runnable](../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span> \(<code>langchain_core.runnables.Runnable</code>\)")], BaseTool]` |  The tool.  
  
Examples:
    
    
    @tool
    def search_api(query: str) -> str:
        # Searches the API for the query.
        return
    
    
    @tool("search", return_direct=True)
    def search_api(query: str) -> str:
        # Searches the API for the query.
        return
    
    
    @tool(response_format="content_and_artifact")
    def search_api(query: str) -> tuple[str, dict]:
        return "partial json of results", {"full": "object of results"}
    

Parse Google-style docstrings:
    
    
    @tool(parse_docstring=True)
    def foo(bar: str, baz: int) -> str:
        """The foo.
    
        Args:
            bar: The bar.
            baz: The baz.
        """
        return bar
    
    foo.args_schema.model_json_schema()
    
    
    
    {
        "title": "foo",
        "description": "The foo.",
        "type": "object",
        "properties": {
            "bar": {
                "title": "Bar",
                "description": "The bar.",
                "type": "string",
            },
            "baz": {
                "title": "Baz",
                "description": "The baz.",
                "type": "integer",
            },
        },
        "required": ["bar", "baz"],
    }
    

Note that parsing by default will raise `ValueError` if the docstring is considered invalid. A docstring is considered invalid if it contains arguments not in the function signature, or is unable to be parsed into a summary and `"Args:"` blocks. Examples below:
    
    
    # No args section
    def invalid_docstring_1(bar: str, baz: int) -> str:
        """The foo."""
        return bar
    
    # Improper whitespace between summary and args section
    def invalid_docstring_2(bar: str, baz: int) -> str:
        """The foo.
        Args:
            bar: The bar.
            baz: The baz.
        """
        return bar
    
    # Documented args absent from function signature
    def invalid_docstring_3(bar: str, baz: int) -> str:
        """The foo.
    
        Args:
            banana: The bar.
            monkey: The baz.
        """
        return bar
    

##  `` langchain.tools.BaseTool ¶

Bases: `[RunnableSerializable](../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span> \(<code>langchain_core.runnables.RunnableSerializable</code>\)")[[str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict) | [ToolCall](../messages/#langchain.messages.ToolCall "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolCall</span> \(<code>langchain_core.messages.tool.ToolCall</code>\)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`

Base class for all LangChain tools.

This abstract class defines the interface that all LangChain tools must implement.

Tools are components that can be called by agents to perform specific actions.

METHOD | DESCRIPTION  
---|---  
`invoke` |  Transform a single input into an output.  
`ainvoke` |  Transform a single input into an output.  
`get_input_schema` |  The tool's input schema.  
`get_output_schema` |  Get a Pydantic model that can be used to validate output to the `Runnable`.  
  
###  `` name `instance-attribute` ¶
    
    
    name: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

The unique name of the tool that clearly communicates its purpose.

###  `` description `instance-attribute` ¶
    
    
    description: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

Used to tell the model how/when/why to use the tool.

You can provide few-shot examples as a part of the description.

###  `` response_format `class-attribute` `instance-attribute` ¶
    
    
    response_format: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['content', 'content_and_artifact'] = 'content'
    

The tool response format.

If `'content'` then the output of the tool is interpreted as the contents of a `ToolMessage`. If `'content_and_artifact'` then the output is expected to be a two-tuple corresponding to the `(content, artifact)` of a `ToolMessage`.

###  `` invoke ¶
    
    
    invoke(
        input: [str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict) | [ToolCall](../messages/#langchain.messages.ToolCall "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolCall</span> \(<code>langchain_core.messages.tool.ToolCall</code>\)"), config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Transform a single input into an output.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input to the `Runnable`. **TYPE:** `Input`  
`config` |  A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. **TYPE:** `[RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`Output` |  The output of the `Runnable`.  
  
###  `` ainvoke `async` ¶
    
    
    ainvoke(
        input: [str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict) | [ToolCall](../messages/#langchain.messages.ToolCall "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolCall</span> \(<code>langchain_core.messages.tool.ToolCall</code>\)"), config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Transform a single input into an output.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input to the `Runnable`. **TYPE:** `Input`  
`config` |  A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. **TYPE:** `[RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`Output` |  The output of the `Runnable`.  
  
###  `` get_input_schema ¶
    
    
    get_input_schema(config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None = None) -> [type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]
    

The tool's input schema.

PARAMETER | DESCRIPTION  
---|---  
`config` |  The configuration for the tool. **TYPE:** `[RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]` |  The input schema for the tool.  
  
###  `` get_output_schema ¶
    
    
    get_output_schema(config: [RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None) -> [type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]
    

Get a Pydantic model that can be used to validate output to the `Runnable`.

`Runnable` objects that leverage the `configurable_fields` and `configurable_alternatives` methods will have a dynamic output schema that depends on which configuration the `Runnable` is invoked with.

This method allows to get an output schema for a specific configuration.

PARAMETER | DESCRIPTION  
---|---  
`config` |  A config to use when generating the schema. **TYPE:** `[RunnableConfig](../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]` |  A Pydantic model that can be used to validate output.  
  
##  `` langchain.tools.InjectedState ¶

Bases: `InjectedToolArg`

Annotation for injecting graph state into tool arguments.

This annotation enables tools to access graph state without exposing state management details to the language model. Tools annotated with `InjectedState` receive state data automatically during execution while remaining invisible to the model's tool-calling interface.

PARAMETER | DESCRIPTION  
---|---  
`field` |  Optional key to extract from the state dictionary. If `None`, the entire state is injected. If specified, only that field's value is injected. This allows tools to request specific state components rather than processing the full state structure. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
Example
    
    
    from typing import List
    from typing_extensions import Annotated, TypedDict
    
    from langchain_core.messages import BaseMessage, AIMessage
    from langchain.tools import InjectedState, ToolNode, tool
    
    
    class AgentState(TypedDict):
        messages: List[BaseMessage]
        foo: str
    
    
    @tool
    def state_tool(x: int, state: Annotated[dict, InjectedState]) -> str:
        '''Do something with state.'''
        if len(state["messages"]) > 2:
            return state["foo"] + str(x)
        else:
            return "not enough messages"
    
    
    @tool
    def foo_tool(x: int, foo: Annotated[str, InjectedState("foo")]) -> str:
        '''Do something else with state.'''
        return foo + str(x + 1)
    
    
    node = ToolNode([state_tool, foo_tool])
    
    tool_call1 = {"name": "state_tool", "args": {"x": 1}, "id": "1", "type": "tool_call"}
    tool_call2 = {"name": "foo_tool", "args": {"x": 1}, "id": "2", "type": "tool_call"}
    state = {
        "messages": [AIMessage("", tool_calls=[tool_call1, tool_call2])],
        "foo": "bar",
    }
    node.invoke(state)
    
    
    
    [
        ToolMessage(content="not enough messages", name="state_tool", tool_call_id="1"),
        ToolMessage(content="bar2", name="foo_tool", tool_call_id="2"),
    ]
    

Note

  * `InjectedState` arguments are automatically excluded from tool schemas presented to language models
  * `ToolNode` handles the injection process during execution
  * Tools can mix regular arguments (controlled by the model) with injected arguments (controlled by the system)
  * State injection occurs after the model generates tool calls but before tool execution



METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the `InjectedState` annotation.  
  
###  `` __init__ ¶
    
    
    __init__(field: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None) -> None
    

Initialize the `InjectedState` annotation.

##  `` langchain.tools.InjectedStore ¶

Bases: `InjectedToolArg`

Annotation for injecting persistent store into tool arguments.

This annotation enables tools to access LangGraph's persistent storage system without exposing storage details to the language model. Tools annotated with `InjectedStore` receive the store instance automatically during execution while remaining invisible to the model's tool-calling interface.

The store provides persistent, cross-session data storage that tools can use for maintaining context, user preferences, or any other data that needs to persist beyond individual workflow executions.

Warning

`InjectedStore` annotation requires `langchain-core >= 0.3.8`

Example
    
    
    from typing_extensions import Annotated
    from langgraph.store.memory import InMemoryStore
    from langchain.tools import InjectedStore, ToolNode, tool
    
    @tool
    def save_preference(
        key: str,
        value: str,
        store: Annotated[Any, InjectedStore()]
    ) -> str:
        """Save user preference to persistent storage."""
        store.put(("preferences",), key, value)
        return f"Saved {key} = {value}"
    
    @tool
    def get_preference(
        key: str,
        store: Annotated[Any, InjectedStore()]
    ) -> str:
        """Retrieve user preference from persistent storage."""
        result = store.get(("preferences",), key)
        return result.value if result else "Not found"
    

Usage with `ToolNode` and graph compilation:
    
    
    from langgraph.graph import StateGraph
    from langgraph.store.memory import InMemoryStore
    
    store = InMemoryStore()
    tool_node = ToolNode([save_preference, get_preference])
    
    graph = StateGraph(State)
    graph.add_node("tools", tool_node)
    compiled_graph = graph.compile(store=store)  # Store is injected automatically
    

Cross-session persistence:
    
    
    # First session
    result1 = graph.invoke({"messages": [HumanMessage("Save my favorite color as blue")]})
    
    # Later session - data persists
    result2 = graph.invoke({"messages": [HumanMessage("What's my favorite color?")]})
    

Note

  * `InjectedStore` arguments are automatically excluded from tool schemas presented to language models
  * The store instance is automatically injected by `ToolNode` during execution
  * Tools can access namespaced storage using the store's get/put methods
  * Store injection requires the graph to be compiled with a store instance
  * Multiple tools can share the same store instance for data consistency



##  `` langchain.tools.InjectedToolArg ¶

Annotation for tool arguments that are injected at runtime.

Tool arguments annotated with this class are not included in the tool schema sent to language models and are instead injected during execution.

##  `` langchain.tools.InjectedToolCallId ¶

Bases: `InjectedToolArg`

Annotation for injecting the tool call ID.

This annotation is used to mark a tool parameter that should receive the tool call ID at runtime.
    
    
    from typing import Annotated
    from langchain_core.messages import ToolMessage
    from langchain_core.tools import tool, InjectedToolCallId
    
    @tool
    def foo(
        x: int, tool_call_id: Annotated[str, InjectedToolCallId]
    ) -> ToolMessage:
        """Return x."""
        return ToolMessage(
            str(x),
            artifact=x,
            name="foo",
            tool_call_id=tool_call_id
        )
    

Back to top

---
