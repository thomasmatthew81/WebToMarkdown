# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:21.

## Converted Web Pages

### Deep Agents overview | LangChain Reference

**Source:** https://reference.langchain.com/python/deepagents/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/deepagents/index.md "Edit this page")

# Deep Agents reference

[](https://pypi.org/project/deepagents/#history) [](https://opensource.org/licenses/MIT) [](https://pypistats.org/packages/deepagents)

Welcome to the [Deep Agents](https://github.com/langchain-ai/deepagents) reference documentation!

Work in progress

This page is a work in progress, and we appreciate your patience as we continue to expand and improve the content.

##  `` deepagents ¶

DeepAgents package.

FUNCTION | DESCRIPTION  
---|---  
`create_deep_agent` |  Create a deep agent.  
  
###  `` FilesystemMiddleware ¶

Bases: `AgentMiddleware`

Middleware for providing filesystem and optional execution tools to an agent.

This middleware adds filesystem tools to the agent: ls, read_file, write_file, edit_file, glob, and grep. Files can be stored using any backend that implements the BackendProtocol.

If the backend implements SandboxBackendProtocol, an execute tool is also added for running shell commands.

PARAMETER | DESCRIPTION  
---|---  
`backend` |  Backend for file storage and optional execution. If not provided, defaults to StateBackend (ephemeral storage in agent state). For persistent storage or hybrid setups, use CompositeBackend with custom routes. For execution support, use a backend that implements SandboxBackendProtocol. **TYPE:** `BACKEND_TYPES | None` **DEFAULT:** `None`  
`system_prompt` |  Optional custom system prompt override. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`custom_tool_descriptions` |  Optional custom tool descriptions override. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`tool_token_limit_before_evict` |  Optional token limit before evicting a tool result to the filesystem. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int) | None` **DEFAULT:** `20000`  
Example
    
    
    from deepagents.middleware.filesystem import FilesystemMiddleware
    from deepagents.backends import StateBackend, StoreBackend, CompositeBackend
    from langchain.agents import create_agent
    
    # Ephemeral storage only (default, no execution)
    agent = create_agent(middleware=[FilesystemMiddleware()])
    
    # With hybrid storage (ephemeral + persistent /memories/)
    backend = CompositeBackend(default=StateBackend(), routes={"/memories/": StoreBackend()})
    agent = create_agent(middleware=[FilesystemMiddleware(backend=backend)])
    
    # With sandbox backend (supports execution)
    from my_sandbox import DockerSandboxBackend
    
    sandbox = DockerSandboxBackend(container_id="my-container")
    agent = create_agent(middleware=[FilesystemMiddleware(backend=sandbox)])
    

METHOD | DESCRIPTION  
---|---  
`before_agent` |  Logic to run before the agent execution starts.  
`abefore_agent` |  Async logic to run before the agent execution starts.  
`before_model` |  Logic to run before the model is called.  
`abefore_model` |  Async logic to run before the model is called.  
`after_model` |  Logic to run after the model is called.  
`aafter_model` |  Async logic to run after the model is called.  
`after_agent` |  Logic to run after the agent execution completes.  
`aafter_agent` |  Async logic to run after the agent execution completes.  
`__init__` |  Initialize the filesystem middleware.  
`wrap_model_call` |  Update the system prompt and filter tools based on backend capabilities.  
`awrap_model_call` |  (async) Update the system prompt and filter tools based on backend capabilities.  
`wrap_tool_call` |  Check the size of the tool call result and evict to filesystem if too large.  
`awrap_tool_call` |  (async)Check the size of the tool call result and evict to filesystem if too large.  
  
####  `` name `property` ¶
    
    
    name: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

The name of the middleware instance.

Defaults to the class name, but can be overridden for custom naming.

####  `` state_schema `class-attribute` `instance-attribute` ¶
    
    
    state_schema = FilesystemState
    

The schema for state passed to the middleware nodes.

####  `` tools `instance-attribute` ¶
    
    
    tools = _get_filesystem_tools(backend, custom_tool_descriptions)
    

Additional tools registered by the middleware.

####  `` before_agent ¶
    
    
    before_agent(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Logic to run before the agent execution starts.

####  `` abefore_agent `async` ¶
    
    
    abefore_agent(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Async logic to run before the agent execution starts.

####  `` before_model ¶
    
    
    before_model(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Logic to run before the model is called.

####  `` abefore_model `async` ¶
    
    
    abefore_model(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Async logic to run before the model is called.

####  `` after_model ¶
    
    
    after_model(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Logic to run after the model is called.

####  `` aafter_model `async` ¶
    
    
    aafter_model(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Async logic to run after the model is called.

####  `` after_agent ¶
    
    
    after_agent(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Logic to run after the agent execution completes.

####  `` aafter_agent `async` ¶
    
    
    aafter_agent(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Async logic to run after the agent execution completes.

####  `` __init__ ¶
    
    
    __init__(
        *,
        backend: BACKEND_TYPES | None = None,
        system_prompt: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        custom_tool_descriptions: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        tool_token_limit_before_evict: [int](https://docs.python.org/3/library/functions.html#int) | None = 20000,
    ) -> None
    

Initialize the filesystem middleware.

PARAMETER | DESCRIPTION  
---|---  
`backend` |  Backend for file storage and optional execution, or a factory callable. Defaults to StateBackend if not provided. **TYPE:** `BACKEND_TYPES | None` **DEFAULT:** `None`  
`system_prompt` |  Optional custom system prompt override. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`custom_tool_descriptions` |  Optional custom tool descriptions override. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`tool_token_limit_before_evict` |  Optional token limit before evicting a tool result to the filesystem. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int) | None` **DEFAULT:** `20000`  
  
####  `` wrap_model_call ¶
    
    
    wrap_model_call(
        request: ModelRequest, handler: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ModelRequest], ModelResponse]
    ) -> ModelResponse
    

Update the system prompt and filter tools based on backend capabilities.

PARAMETER | DESCRIPTION  
---|---  
`request` |  The model request being processed. **TYPE:** `ModelRequest`  
`handler` |  The handler function to call with the modified request. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ModelRequest], ModelResponse]`  
RETURNS | DESCRIPTION  
---|---  
`ModelResponse` |  The model response from the handler.  
  
####  `` awrap_model_call `async` ¶
    
    
    awrap_model_call(
        request: ModelRequest, handler: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ModelRequest], [Awaitable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "<code>collections.abc.Awaitable</code>")[ModelResponse]]
    ) -> ModelResponse
    

(async) Update the system prompt and filter tools based on backend capabilities.

PARAMETER | DESCRIPTION  
---|---  
`request` |  The model request being processed. **TYPE:** `ModelRequest`  
`handler` |  The handler function to call with the modified request. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ModelRequest], [Awaitable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "<code>collections.abc.Awaitable</code>")[ModelResponse]]`  
RETURNS | DESCRIPTION  
---|---  
`ModelResponse` |  The model response from the handler.  
  
####  `` wrap_tool_call ¶
    
    
    wrap_tool_call(
        request: ToolCallRequest,
        handler: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ToolCallRequest], [ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.Command</code>\)")],
    ) -> [ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.Command</code>\)")
    

Check the size of the tool call result and evict to filesystem if too large.

PARAMETER | DESCRIPTION  
---|---  
`request` |  The tool call request being processed. **TYPE:** `ToolCallRequest`  
`handler` |  The handler function to call with the modified request. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ToolCallRequest], [ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.Command</code>\)")]`  
RETURNS | DESCRIPTION  
---|---  
`[ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.Command</code>\)")` |  The raw ToolMessage, or a pseudo tool message with the ToolResult in state.  
  
####  `` awrap_tool_call `async` ¶
    
    
    awrap_tool_call(
        request: ToolCallRequest,
        handler: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ToolCallRequest], [Awaitable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "<code>collections.abc.Awaitable</code>")[[ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.Command</code>\)")]],
    ) -> [ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.Command</code>\)")
    

(async)Check the size of the tool call result and evict to filesystem if too large.

PARAMETER | DESCRIPTION  
---|---  
`request` |  The tool call request being processed. **TYPE:** `ToolCallRequest`  
`handler` |  The handler function to call with the modified request. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ToolCallRequest], [Awaitable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "<code>collections.abc.Awaitable</code>")[[ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.Command</code>\)")]]`  
RETURNS | DESCRIPTION  
---|---  
`[ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.Command</code>\)")` |  The raw ToolMessage, or a pseudo tool message with the ToolResult in state.  
  
###  `` CompiledSubAgent ¶

Bases: `[TypedDict](https://docs.python.org/3/library/typing.html#typing.TypedDict "<code>typing.TypedDict</code>")`

A pre-compiled agent spec.

####  `` name `instance-attribute` ¶
    
    
    name: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

The name of the agent.

####  `` description `instance-attribute` ¶
    
    
    description: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

The description of the agent.

####  `` runnable `instance-attribute` ¶
    
    
    runnable: [Runnable](../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span> \(<code>langchain_core.runnables.Runnable</code>\)")
    

The Runnable to use for the agent.

###  `` SubAgent ¶

Bases: `[TypedDict](https://docs.python.org/3/library/typing.html#typing.TypedDict "<code>typing.TypedDict</code>")`

Specification for an agent.

When specifying custom agents, the `default_middleware` from `SubAgentMiddleware` will be applied first, followed by any `middleware` specified in this spec. To use only custom middleware without the defaults, pass `default_middleware=[]` to `SubAgentMiddleware`.

####  `` name `instance-attribute` ¶
    
    
    name: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

The name of the agent.

####  `` description `instance-attribute` ¶
    
    
    description: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

The description of the agent.

####  `` system_prompt `instance-attribute` ¶
    
    
    system_prompt: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

The system prompt to use for the agent.

####  `` tools `instance-attribute` ¶
    
    
    tools: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[BaseTool](../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span>") | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

The tools to use for the agent.

####  `` model `instance-attribute` ¶
    
    
    model: [NotRequired](https://docs.python.org/3/library/typing.html#typing.NotRequired "<code>typing.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.BaseChatModel</code>\)")]
    

The model for the agent. Defaults to `default_model`.

####  `` middleware `instance-attribute` ¶
    
    
    middleware: [NotRequired](https://docs.python.org/3/library/typing.html#typing.NotRequired "<code>typing.NotRequired</code>")[[list](https://docs.python.org/3/library/stdtypes.html#list)[AgentMiddleware]]
    

Additional middleware to append after `default_middleware`.

####  `` interrupt_on `instance-attribute` ¶
    
    
    interrupt_on: [NotRequired](https://docs.python.org/3/library/typing.html#typing.NotRequired "<code>typing.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [bool](https://docs.python.org/3/library/functions.html#bool) | InterruptOnConfig]]
    

The tool configs to use for the agent.

###  `` SubAgentMiddleware ¶

Bases: `AgentMiddleware`

Middleware for providing subagents to an agent via a `task` tool.

This middleware adds a `task` tool to the agent that can be used to invoke subagents. Subagents are useful for handling complex tasks that require multiple steps, or tasks that require a lot of context to resolve.

A chief benefit of subagents is that they can handle multi-step tasks, and then return a clean, concise response to the main agent.

Subagents are also great for different domains of expertise that require a narrower subset of tools and focus.

This middleware comes with a default general-purpose subagent that can be used to handle the same tasks as the main agent, but with isolated context.

PARAMETER | DESCRIPTION  
---|---  
`default_model` |  The model to use for subagents. Can be a LanguageModelLike or a dict for init_chat_model. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.BaseChatModel</code>\)")`  
`default_tools` |  The tools to use for the default general-purpose subagent. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[BaseTool](../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span>") | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]] | None` **DEFAULT:** `None`  
`default_middleware` |  Default middleware to apply to all subagents. If `None` (default), no default middleware is applied. Pass a list to specify custom middleware. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[AgentMiddleware] | None` **DEFAULT:** `None`  
`default_interrupt_on` |  The tool configs to use for the default general-purpose subagent. These are also the fallback for any subagents that don't specify their own tool configs. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [bool](https://docs.python.org/3/library/functions.html#bool) | InterruptOnConfig] | None` **DEFAULT:** `None`  
`subagents` |  A list of additional subagents to provide to the agent. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[SubAgent | CompiledSubAgent] | None` **DEFAULT:** `None`  
`system_prompt` |  Full system prompt override. When provided, completely replaces the agent's system prompt. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `TASK_SYSTEM_PROMPT`  
`general_purpose_agent` |  Whether to include the general-purpose agent. Defaults to `True`. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
`task_description` |  Custom description for the task tool. If `None`, uses the default description template. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
Example
    
    
    from langchain.agents.middleware.subagents import SubAgentMiddleware
    from langchain.agents import create_agent
    
    # Basic usage with defaults (no default middleware)
    agent = create_agent(
        "openai:gpt-4o",
        middleware=[
            SubAgentMiddleware(
                default_model="openai:gpt-4o",
                subagents=[],
            )
        ],
    )
    
    # Add custom middleware to subagents
    agent = create_agent(
        "openai:gpt-4o",
        middleware=[
            SubAgentMiddleware(
                default_model="openai:gpt-4o",
                default_middleware=[TodoListMiddleware()],
                subagents=[],
            )
        ],
    )
    

METHOD | DESCRIPTION  
---|---  
`before_agent` |  Logic to run before the agent execution starts.  
`abefore_agent` |  Async logic to run before the agent execution starts.  
`before_model` |  Logic to run before the model is called.  
`abefore_model` |  Async logic to run before the model is called.  
`after_model` |  Logic to run after the model is called.  
`aafter_model` |  Async logic to run after the model is called.  
`after_agent` |  Logic to run after the agent execution completes.  
`aafter_agent` |  Async logic to run after the agent execution completes.  
`wrap_tool_call` |  Intercept tool execution for retries, monitoring, or modification.  
`awrap_tool_call` |  Intercept and control async tool execution via handler callback.  
`__init__` |  Initialize the SubAgentMiddleware.  
`wrap_model_call` |  Update the system prompt to include instructions on using subagents.  
`awrap_model_call` |  (async) Update the system prompt to include instructions on using subagents.  
  
####  `` state_schema `class-attribute` `instance-attribute` ¶
    
    
    state_schema: [type](https://docs.python.org/3/library/functions.html#type)[StateT] = [cast](https://docs.python.org/3/library/typing.html#typing.cast "<code>typing.cast</code>")('type[StateT]', [AgentState](../langchain/agents/#langchain.agents.AgentState "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">AgentState</span> \(<code>langchain.agents.middleware.types.AgentState</code>\)"))
    

The schema for state passed to the middleware nodes.

####  `` name `property` ¶
    
    
    name: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

The name of the middleware instance.

Defaults to the class name, but can be overridden for custom naming.

####  `` tools `instance-attribute` ¶
    
    
    tools = [task_tool]
    

Additional tools registered by the middleware.

####  `` before_agent ¶
    
    
    before_agent(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Logic to run before the agent execution starts.

####  `` abefore_agent `async` ¶
    
    
    abefore_agent(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Async logic to run before the agent execution starts.

####  `` before_model ¶
    
    
    before_model(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Logic to run before the model is called.

####  `` abefore_model `async` ¶
    
    
    abefore_model(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Async logic to run before the model is called.

####  `` after_model ¶
    
    
    after_model(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Logic to run after the model is called.

####  `` aafter_model `async` ¶
    
    
    aafter_model(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Async logic to run after the model is called.

####  `` after_agent ¶
    
    
    after_agent(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Logic to run after the agent execution completes.

####  `` aafter_agent `async` ¶
    
    
    aafter_agent(state: StateT, runtime: [Runtime](../langgraph/runtime/#langgraph.runtime.Runtime "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.runtime.Runtime</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span>")[ContextT]) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None
    

Async logic to run after the agent execution completes.

####  `` wrap_tool_call ¶
    
    
    wrap_tool_call(
        request: ToolCallRequest,
        handler: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ToolCallRequest], [ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.Command</code>\)")],
    ) -> [ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.Command</code>\)")
    

Intercept tool execution for retries, monitoring, or modification.

Multiple middleware compose automatically (first defined = outermost).

Exceptions propagate unless `handle_tool_errors` is configured on `ToolNode`.

PARAMETER | DESCRIPTION  
---|---  
`request` |  Tool call request with call `dict`, `BaseTool`, state, and runtime. Access state via `request.state` and runtime via `request.runtime`. **TYPE:** `ToolCallRequest`  
`handler` |  `Callable` to execute the tool (can be called multiple times). **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ToolCallRequest], [ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.Command</code>\)")]`  
RETURNS | DESCRIPTION  
---|---  
`[ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.Command</code>\)")` |  `ToolMessage` or `Command` (the final result).  
  
The handler `Callable` can be invoked multiple times for retry logic.

Each call to handler is independent and stateless.

Examples:

Modify request before execution
    
    
    def wrap_tool_call(self, request, handler):
        request.tool_call["args"]["value"] *= 2
        return handler(request)
    

Retry on error (call handler multiple times)
    
    
    def wrap_tool_call(self, request, handler):
        for attempt in range(3):
            try:
                result = handler(request)
                if is_valid(result):
                    return result
            except Exception:
                if attempt == 2:
                    raise
        return result
    

Conditional retry based on response
    
    
    def wrap_tool_call(self, request, handler):
        for attempt in range(3):
            result = handler(request)
            if isinstance(result, ToolMessage) and result.status != "error":
                return result
            if attempt < 2:
                continue
            return result
    

####  `` awrap_tool_call `async` ¶
    
    
    awrap_tool_call(
        request: ToolCallRequest,
        handler: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ToolCallRequest], [Awaitable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "<code>collections.abc.Awaitable</code>")[[ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.Command</code>\)")]],
    ) -> [ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
      </span> \(<code>langgraph.types.Command</code>\)")
    

Intercept and control async tool execution via handler callback.

The handler callback executes the tool call and returns a `ToolMessage` or `Command`. Middleware can call the handler multiple times for retry logic, skip calling it to short-circuit, or modify the request/response. Multiple middleware compose with first in list as outermost layer.

PARAMETER | DESCRIPTION  
---|---  
`request` |  Tool call request with call `dict`, `BaseTool`, state, and runtime. Access state via `request.state` and runtime via `request.runtime`. **TYPE:** `ToolCallRequest`  
`handler` |  Async callable to execute the tool and returns `ToolMessage` or `Command`. Call this to execute the tool. Can be called multiple times for retry logic. Can skip calling it to short-circuit. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ToolCallRequest], [Awaitable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "<code>collections.abc.Awaitable</code>")[[ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.Command</code>\)")]]`  
RETURNS | DESCRIPTION  
---|---  
`[ToolMessage](../langchain/messages/#langchain.messages.ToolMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ToolMessage</span> \(<code>langchain_core.messages.ToolMessage</code>\)") | [Command](../langgraph/types/#langgraph.types.Command "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Command</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span> \(<code>langgraph.types.Command</code>\)")` |  `ToolMessage` or `Command` (the final result).  
  
The handler `Callable` can be invoked multiple times for retry logic.

Each call to handler is independent and stateless.

Examples:

Async retry on error
    
    
    async def awrap_tool_call(self, request, handler):
        for attempt in range(3):
            try:
                result = await handler(request)
                if is_valid(result):
                    return result
            except Exception:
                if attempt == 2:
                    raise
        return result
    
    
    
    async def awrap_tool_call(self, request, handler):
        if cached := await get_cache_async(request):
            return ToolMessage(content=cached, tool_call_id=request.tool_call["id"])
        result = await handler(request)
        await save_cache_async(request, result)
        return result
    

####  `` __init__ ¶
    
    
    __init__(
        *,
        default_model: [str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.BaseChatModel</code>\)"),
        default_tools: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[BaseTool](../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span>") | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]] | None = None,
        default_middleware: [list](https://docs.python.org/3/library/stdtypes.html#list)[AgentMiddleware] | None = None,
        default_interrupt_on: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [bool](https://docs.python.org/3/library/functions.html#bool) | InterruptOnConfig] | None = None,
        subagents: [list](https://docs.python.org/3/library/stdtypes.html#list)[SubAgent | CompiledSubAgent] | None = None,
        system_prompt: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = TASK_SYSTEM_PROMPT,
        general_purpose_agent: [bool](https://docs.python.org/3/library/functions.html#bool) = True,
        task_description: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    ) -> None
    

Initialize the SubAgentMiddleware.

####  `` wrap_model_call ¶
    
    
    wrap_model_call(
        request: ModelRequest, handler: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ModelRequest], ModelResponse]
    ) -> ModelResponse
    

Update the system prompt to include instructions on using subagents.

####  `` awrap_model_call `async` ¶
    
    
    awrap_model_call(
        request: ModelRequest, handler: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[ModelRequest], [Awaitable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "<code>collections.abc.Awaitable</code>")[ModelResponse]]
    ) -> ModelResponse
    

(async) Update the system prompt to include instructions on using subagents.

###  `` create_deep_agent ¶
    
    
    create_deep_agent(
        model: [str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.BaseChatModel</code>\)") | None = None,
        tools: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[BaseTool](../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span> \(<code>langchain_core.tools.BaseTool</code>\)") | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]] | None = None,
        *,
        system_prompt: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        middleware: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[AgentMiddleware] = (),
        subagents: [list](https://docs.python.org/3/library/stdtypes.html#list)[SubAgent | CompiledSubAgent] | None = None,
        response_format: ResponseFormat | None = None,
        context_schema: [type](https://docs.python.org/3/library/functions.html#type)[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        checkpointer: Checkpointer | None = None,
        store: [BaseStore](../langgraph/store/#langgraph.store.base.BaseStore "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseStore</span> \(<code>langgraph.store.base.BaseStore</code>\)") | None = None,
        backend: BackendProtocol | BackendFactory | None = None,
        interrupt_on: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [bool](https://docs.python.org/3/library/functions.html#bool) | InterruptOnConfig] | None = None,
        debug: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        cache: [BaseCache](../langgraph/cache/#langgraph.cache.base.BaseCache "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseCache</span> \(<code>langgraph.cache.base.BaseCache</code>\)") | None = None,
    ) -> [CompiledStateGraph](../langgraph/graphs/#langgraph.graph.state.CompiledStateGraph "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.graph.state.CompiledStateGraph</span>")
    

Create a deep agent.

This agent will by default have access to a tool to write todos (write_todos), seven file and execution tools: ls, read_file, write_file, edit_file, glob, grep, execute, and a tool to call subagents.

The execute tool allows running shell commands if the backend implements SandboxBackendProtocol. For non-sandbox backends, the execute tool will return an error message.

PARAMETER | DESCRIPTION  
---|---  
`model` |  The model to use. Defaults to Claude Sonnet 4. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.BaseChatModel</code>\)") | None` **DEFAULT:** `None`  
`tools` |  The tools the agent should have access to. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[BaseTool](../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span> \(<code>langchain_core.tools.BaseTool</code>\)") | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]] | None` **DEFAULT:** `None`  
`system_prompt` |  The additional instructions the agent should have. Will go in the system prompt. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`middleware` |  Additional middleware to apply after standard middleware. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[AgentMiddleware]` **DEFAULT:** `()`  
`subagents` |  The subagents to use. Each subagent should be a dictionary with the following keys: \- `name` \- `description` (used by the main agent to decide whether to call the sub agent) \- `prompt` (used as the system prompt in the subagent) \- (optional) `tools` \- (optional) `model` (either a LanguageModelLike instance or dict settings) \- (optional) `middleware` (list of AgentMiddleware) **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[SubAgent | CompiledSubAgent] | None` **DEFAULT:** `None`  
`response_format` |  A structured output response format to use for the agent. **TYPE:** `ResponseFormat | None` **DEFAULT:** `None`  
`context_schema` |  The schema of the deep agent. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`checkpointer` |  Optional checkpointer for persisting agent state between runs. **TYPE:** `Checkpointer | None` **DEFAULT:** `None`  
`store` |  Optional store for persistent storage (required if backend uses StoreBackend). **TYPE:** `[BaseStore](../langgraph/store/#langgraph.store.base.BaseStore "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseStore</span> \(<code>langgraph.store.base.BaseStore</code>\)") | None` **DEFAULT:** `None`  
`backend` |  Optional backend for file storage and execution. Pass either a Backend instance or a callable factory like `lambda rt: StateBackend(rt)`. For execution support, use a backend that implements SandboxBackendProtocol. **TYPE:** `BackendProtocol | BackendFactory | None` **DEFAULT:** `None`  
`interrupt_on` |  Optional Dict[str, bool | InterruptOnConfig] mapping tool names to interrupt configs. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [bool](https://docs.python.org/3/library/functions.html#bool) | InterruptOnConfig] | None` **DEFAULT:** `None`  
`debug` |  Whether to enable debug mode. Passed through to create_agent. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`name` |  The name of the agent. Passed through to create_agent. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`cache` |  The cache to use for the agent. Passed through to create_agent. **TYPE:** `[BaseCache](../langgraph/cache/#langgraph.cache.base.BaseCache "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseCache</span> \(<code>langgraph.cache.base.BaseCache</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[CompiledStateGraph](../langgraph/graphs/#langgraph.graph.state.CompiledStateGraph "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langgraph.graph.state.CompiledStateGraph</span>")` |  A configured deep agent.  
  
Back to top

---
