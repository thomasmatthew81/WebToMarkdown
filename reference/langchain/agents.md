# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:26.

## Converted Web Pages

### Agents | LangChain Reference

**Source:** https://reference.langchain.com/python/langchain/agents/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langchain/agents.md "Edit this page")

# Agents

Reference docs

This page contains **reference documentation** for Agents. See [the docs](https://docs.langchain.com/oss/python/langchain/agents) for conceptual guides, tutorials, and examples on using Agents.

##  `` langchain.agents ¶

Entrypoint to building [Agents](https://docs.langchain.com/oss/python/langchain/agents) with LangChain.

###  `` create_agent ¶
    
    
    create_agent(
        model: [str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.chat_models.BaseChatModel</code>\)"),
        tools: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[BaseTool](../tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span> \(<code>langchain_core.tools.BaseTool</code>\)") | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]] | None = None,
        *,
        system_prompt: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        middleware: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[AgentMiddleware[StateT_co, ContextT]] = (),
        response_format: ResponseFormat[ResponseT] | [type](https://docs.python.org/3/library/functions.html#type)[ResponseT] | None = None,
        state_schema: [type](https://docs.python.org/3/library/functions.html#type)[AgentState[ResponseT]] | None = None,
        context_schema: [type](https://docs.python.org/3/library/functions.html#type)[ContextT] | None = None,
        checkpointer: Checkpointer | None = None,
        store: [BaseStore](../../langgraph/store/#langgraph.store.base.BaseStore "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseStore</span> \(<code>langgraph.store.base.BaseStore</code>\)") | None = None,
        interrupt_before: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        interrupt_after: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        debug: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        cache: [BaseCache](../../langgraph/cache/#langgraph.cache.base.BaseCache "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseCache</span> \(<code>langgraph.cache.base.BaseCache</code>\)") | None = None,
    ) -> [CompiledStateGraph](../../langgraph/graphs/#langgraph.graph.state.CompiledStateGraph "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.graph.state.CompiledStateGraph</span>")[
        AgentState[ResponseT], ContextT, _InputAgentState, _OutputAgentState[ResponseT]
    ]
    

Creates an agent graph that calls tools in a loop until a stopping condition is met.

For more details on using `create_agent`, visit the [Agents](https://docs.langchain.com/oss/python/langchain/agents) docs.

PARAMETER | DESCRIPTION  
---|---  
  
####  `model` ¶

|  The language model for the agent. Can be a string identifier (e.g., `"openai:gpt-4"`) or a direct chat model instance (e.g., [`ChatOpenAI`](../../integrations/langchain_openai/ChatOpenAI/#langchain_openai.chat_models.ChatOpenAI "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_openai.chat_models.ChatOpenAI</span>") or other another [LangChain chat model](https://docs.langchain.com/oss/python/integrations/chat)). For a full list of supported model strings, see [`init_chat_model`](../models/#langchain.chat_models.init_chat_model\(model_provider\) "<code>model_provider</code>"). See the [Models](https://docs.langchain.com/oss/python/langchain/models) docs for more information. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.chat_models.BaseChatModel</code>\)")`  
  
####  `tools` ¶

|  A list of tools, `dict`, or `Callable`. If `None` or an empty list, the agent will consist of a model node without a tool calling loop. See the [Tools](https://docs.langchain.com/oss/python/langchain/tools) docs for more information. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[BaseTool](../tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span> \(<code>langchain_core.tools.BaseTool</code>\)") | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]] | None` **DEFAULT:** `None`  
  
####  `system_prompt` ¶

|  An optional system prompt for the LLM. Prompts are converted to a [`SystemMessage`](../messages/#langchain.messages.SystemMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">SystemMessage</span>") and added to the beginning of the message list. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
  
####  `middleware` ¶

|  A sequence of middleware instances to apply to the agent. Middleware can intercept and modify agent behavior at various stages. See the [Middleware](https://docs.langchain.com/oss/python/langchain/middleware) docs for more information. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[AgentMiddleware[StateT_co, ContextT]]` **DEFAULT:** `()`  
  
####  `response_format` ¶

|  An optional configuration for structured responses. Can be a `ToolStrategy`, `ProviderStrategy`, or a Pydantic model class. If provided, the agent will handle structured output during the conversation flow. Raw schemas will be wrapped in an appropriate strategy based on model capabilities. See the [Structured output](https://docs.langchain.com/oss/python/langchain/structured-output) docs for more information. **TYPE:** `ResponseFormat[ResponseT] | [type](https://docs.python.org/3/library/functions.html#type)[ResponseT] | None` **DEFAULT:** `None`  
  
####  `state_schema` ¶

|  An optional `TypedDict` schema that extends `AgentState`. When provided, this schema is used instead of `AgentState` as the base schema for merging with middleware state schemas. This allows users to add custom state fields without needing to create custom middleware. Generally, it's recommended to use `state_schema` extensions via middleware to keep relevant extensions scoped to corresponding hooks / tools. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[AgentState[ResponseT]] | None` **DEFAULT:** `None`  
  
####  `context_schema` ¶

|  An optional schema for runtime context. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[ContextT] | None` **DEFAULT:** `None`  
  
####  `checkpointer` ¶

|  An optional checkpoint saver object. Used for persisting the state of the graph (e.g., as chat memory) for a single thread (e.g., a single conversation). **TYPE:** `Checkpointer | None` **DEFAULT:** `None`  
  
####  `store` ¶

|  An optional store object. Used for persisting data across multiple threads (e.g., multiple conversations / users). **TYPE:** `[BaseStore](../../langgraph/store/#langgraph.store.base.BaseStore "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseStore</span> \(<code>langgraph.store.base.BaseStore</code>\)") | None` **DEFAULT:** `None`  
  
####  `interrupt_before` ¶

|  An optional list of node names to interrupt before. Useful if you want to add a user confirmation or other interrupt before taking an action. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
  
####  `interrupt_after` ¶

|  An optional list of node names to interrupt after. Useful if you want to return directly or run additional processing on an output. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
  
####  `debug` ¶

|  Whether to enable verbose logging for graph execution. When enabled, prints detailed information about each node execution, state updates, and transitions during agent runtime. Useful for debugging middleware behavior and understanding agent execution flow. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
  
####  `name` ¶

|  An optional name for the `CompiledStateGraph`. This name will be automatically used when adding the agent graph to another graph as a subgraph node - particularly useful for building multi-agent systems. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
  
####  `cache` ¶

|  An optional `BaseCache` instance to enable caching of graph execution. **TYPE:** `[BaseCache](../../langgraph/cache/#langgraph.cache.base.BaseCache "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseCache</span> \(<code>langgraph.cache.base.BaseCache</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[CompiledStateGraph](../../langgraph/graphs/#langgraph.graph.state.CompiledStateGraph "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.graph.state.CompiledStateGraph</span>")[AgentState[ResponseT], ContextT, _InputAgentState, _OutputAgentState[ResponseT]]` |  A compiled `StateGraph` that can be used for chat interactions.  
  
The agent node calls the language model with the messages list (after applying the system prompt). If the resulting [`AIMessage`](../messages/#langchain.messages.AIMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">AIMessage</span>") contains `tool_calls`, the graph will then call the tools. The tools node executes the tools and adds the responses to the messages list as [`ToolMessage`](../messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span>") objects. The agent node then calls the language model again. The process repeats until no more `tool_calls` are present in the response. The agent then returns the full list of messages.

Example
    
    
    from langchain.agents import create_agent
    
    
    def check_weather(location: str) -> str:
        '''Return the weather forecast for the specified location.'''
        return f"It's always sunny in {location}"
    
    
    graph = create_agent(
        model="anthropic:claude-sonnet-4-5-20250929",
        tools=[check_weather],
        system_prompt="You are a helpful assistant",
    )
    inputs = {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    for chunk in graph.stream(inputs, stream_mode="updates"):
        print(chunk)
    

###  `` AgentState ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`, `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "<code>typing.Generic</code>")[ResponseT]`

State schema for the agent.

Back to top

---
