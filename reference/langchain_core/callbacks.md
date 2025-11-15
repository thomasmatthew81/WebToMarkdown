# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:28.

## Converted Web Pages

### Callbacks | LangChain Reference

**Source:** https://reference.langchain.com/python/langchain_core/callbacks/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langchain_core/callbacks.md "Edit this page")

# Callbacks

##  `` langchain_core.callbacks.base.AsyncCallbackHandler ¶

Bases: `BaseCallbackHandler`

Async callback handler for LangChain.

METHOD | DESCRIPTION  
---|---  
`on_llm_start` |  Run when the model starts running.  
`on_chat_model_start` |  Run when a chat model starts running.  
`on_llm_new_token` |  Run on new output token. Only available when streaming is enabled.  
`on_llm_end` |  Run when the model ends running.  
`on_llm_error` |  Run when LLM errors.  
`on_chain_start` |  Run when a chain starts running.  
`on_chain_end` |  Run when a chain ends running.  
`on_chain_error` |  Run when chain errors.  
`on_tool_start` |  Run when the tool starts running.  
`on_tool_end` |  Run when the tool ends running.  
`on_tool_error` |  Run when tool errors.  
`on_text` |  Run on an arbitrary text.  
`on_retry` |  Run on a retry event.  
`on_agent_action` |  Run on agent action.  
`on_agent_finish` |  Run on the agent end.  
`on_retriever_start` |  Run on the retriever start.  
`on_retriever_end` |  Run on the retriever end.  
`on_retriever_error` |  Run on retriever error.  
`on_custom_event` |  Override to define a handler for custom events.  
  
###  `` raise_error `class-attribute` `instance-attribute` ¶
    
    
    raise_error: [bool](https://docs.python.org/3/library/functions.html#bool) = False
    

Whether to raise an error if an exception occurs.

###  `` run_inline `class-attribute` `instance-attribute` ¶
    
    
    run_inline: [bool](https://docs.python.org/3/library/functions.html#bool) = False
    

Whether to run the callback inline.

###  `` ignore_llm `property` ¶
    
    
    ignore_llm: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore LLM callbacks.

###  `` ignore_retry `property` ¶
    
    
    ignore_retry: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore retry callbacks.

###  `` ignore_chain `property` ¶
    
    
    ignore_chain: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore chain callbacks.

###  `` ignore_agent `property` ¶
    
    
    ignore_agent: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore agent callbacks.

###  `` ignore_retriever `property` ¶
    
    
    ignore_retriever: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore retriever callbacks.

###  `` ignore_chat_model `property` ¶
    
    
    ignore_chat_model: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore chat model callbacks.

###  `` ignore_custom_event `property` ¶
    
    
    ignore_custom_event: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Ignore custom event.

###  `` on_llm_start `async` ¶
    
    
    on_llm_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        prompts: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run when the model starts running.

Warning

This method is called for non-chat models (regular LLMs). If you're implementing a handler for a chat model, you should use `on_chat_model_start` instead.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized LLM. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`prompts` |  The prompts. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_chat_model_start `async` ¶
    
    
    on_chat_model_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when a chat model starts running.

Warning

This method is called for chat models. If you're implementing a handler for a non-chat model, you should use `on_llm_start` instead.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized chat model. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`messages` |  The messages. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_llm_new_token `async` ¶
    
    
    on_llm_new_token(
        token: [str](https://docs.python.org/3/library/stdtypes.html#str),
        *,
        chunk: GenerationChunk | ChatGenerationChunk | None = None,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run on new output token. Only available when streaming is enabled.

For both chat models and non-chat models (legacy LLMs).

PARAMETER | DESCRIPTION  
---|---  
`token` |  The new token. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`chunk` |  The new generated chunk, containing content and other information. **TYPE:** `GenerationChunk | ChatGenerationChunk | None` **DEFAULT:** `None`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_llm_end `async` ¶
    
    
    on_llm_end(
        response: LLMResult,
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run when the model ends running.

PARAMETER | DESCRIPTION  
---|---  
`response` |  The response which was generated. **TYPE:** `LLMResult`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_llm_error `async` ¶
    
    
    on_llm_error(
        error: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run when LLM errors.

PARAMETER | DESCRIPTION  
---|---  
`error` |  The error that occurred. **TYPE:** `[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. \- response (LLMResult): The response which was generated before the error occurred. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_chain_start `async` ¶
    
    
    on_chain_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        inputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run when a chain starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized chain. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`inputs` |  The inputs. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_chain_end `async` ¶
    
    
    on_chain_end(
        outputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run when a chain ends running.

PARAMETER | DESCRIPTION  
---|---  
`outputs` |  The outputs of the chain. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_chain_error `async` ¶
    
    
    on_chain_error(
        error: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run when chain errors.

PARAMETER | DESCRIPTION  
---|---  
`error` |  The error that occurred. **TYPE:** `[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_tool_start `async` ¶
    
    
    on_tool_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        input_str: [str](https://docs.python.org/3/library/stdtypes.html#str),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        inputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run when the tool starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized tool. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`input_str` |  The input string. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`inputs` |  The inputs. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_tool_end `async` ¶
    
    
    on_tool_end(
        output: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run when the tool ends running.

PARAMETER | DESCRIPTION  
---|---  
`output` |  The output of the tool. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_tool_error `async` ¶
    
    
    on_tool_error(
        error: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run when tool errors.

PARAMETER | DESCRIPTION  
---|---  
`error` |  The error that occurred. **TYPE:** `[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_text `async` ¶
    
    
    on_text(
        text: [str](https://docs.python.org/3/library/stdtypes.html#str),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run on an arbitrary text.

PARAMETER | DESCRIPTION  
---|---  
`text` |  The text. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_retry `async` ¶
    
    
    on_retry(
        retry_state: RetryCallState,
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run on a retry event.

PARAMETER | DESCRIPTION  
---|---  
`retry_state` |  The retry state. **TYPE:** `RetryCallState`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_agent_action `async` ¶
    
    
    on_agent_action(
        action: AgentAction,
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run on agent action.

PARAMETER | DESCRIPTION  
---|---  
`action` |  The agent action. **TYPE:** `AgentAction`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_agent_finish `async` ¶
    
    
    on_agent_finish(
        finish: AgentFinish,
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run on the agent end.

PARAMETER | DESCRIPTION  
---|---  
`finish` |  The agent finish. **TYPE:** `AgentFinish`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_retriever_start `async` ¶
    
    
    on_retriever_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        query: [str](https://docs.python.org/3/library/stdtypes.html#str),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run on the retriever start.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized retriever. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`query` |  The query. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_retriever_end `async` ¶
    
    
    on_retriever_end(
        documents: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Document](../documents/#langchain_core.documents.base.Document "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.documents.base.Document</span> \(<code>langchain_core.documents.Document</code>\)")],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run on the retriever end.

PARAMETER | DESCRIPTION  
---|---  
`documents` |  The documents retrieved. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Document](../documents/#langchain_core.documents.base.Document "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.documents.base.Document</span> \(<code>langchain_core.documents.Document</code>\)")]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_retriever_error `async` ¶
    
    
    on_retriever_error(
        error: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Run on retriever error.

PARAMETER | DESCRIPTION  
---|---  
`error` |  The error that occurred. **TYPE:** `[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_custom_event `async` ¶
    
    
    on_custom_event(
        name: [str](https://docs.python.org/3/library/stdtypes.html#str),
        data: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Override to define a handler for custom events.

PARAMETER | DESCRIPTION  
---|---  
`name` |  The name of the custom event. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`data` |  The data for the custom event. Format will match the format specified by the user. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`tags` |  The tags associated with the custom event (includes inherited tags). **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata associated with the custom event (includes inherited metadata). **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
  
##  `` langchain_core.callbacks.base.BaseCallbackHandler ¶

Bases: `LLMManagerMixin`, `ChainManagerMixin`, `ToolManagerMixin`, `RetrieverManagerMixin`, `CallbackManagerMixin`, `RunManagerMixin`

Base callback handler for LangChain.

METHOD | DESCRIPTION  
---|---  
`on_text` |  Run on an arbitrary text.  
`on_retry` |  Run on a retry event.  
`on_custom_event` |  Override to define a handler for a custom event.  
`on_llm_start` |  Run when LLM starts running.  
`on_chat_model_start` |  Run when a chat model starts running.  
`on_retriever_start` |  Run when the Retriever starts running.  
`on_chain_start` |  Run when a chain starts running.  
`on_tool_start` |  Run when the tool starts running.  
`on_retriever_error` |  Run when Retriever errors.  
`on_retriever_end` |  Run when Retriever ends running.  
`on_tool_end` |  Run when the tool ends running.  
`on_tool_error` |  Run when tool errors.  
`on_chain_end` |  Run when chain ends running.  
`on_chain_error` |  Run when chain errors.  
`on_agent_action` |  Run on agent action.  
`on_agent_finish` |  Run on the agent end.  
`on_llm_new_token` |  Run on new output token. Only available when streaming is enabled.  
`on_llm_end` |  Run when LLM ends running.  
`on_llm_error` |  Run when LLM errors.  
  
###  `` raise_error `class-attribute` `instance-attribute` ¶
    
    
    raise_error: [bool](https://docs.python.org/3/library/functions.html#bool) = False
    

Whether to raise an error if an exception occurs.

###  `` run_inline `class-attribute` `instance-attribute` ¶
    
    
    run_inline: [bool](https://docs.python.org/3/library/functions.html#bool) = False
    

Whether to run the callback inline.

###  `` ignore_llm `property` ¶
    
    
    ignore_llm: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore LLM callbacks.

###  `` ignore_retry `property` ¶
    
    
    ignore_retry: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore retry callbacks.

###  `` ignore_chain `property` ¶
    
    
    ignore_chain: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore chain callbacks.

###  `` ignore_agent `property` ¶
    
    
    ignore_agent: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore agent callbacks.

###  `` ignore_retriever `property` ¶
    
    
    ignore_retriever: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore retriever callbacks.

###  `` ignore_chat_model `property` ¶
    
    
    ignore_chat_model: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore chat model callbacks.

###  `` ignore_custom_event `property` ¶
    
    
    ignore_custom_event: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Ignore custom event.

###  `` on_text ¶
    
    
    on_text(
        text: [str](https://docs.python.org/3/library/stdtypes.html#str), *, run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"), parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run on an arbitrary text.

PARAMETER | DESCRIPTION  
---|---  
`text` |  The text. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_retry ¶
    
    
    on_retry(
        retry_state: RetryCallState,
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run on a retry event.

PARAMETER | DESCRIPTION  
---|---  
`retry_state` |  The retry state. **TYPE:** `RetryCallState`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_custom_event ¶
    
    
    on_custom_event(
        name: [str](https://docs.python.org/3/library/stdtypes.html#str),
        data: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Override to define a handler for a custom event.

PARAMETER | DESCRIPTION  
---|---  
`name` |  The name of the custom event. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`data` |  The data for the custom event. Format will match the format specified by the user. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`tags` |  The tags associated with the custom event (includes inherited tags). **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata associated with the custom event (includes inherited metadata). **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
  
###  `` on_llm_start ¶
    
    
    on_llm_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        prompts: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when LLM starts running.

Warning

This method is called for non-chat models (regular LLMs). If you're implementing a handler for a chat model, you should use `on_chat_model_start` instead.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized LLM. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`prompts` |  The prompts. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_chat_model_start ¶
    
    
    on_chat_model_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when a chat model starts running.

Warning

This method is called for chat models. If you're implementing a handler for a non-chat model, you should use `on_llm_start` instead.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized chat model. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`messages` |  The messages. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_retriever_start ¶
    
    
    on_retriever_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        query: [str](https://docs.python.org/3/library/stdtypes.html#str),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when the Retriever starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized Retriever. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`query` |  The query. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_chain_start ¶
    
    
    on_chain_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        inputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when a chain starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized chain. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`inputs` |  The inputs. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_tool_start ¶
    
    
    on_tool_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        input_str: [str](https://docs.python.org/3/library/stdtypes.html#str),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        inputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when the tool starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized chain. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`input_str` |  The input string. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`inputs` |  The inputs. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_retriever_error ¶
    
    
    on_retriever_error(
        error: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when Retriever errors.

PARAMETER | DESCRIPTION  
---|---  
`error` |  The error that occurred. **TYPE:** `[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_retriever_end ¶
    
    
    on_retriever_end(
        documents: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Document](../documents/#langchain_core.documents.base.Document "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.documents.base.Document</span> \(<code>langchain_core.documents.Document</code>\)")],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when Retriever ends running.

PARAMETER | DESCRIPTION  
---|---  
`documents` |  The documents retrieved. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Document](../documents/#langchain_core.documents.base.Document "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.documents.base.Document</span> \(<code>langchain_core.documents.Document</code>\)")]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_tool_end ¶
    
    
    on_tool_end(
        output: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), *, run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"), parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when the tool ends running.

PARAMETER | DESCRIPTION  
---|---  
`output` |  The output of the tool. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_tool_error ¶
    
    
    on_tool_error(
        error: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when tool errors.

PARAMETER | DESCRIPTION  
---|---  
`error` |  The error that occurred. **TYPE:** `[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_chain_end ¶
    
    
    on_chain_end(
        outputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when chain ends running.

PARAMETER | DESCRIPTION  
---|---  
`outputs` |  The outputs of the chain. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_chain_error ¶
    
    
    on_chain_error(
        error: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when chain errors.

PARAMETER | DESCRIPTION  
---|---  
`error` |  The error that occurred. **TYPE:** `[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_agent_action ¶
    
    
    on_agent_action(
        action: AgentAction,
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run on agent action.

PARAMETER | DESCRIPTION  
---|---  
`action` |  The agent action. **TYPE:** `AgentAction`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_agent_finish ¶
    
    
    on_agent_finish(
        finish: AgentFinish,
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run on the agent end.

PARAMETER | DESCRIPTION  
---|---  
`finish` |  The agent finish. **TYPE:** `AgentFinish`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_llm_new_token ¶
    
    
    on_llm_new_token(
        token: [str](https://docs.python.org/3/library/stdtypes.html#str),
        *,
        chunk: GenerationChunk | ChatGenerationChunk | None = None,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run on new output token. Only available when streaming is enabled.

For both chat models and non-chat models (legacy LLMs).

PARAMETER | DESCRIPTION  
---|---  
`token` |  The new token. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`chunk` |  The new generated chunk, containing content and other information. **TYPE:** `GenerationChunk | ChatGenerationChunk | None` **DEFAULT:** `None`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_llm_end ¶
    
    
    on_llm_end(
        response: LLMResult,
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when LLM ends running.

PARAMETER | DESCRIPTION  
---|---  
`response` |  The response which was generated. **TYPE:** `LLMResult`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_llm_error ¶
    
    
    on_llm_error(
        error: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when LLM errors.

PARAMETER | DESCRIPTION  
---|---  
`error` |  The error that occurred. **TYPE:** `[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
##  `` langchain_core.callbacks.manager.AsyncCallbackManager ¶

Bases: `BaseCallbackManager`

Async callback manager that handles callbacks from LangChain.

METHOD | DESCRIPTION  
---|---  
`on_llm_start` |  Run when LLM starts running.  
`on_chat_model_start` |  Async run when LLM starts running.  
`on_chain_start` |  Async run when chain starts running.  
`on_tool_start` |  Run when the tool starts running.  
`on_custom_event` |  Dispatch an adhoc event to the handlers (async version).  
`on_retriever_start` |  Run when the retriever starts running.  
`configure` |  Configure the async callback manager.  
`__init__` |  Initialize callback manager.  
`copy` |  Return a copy of the callback manager.  
`merge` |  Merge the callback manager with another callback manager.  
`add_handler` |  Add a handler to the callback manager.  
`remove_handler` |  Remove a handler from the callback manager.  
`set_handlers` |  Set handlers as the only handlers on the callback manager.  
`set_handler` |  Set handler as the only handler on the callback manager.  
`add_tags` |  Add tags to the callback manager.  
`remove_tags` |  Remove tags from the callback manager.  
`add_metadata` |  Add metadata to the callback manager.  
`remove_metadata` |  Remove metadata from the callback manager.  
  
###  `` is_async `property` ¶
    
    
    is_async: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Return whether the handler is async.

###  `` on_llm_start `async` ¶
    
    
    on_llm_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        prompts: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)],
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [list](https://docs.python.org/3/library/stdtypes.html#list)[AsyncCallbackManagerForLLMRun]
    

Run when LLM starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized LLM. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`prompts` |  The list of prompts. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[AsyncCallbackManagerForLLMRun]` |  The list of async callback managers, one for each LLM Run corresponding to  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[AsyncCallbackManagerForLLMRun]` |  each prompt.  
  
###  `` on_chat_model_start `async` ¶
    
    
    on_chat_model_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]],
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [list](https://docs.python.org/3/library/stdtypes.html#list)[AsyncCallbackManagerForLLMRun]
    

Async run when LLM starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized LLM. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`messages` |  The list of messages. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]]`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[AsyncCallbackManagerForLLMRun]` |  The list of async callback managers, one for each LLM Run corresponding to  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[AsyncCallbackManagerForLLMRun]` |  each inner message list.  
  
###  `` on_chain_start `async` ¶
    
    
    on_chain_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None,
        inputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> AsyncCallbackManagerForChainRun
    

Async run when chain starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized chain. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None`  
`inputs` |  The inputs to the chain. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`AsyncCallbackManagerForChainRun` |  The async callback manager for the chain run.  
  
###  `` on_tool_start `async` ¶
    
    
    on_tool_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None,
        input_str: [str](https://docs.python.org/3/library/stdtypes.html#str),
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> AsyncCallbackManagerForToolRun
    

Run when the tool starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized tool. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None`  
`input_str` |  The input to the tool. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`parent_run_id` |  The ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`AsyncCallbackManagerForToolRun` |  The async callback manager for the tool run.  
  
###  `` on_custom_event `async` ¶
    
    
    on_custom_event(
        name: [str](https://docs.python.org/3/library/stdtypes.html#str), data: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    ) -> None
    

Dispatch an adhoc event to the handlers (async version).

This event should NOT be used in any internal LangChain code. The event is meant specifically for users of the library to dispatch custom events that are tailored to their application.

PARAMETER | DESCRIPTION  
---|---  
`name` |  The name of the adhoc event. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`data` |  The data for the adhoc event. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If additional keyword arguments are passed.  
  
###  `` on_retriever_start `async` ¶
    
    
    on_retriever_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None,
        query: [str](https://docs.python.org/3/library/stdtypes.html#str),
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> AsyncCallbackManagerForRetrieverRun
    

Run when the retriever starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized retriever. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None`  
`query` |  The query. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`parent_run_id` |  The ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`AsyncCallbackManagerForRetrieverRun` |  The async callback manager for the retriever run.  
  
###  `` configure `classmethod` ¶
    
    
    configure(
        inheritable_callbacks: Callbacks = None,
        local_callbacks: Callbacks = None,
        verbose: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        inheritable_tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        local_tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        inheritable_metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        local_metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
    ) -> AsyncCallbackManager
    

Configure the async callback manager.

PARAMETER | DESCRIPTION  
---|---  
`inheritable_callbacks` |  The inheritable callbacks. **TYPE:** `Callbacks` **DEFAULT:** `None`  
`local_callbacks` |  The local callbacks. **TYPE:** `Callbacks` **DEFAULT:** `None`  
`verbose` |  Whether to enable verbose mode. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`inheritable_tags` |  The inheritable tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`local_tags` |  The local tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`inheritable_metadata` |  The inheritable metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`local_metadata` |  The local metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`AsyncCallbackManager` |  The configured async callback manager.  
  
###  `` __init__ ¶
    
    
    __init__(
        handlers: [list](https://docs.python.org/3/library/stdtypes.html#list)[BaseCallbackHandler],
        inheritable_handlers: [list](https://docs.python.org/3/library/stdtypes.html#list)[BaseCallbackHandler] | None = None,
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        *,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        inheritable_tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        inheritable_metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
    ) -> None
    

Initialize callback manager.

PARAMETER | DESCRIPTION  
---|---  
`handlers` |  The handlers. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[BaseCallbackHandler]`  
`inheritable_handlers` |  The inheritable handlers. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[BaseCallbackHandler] | None` **DEFAULT:** `None`  
`parent_run_id` |  The parent run ID. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`inheritable_tags` |  The inheritable tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`inheritable_metadata` |  The inheritable metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
  
###  `` copy ¶
    
    
    copy() -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a copy of the callback manager.

###  `` merge ¶
    
    
    merge(other: BaseCallbackManager) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Merge the callback manager with another callback manager.

May be overwritten in subclasses. Primarily used internally within merge_configs.

RETURNS | DESCRIPTION  
---|---  
`[Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")` |  The merged callback manager of the same type as the current object.  
  
Example: Merging two callback managers.
    
    
    ```python
    from langchain_core.callbacks.manager import (
        CallbackManager,
        trace_as_chain_group,
    )
    from langchain_core.callbacks.stdout import StdOutCallbackHandler
    
    manager = CallbackManager(handlers=[StdOutCallbackHandler()], tags=["tag2"])
    with trace_as_chain_group("My Group Name", tags=["tag1"]) as group_manager:
        merged_manager = group_manager.merge(manager)
        print(merged_manager.handlers)
        # [
        #    <langchain_core.callbacks.stdout.StdOutCallbackHandler object at ...>,
        #    <langchain_core.callbacks.streaming_stdout.StreamingStdOutCallbackHandler object at ...>,
        # ]
    
        print(merged_manager.tags)
        #    ['tag2', 'tag1']
    ```
    

###  `` add_handler ¶
    
    
    add_handler(handler: BaseCallbackHandler, inherit: [bool](https://docs.python.org/3/library/functions.html#bool) = True) -> None
    

Add a handler to the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`handler` |  The handler to add. **TYPE:** `BaseCallbackHandler`  
`inherit` |  Whether to inherit the handler. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
  
###  `` remove_handler ¶
    
    
    remove_handler(handler: BaseCallbackHandler) -> None
    

Remove a handler from the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`handler` |  The handler to remove. **TYPE:** `BaseCallbackHandler`  
  
###  `` set_handlers ¶
    
    
    set_handlers(handlers: [list](https://docs.python.org/3/library/stdtypes.html#list)[BaseCallbackHandler], inherit: [bool](https://docs.python.org/3/library/functions.html#bool) = True) -> None
    

Set handlers as the only handlers on the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`handlers` |  The handlers to set. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[BaseCallbackHandler]`  
`inherit` |  Whether to inherit the handlers. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
  
###  `` set_handler ¶
    
    
    set_handler(handler: BaseCallbackHandler, inherit: [bool](https://docs.python.org/3/library/functions.html#bool) = True) -> None
    

Set handler as the only handler on the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`handler` |  The handler to set. **TYPE:** `BaseCallbackHandler`  
`inherit` |  Whether to inherit the handler. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
  
###  `` add_tags ¶
    
    
    add_tags(tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)], inherit: [bool](https://docs.python.org/3/library/functions.html#bool) = True) -> None
    

Add tags to the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`tags` |  The tags to add. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`inherit` |  Whether to inherit the tags. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
  
###  `` remove_tags ¶
    
    
    remove_tags(tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]) -> None
    

Remove tags from the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`tags` |  The tags to remove. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
  
###  `` add_metadata ¶
    
    
    add_metadata(metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], inherit: [bool](https://docs.python.org/3/library/functions.html#bool) = True) -> None
    

Add metadata to the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`metadata` |  The metadata to add. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`inherit` |  Whether to inherit the metadata. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
  
###  `` remove_metadata ¶
    
    
    remove_metadata(keys: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]) -> None
    

Remove metadata from the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`keys` |  The keys to remove. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
  
##  `` langchain_core.callbacks.manager.CallbackManager ¶

Bases: `BaseCallbackManager`

Callback manager for LangChain.

METHOD | DESCRIPTION  
---|---  
`on_llm_start` |  Run when LLM starts running.  
`on_chat_model_start` |  Run when chat model starts running.  
`on_chain_start` |  Run when chain starts running.  
`on_tool_start` |  Run when tool starts running.  
`on_retriever_start` |  Run when the retriever starts running.  
`on_custom_event` |  Dispatch an adhoc event to the handlers (async version).  
`configure` |  Configure the callback manager.  
`__init__` |  Initialize callback manager.  
`copy` |  Return a copy of the callback manager.  
`merge` |  Merge the callback manager with another callback manager.  
`add_handler` |  Add a handler to the callback manager.  
`remove_handler` |  Remove a handler from the callback manager.  
`set_handlers` |  Set handlers as the only handlers on the callback manager.  
`set_handler` |  Set handler as the only handler on the callback manager.  
`add_tags` |  Add tags to the callback manager.  
`remove_tags` |  Remove tags from the callback manager.  
`add_metadata` |  Add metadata to the callback manager.  
`remove_metadata` |  Remove metadata from the callback manager.  
  
###  `` is_async `property` ¶
    
    
    is_async: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether the callback manager is async.

###  `` on_llm_start ¶
    
    
    on_llm_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        prompts: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)],
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [list](https://docs.python.org/3/library/stdtypes.html#list)[CallbackManagerForLLMRun]
    

Run when LLM starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized LLM. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`prompts` |  The list of prompts. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[CallbackManagerForLLMRun]` |  A callback manager for each prompt as an LLM run.  
  
###  `` on_chat_model_start ¶
    
    
    on_chat_model_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]],
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [list](https://docs.python.org/3/library/stdtypes.html#list)[CallbackManagerForLLMRun]
    

Run when chat model starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized LLM. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`messages` |  The list of messages. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]]`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[CallbackManagerForLLMRun]` |  A callback manager for each list of messages as an LLM run.  
  
###  `` on_chain_start ¶
    
    
    on_chain_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None,
        inputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> CallbackManagerForChainRun
    

Run when chain starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized chain. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None`  
`inputs` |  The inputs to the chain. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`CallbackManagerForChainRun` |  The callback manager for the chain run.  
  
###  `` on_tool_start ¶
    
    
    on_tool_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None,
        input_str: [str](https://docs.python.org/3/library/stdtypes.html#str),
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        inputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> CallbackManagerForToolRun
    

Run when tool starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  Serialized representation of the tool. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None`  
`input_str` |  The input to the tool as a string. Non-string inputs are cast to strings. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  ID for the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`parent_run_id` |  The ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`inputs` |  The original input to the tool if provided. Recommended for usage instead of input_str when the original input is needed. If provided, the inputs are expected to be formatted as a dict. The keys will correspond to the named-arguments in the tool. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  The keyword arguments to pass to the event handler **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`CallbackManagerForToolRun` |  The callback manager for the tool run.  
  
###  `` on_retriever_start ¶
    
    
    on_retriever_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None,
        query: [str](https://docs.python.org/3/library/stdtypes.html#str),
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> CallbackManagerForRetrieverRun
    

Run when the retriever starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized retriever. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None`  
`query` |  The query. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`parent_run_id` |  The ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`CallbackManagerForRetrieverRun` |  The callback manager for the retriever run.  
  
###  `` on_custom_event ¶
    
    
    on_custom_event(
        name: [str](https://docs.python.org/3/library/stdtypes.html#str), data: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    ) -> None
    

Dispatch an adhoc event to the handlers (async version).

This event should NOT be used in any internal LangChain code. The event is meant specifically for users of the library to dispatch custom events that are tailored to their application.

PARAMETER | DESCRIPTION  
---|---  
`name` |  The name of the adhoc event. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`data` |  The data for the adhoc event. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If additional keyword arguments are passed.  
  
###  `` configure `classmethod` ¶
    
    
    configure(
        inheritable_callbacks: Callbacks = None,
        local_callbacks: Callbacks = None,
        verbose: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        inheritable_tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        local_tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        inheritable_metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        local_metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
    ) -> CallbackManager
    

Configure the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`inheritable_callbacks` |  The inheritable callbacks. **TYPE:** `Callbacks` **DEFAULT:** `None`  
`local_callbacks` |  The local callbacks. **TYPE:** `Callbacks` **DEFAULT:** `None`  
`verbose` |  Whether to enable verbose mode. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`inheritable_tags` |  The inheritable tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`local_tags` |  The local tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`inheritable_metadata` |  The inheritable metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`local_metadata` |  The local metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`CallbackManager` |  The configured callback manager.  
  
###  `` __init__ ¶
    
    
    __init__(
        handlers: [list](https://docs.python.org/3/library/stdtypes.html#list)[BaseCallbackHandler],
        inheritable_handlers: [list](https://docs.python.org/3/library/stdtypes.html#list)[BaseCallbackHandler] | None = None,
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        *,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        inheritable_tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        inheritable_metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
    ) -> None
    

Initialize callback manager.

PARAMETER | DESCRIPTION  
---|---  
`handlers` |  The handlers. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[BaseCallbackHandler]`  
`inheritable_handlers` |  The inheritable handlers. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[BaseCallbackHandler] | None` **DEFAULT:** `None`  
`parent_run_id` |  The parent run ID. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`inheritable_tags` |  The inheritable tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`inheritable_metadata` |  The inheritable metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
  
###  `` copy ¶
    
    
    copy() -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Return a copy of the callback manager.

###  `` merge ¶
    
    
    merge(other: BaseCallbackManager) -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Merge the callback manager with another callback manager.

May be overwritten in subclasses. Primarily used internally within merge_configs.

RETURNS | DESCRIPTION  
---|---  
`[Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")` |  The merged callback manager of the same type as the current object.  
  
Example: Merging two callback managers.
    
    
    ```python
    from langchain_core.callbacks.manager import (
        CallbackManager,
        trace_as_chain_group,
    )
    from langchain_core.callbacks.stdout import StdOutCallbackHandler
    
    manager = CallbackManager(handlers=[StdOutCallbackHandler()], tags=["tag2"])
    with trace_as_chain_group("My Group Name", tags=["tag1"]) as group_manager:
        merged_manager = group_manager.merge(manager)
        print(merged_manager.handlers)
        # [
        #    <langchain_core.callbacks.stdout.StdOutCallbackHandler object at ...>,
        #    <langchain_core.callbacks.streaming_stdout.StreamingStdOutCallbackHandler object at ...>,
        # ]
    
        print(merged_manager.tags)
        #    ['tag2', 'tag1']
    ```
    

###  `` add_handler ¶
    
    
    add_handler(handler: BaseCallbackHandler, inherit: [bool](https://docs.python.org/3/library/functions.html#bool) = True) -> None
    

Add a handler to the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`handler` |  The handler to add. **TYPE:** `BaseCallbackHandler`  
`inherit` |  Whether to inherit the handler. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
  
###  `` remove_handler ¶
    
    
    remove_handler(handler: BaseCallbackHandler) -> None
    

Remove a handler from the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`handler` |  The handler to remove. **TYPE:** `BaseCallbackHandler`  
  
###  `` set_handlers ¶
    
    
    set_handlers(handlers: [list](https://docs.python.org/3/library/stdtypes.html#list)[BaseCallbackHandler], inherit: [bool](https://docs.python.org/3/library/functions.html#bool) = True) -> None
    

Set handlers as the only handlers on the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`handlers` |  The handlers to set. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[BaseCallbackHandler]`  
`inherit` |  Whether to inherit the handlers. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
  
###  `` set_handler ¶
    
    
    set_handler(handler: BaseCallbackHandler, inherit: [bool](https://docs.python.org/3/library/functions.html#bool) = True) -> None
    

Set handler as the only handler on the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`handler` |  The handler to set. **TYPE:** `BaseCallbackHandler`  
`inherit` |  Whether to inherit the handler. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
  
###  `` add_tags ¶
    
    
    add_tags(tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)], inherit: [bool](https://docs.python.org/3/library/functions.html#bool) = True) -> None
    

Add tags to the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`tags` |  The tags to add. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`inherit` |  Whether to inherit the tags. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
  
###  `` remove_tags ¶
    
    
    remove_tags(tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]) -> None
    

Remove tags from the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`tags` |  The tags to remove. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
  
###  `` add_metadata ¶
    
    
    add_metadata(metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], inherit: [bool](https://docs.python.org/3/library/functions.html#bool) = True) -> None
    

Add metadata to the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`metadata` |  The metadata to add. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`inherit` |  Whether to inherit the metadata. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
  
###  `` remove_metadata ¶
    
    
    remove_metadata(keys: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]) -> None
    

Remove metadata from the callback manager.

PARAMETER | DESCRIPTION  
---|---  
`keys` |  The keys to remove. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
  
##  `` langchain_core.callbacks.usage.UsageMetadataCallbackHandler ¶

Bases: `BaseCallbackHandler`

Callback Handler that tracks AIMessage.usage_metadata.

Example
    
    
    from langchain.chat_models import init_chat_model
    from langchain_core.callbacks import UsageMetadataCallbackHandler
    
    llm_1 = init_chat_model(model="openai:gpt-4o-mini")
    llm_2 = init_chat_model(model="anthropic:claude-3-5-haiku-20241022")
    
    callback = UsageMetadataCallbackHandler()
    result_1 = llm_1.invoke("Hello", config={"callbacks": [callback]})
    result_2 = llm_2.invoke("Hello", config={"callbacks": [callback]})
    callback.usage_metadata
    
    
    
    {'gpt-4o-mini-2024-07-18': {'input_tokens': 8,
      'output_tokens': 10,
      'total_tokens': 18,
      'input_token_details': {'audio': 0, 'cache_read': 0},
      'output_token_details': {'audio': 0, 'reasoning': 0}},
     'claude-3-5-haiku-20241022': {'input_tokens': 8,
      'output_tokens': 21,
      'total_tokens': 29,
      'input_token_details': {'cache_read': 0, 'cache_creation': 0}}}
    

Added in `langchain-core` 0.3.49

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize the UsageMetadataCallbackHandler.  
`on_llm_end` |  Collect token usage.  
`on_text` |  Run on an arbitrary text.  
`on_retry` |  Run on a retry event.  
`on_custom_event` |  Override to define a handler for a custom event.  
`on_llm_start` |  Run when LLM starts running.  
`on_chat_model_start` |  Run when a chat model starts running.  
`on_retriever_start` |  Run when the Retriever starts running.  
`on_chain_start` |  Run when a chain starts running.  
`on_tool_start` |  Run when the tool starts running.  
`on_retriever_error` |  Run when Retriever errors.  
`on_retriever_end` |  Run when Retriever ends running.  
`on_tool_end` |  Run when the tool ends running.  
`on_tool_error` |  Run when tool errors.  
`on_chain_end` |  Run when chain ends running.  
`on_chain_error` |  Run when chain errors.  
`on_agent_action` |  Run on agent action.  
`on_agent_finish` |  Run on the agent end.  
`on_llm_new_token` |  Run on new output token. Only available when streaming is enabled.  
`on_llm_error` |  Run when LLM errors.  
  
###  `` raise_error `class-attribute` `instance-attribute` ¶
    
    
    raise_error: [bool](https://docs.python.org/3/library/functions.html#bool) = False
    

Whether to raise an error if an exception occurs.

###  `` run_inline `class-attribute` `instance-attribute` ¶
    
    
    run_inline: [bool](https://docs.python.org/3/library/functions.html#bool) = False
    

Whether to run the callback inline.

###  `` ignore_llm `property` ¶
    
    
    ignore_llm: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore LLM callbacks.

###  `` ignore_retry `property` ¶
    
    
    ignore_retry: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore retry callbacks.

###  `` ignore_chain `property` ¶
    
    
    ignore_chain: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore chain callbacks.

###  `` ignore_agent `property` ¶
    
    
    ignore_agent: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore agent callbacks.

###  `` ignore_retriever `property` ¶
    
    
    ignore_retriever: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore retriever callbacks.

###  `` ignore_chat_model `property` ¶
    
    
    ignore_chat_model: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Whether to ignore chat model callbacks.

###  `` ignore_custom_event `property` ¶
    
    
    ignore_custom_event: [bool](https://docs.python.org/3/library/functions.html#bool)
    

Ignore custom event.

###  `` __init__ ¶
    
    
    __init__() -> None
    

Initialize the UsageMetadataCallbackHandler.

###  `` on_llm_end ¶
    
    
    on_llm_end(response: LLMResult, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> None
    

Collect token usage.

###  `` on_text ¶
    
    
    on_text(
        text: [str](https://docs.python.org/3/library/stdtypes.html#str), *, run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"), parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run on an arbitrary text.

PARAMETER | DESCRIPTION  
---|---  
`text` |  The text. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_retry ¶
    
    
    on_retry(
        retry_state: RetryCallState,
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run on a retry event.

PARAMETER | DESCRIPTION  
---|---  
`retry_state` |  The retry state. **TYPE:** `RetryCallState`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_custom_event ¶
    
    
    on_custom_event(
        name: [str](https://docs.python.org/3/library/stdtypes.html#str),
        data: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Override to define a handler for a custom event.

PARAMETER | DESCRIPTION  
---|---  
`name` |  The name of the custom event. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`data` |  The data for the custom event. Format will match the format specified by the user. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`tags` |  The tags associated with the custom event (includes inherited tags). **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata associated with the custom event (includes inherited metadata). **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
  
###  `` on_llm_start ¶
    
    
    on_llm_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        prompts: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when LLM starts running.

Warning

This method is called for non-chat models (regular LLMs). If you're implementing a handler for a chat model, you should use `on_chat_model_start` instead.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized LLM. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`prompts` |  The prompts. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_chat_model_start ¶
    
    
    on_chat_model_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when a chat model starts running.

Warning

This method is called for chat models. If you're implementing a handler for a non-chat model, you should use `on_llm_start` instead.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized chat model. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`messages` |  The messages. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_retriever_start ¶
    
    
    on_retriever_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        query: [str](https://docs.python.org/3/library/stdtypes.html#str),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when the Retriever starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized Retriever. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`query` |  The query. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_chain_start ¶
    
    
    on_chain_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        inputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when a chain starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized chain. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`inputs` |  The inputs. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_tool_start ¶
    
    
    on_tool_start(
        serialized: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        input_str: [str](https://docs.python.org/3/library/stdtypes.html#str),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        inputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when the tool starts running.

PARAMETER | DESCRIPTION  
---|---  
`serialized` |  The serialized chain. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`input_str` |  The input string. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`tags` |  The tags. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`inputs` |  The inputs. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_retriever_error ¶
    
    
    on_retriever_error(
        error: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when Retriever errors.

PARAMETER | DESCRIPTION  
---|---  
`error` |  The error that occurred. **TYPE:** `[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_retriever_end ¶
    
    
    on_retriever_end(
        documents: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Document](../documents/#langchain_core.documents.base.Document "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.documents.base.Document</span> \(<code>langchain_core.documents.Document</code>\)")],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when Retriever ends running.

PARAMETER | DESCRIPTION  
---|---  
`documents` |  The documents retrieved. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Document](../documents/#langchain_core.documents.base.Document "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.documents.base.Document</span> \(<code>langchain_core.documents.Document</code>\)")]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_tool_end ¶
    
    
    on_tool_end(
        output: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), *, run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"), parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when the tool ends running.

PARAMETER | DESCRIPTION  
---|---  
`output` |  The output of the tool. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_tool_error ¶
    
    
    on_tool_error(
        error: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when tool errors.

PARAMETER | DESCRIPTION  
---|---  
`error` |  The error that occurred. **TYPE:** `[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_chain_end ¶
    
    
    on_chain_end(
        outputs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when chain ends running.

PARAMETER | DESCRIPTION  
---|---  
`outputs` |  The outputs of the chain. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_chain_error ¶
    
    
    on_chain_error(
        error: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when chain errors.

PARAMETER | DESCRIPTION  
---|---  
`error` |  The error that occurred. **TYPE:** `[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_agent_action ¶
    
    
    on_agent_action(
        action: AgentAction,
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run on agent action.

PARAMETER | DESCRIPTION  
---|---  
`action` |  The agent action. **TYPE:** `AgentAction`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_agent_finish ¶
    
    
    on_agent_finish(
        finish: AgentFinish,
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run on the agent end.

PARAMETER | DESCRIPTION  
---|---  
`finish` |  The agent finish. **TYPE:** `AgentFinish`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_llm_new_token ¶
    
    
    on_llm_new_token(
        token: [str](https://docs.python.org/3/library/stdtypes.html#str),
        *,
        chunk: GenerationChunk | ChatGenerationChunk | None = None,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run on new output token. Only available when streaming is enabled.

For both chat models and non-chat models (legacy LLMs).

PARAMETER | DESCRIPTION  
---|---  
`token` |  The new token. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`chunk` |  The new generated chunk, containing content and other information. **TYPE:** `GenerationChunk | ChatGenerationChunk | None` **DEFAULT:** `None`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` on_llm_error ¶
    
    
    on_llm_error(
        error: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException),
        *,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>"),
        parent_run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Run when LLM errors.

PARAMETER | DESCRIPTION  
---|---  
`error` |  The error that occurred. **TYPE:** `[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)`  
`run_id` |  The run ID. This is the ID of the current run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>")`  
`parent_run_id` |  The parent run ID. This is the ID of the parent run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
##  `` langchain_core.callbacks.usage.get_usage_metadata_callback ¶
    
    
    get_usage_metadata_callback(
        name: [str](https://docs.python.org/3/library/stdtypes.html#str) = "usage_metadata_callback",
    ) -> [Generator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "<code>collections.abc.Generator</code>")[UsageMetadataCallbackHandler, None, None]
    

Get usage metadata callback.

Get context manager for tracking usage metadata across chat model calls using `AIMessage.usage_metadata`.

PARAMETER | DESCRIPTION  
---|---  
`name` |  The name of the context variable. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)` **DEFAULT:** `'usage_metadata_callback'`  
YIELDS | DESCRIPTION  
---|---  
`UsageMetadataCallbackHandler` |  The usage metadata callback.  
Example
    
    
    from langchain.chat_models import init_chat_model
    from langchain_core.callbacks import get_usage_metadata_callback
    
    llm_1 = init_chat_model(model="openai:gpt-4o-mini")
    llm_2 = init_chat_model(model="anthropic:claude-3-5-haiku-20241022")
    
    with get_usage_metadata_callback() as cb:
        llm_1.invoke("Hello")
        llm_2.invoke("Hello")
        print(cb.usage_metadata)
    
    
    
    {
        "gpt-4o-mini-2024-07-18": {
            "input_tokens": 8,
            "output_tokens": 10,
            "total_tokens": 18,
            "input_token_details": {"audio": 0, "cache_read": 0},
            "output_token_details": {"audio": 0, "reasoning": 0},
        },
        "claude-3-5-haiku-20241022": {
            "input_tokens": 8,
            "output_tokens": 21,
            "total_tokens": 29,
            "input_token_details": {"cache_read": 0, "cache_creation": 0},
        },
    }
    

Added in `langchain-core` 0.3.49

Back to top

---
