# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:27.

## Converted Web Pages

### Middleware | LangChain Reference

**Source:** https://reference.langchain.com/python/langchain/middleware/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langchain/middleware.md "Edit this page")

# Middleware

Reference docs

This page contains **reference documentation** for Middleware. See [the docs](https://docs.langchain.com/oss/python/langchain/middleware) for conceptual guides, tutorials, and examples on using Middleware.

## Middleware classes¶

LangChain provides prebuilt middleware for common agent use cases:

CLASS | DESCRIPTION  
---|---  
`SummarizationMiddleware` | Automatically summarize conversation history when approaching token limits  
`HumanInTheLoopMiddleware` | Pause execution for human approval of tool calls  
`ModelCallLimitMiddleware` | Limit the number of model calls to prevent excessive costs  
`ToolCallLimitMiddleware` | Control tool execution by limiting call counts  
`ModelFallbackMiddleware` | Automatically fallback to alternative models when primary fails  
`PIIMiddleware` | Detect and handle Personally Identifiable Information  
`TodoListMiddleware` | Equip agents with task planning and tracking capabilities  
`LLMToolSelectorMiddleware` | Use an LLM to select relevant tools before calling main model  
`ToolRetryMiddleware` | Automatically retry failed tool calls with exponential backoff  
`LLMToolEmulator` | Emulate tool execution using LLM for testing purposes  
`ContextEditingMiddleware` | Manage conversation context by trimming or clearing tool uses  
`ShellToolMiddleware` | Expose a persistent shell session to agents for command execution  
`FilesystemFileSearchMiddleware` | Provide Glob and Grep search tools over filesystem files  
`AgentMiddleware` | Base middleware class for creating custom middleware  
  
## Decorators¶

Create custom middleware using these decorators:

DECORATOR | DESCRIPTION  
---|---  
`@before_agent` | Execute logic before agent execution starts  
`@before_model` | Execute logic before each model call  
`@after_model` | Execute logic after each model receives a response  
`@after_agent` | Execute logic after agent execution completes  
`@wrap_model_call` | Wrap and intercept model calls  
`@wrap_tool_call` | Wrap and intercept tool calls  
`@dynamic_prompt` | Generate dynamic system prompts based on request context  
`@hook_config` | Configure hook behavior (e.g., conditional routing)  
  
## Types and utilities¶

Core types for building middleware:

TYPE | DESCRIPTION  
---|---  
`AgentState` | State container for agent execution  
`ModelRequest` | Request details passed to model calls  
`ModelResponse` | Response details from model calls  
`ClearToolUsesEdit` | Utility for clearing tool usage history from context  
`InterruptOnConfig` | Configuration for human-in-the-loop interruptions  
  
##  `` langchain.agents.middleware.SummarizationMiddleware ¶

Summarizes conversation history when token limits are approached.

This middleware monitors message token counts and automatically summarizes older messages when a threshold is reached, preserving recent messages and maintaining context continuity by ensuring AI/Tool message pairs remain together.

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize summarization middleware.  
  
###  `` __init__ ¶
    
    
    __init__(
        model: [str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain.chat_models.BaseChatModel</code>\)"),
        *,
        trigger: ContextSize | [list](https://docs.python.org/3/library/stdtypes.html#list)[ContextSize] | None = None,
        keep: ContextSize = ("messages", _DEFAULT_MESSAGES_TO_KEEP),
        token_counter: TokenCounter = count_tokens_approximately,
        summary_prompt: [str](https://docs.python.org/3/library/stdtypes.html#str) = DEFAULT_SUMMARY_PROMPT,
        trim_tokens_to_summarize: [int](https://docs.python.org/3/library/functions.html#int) | None = _DEFAULT_TRIM_TOKEN_LIMIT,
        **deprecated_kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Initialize summarization middleware.

PARAMETER | DESCRIPTION  
---|---  
`model` |  The language model to use for generating summaries. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain.chat_models.BaseChatModel</code>\)")`  
`trigger` |  One or more thresholds that trigger summarization. Provide a single `ContextSize` tuple or a list of tuples, in which case summarization runs when any threshold is breached. Examples: `("messages", 50)`, `("tokens", 3000)`, `[("fraction", 0.8), ("messages", 100)]`. **TYPE:** `ContextSize | [list](https://docs.python.org/3/library/stdtypes.html#list)[ContextSize] | None` **DEFAULT:** `None`  
`keep` |  Context retention policy applied after summarization. Provide a `ContextSize` tuple to specify how much history to preserve. Defaults to keeping the most recent 20 messages. Examples: `("messages", 20)`, `("tokens", 3000)`, or `("fraction", 0.3)`. **TYPE:** `ContextSize` **DEFAULT:** `('messages', _DEFAULT_MESSAGES_TO_KEEP)`  
`token_counter` |  Function to count tokens in messages. **TYPE:** `TokenCounter` **DEFAULT:** `count_tokens_approximately`  
`summary_prompt` |  Prompt template for generating summaries. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)` **DEFAULT:** `DEFAULT_SUMMARY_PROMPT`  
`trim_tokens_to_summarize` |  Maximum tokens to keep when preparing messages for the summarization call. Pass `None` to skip trimming entirely. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int) | None` **DEFAULT:** `_DEFAULT_TRIM_TOKEN_LIMIT`  
  
##  `` langchain.agents.middleware.HumanInTheLoopMiddleware ¶

Human in the loop middleware.

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the human in the loop middleware.  
  
###  `` __init__ ¶
    
    
    __init__(
        interrupt_on: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [bool](https://docs.python.org/3/library/functions.html#bool) | InterruptOnConfig],
        *,
        description_prefix: [str](https://docs.python.org/3/library/stdtypes.html#str) = "Tool execution requires approval",
    ) -> None
    

Initialize the human in the loop middleware.

PARAMETER | DESCRIPTION  
---|---  
`interrupt_on` |  Mapping of tool name to allowed actions. If a tool doesn't have an entry, it's auto-approved by default.

  * `True` indicates all decisions are allowed: approve, edit, and reject.
  * `False` indicates that the tool is auto-approved.
  * `InterruptOnConfig` indicates the specific decisions allowed for this tool. The `InterruptOnConfig` can include a `description` field (`str` or `Callable`) for custom formatting of the interrupt description.

**TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [bool](https://docs.python.org/3/library/functions.html#bool) | InterruptOnConfig]`  
`description_prefix` |  The prefix to use when constructing action requests. This is used to provide context about the tool call and the action being requested. Not used if a tool has a `description` in its `InterruptOnConfig`. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)` **DEFAULT:** `'Tool execution requires approval'`  
  
##  `` langchain.agents.middleware.ModelCallLimitMiddleware ¶

Tracks model call counts and enforces limits.

This middleware monitors the number of model calls made during agent execution and can terminate the agent when specified limits are reached. It supports both thread-level and run-level call counting with configurable exit behaviors.

Thread-level: The middleware tracks the number of model calls and persists call count across multiple runs (invocations) of the agent.

Run-level: The middleware tracks the number of model calls made during a single run (invocation) of the agent.

Example
    
    
    from langchain.agents.middleware.call_tracking import ModelCallLimitMiddleware
    from langchain.agents import create_agent
    
    # Create middleware with limits
    call_tracker = ModelCallLimitMiddleware(thread_limit=10, run_limit=5, exit_behavior="end")
    
    agent = create_agent("openai:gpt-4o", middleware=[call_tracker])
    
    # Agent will automatically jump to end when limits are exceeded
    result = await agent.invoke({"messages": [HumanMessage("Help me with a task")]})
    

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the call tracking middleware.  
  
###  `` state_schema `class-attribute` `instance-attribute` ¶
    
    
    state_schema = ModelCallLimitState
    

The schema for state passed to the middleware nodes.

###  `` __init__ ¶
    
    
    __init__(
        *,
        thread_limit: [int](https://docs.python.org/3/library/functions.html#int) | None = None,
        run_limit: [int](https://docs.python.org/3/library/functions.html#int) | None = None,
        exit_behavior: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")["end", "error"] = "end",
    ) -> None
    

Initialize the call tracking middleware.

PARAMETER | DESCRIPTION  
---|---  
`thread_limit` |  Maximum number of model calls allowed per thread. `None` means no limit. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int) | None` **DEFAULT:** `None`  
`run_limit` |  Maximum number of model calls allowed per run. `None` means no limit. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int) | None` **DEFAULT:** `None`  
`exit_behavior` |  What to do when limits are exceeded. \- `'end'`: Jump to the end of the agent execution and inject an artificial AI message indicating that the limit was exceeded. \- `'error'`: Raise a `ModelCallLimitExceededError` **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['end', 'error']` **DEFAULT:** `'end'`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If both limits are `None` or if `exit_behavior` is invalid.  
  
##  `` langchain.agents.middleware.ToolCallLimitMiddleware ¶

Track tool call counts and enforces limits during agent execution.

This middleware monitors the number of tool calls made and can terminate or restrict execution when limits are exceeded. It supports both thread-level (persistent across runs) and run-level (per invocation) call counting.

Configuration

  * `exit_behavior`: How to handle when limits are exceeded
    * `'continue'`: Block exceeded tools, let execution continue (default)
    * `'error'`: Raise an exception
    * `'end'`: Stop immediately with a `ToolMessage` \+ AI message for the single tool call that exceeded the limit (raises `NotImplementedError` if there are other pending tool calls (due to parallel tool calling).



Examples:

Continue execution with blocked tools (default)
    
    
    from langchain.agents.middleware.tool_call_limit import ToolCallLimitMiddleware
    from langchain.agents import create_agent
    
    # Block exceeded tools but let other tools and model continue
    limiter = ToolCallLimitMiddleware(
        thread_limit=20,
        run_limit=10,
        exit_behavior="continue",  # default
    )
    
    agent = create_agent("openai:gpt-4o", middleware=[limiter])
    

Stop immediately when limit exceeded
    
    
    # End execution immediately with an AI message
    limiter = ToolCallLimitMiddleware(run_limit=5, exit_behavior="end")
    
    agent = create_agent("openai:gpt-4o", middleware=[limiter])
    

Raise exception on limit
    
    
    # Strict limit with exception handling
    limiter = ToolCallLimitMiddleware(tool_name="search", thread_limit=5, exit_behavior="error")
    
    agent = create_agent("openai:gpt-4o", middleware=[limiter])
    
    try:
        result = await agent.invoke({"messages": [HumanMessage("Task")]})
    except ToolCallLimitExceededError as e:
        print(f"Search limit exceeded: {e}")
    

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the tool call limit middleware.  
  
###  `` state_schema `class-attribute` `instance-attribute` ¶
    
    
    state_schema = ToolCallLimitState
    

The schema for state passed to the middleware nodes.

###  `` __init__ ¶
    
    
    __init__(
        *,
        tool_name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        thread_limit: [int](https://docs.python.org/3/library/functions.html#int) | None = None,
        run_limit: [int](https://docs.python.org/3/library/functions.html#int) | None = None,
        exit_behavior: ExitBehavior = "continue",
    ) -> None
    

Initialize the tool call limit middleware.

PARAMETER | DESCRIPTION  
---|---  
`tool_name` |  Name of the specific tool to limit. If `None`, limits apply to all tools. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`thread_limit` |  Maximum number of tool calls allowed per thread. `None` means no limit. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int) | None` **DEFAULT:** `None`  
`run_limit` |  Maximum number of tool calls allowed per run. `None` means no limit. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int) | None` **DEFAULT:** `None`  
`exit_behavior` |  How to handle when limits are exceeded. \- `'continue'`: Block exceeded tools with error messages, let other tools continue. Model decides when to end. \- `'error'`: Raise a `ToolCallLimitExceededError` exception \- `'end'`: Stop execution immediately with a `ToolMessage` \+ AI message for the single tool call that exceeded the limit. Raises `NotImplementedError` if there are multiple parallel tool calls to other tools or multiple pending tool calls. **TYPE:** `ExitBehavior` **DEFAULT:** `'continue'`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If both limits are `None`, if `exit_behavior` is invalid, or if `run_limit` exceeds thread_limit.  
  
##  `` langchain.agents.middleware.ModelFallbackMiddleware ¶

Automatic fallback to alternative models on errors.

Retries failed model calls with alternative models in sequence until success or all models exhausted. Primary model specified in `create_agent`.

Example
    
    
    from langchain.agents.middleware.model_fallback import ModelFallbackMiddleware
    from langchain.agents import create_agent
    
    fallback = ModelFallbackMiddleware(
        "openai:gpt-4o-mini",  # Try first on error
        "anthropic:claude-sonnet-4-5-20250929",  # Then this
    )
    
    agent = create_agent(
        model="openai:gpt-4o",  # Primary model
        middleware=[fallback],
    )
    
    # If primary fails: tries gpt-4o-mini, then claude-sonnet-4-5-20250929
    result = await agent.invoke({"messages": [HumanMessage("Hello")]})
    

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize model fallback middleware.  
  
###  `` __init__ ¶
    
    
    __init__(
        first_model: [str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.chat_models.BaseChatModel</code>\)"), *additional_models: [str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.chat_models.BaseChatModel</code>\)")
    ) -> None
    

Initialize model fallback middleware.

PARAMETER | DESCRIPTION  
---|---  
`first_model` |  First fallback model (string name or instance). **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.chat_models.BaseChatModel</code>\)")`  
`*additional_models` |  Additional fallbacks in order. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.chat_models.BaseChatModel</code>\)")` **DEFAULT:** `()`  
  
##  `` langchain.agents.middleware.PIIMiddleware ¶

Detect and handle Personally Identifiable Information (PII) in conversations.

This middleware detects common PII types and applies configurable strategies to handle them. It can detect emails, credit cards, IP addresses, MAC addresses, and URLs in both user input and agent output.

Built-in PII types:

  * `email`: Email addresses
  * `credit_card`: Credit card numbers (validated with Luhn algorithm)
  * `ip`: IP addresses (validated with stdlib)
  * `mac_address`: MAC addresses
  * `url`: URLs (both `http`/`https` and bare URLs)



Strategies:

  * `block`: Raise an exception when PII is detected
  * `redact`: Replace PII with `[REDACTED_TYPE]` placeholders
  * `mask`: Partially mask PII (e.g., `****-****-****-1234` for credit card)
  * `hash`: Replace PII with deterministic hash (e.g., `<email_hash:a1b2c3d4>`)



Strategy Selection Guide:

Strategy | Preserves Identity? | Best For  
---|---|---  
`block` | N/A | Avoid PII completely  
`redact` | No | General compliance, log sanitization  
`mask` | No | Human readability, customer service UIs  
`hash` | Yes (pseudonymous) | Analytics, debugging  
Example
    
    
    from langchain.agents.middleware import PIIMiddleware
    from langchain.agents import create_agent
    
    # Redact all emails in user input
    agent = create_agent(
        "openai:gpt-5",
        middleware=[
            PIIMiddleware("email", strategy="redact"),
        ],
    )
    
    # Use different strategies for different PII types
    agent = create_agent(
        "openai:gpt-4o",
        middleware=[
            PIIMiddleware("credit_card", strategy="mask"),
            PIIMiddleware("url", strategy="redact"),
            PIIMiddleware("ip", strategy="hash"),
        ],
    )
    
    # Custom PII type with regex
    agent = create_agent(
        "openai:gpt-5",
        middleware=[
            PIIMiddleware("api_key", detector=r"sk-[a-zA-Z0-9]{32}", strategy="block"),
        ],
    )
    

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the PII detection middleware.  
  
###  `` __init__ ¶
    
    
    __init__(
        pii_type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")["email", "credit_card", "ip", "mac_address", "url"] | [str](https://docs.python.org/3/library/stdtypes.html#str),
        *,
        strategy: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")["block", "redact", "mask", "hash"] = "redact",
        detector: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[str](https://docs.python.org/3/library/stdtypes.html#str)], [list](https://docs.python.org/3/library/stdtypes.html#list)[PIIMatch]] | [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        apply_to_input: [bool](https://docs.python.org/3/library/functions.html#bool) = True,
        apply_to_output: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        apply_to_tool_results: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
    ) -> None
    

Initialize the PII detection middleware.

PARAMETER | DESCRIPTION  
---|---  
`pii_type` |  Type of PII to detect. Can be a built-in type (`email`, `credit_card`, `ip`, `mac_address`, `url`) or a custom type name. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['email', 'credit_card', 'ip', 'mac_address', 'url'] | [str](https://docs.python.org/3/library/stdtypes.html#str)`  
`strategy` |  How to handle detected PII. Options:

  * `block`: Raise `PIIDetectionError` when PII is detected
  * `redact`: Replace with `[REDACTED_TYPE]` placeholders
  * `mask`: Partially mask PII (show last few characters)
  * `hash`: Replace with deterministic hash (format: `<type_hash:digest>`)

**TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['block', 'redact', 'mask', 'hash']` **DEFAULT:** `'redact'`  
`detector` |  Custom detector function or regex pattern.

  * If `Callable`: Function that takes content string and returns list of `PIIMatch` objects
  * If `str`: Regex pattern to match PII
  * If `None`: Uses built-in detector for the `pii_type`

**TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[str](https://docs.python.org/3/library/stdtypes.html#str)], [list](https://docs.python.org/3/library/stdtypes.html#list)[PIIMatch]] | [str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`apply_to_input` |  Whether to check user messages before model call. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
`apply_to_output` |  Whether to check AI messages after model call. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`apply_to_tool_results` |  Whether to check tool result messages after tool execution. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If `pii_type` is not built-in and no detector is provided.  
  
##  `` langchain.agents.middleware.TodoListMiddleware ¶

Middleware that provides todo list management capabilities to agents.

This middleware adds a `write_todos` tool that allows agents to create and manage structured task lists for complex multi-step operations. It's designed to help agents track progress, organize complex tasks, and provide users with visibility into task completion status.

The middleware automatically injects system prompts that guide the agent on when and how to use the todo functionality effectively.

Example
    
    
    from langchain.agents.middleware.todo import TodoListMiddleware
    from langchain.agents import create_agent
    
    agent = create_agent("openai:gpt-4o", middleware=[TodoListMiddleware()])
    
    # Agent now has access to write_todos tool and todo state tracking
    result = await agent.invoke({"messages": [HumanMessage("Help me refactor my codebase")]})
    
    print(result["todos"])  # Array of todo items with status tracking
    

PARAMETER | DESCRIPTION  
---|---  
`system_prompt` |  Custom system prompt to guide the agent on using the todo tool. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)` **DEFAULT:** `WRITE_TODOS_SYSTEM_PROMPT`  
`tool_description` |  Custom description for the write_todos tool. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)` **DEFAULT:** `WRITE_TODOS_TOOL_DESCRIPTION`  
METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the `TodoListMiddleware` with optional custom prompts.  
  
###  `` state_schema `class-attribute` `instance-attribute` ¶
    
    
    state_schema = PlanningState
    

The schema for state passed to the middleware nodes.

###  `` __init__ ¶
    
    
    __init__(
        *,
        system_prompt: [str](https://docs.python.org/3/library/stdtypes.html#str) = WRITE_TODOS_SYSTEM_PROMPT,
        tool_description: [str](https://docs.python.org/3/library/stdtypes.html#str) = WRITE_TODOS_TOOL_DESCRIPTION,
    ) -> None
    

Initialize the `TodoListMiddleware` with optional custom prompts.

PARAMETER | DESCRIPTION  
---|---  
`system_prompt` |  Custom system prompt to guide the agent on using the todo tool. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)` **DEFAULT:** `WRITE_TODOS_SYSTEM_PROMPT`  
`tool_description` |  Custom description for the `write_todos` tool. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)` **DEFAULT:** `WRITE_TODOS_TOOL_DESCRIPTION`  
  
##  `` langchain.agents.middleware.LLMToolSelectorMiddleware ¶

Uses an LLM to select relevant tools before calling the main model.

When an agent has many tools available, this middleware filters them down to only the most relevant ones for the user's query. This reduces token usage and helps the main model focus on the right tools.

Examples:

Limit to 3 tools
    
    
    from langchain.agents.middleware import LLMToolSelectorMiddleware
    
    middleware = LLMToolSelectorMiddleware(max_tools=3)
    
    agent = create_agent(
        model="openai:gpt-4o",
        tools=[tool1, tool2, tool3, tool4, tool5],
        middleware=[middleware],
    )
    

Use a smaller model for selection
    
    
    middleware = LLMToolSelectorMiddleware(model="openai:gpt-4o-mini", max_tools=2)
    

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the tool selector.  
  
###  `` __init__ ¶
    
    
    __init__(
        *,
        model: [str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.chat_models.BaseChatModel</code>\)") | None = None,
        system_prompt: [str](https://docs.python.org/3/library/stdtypes.html#str) = DEFAULT_SYSTEM_PROMPT,
        max_tools: [int](https://docs.python.org/3/library/functions.html#int) | None = None,
        always_include: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
    ) -> None
    

Initialize the tool selector.

PARAMETER | DESCRIPTION  
---|---  
`model` |  Model to use for selection. If not provided, uses the agent's main model. Can be a model identifier string or `BaseChatModel` instance. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.chat_models.BaseChatModel</code>\)") | None` **DEFAULT:** `None`  
`system_prompt` |  Instructions for the selection model. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)` **DEFAULT:** `DEFAULT_SYSTEM_PROMPT`  
`max_tools` |  Maximum number of tools to select. If the model selects more, only the first `max_tools` will be used. No limit if not specified. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int) | None` **DEFAULT:** `None`  
`always_include` |  Tool names to always include regardless of selection. These do not count against the `max_tools` limit. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
  
##  `` langchain.agents.middleware.ToolRetryMiddleware ¶

Middleware that automatically retries failed tool calls with configurable backoff.

Supports retrying on specific exceptions and exponential backoff.

Examples:

Basic usage with default settings (2 retries, exponential backoff):
    
    
    from langchain.agents import create_agent
    from langchain.agents.middleware import ToolRetryMiddleware
    
    agent = create_agent(model, tools=[search_tool], middleware=[ToolRetryMiddleware()])
    

Retry specific exceptions only:
    
    
    from requests.exceptions import RequestException, Timeout
    
    retry = ToolRetryMiddleware(
        max_retries=4,
        retry_on=(RequestException, Timeout),
        backoff_factor=1.5,
    )
    

Custom exception filtering:
    
    
    from requests.exceptions import HTTPError
    
    
    def should_retry(exc: Exception) -> bool:
        # Only retry on 5xx errors
        if isinstance(exc, HTTPError):
            return 500 <= exc.status_code < 600
        return False
    
    
    retry = ToolRetryMiddleware(
        max_retries=3,
        retry_on=should_retry,
    )
    

Apply to specific tools with custom error handling:
    
    
    def format_error(exc: Exception) -> str:
        return "Database temporarily unavailable. Please try again later."
    
    
    retry = ToolRetryMiddleware(
        max_retries=4,
        tools=["search_database"],
        on_failure=format_error,
    )
    

Apply to specific tools using BaseTool instances:
    
    
    from langchain_core.tools import tool
    
    
    @tool
    def search_database(query: str) -> str:
        '''Search the database.'''
        return results
    
    
    retry = ToolRetryMiddleware(
        max_retries=4,
        tools=[search_database],  # Pass BaseTool instance
    )
    

Constant backoff (no exponential growth):
    
    
    retry = ToolRetryMiddleware(
        max_retries=5,
        backoff_factor=0.0,  # No exponential growth
        initial_delay=2.0,  # Always wait 2 seconds
    )
    

Raise exception on failure:
    
    
    retry = ToolRetryMiddleware(
        max_retries=2,
        on_failure="raise",  # Re-raise exception instead of returning message
    )
    

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize `ToolRetryMiddleware`.  
  
###  `` __init__ ¶
    
    
    __init__(
        *,
        max_retries: [int](https://docs.python.org/3/library/functions.html#int) = 2,
        tools: [list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseTool](../tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span>") | [str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        retry_on: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type)[[Exception](https://docs.python.org/3/library/exceptions.html#Exception)], ...] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Exception](https://docs.python.org/3/library/exceptions.html#Exception)], [bool](https://docs.python.org/3/library/functions.html#bool)] = ([Exception](https://docs.python.org/3/library/exceptions.html#Exception),),
        on_failure: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")["raise", "return_message"]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Exception](https://docs.python.org/3/library/exceptions.html#Exception)], [str](https://docs.python.org/3/library/stdtypes.html#str)] = "return_message",
        backoff_factor: [float](https://docs.python.org/3/library/functions.html#float) = 2.0,
        initial_delay: [float](https://docs.python.org/3/library/functions.html#float) = 1.0,
        max_delay: [float](https://docs.python.org/3/library/functions.html#float) = 60.0,
        jitter: [bool](https://docs.python.org/3/library/functions.html#bool) = True,
    ) -> None
    

Initialize `ToolRetryMiddleware`.

PARAMETER | DESCRIPTION  
---|---  
`max_retries` |  Maximum number of retry attempts after the initial call. Default is `2` retries (`3` total attempts). Must be `>= 0`. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)` **DEFAULT:** `2`  
`tools` |  Optional list of tools or tool names to apply retry logic to. Can be a list of `BaseTool` instances or tool name strings. If `None`, applies to all tools. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseTool](../tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span>") | [str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`retry_on` |  Either a tuple of exception types to retry on, or a callable that takes an exception and returns `True` if it should be retried. Default is to retry on all exceptions. **TYPE:** `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type)[[Exception](https://docs.python.org/3/library/exceptions.html#Exception)], ...] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Exception](https://docs.python.org/3/library/exceptions.html#Exception)], [bool](https://docs.python.org/3/library/functions.html#bool)]` **DEFAULT:** `([Exception](https://docs.python.org/3/library/exceptions.html#Exception),)`  
`on_failure` |  Behavior when all retries are exhausted. Options:

  * `'return_message'`: Return a `ToolMessage` with error details, allowing the LLM to handle the failure and potentially recover.
  * `'raise'`: Re-raise the exception, stopping agent execution.
  * Custom callable: Function that takes the exception and returns a string for the `ToolMessage` content, allowing custom error formatting.

**TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['raise', 'return_message'] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Exception](https://docs.python.org/3/library/exceptions.html#Exception)], [str](https://docs.python.org/3/library/stdtypes.html#str)]` **DEFAULT:** `'return_message'`  
`backoff_factor` |  Multiplier for exponential backoff. Each retry waits `initial_delay * (backoff_factor ** retry_number)` seconds. Set to `0.0` for constant delay. **TYPE:** `[float](https://docs.python.org/3/library/functions.html#float)` **DEFAULT:** `2.0`  
`initial_delay` |  Initial delay in seconds before first retry. **TYPE:** `[float](https://docs.python.org/3/library/functions.html#float)` **DEFAULT:** `1.0`  
`max_delay` |  Maximum delay in seconds between retries. Caps exponential backoff growth. **TYPE:** `[float](https://docs.python.org/3/library/functions.html#float)` **DEFAULT:** `60.0`  
`jitter` |  Whether to add random jitter (`±25%`) to delay to avoid thundering herd. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If `max_retries < 0` or delays are negative.  
  
##  `` langchain.agents.middleware.LLMToolEmulator ¶

Emulates specified tools using an LLM instead of executing them.

This middleware allows selective emulation of tools for testing purposes.

By default (when `tools=None`), all tools are emulated. You can specify which tools to emulate by passing a list of tool names or BaseTool instances.

Examples:

Emulate all tools (default behavior)
    
    
    from langchain.agents.middleware import LLMToolEmulator
    
    middleware = LLMToolEmulator()
    
    agent = create_agent(
        model="openai:gpt-4o",
        tools=[get_weather, get_user_location, calculator],
        middleware=[middleware],
    )
    

Emulate specific tools by name
    
    
    middleware = LLMToolEmulator(tools=["get_weather", "get_user_location"])
    

Use a custom model for emulation
    
    
    middleware = LLMToolEmulator(
        tools=["get_weather"], model="anthropic:claude-sonnet-4-5-20250929"
    )
    

Emulate specific tools by passing tool instances
    
    
    middleware = LLMToolEmulator(tools=[get_weather, get_user_location])
    

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the tool emulator.  
  
###  `` __init__ ¶
    
    
    __init__(
        *,
        tools: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseTool](../tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span>")] | None = None,
        model: [str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.chat_models.BaseChatModel</code>\)") | None = None,
    ) -> None
    

Initialize the tool emulator.

PARAMETER | DESCRIPTION  
---|---  
`tools` |  List of tool names (`str`) or `BaseTool` instances to emulate. If `None`, ALL tools will be emulated. If empty list, no tools will be emulated. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseTool](../tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span>")] | None` **DEFAULT:** `None`  
`model` |  Model to use for emulation. Defaults to `'anthropic:claude-sonnet-4-5-20250929'`. Can be a model identifier string or `BaseChatModel` instance. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [BaseChatModel](../../langchain_core/language_models/#langchain_core.language_models.BaseChatModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatModel</span> \(<code>langchain_core.language_models.chat_models.BaseChatModel</code>\)") | None` **DEFAULT:** `None`  
  
##  `` langchain.agents.middleware.ContextEditingMiddleware ¶

Automatically prune tool results to manage context size.

The middleware applies a sequence of edits when the total input token count exceeds configured thresholds.

Currently the `ClearToolUsesEdit` strategy is supported, aligning with Anthropic's `clear_tool_uses_20250919` behavior [(read more)](https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool).

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize an instance of context editing middleware.  
  
###  `` __init__ ¶
    
    
    __init__(
        *,
        edits: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "<code>collections.abc.Iterable</code>")[ContextEdit] | None = None,
        token_count_method: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")["approximate", "model"] = "approximate",
    ) -> None
    

Initialize an instance of context editing middleware.

PARAMETER | DESCRIPTION  
---|---  
`edits` |  Sequence of edit strategies to apply. Defaults to a single `ClearToolUsesEdit` mirroring Anthropic defaults. **TYPE:** `[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "<code>collections.abc.Iterable</code>")[ContextEdit] | None` **DEFAULT:** `None`  
`token_count_method` |  Whether to use approximate token counting (faster, less accurate) or exact counting implemented by the chat model (potentially slower, more accurate). **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['approximate', 'model']` **DEFAULT:** `'approximate'`  
  
##  `` langchain.agents.middleware.ShellToolMiddleware ¶

Middleware that registers a persistent shell tool for agents.

The middleware exposes a single long-lived shell session. Use the execution policy to match your deployment's security posture:

  * `HostExecutionPolicy` – full host access; best for trusted environments where the agent already runs inside a container or VM that provides isolation.
  * `CodexSandboxExecutionPolicy` – reuses the Codex CLI sandbox for additional syscall/filesystem restrictions when the CLI is available.
  * `DockerExecutionPolicy` – launches a separate Docker container for each agent run, providing harder isolation, optional read-only root filesystems, and user remapping.



When no policy is provided the middleware defaults to `HostExecutionPolicy`.

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the middleware.  
  
###  `` __init__ ¶
    
    
    __init__(
        workspace_root: [str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "<code>pathlib.Path</code>") | None = None,
        *,
        startup_commands: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        shutdown_commands: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        execution_policy: BaseExecutionPolicy | None = None,
        redaction_rules: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[RedactionRule, ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[RedactionRule] | None = None,
        tool_description: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        tool_name: [str](https://docs.python.org/3/library/stdtypes.html#str) = SHELL_TOOL_NAME,
        shell_command: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        env: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
    ) -> None
    

Initialize the middleware.

PARAMETER | DESCRIPTION  
---|---  
`workspace_root` |  Base directory for the shell session. If omitted, a temporary directory is created when the agent starts and removed when it ends. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "<code>pathlib.Path</code>") | None` **DEFAULT:** `None`  
`startup_commands` |  Optional commands executed sequentially after the session starts. **TYPE:** `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`shutdown_commands` |  Optional commands executed before the session shuts down. **TYPE:** `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`execution_policy` |  Execution policy controlling timeouts, output limits, and resource configuration. Defaults to `HostExecutionPolicy` for native execution. **TYPE:** `BaseExecutionPolicy | None` **DEFAULT:** `None`  
`redaction_rules` |  Optional redaction rules to sanitize command output before returning it to the model. **TYPE:** `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[RedactionRule, ...] | [list](https://docs.python.org/3/library/stdtypes.html#list)[RedactionRule] | None` **DEFAULT:** `None`  
`tool_description` |  Optional override for the registered shell tool description. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`tool_name` |  Name for the registered shell tool. Defaults to `"shell"`. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)` **DEFAULT:** `SHELL_TOOL_NAME`  
`shell_command` |  Optional shell executable (string) or argument sequence used to launch the persistent session. Defaults to an implementation-defined bash command. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`env` |  Optional environment variables to supply to the shell session. Values are coerced to strings before command execution. If omitted, the session inherits the parent process environment. **TYPE:** `[Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
  
##  `` langchain.agents.middleware.FilesystemFileSearchMiddleware ¶

Provides Glob and Grep search over filesystem files.

This middleware adds two tools that search through local filesystem:

  * Glob: Fast file pattern matching by file path
  * Grep: Fast content search using ripgrep or Python fallback

Example
    
    
    from langchain.agents import create_agent
    from langchain.agents.middleware import (
        FilesystemFileSearchMiddleware,
    )
    
    agent = create_agent(
        model=model,
        tools=[],  # Add tools as needed
        middleware=[
            FilesystemFileSearchMiddleware(root_path="/workspace"),
        ],
    )
    

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the search middleware.  
  
###  `` __init__ ¶
    
    
    __init__(
        *, root_path: [str](https://docs.python.org/3/library/stdtypes.html#str), use_ripgrep: [bool](https://docs.python.org/3/library/functions.html#bool) = True, max_file_size_mb: [int](https://docs.python.org/3/library/functions.html#int) = 10
    ) -> None
    

Initialize the search middleware.

PARAMETER | DESCRIPTION  
---|---  
`root_path` |  Root directory to search. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`use_ripgrep` |  Whether to use ripgrep for search. Falls back to Python if ripgrep unavailable. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
`max_file_size_mb` |  Maximum file size to search in MB. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)` **DEFAULT:** `10`  
  
Back to top

---
