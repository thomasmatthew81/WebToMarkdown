# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:27.

## Converted Web Pages

### Messages | LangChain Reference

**Source:** https://reference.langchain.com/python/langchain/messages/#langchain.messages

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langchain/messages.md "Edit this page")

# Messages

Reference docs

This page contains **reference documentation** for Messages. See [the docs](https://docs.langchain.com/oss/python/langchain/messages) for conceptual guides, tutorials, and examples on using Messages.

##  `` langchain.messages ¶

Message and message content types.

Includes message types for different roles (e.g., human, AI, system), as well as types for message content blocks (e.g., text, image, audio) and tool calls.

CLASS | DESCRIPTION  
---|---  
`AIMessage` |  Message from an AI.  
`AIMessageChunk` |  Message chunk from an AI (yielded when streaming).  
`HumanMessage` |  Message from the user.  
`SystemMessage` |  Message for priming AI behavior.  
`ToolMessage` |  Message for passing the result of executing a tool back to a model.  
`ToolCall` |  Represents an AI's request to call a tool.  
`InvalidToolCall` |  Allowance for errors made by LLM.  
`ToolCallChunk` |  A chunk of a tool call (yielded when streaming).  
`ServerToolCall` |  Tool call that is executed server-side.  
`ServerToolCallChunk` |  A chunk of a server-side tool call (yielded when streaming).  
`ServerToolResult` |  Result of a server-side tool call.  
`TextContentBlock` |  Text output from a LLM.  
`Citation` |  Annotation for citing data from a document.  
`NonStandardAnnotation` |  Provider-specific annotation format.  
`ReasoningContentBlock` |  Reasoning output from a LLM.  
`ImageContentBlock` |  Image data.  
`VideoContentBlock` |  Video data.  
`AudioContentBlock` |  Audio data.  
`PlainTextContentBlock` |  Plaintext data (e.g., from a `.txt` or `.md` document).  
`FileContentBlock` |  File data that doesn't fit into other multimodal block types.  
`NonStandardContentBlock` |  Provider-specific content data.  
`UsageMetadata` |  Usage metadata for a message, such as token counts.  
`InputTokenDetails` |  Breakdown of input token counts.  
`OutputTokenDetails` |  Breakdown of output token counts.  
FUNCTION | DESCRIPTION  
---|---  
`trim_messages` |  Trim messages to be below a token count.  
ATTRIBUTE | DESCRIPTION  
---|---  
`AnyMessage` |  A type representing any defined `Message` or `MessageChunk` type.  
`MessageLikeRepresentation` |  A type representing the various ways a message can be represented.  
`ContentBlock` |  A union of all defined `ContentBlock` types and aliases.  
`Annotation` |  A union of all defined `Annotation` types.  
`DataContentBlock` |  A union of all defined multimodal data `ContentBlock` types.  
  
###  `` AIMessage ¶

Bases: `[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")`

Message from an AI.

An `AIMessage` is returned from a chat model as a response to a prompt.

This message represents the output of the model and consists of both the raw output as returned by the model and standardized fields (e.g., tool calls, usage metadata) added by the LangChain framework.

METHOD | DESCRIPTION  
---|---  
`__init__` |  Initialize an `AIMessage`.  
`pretty_repr` |  Return a pretty representation of the message for display.  
ATTRIBUTE | DESCRIPTION  
---|---  
`tool_calls` |  If present, tool calls associated with the message. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[ToolCall]`  
`invalid_tool_calls` |  If present, tool calls with parsing errors associated with the message. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[InvalidToolCall]`  
`usage_metadata` |  If present, usage metadata for a message, such as token counts. **TYPE:** `UsageMetadata | None`  
`type` |  The type of the message (used for deserialization). **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['ai']`  
`lc_attributes` |  Attributes to be serialized. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)`  
`content_blocks` |  Return standard, typed `ContentBlock` dicts from the message. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[ContentBlock]`  
  
####  `` tool_calls `class-attribute` `instance-attribute` ¶
    
    
    tool_calls: [list](https://docs.python.org/3/library/stdtypes.html#list)[ToolCall] = []
    

If present, tool calls associated with the message.

####  `` invalid_tool_calls `class-attribute` `instance-attribute` ¶
    
    
    invalid_tool_calls: [list](https://docs.python.org/3/library/stdtypes.html#list)[InvalidToolCall] = []
    

If present, tool calls with parsing errors associated with the message.

####  `` usage_metadata `class-attribute` `instance-attribute` ¶
    
    
    usage_metadata: UsageMetadata | None = None
    

If present, usage metadata for a message, such as token counts.

This is a standard representation of token usage that is consistent across models.

####  `` type `class-attribute` `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['ai'] = 'ai'
    

The type of the message (used for deserialization).

####  `` __init__ ¶
    
    
    __init__(
        content: [str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)] | None = None,
        content_blocks: [list](https://docs.python.org/3/library/stdtypes.html#list)[ContentBlock] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Initialize an `AIMessage`.

Specify `content` as positional arg or `content_blocks` for typing.

PARAMETER | DESCRIPTION  
---|---  
`content` |  The content of the message. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)] | None` **DEFAULT:** `None`  
`content_blocks` |  Typed standard content. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[ContentBlock] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional arguments to pass to the parent class. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
####  `` lc_attributes `property` ¶
    
    
    lc_attributes: [dict](https://docs.python.org/3/library/stdtypes.html#dict)
    

Attributes to be serialized.

Includes all attributes, even if they are derived from other initialization arguments.

####  `` content_blocks `property` ¶
    
    
    content_blocks: [list](https://docs.python.org/3/library/stdtypes.html#list)[ContentBlock]
    

Return standard, typed `ContentBlock` dicts from the message.

If the message has a known model provider, use the provider-specific translator first before falling back to best-effort parsing. For details, see the property on `BaseMessage`.

####  `` pretty_repr ¶
    
    
    pretty_repr(html: [bool](https://docs.python.org/3/library/functions.html#bool) = False) -> [str](https://docs.python.org/3/library/stdtypes.html#str)
    

Return a pretty representation of the message for display.

PARAMETER | DESCRIPTION  
---|---  
`html` |  Whether to return an HTML-formatted string. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
RETURNS | DESCRIPTION  
---|---  
`[str](https://docs.python.org/3/library/stdtypes.html#str)` |  A pretty representation of the message.  
  
###  `` AIMessageChunk ¶

Bases: `AIMessage`, `[BaseMessageChunk](../../langchain_core/language_models/#langchain_core.messages.BaseMessageChunk "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessageChunk</span> \(<code>langchain_core.messages.base.BaseMessageChunk</code>\)")`

Message chunk from an AI (yielded when streaming).

METHOD | DESCRIPTION  
---|---  
`init_tool_calls` |  Initialize tool calls from tool call chunks.  
`init_server_tool_calls` |  Parse `server_tool_call_chunks`.  
`__add__` |  Message chunks support concatenation with other message chunks.  
ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  The type of the message (used for deserialization). **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['AIMessageChunk']`  
`tool_call_chunks` |  If provided, tool call chunks associated with the message. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[ToolCallChunk]`  
`chunk_position` |  Optional span represented by an aggregated `AIMessageChunk`. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['last'] | None`  
`lc_attributes` |  Attributes to be serialized, even if they are derived from other initialization args. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)`  
`content_blocks` |  Return standard, typed `ContentBlock` dicts from the message. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[ContentBlock]`  
  
####  `` type `class-attribute` `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['AIMessageChunk'] = 'AIMessageChunk'
    

The type of the message (used for deserialization).

####  `` tool_call_chunks `class-attribute` `instance-attribute` ¶
    
    
    tool_call_chunks: [list](https://docs.python.org/3/library/stdtypes.html#list)[ToolCallChunk] = []
    

If provided, tool call chunks associated with the message.

####  `` chunk_position `class-attribute` `instance-attribute` ¶
    
    
    chunk_position: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['last'] | None = None
    

Optional span represented by an aggregated `AIMessageChunk`.

If a chunk with `chunk_position="last"` is aggregated into a stream, `tool_call_chunks` in message content will be parsed into `tool_calls`.

####  `` lc_attributes `property` ¶
    
    
    lc_attributes: [dict](https://docs.python.org/3/library/stdtypes.html#dict)
    

Attributes to be serialized, even if they are derived from other initialization args.

####  `` content_blocks `property` ¶
    
    
    content_blocks: [list](https://docs.python.org/3/library/stdtypes.html#list)[ContentBlock]
    

Return standard, typed `ContentBlock` dicts from the message.

####  `` init_tool_calls ¶
    
    
    init_tool_calls() -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Initialize tool calls from tool call chunks.

RETURNS | DESCRIPTION  
---|---  
`[Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")` |  The values with tool calls initialized.  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If the tool call chunks are malformed.  
  
####  `` init_server_tool_calls ¶
    
    
    init_server_tool_calls() -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Parse `server_tool_call_chunks`.

####  `` __add__ ¶
    
    
    __add__(other: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> [BaseMessageChunk](../../langchain_core/language_models/#langchain_core.messages.BaseMessageChunk "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessageChunk</span> \(<code>langchain_core.messages.base.BaseMessageChunk</code>\)")
    

Message chunks support concatenation with other message chunks.

This functionality is useful to combine message chunks yielded from a streaming model into a complete message.

PARAMETER | DESCRIPTION  
---|---  
`other` |  Another message chunk to concatenate with this one. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
RETURNS | DESCRIPTION  
---|---  
`[BaseMessageChunk](../../langchain_core/language_models/#langchain_core.messages.BaseMessageChunk "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessageChunk</span> \(<code>langchain_core.messages.base.BaseMessageChunk</code>\)")` |  A new message chunk that is the concatenation of this message chunk  
`[BaseMessageChunk](../../langchain_core/language_models/#langchain_core.messages.BaseMessageChunk "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessageChunk</span> \(<code>langchain_core.messages.base.BaseMessageChunk</code>\)")` |  and the other message chunk.  
RAISES | DESCRIPTION  
---|---  
`[TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)` |  If the other object is not a message chunk.  
  
For example,

`AIMessageChunk(content="Hello") + AIMessageChunk(content=" World")`

will give `AIMessageChunk(content="Hello World")`

###  `` HumanMessage ¶

Bases: `[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")`

Message from the user.

A `HumanMessage` is a message that is passed in from a user to the model.

Example
    
    
    from langchain_core.messages import HumanMessage, SystemMessage
    
    messages = [
        SystemMessage(content="You are a helpful assistant! Your name is Bob."),
        HumanMessage(content="What is your name?"),
    ]
    
    # Instantiate a chat model and invoke it with the messages
    model = ...
    print(model.invoke(messages))
    

METHOD | DESCRIPTION  
---|---  
`__init__` |  Specify `content` as positional arg or `content_blocks` for typing.  
ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  The type of the message (used for serialization). **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['human']`  
  
####  `` type `class-attribute` `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['human'] = 'human'
    

The type of the message (used for serialization).

####  `` __init__ ¶
    
    
    __init__(
        content: [str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)] | None = None,
        content_blocks: [list](https://docs.python.org/3/library/stdtypes.html#list)[ContentBlock] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Specify `content` as positional arg or `content_blocks` for typing.

###  `` SystemMessage ¶

Bases: `[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")`

Message for priming AI behavior.

The system message is usually passed in as the first of a sequence of input messages.

Example
    
    
    from langchain_core.messages import HumanMessage, SystemMessage
    
    messages = [
        SystemMessage(content="You are a helpful assistant! Your name is Bob."),
        HumanMessage(content="What is your name?"),
    ]
    
    # Define a chat model and invoke it with the messages
    print(model.invoke(messages))
    

METHOD | DESCRIPTION  
---|---  
`__init__` |  Specify `content` as positional arg or `content_blocks` for typing.  
ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  The type of the message (used for serialization). **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['system']`  
  
####  `` type `class-attribute` `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['system'] = 'system'
    

The type of the message (used for serialization).

####  `` __init__ ¶
    
    
    __init__(
        content: [str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)] | None = None,
        content_blocks: [list](https://docs.python.org/3/library/stdtypes.html#list)[ContentBlock] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Specify `content` as positional arg or `content_blocks` for typing.

###  `` AnyMessage `module-attribute` ¶
    
    
    AnyMessage = [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[
        [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[AIMessage, [Tag](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "<code>pydantic.Tag</code>")(tag="ai")]
        | [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[HumanMessage, [Tag](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "<code>pydantic.Tag</code>")(tag="human")]
        | [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[ChatMessage, [Tag](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "<code>pydantic.Tag</code>")(tag="chat")]
        | [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[SystemMessage, [Tag](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "<code>pydantic.Tag</code>")(tag="system")]
        | [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[FunctionMessage, [Tag](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "<code>pydantic.Tag</code>")(tag="function")]
        | [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[ToolMessage, [Tag](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "<code>pydantic.Tag</code>")(tag="tool")]
        | [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[AIMessageChunk, [Tag](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "<code>pydantic.Tag</code>")(tag="AIMessageChunk")]
        | [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[HumanMessageChunk, [Tag](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "<code>pydantic.Tag</code>")(tag="HumanMessageChunk")]
        | [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[ChatMessageChunk, [Tag](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "<code>pydantic.Tag</code>")(tag="ChatMessageChunk")]
        | [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[SystemMessageChunk, [Tag](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "<code>pydantic.Tag</code>")(tag="SystemMessageChunk")]
        | [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[FunctionMessageChunk, [Tag](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "<code>pydantic.Tag</code>")(tag="FunctionMessageChunk")]
        | [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[ToolMessageChunk, [Tag](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Tag "<code>pydantic.Tag</code>")(tag="ToolMessageChunk")],
        [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(discriminator=[Discriminator](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "<code>pydantic.Discriminator</code>")(_get_type)),
    ]
    

A type representing any defined `Message` or `MessageChunk` type.

###  `` MessageLikeRepresentation `module-attribute` ¶
    
    
    MessageLikeRepresentation = (
        [BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)] | [str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    )
    

A type representing the various ways a message can be represented.

###  `` ToolMessage ¶

Bases: `[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")`, `ToolOutputMixin`

Message for passing the result of executing a tool back to a model.

`ToolMessage` objects contain the result of a tool invocation. Typically, the result is encoded inside the `content` field.

Example: A `ToolMessage` representing a result of `42` from a tool call with id
    
    
    from langchain_core.messages import ToolMessage
    
    ToolMessage(content="42", tool_call_id="call_Jja7J89XsjrOLA5r!MEOW!SL")
    

Example: A `ToolMessage` where only part of the tool output is sent to the model and the full output is passed in to artifact.
    
    
    from langchain_core.messages import ToolMessage
    
    tool_output = {
        "stdout": "From the graph we can see that the correlation between "
        "x and y is ...",
        "stderr": None,
        "artifacts": {"type": "image", "base64_data": "/9j/4gIcSU..."},
    }
    
    ToolMessage(
        content=tool_output["stdout"],
        artifact=tool_output,
        tool_call_id="call_Jja7J89XsjrOLA5r!MEOW!SL",
    )
    

The `tool_call_id` field is used to associate the tool call request with the tool call response. Useful in situations where a chat model is able to request multiple tool calls in parallel.

METHOD | DESCRIPTION  
---|---  
`coerce_args` |  Coerce the model arguments to the correct types.  
`__init__` |  Initialize a `ToolMessage`.  
ATTRIBUTE | DESCRIPTION  
---|---  
`tool_call_id` |  Tool call that this message is responding to. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`type` |  The type of the message (used for serialization). **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['tool']`  
`artifact` |  Artifact of the Tool execution which is not meant to be sent to the model. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`status` |  Status of the tool invocation. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['success', 'error']`  
`additional_kwargs` |  Currently inherited from `BaseMessage`, but not used. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)`  
`response_metadata` |  Currently inherited from `BaseMessage`, but not used. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)`  
  
####  `` tool_call_id `instance-attribute` ¶
    
    
    tool_call_id: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

Tool call that this message is responding to.

####  `` type `class-attribute` `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['tool'] = 'tool'
    

The type of the message (used for serialization).

####  `` artifact `class-attribute` `instance-attribute` ¶
    
    
    artifact: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") = None
    

Artifact of the Tool execution which is not meant to be sent to the model.

Should only be specified if it is different from the message content, e.g. if only a subset of the full tool output is being passed as message content but the full output is needed in other parts of the code.

####  `` status `class-attribute` `instance-attribute` ¶
    
    
    status: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['success', 'error'] = 'success'
    

Status of the tool invocation.

####  `` additional_kwargs `class-attribute` `instance-attribute` ¶
    
    
    additional_kwargs: [dict](https://docs.python.org/3/library/stdtypes.html#dict) = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default_factory=[dict](https://docs.python.org/3/library/stdtypes.html#dict), repr=False)
    

Currently inherited from `BaseMessage`, but not used.

####  `` response_metadata `class-attribute` `instance-attribute` ¶
    
    
    response_metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict) = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default_factory=[dict](https://docs.python.org/3/library/stdtypes.html#dict), repr=False)
    

Currently inherited from `BaseMessage`, but not used.

####  `` coerce_args `classmethod` ¶
    
    
    coerce_args(values: [dict](https://docs.python.org/3/library/stdtypes.html#dict)) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)
    

Coerce the model arguments to the correct types.

PARAMETER | DESCRIPTION  
---|---  
`values` |  The model arguments. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)`  
  
####  `` __init__ ¶
    
    
    __init__(
        content: [str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)] | None = None,
        content_blocks: [list](https://docs.python.org/3/library/stdtypes.html#list)[ContentBlock] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Initialize a `ToolMessage`.

Specify `content` as positional arg or `content_blocks` for typing.

PARAMETER | DESCRIPTION  
---|---  
`content` |  The contents of the message. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)] | None` **DEFAULT:** `None`  
`content_blocks` |  Typed standard content. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[ContentBlock] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional fields. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` ToolCall ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Represents an AI's request to call a tool.

Example
    
    
    {"name": "foo", "args": {"a": 1}, "id": "123"}
    

This represents a request to call the tool named `'foo'` with arguments `{"a": 1}` and an identifier of `'123'`.

ATTRIBUTE | DESCRIPTION  
---|---  
`name` |  The name of the tool to be called. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`args` |  The arguments to the tool call. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`id` |  An identifier associated with the tool call. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None`  
  
####  `` name `instance-attribute` ¶
    
    
    name: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

The name of the tool to be called.

####  `` args `instance-attribute` ¶
    
    
    args: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

The arguments to the tool call.

####  `` id `instance-attribute` ¶
    
    
    id: [str](https://docs.python.org/3/library/stdtypes.html#str) | None
    

An identifier associated with the tool call.

An identifier is needed to associate a tool call request with a tool call result in events when multiple concurrent tool calls are made.

###  `` InvalidToolCall ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Allowance for errors made by LLM.

Here we add an `error` key to surface errors made during generation (e.g., invalid JSON arguments.)

ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['invalid_tool_call']`  
`id` |  An identifier associated with the tool call. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None`  
`name` |  The name of the tool to be called. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None`  
`args` |  The arguments to the tool call. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None`  
`error` |  An error message associated with the tool call. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None`  
`index` |  Index of block in aggregate response. Used during streaming. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`extras` |  Provider-specific metadata. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['invalid_tool_call']
    

Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [str](https://docs.python.org/3/library/stdtypes.html#str) | None
    

An identifier associated with the tool call.

An identifier is needed to associate a tool call request with a tool call result in events when multiple concurrent tool calls are made.

####  `` name `instance-attribute` ¶
    
    
    name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None
    

The name of the tool to be called.

####  `` args `instance-attribute` ¶
    
    
    args: [str](https://docs.python.org/3/library/stdtypes.html#str) | None
    

The arguments to the tool call.

####  `` error `instance-attribute` ¶
    
    
    error: [str](https://docs.python.org/3/library/stdtypes.html#str) | None
    

An error message associated with the tool call.

####  `` index `instance-attribute` ¶
    
    
    index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Index of block in aggregate response. Used during streaming.

####  `` extras `instance-attribute` ¶
    
    
    extras: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

Provider-specific metadata.

###  `` ToolCallChunk ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

A chunk of a tool call (yielded when streaming).

When merging `ToolCallChunk`s (e.g., via `AIMessageChunk.__add__`), all string attributes are concatenated. Chunks are only merged if their values of `index` are equal and not None.

Example: 
    
    
    left_chunks = [ToolCallChunk(name="foo", args='{"a":', index=0)]
    right_chunks = [ToolCallChunk(name=None, args="1}", index=0)]
    
    (
        AIMessageChunk(content="", tool_call_chunks=left_chunks)
        + AIMessageChunk(content="", tool_call_chunks=right_chunks)
    ).tool_call_chunks == [ToolCallChunk(name="foo", args='{"a":1}', index=0)]
    

ATTRIBUTE | DESCRIPTION  
---|---  
`name` |  The name of the tool to be called. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None`  
`args` |  The arguments to the tool call. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None`  
`id` |  An identifier associated with the tool call. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None`  
`index` |  The index of the tool call in a sequence. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int) | None`  
  
####  `` name `instance-attribute` ¶
    
    
    name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None
    

The name of the tool to be called.

####  `` args `instance-attribute` ¶
    
    
    args: [str](https://docs.python.org/3/library/stdtypes.html#str) | None
    

The arguments to the tool call.

####  `` id `instance-attribute` ¶
    
    
    id: [str](https://docs.python.org/3/library/stdtypes.html#str) | None
    

An identifier associated with the tool call.

####  `` index `instance-attribute` ¶
    
    
    index: [int](https://docs.python.org/3/library/functions.html#int) | None
    

The index of the tool call in a sequence.

###  `` ServerToolCall ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Tool call that is executed server-side.

For example: code execution, web search, etc.

ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['server_tool_call']`  
`id` |  An identifier associated with the tool call. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`name` |  The name of the tool to be called. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`args` |  The arguments to the tool call. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`index` |  Index of block in aggregate response. Used during streaming. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`extras` |  Provider-specific metadata. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['server_tool_call']
    

Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

An identifier associated with the tool call.

####  `` name `instance-attribute` ¶
    
    
    name: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

The name of the tool to be called.

####  `` args `instance-attribute` ¶
    
    
    args: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

The arguments to the tool call.

####  `` index `instance-attribute` ¶
    
    
    index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Index of block in aggregate response. Used during streaming.

####  `` extras `instance-attribute` ¶
    
    
    extras: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

Provider-specific metadata.

###  `` ServerToolCallChunk ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

A chunk of a server-side tool call (yielded when streaming).

ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['server_tool_call_chunk']`  
`name` |  The name of the tool to be called. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`args` |  JSON substring of the arguments to the tool call. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`id` |  An identifier associated with the tool call. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`index` |  Index of block in aggregate response. Used during streaming. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`extras` |  Provider-specific metadata. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['server_tool_call_chunk']
    

Used for discrimination.

####  `` name `instance-attribute` ¶
    
    
    name: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

The name of the tool to be called.

####  `` args `instance-attribute` ¶
    
    
    args: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

JSON substring of the arguments to the tool call.

####  `` id `instance-attribute` ¶
    
    
    id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

An identifier associated with the tool call.

####  `` index `instance-attribute` ¶
    
    
    index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Index of block in aggregate response. Used during streaming.

####  `` extras `instance-attribute` ¶
    
    
    extras: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

Provider-specific metadata.

###  `` ServerToolResult ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Result of a server-side tool call.

ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['server_tool_result']`  
`id` |  An identifier associated with the server tool result. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`tool_call_id` |  ID of the corresponding server tool call. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`status` |  Execution status of the server-side tool. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['success', 'error']`  
`output` |  Output of the executed tool. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`index` |  Index of block in aggregate response. Used during streaming. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`extras` |  Provider-specific metadata. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['server_tool_result']
    

Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

An identifier associated with the server tool result.

####  `` tool_call_id `instance-attribute` ¶
    
    
    tool_call_id: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

ID of the corresponding server tool call.

####  `` status `instance-attribute` ¶
    
    
    status: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['success', 'error']
    

Execution status of the server-side tool.

####  `` output `instance-attribute` ¶
    
    
    output: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Output of the executed tool.

####  `` index `instance-attribute` ¶
    
    
    index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Index of block in aggregate response. Used during streaming.

####  `` extras `instance-attribute` ¶
    
    
    extras: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

Provider-specific metadata.

###  `` ContentBlock `module-attribute` ¶
    
    
    ContentBlock = (
        TextContentBlock
        | InvalidToolCall
        | ReasoningContentBlock
        | NonStandardContentBlock
        | DataContentBlock
        | ToolContentBlock
    )
    

A union of all defined `ContentBlock` types and aliases.

###  `` TextContentBlock ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Text output from a LLM.

This typically represents the main text content of a message, such as the response from a language model or the text of a user message.

Factory function

`create_text_block` may also be used as a factory to create a `TextContentBlock`. Benefits include:

  * Automatic ID generation (when not provided)
  * Required arguments strictly validated at creation time



ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Type of the content block. Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['text']`  
`id` |  Content block identifier. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`text` |  Block text. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`annotations` |  `Citation`s and other annotations. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[list](https://docs.python.org/3/library/stdtypes.html#list)[Annotation]]`  
`index` |  Index of block in aggregate response. Used during streaming. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`extras` |  Provider-specific metadata. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['text']
    

Type of the content block. Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Content block identifier.

Either:

  * Generated by the provider (e.g., OpenAI's file ID)
  * Generated by LangChain upon creation (`UUID4` prefixed with `'lc_'`))



####  `` text `instance-attribute` ¶
    
    
    text: [str](https://docs.python.org/3/library/stdtypes.html#str)
    

Block text.

####  `` annotations `instance-attribute` ¶
    
    
    annotations: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[list](https://docs.python.org/3/library/stdtypes.html#list)[Annotation]]
    

`Citation`s and other annotations.

####  `` index `instance-attribute` ¶
    
    
    index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Index of block in aggregate response. Used during streaming.

####  `` extras `instance-attribute` ¶
    
    
    extras: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

Provider-specific metadata.

###  `` Annotation `module-attribute` ¶
    
    
    Annotation = Citation | NonStandardAnnotation
    

A union of all defined `Annotation` types.

###  `` Citation ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Annotation for citing data from a document.

Note

`start`/`end` indices refer to the **response text** , not the source text. This means that the indices are relative to the model's response, not the original document (as specified in the `url`).

Factory function

`create_citation` may also be used as a factory to create a `Citation`. Benefits include:

  * Automatic ID generation (when not provided)
  * Required arguments strictly validated at creation time



ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Type of the content block. Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['citation']`  
`id` |  Content block identifier. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`url` |  URL of the document source. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`title` |  Source document title. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`start_index` |  Start index of the **response text** (`TextContentBlock.text`). **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int)]`  
`end_index` |  End index of the **response text** (`TextContentBlock.text`) **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int)]`  
`cited_text` |  Excerpt of source text being cited. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`extras` |  Provider-specific metadata. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['citation']
    

Type of the content block. Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Content block identifier.

Either:

  * Generated by the provider (e.g., OpenAI's file ID)
  * Generated by LangChain upon creation (`UUID4` prefixed with `'lc_'`))



####  `` url `instance-attribute` ¶
    
    
    url: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

URL of the document source.

####  `` title `instance-attribute` ¶
    
    
    title: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Source document title.

For example, the page title for a web page or the title of a paper.

####  `` start_index `instance-attribute` ¶
    
    
    start_index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int)]
    

Start index of the **response text** (`TextContentBlock.text`).

####  `` end_index `instance-attribute` ¶
    
    
    end_index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int)]
    

End index of the **response text** (`TextContentBlock.text`)

####  `` cited_text `instance-attribute` ¶
    
    
    cited_text: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Excerpt of source text being cited.

####  `` extras `instance-attribute` ¶
    
    
    extras: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

Provider-specific metadata.

###  `` NonStandardAnnotation ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Provider-specific annotation format.

ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Type of the content block. Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['non_standard_annotation']`  
`id` |  Content block identifier. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`value` |  Provider-specific annotation data. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['non_standard_annotation']
    

Type of the content block. Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Content block identifier.

Either:

  * Generated by the provider (e.g., OpenAI's file ID)
  * Generated by LangChain upon creation (`UUID4` prefixed with `'lc_'`))



####  `` value `instance-attribute` ¶
    
    
    value: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Provider-specific annotation data.

###  `` ReasoningContentBlock ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Reasoning output from a LLM.

Factory function

`create_reasoning_block` may also be used as a factory to create a `ReasoningContentBlock`. Benefits include:

  * Automatic ID generation (when not provided)
  * Required arguments strictly validated at creation time



ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Type of the content block. Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['reasoning']`  
`id` |  Content block identifier. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`reasoning` |  Reasoning text. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`index` |  Index of block in aggregate response. Used during streaming. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`extras` |  Provider-specific metadata. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['reasoning']
    

Type of the content block. Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Content block identifier.

Either:

  * Generated by the provider (e.g., OpenAI's file ID)
  * Generated by LangChain upon creation (`UUID4` prefixed with `'lc_'`))



####  `` reasoning `instance-attribute` ¶
    
    
    reasoning: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Reasoning text.

Either the thought summary or the raw reasoning text itself. This is often parsed from `<think>` tags in the model's response.

####  `` index `instance-attribute` ¶
    
    
    index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Index of block in aggregate response. Used during streaming.

####  `` extras `instance-attribute` ¶
    
    
    extras: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

Provider-specific metadata.

###  `` DataContentBlock `module-attribute` ¶
    
    
    DataContentBlock = (
        ImageContentBlock
        | VideoContentBlock
        | AudioContentBlock
        | PlainTextContentBlock
        | FileContentBlock
    )
    

A union of all defined multimodal data `ContentBlock` types.

###  `` ImageContentBlock ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Image data.

Factory function

`create_image_block` may also be used as a factory to create a `ImageContentBlock`. Benefits include:

  * Automatic ID generation (when not provided)
  * Required arguments strictly validated at creation time



ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Type of the content block. Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['image']`  
`id` |  Content block identifier. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`file_id` |  ID of the image file, e.g., from a file storage system. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`mime_type` |  MIME type of the image. Required for base64. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`index` |  Index of block in aggregate response. Used during streaming. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`url` |  URL of the image. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`base64` |  Data as a base64 string. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`extras` |  Provider-specific metadata. This shouldn't be used for the image data itself. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['image']
    

Type of the content block. Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Content block identifier.

Either:

  * Generated by the provider (e.g., OpenAI's file ID)
  * Generated by LangChain upon creation (`UUID4` prefixed with `'lc_'`))



####  `` file_id `instance-attribute` ¶
    
    
    file_id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

ID of the image file, e.g., from a file storage system.

####  `` mime_type `instance-attribute` ¶
    
    
    mime_type: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

MIME type of the image. Required for base64.

[Examples from IANA](https://www.iana.org/assignments/media-types/media-types.xhtml#image)

####  `` index `instance-attribute` ¶
    
    
    index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Index of block in aggregate response. Used during streaming.

####  `` url `instance-attribute` ¶
    
    
    url: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

URL of the image.

####  `` base64 `instance-attribute` ¶
    
    
    base64: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Data as a base64 string.

####  `` extras `instance-attribute` ¶
    
    
    extras: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

Provider-specific metadata. This shouldn't be used for the image data itself.

###  `` VideoContentBlock ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Video data.

Factory function

`create_video_block` may also be used as a factory to create a `VideoContentBlock`. Benefits include:

  * Automatic ID generation (when not provided)
  * Required arguments strictly validated at creation time



ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Type of the content block. Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['video']`  
`id` |  Content block identifier. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`file_id` |  ID of the video file, e.g., from a file storage system. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`mime_type` |  MIME type of the video. Required for base64. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`index` |  Index of block in aggregate response. Used during streaming. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`url` |  URL of the video. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`base64` |  Data as a base64 string. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`extras` |  Provider-specific metadata. This shouldn't be used for the video data itself. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['video']
    

Type of the content block. Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Content block identifier.

Either:

  * Generated by the provider (e.g., OpenAI's file ID)
  * Generated by LangChain upon creation (`UUID4` prefixed with `'lc_'`))



####  `` file_id `instance-attribute` ¶
    
    
    file_id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

ID of the video file, e.g., from a file storage system.

####  `` mime_type `instance-attribute` ¶
    
    
    mime_type: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

MIME type of the video. Required for base64.

[Examples from IANA](https://www.iana.org/assignments/media-types/media-types.xhtml#video)

####  `` index `instance-attribute` ¶
    
    
    index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Index of block in aggregate response. Used during streaming.

####  `` url `instance-attribute` ¶
    
    
    url: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

URL of the video.

####  `` base64 `instance-attribute` ¶
    
    
    base64: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Data as a base64 string.

####  `` extras `instance-attribute` ¶
    
    
    extras: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

Provider-specific metadata. This shouldn't be used for the video data itself.

###  `` AudioContentBlock ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Audio data.

Factory function

`create_audio_block` may also be used as a factory to create an `AudioContentBlock`. Benefits include: * Automatic ID generation (when not provided) * Required arguments strictly validated at creation time

ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Type of the content block. Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['audio']`  
`id` |  Content block identifier. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`file_id` |  ID of the audio file, e.g., from a file storage system. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`mime_type` |  MIME type of the audio. Required for base64. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`index` |  Index of block in aggregate response. Used during streaming. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`url` |  URL of the audio. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`base64` |  Data as a base64 string. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`extras` |  Provider-specific metadata. This shouldn't be used for the audio data itself. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['audio']
    

Type of the content block. Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Content block identifier.

Either:

  * Generated by the provider (e.g., OpenAI's file ID)
  * Generated by LangChain upon creation (`UUID4` prefixed with `'lc_'`))



####  `` file_id `instance-attribute` ¶
    
    
    file_id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

ID of the audio file, e.g., from a file storage system.

####  `` mime_type `instance-attribute` ¶
    
    
    mime_type: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

MIME type of the audio. Required for base64.

[Examples from IANA](https://www.iana.org/assignments/media-types/media-types.xhtml#audio)

####  `` index `instance-attribute` ¶
    
    
    index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Index of block in aggregate response. Used during streaming.

####  `` url `instance-attribute` ¶
    
    
    url: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

URL of the audio.

####  `` base64 `instance-attribute` ¶
    
    
    base64: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Data as a base64 string.

####  `` extras `instance-attribute` ¶
    
    
    extras: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

Provider-specific metadata. This shouldn't be used for the audio data itself.

###  `` PlainTextContentBlock ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Plaintext data (e.g., from a `.txt` or `.md` document).

Note

A `PlainTextContentBlock` existed in `langchain-core<1.0.0`. Although the name has carried over, the structure has changed significantly. The only shared keys between the old and new versions are `type` and `text`, though the `type` value has changed from `'text'` to `'text-plain'`.

Note

Title and context are optional fields that may be passed to the model. See Anthropic [example](https://docs.claude.com/en/docs/build-with-claude/citations#citable-vs-non-citable-content).

Factory function

`create_plaintext_block` may also be used as a factory to create a `PlainTextContentBlock`. Benefits include:

  * Automatic ID generation (when not provided)
  * Required arguments strictly validated at creation time



ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Type of the content block. Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['text-plain']`  
`id` |  Content block identifier. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`file_id` |  ID of the plaintext file, e.g., from a file storage system. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`mime_type` |  MIME type of the file. Required for base64. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['text/plain']`  
`index` |  Index of block in aggregate response. Used during streaming. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`url` |  URL of the plaintext. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`base64` |  Data as a base64 string. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`text` |  Plaintext content. This is optional if the data is provided as base64. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`title` |  Title of the text data, e.g., the title of a document. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`context` |  Context for the text, e.g., a description or summary of the text's content. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`extras` |  Provider-specific metadata. This shouldn't be used for the data itself. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['text-plain']
    

Type of the content block. Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Content block identifier.

Either:

  * Generated by the provider (e.g., OpenAI's file ID)
  * Generated by LangChain upon creation (`UUID4` prefixed with `'lc_'`))



####  `` file_id `instance-attribute` ¶
    
    
    file_id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

ID of the plaintext file, e.g., from a file storage system.

####  `` mime_type `instance-attribute` ¶
    
    
    mime_type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['text/plain']
    

MIME type of the file. Required for base64.

####  `` index `instance-attribute` ¶
    
    
    index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Index of block in aggregate response. Used during streaming.

####  `` url `instance-attribute` ¶
    
    
    url: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

URL of the plaintext.

####  `` base64 `instance-attribute` ¶
    
    
    base64: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Data as a base64 string.

####  `` text `instance-attribute` ¶
    
    
    text: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Plaintext content. This is optional if the data is provided as base64.

####  `` title `instance-attribute` ¶
    
    
    title: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Title of the text data, e.g., the title of a document.

####  `` context `instance-attribute` ¶
    
    
    context: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Context for the text, e.g., a description or summary of the text's content.

####  `` extras `instance-attribute` ¶
    
    
    extras: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

Provider-specific metadata. This shouldn't be used for the data itself.

###  `` FileContentBlock ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

File data that doesn't fit into other multimodal block types.

This block is intended for files that are not images, audio, or plaintext. For example, it can be used for PDFs, Word documents, etc.

If the file is an image, audio, or plaintext, you should use the corresponding content block type (e.g., `ImageContentBlock`, `AudioContentBlock`, `PlainTextContentBlock`).

Factory function

`create_file_block` may also be used as a factory to create a `FileContentBlock`. Benefits include:

  * Automatic ID generation (when not provided)
  * Required arguments strictly validated at creation time



ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Type of the content block. Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['file']`  
`id` |  Content block identifier. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`file_id` |  ID of the file, e.g., from a file storage system. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`mime_type` |  MIME type of the file. Required for base64. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`index` |  Index of block in aggregate response. Used during streaming. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`url` |  URL of the file. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`base64` |  Data as a base64 string. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`extras` |  Provider-specific metadata. This shouldn't be used for the file data itself. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['file']
    

Type of the content block. Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Content block identifier.

Either:

  * Generated by the provider (e.g., OpenAI's file ID)
  * Generated by LangChain upon creation (`UUID4` prefixed with `'lc_'`))



####  `` file_id `instance-attribute` ¶
    
    
    file_id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

ID of the file, e.g., from a file storage system.

####  `` mime_type `instance-attribute` ¶
    
    
    mime_type: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

MIME type of the file. Required for base64.

[Examples from IANA](https://www.iana.org/assignments/media-types/media-types.xhtml)

####  `` index `instance-attribute` ¶
    
    
    index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Index of block in aggregate response. Used during streaming.

####  `` url `instance-attribute` ¶
    
    
    url: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

URL of the file.

####  `` base64 `instance-attribute` ¶
    
    
    base64: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Data as a base64 string.

####  `` extras `instance-attribute` ¶
    
    
    extras: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
    

Provider-specific metadata. This shouldn't be used for the file data itself.

###  `` NonStandardContentBlock ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Provider-specific content data.

This block contains data for which there is not yet a standard type.

The purpose of this block should be to simply hold a provider-specific payload. If a provider's non-standard output includes reasoning and tool calls, it should be the adapter's job to parse that payload and emit the corresponding standard `ReasoningContentBlock` and `ToolCalls`.

Has no `extras` field, as provider-specific data should be included in the `value` field.

Factory function

`create_non_standard_block` may also be used as a factory to create a `NonStandardContentBlock`. Benefits include:

  * Automatic ID generation (when not provided)
  * Required arguments strictly validated at creation time



ATTRIBUTE | DESCRIPTION  
---|---  
`type` |  Type of the content block. Used for discrimination. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['non_standard']`  
`id` |  Content block identifier. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
`value` |  Provider-specific content data. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
`index` |  Index of block in aggregate response. Used during streaming. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]`  
  
####  `` type `instance-attribute` ¶
    
    
    type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['non_standard']
    

Type of the content block. Used for discrimination.

####  `` id `instance-attribute` ¶
    
    
    id: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Content block identifier.

Either:

  * Generated by the provider (e.g., OpenAI's file ID)
  * Generated by LangChain upon creation (`UUID4` prefixed with `'lc_'`))



####  `` value `instance-attribute` ¶
    
    
    value: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Provider-specific content data.

####  `` index `instance-attribute` ¶
    
    
    index: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[[int](https://docs.python.org/3/library/functions.html#int) | [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Index of block in aggregate response. Used during streaming.

###  `` trim_messages ¶
    
    
    trim_messages(
        messages: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "<code>collections.abc.Iterable</code>")[MessageLikeRepresentation] | PromptValue,
        *,
        max_tokens: [int](https://docs.python.org/3/library/functions.html#int),
        token_counter: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")]], [int](https://docs.python.org/3/library/functions.html#int)]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")], [int](https://docs.python.org/3/library/functions.html#int)]
        | [BaseLanguageModel](../../langchain_core/language_models/#langchain_core.language_models.base.BaseLanguageModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseLanguageModel</span> \(<code>langchain_core.language_models.BaseLanguageModel</code>\)"),
        strategy: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")["first", "last"] = "last",
        allow_partial: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        end_on: [str](https://docs.python.org/3/library/stdtypes.html#str) | [type](https://docs.python.org/3/library/functions.html#type)[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str) | [type](https://docs.python.org/3/library/functions.html#type)[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")]] | None = None,
        start_on: [str](https://docs.python.org/3/library/stdtypes.html#str) | [type](https://docs.python.org/3/library/functions.html#type)[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str) | [type](https://docs.python.org/3/library/functions.html#type)[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")]] | None = None,
        include_system: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        text_splitter: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[str](https://docs.python.org/3/library/stdtypes.html#str)], [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]] | [TextSplitter](../../langchain_text_splitters/#langchain_text_splitters.TextSplitter "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">TextSplitter</span> \(<code>langchain_text_splitters.TextSplitter</code>\)") | None = None,
    ) -> [list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")]
    

Trim messages to be below a token count.

`trim_messages` can be used to reduce the size of a chat history to a specified token or message count.

In either case, if passing the trimmed chat history back into a chat model directly, the resulting chat history should usually satisfy the following properties:

  1. The resulting chat history should be valid. Most chat models expect that chat history starts with either (1) a `HumanMessage` or (2) a `SystemMessage` followed by a `HumanMessage`. To achieve this, set `start_on='human'`. In addition, generally a `ToolMessage` can only appear after an `AIMessage` that involved a tool call.
  2. It includes recent messages and drops old messages in the chat history. To achieve this set the `strategy='last'`.
  3. Usually, the new chat history should include the `SystemMessage` if it was present in the original chat history since the `SystemMessage` includes special instructions to the chat model. The `SystemMessage` is almost always the first message in the history if present. To achieve this set the `include_system=True`.



Note

The examples below show how to configure `trim_messages` to achieve a behavior consistent with the above properties.

PARAMETER | DESCRIPTION  
---|---  
`messages` |  Sequence of Message-like objects to trim. **TYPE:** `[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "<code>collections.abc.Iterable</code>")[MessageLikeRepresentation] | PromptValue`  
`max_tokens` |  Max token count of trimmed messages. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)`  
`token_counter` |  Function or llm for counting tokens in a `BaseMessage` or a list of `BaseMessage`. If a `BaseLanguageModel` is passed in then `BaseLanguageModel.get_num_tokens_from_messages()` will be used. Set to `len` to count the number of **messages** in the chat history. Note Use `count_tokens_approximately` to get fast, approximate token counts. This is recommended for using `trim_messages` on the hot path, where exact token counting is not necessary. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")]], [int](https://docs.python.org/3/library/functions.html#int)] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")], [int](https://docs.python.org/3/library/functions.html#int)] | [BaseLanguageModel](../../langchain_core/language_models/#langchain_core.language_models.base.BaseLanguageModel "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseLanguageModel</span> \(<code>langchain_core.language_models.BaseLanguageModel</code>\)")`  
`strategy` |  Strategy for trimming. \- `'first'`: Keep the first `<= n_count` tokens of the messages. \- `'last'`: Keep the last `<= n_count` tokens of the messages. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['first', 'last']` **DEFAULT:** `'last'`  
`allow_partial` |  Whether to split a message if only part of the message can be included. If `strategy='last'` then the last partial contents of a message are included. If `strategy='first'` then the first partial contents of a message are included. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`end_on` |  The message type to end on. If specified then every message after the last occurrence of this type is ignored. If `strategy='last'` then this is done before we attempt to get the last `max_tokens`. If `strategy='first'` then this is done after we get the first `max_tokens`. Can be specified as string names (e.g. `'system'`, `'human'`, `'ai'`, ...) or as `BaseMessage` classes (e.g. `SystemMessage`, `HumanMessage`, `AIMessage`, ...). Can be a single type or a list of types. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [type](https://docs.python.org/3/library/functions.html#type)[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str) | [type](https://docs.python.org/3/library/functions.html#type)[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")]] | None` **DEFAULT:** `None`  
`start_on` |  The message type to start on. Should only be specified if `strategy='last'`. If specified then every message before the first occurrence of this type is ignored. This is done after we trim the initial messages to the last `max_tokens`. Does not apply to a `SystemMessage` at index 0 if `include_system=True`. Can be specified as string names (e.g. `'system'`, `'human'`, `'ai'`, ...) or as `BaseMessage` classes (e.g. `SystemMessage`, `HumanMessage`, `AIMessage`, ...). Can be a single type or a list of types. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [type](https://docs.python.org/3/library/functions.html#type)[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")] | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str) | [type](https://docs.python.org/3/library/functions.html#type)[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")]] | None` **DEFAULT:** `None`  
`include_system` |  Whether to keep the `SystemMessage` if there is one at index `0`. Should only be specified if `strategy="last"`. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`text_splitter` |  Function or `langchain_text_splitters.TextSplitter` for splitting the string contents of a message. Only used if `allow_partial=True`. If `strategy='last'` then the last split tokens from a partial message will be included. if `strategy='first'` then the first split tokens from a partial message will be included. Token splitter assumes that separators are kept, so that split contents can be directly concatenated to recreate the original text. Defaults to splitting on newlines. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[str](https://docs.python.org/3/library/stdtypes.html#str)], [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]] | [TextSplitter](../../langchain_text_splitters/#langchain_text_splitters.TextSplitter "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">TextSplitter</span> \(<code>langchain_text_splitters.TextSplitter</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.base.BaseMessage</code>\)")]` |  List of trimmed `BaseMessage`.  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  if two incompatible arguments are specified or an unrecognized `strategy` is specified.  
Example

Trim chat history based on token count, keeping the `SystemMessage` if present, and ensuring that the chat history starts with a `HumanMessage` ( or a `SystemMessage` followed by a `HumanMessage`).
    
    
    from langchain_core.messages import (
        AIMessage,
        HumanMessage,
        BaseMessage,
        SystemMessage,
        trim_messages,
    )
    
    messages = [
        SystemMessage("you're a good assistant, you always respond with a joke."),
        HumanMessage("i wonder why it's called langchain"),
        AIMessage(
            'Well, I guess they thought "WordRope" and "SentenceString" just '
            "didn't have the same ring to it!"
        ),
        HumanMessage("and who is harrison chasing anyways"),
        AIMessage(
            "Hmmm let me think.\n\nWhy, he's probably chasing after the last "
            "cup of coffee in the office!"
        ),
        HumanMessage("what do you call a speechless parrot"),
    ]
    
    
    trim_messages(
        messages,
        max_tokens=45,
        strategy="last",
        token_counter=ChatOpenAI(model="gpt-4o"),
        # Most chat models expect that chat history starts with either:
        # (1) a HumanMessage or
        # (2) a SystemMessage followed by a HumanMessage
        start_on="human",
        # Usually, we want to keep the SystemMessage
        # if it's present in the original history.
        # The SystemMessage has special instructions for the model.
        include_system=True,
        allow_partial=False,
    )
    
    
    
    [
        SystemMessage(
            content="you're a good assistant, you always respond with a joke."
        ),
        HumanMessage(content="what do you call a speechless parrot"),
    ]
    

Trim chat history based on the message count, keeping the `SystemMessage` if present, and ensuring that the chat history starts with a `HumanMessage` ( or a `SystemMessage` followed by a `HumanMessage`).
    
    
    trim_messages(
        messages,
        # When `len` is passed in as the token counter function,
        # max_tokens will count the number of messages in the chat history.
        max_tokens=4,
        strategy="last",
        # Passing in `len` as a token counter function will
        # count the number of messages in the chat history.
        token_counter=len,
        # Most chat models expect that chat history starts with either:
        # (1) a HumanMessage or
        # (2) a SystemMessage followed by a HumanMessage
        start_on="human",
        # Usually, we want to keep the SystemMessage
        # if it's present in the original history.
        # The SystemMessage has special instructions for the model.
        include_system=True,
        allow_partial=False,
    )
    
    
    
    [
        SystemMessage(
            content="you're a good assistant, you always respond with a joke."
        ),
        HumanMessage(content="and who is harrison chasing anyways"),
        AIMessage(
            content="Hmmm let me think.\n\nWhy, he's probably chasing after "
            "the last cup of coffee in the office!"
        ),
        HumanMessage(content="what do you call a speechless parrot"),
    ]
    

Trim chat history using a custom token counter function that counts the number of tokens in each message.
    
    
    messages = [
        SystemMessage("This is a 4 token text. The full message is 10 tokens."),
        HumanMessage(
            "This is a 4 token text. The full message is 10 tokens.", id="first"
        ),
        AIMessage(
            [
                {"type": "text", "text": "This is the FIRST 4 token block."},
                {"type": "text", "text": "This is the SECOND 4 token block."},
            ],
            id="second",
        ),
        HumanMessage(
            "This is a 4 token text. The full message is 10 tokens.", id="third"
        ),
        AIMessage(
            "This is a 4 token text. The full message is 10 tokens.",
            id="fourth",
        ),
    ]
    
    
    def dummy_token_counter(messages: list[BaseMessage]) -> int:
        # treat each message like it adds 3 default tokens at the beginning
        # of the message and at the end of the message. 3 + 4 + 3 = 10 tokens
        # per message.
    
        default_content_len = 4
        default_msg_prefix_len = 3
        default_msg_suffix_len = 3
    
        count = 0
        for msg in messages:
            if isinstance(msg.content, str):
                count += (
                    default_msg_prefix_len
                    + default_content_len
                    + default_msg_suffix_len
                )
            if isinstance(msg.content, list):
                count += (
                    default_msg_prefix_len
                    + len(msg.content) * default_content_len
                    + default_msg_suffix_len
                )
        return count
    

First 30 tokens, allowing partial messages: 
    
    
    trim_messages(
        messages,
        max_tokens=30,
        token_counter=dummy_token_counter,
        strategy="first",
        allow_partial=True,
    )
    
    
    
    [
        SystemMessage("This is a 4 token text. The full message is 10 tokens."),
        HumanMessage(
            "This is a 4 token text. The full message is 10 tokens.",
            id="first",
        ),
        AIMessage(
            [{"type": "text", "text": "This is the FIRST 4 token block."}],
            id="second",
        ),
    ]
    

###  `` UsageMetadata ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Usage metadata for a message, such as token counts.

This is a standard representation of token usage that is consistent across models.

Example
    
    
    {
        "input_tokens": 350,
        "output_tokens": 240,
        "total_tokens": 590,
        "input_token_details": {
            "audio": 10,
            "cache_creation": 200,
            "cache_read": 100,
        },
        "output_token_details": {
            "audio": 10,
            "reasoning": 200,
        },
    }
    

Behavior changed in `langchain-core` 0.3.9

Added `input_token_details` and `output_token_details`.

LangSmith SDK

The LangSmith SDK also has a `UsageMetadata` class. While the two share fields, LangSmith's `UsageMetadata` has additional fields to capture cost information used by the LangSmith platform.

ATTRIBUTE | DESCRIPTION  
---|---  
`input_tokens` |  Count of input (or prompt) tokens. Sum of all input token types. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)`  
`output_tokens` |  Count of output (or completion) tokens. Sum of all output token types. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)`  
`total_tokens` |  Total token count. Sum of `input_tokens` \+ `output_tokens`. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)`  
`input_token_details` |  Breakdown of input token counts. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[InputTokenDetails]`  
`output_token_details` |  Breakdown of output token counts. **TYPE:** `[NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[OutputTokenDetails]`  
  
####  `` input_tokens `instance-attribute` ¶
    
    
    input_tokens: [int](https://docs.python.org/3/library/functions.html#int)
    

Count of input (or prompt) tokens. Sum of all input token types.

####  `` output_tokens `instance-attribute` ¶
    
    
    output_tokens: [int](https://docs.python.org/3/library/functions.html#int)
    

Count of output (or completion) tokens. Sum of all output token types.

####  `` total_tokens `instance-attribute` ¶
    
    
    total_tokens: [int](https://docs.python.org/3/library/functions.html#int)
    

Total token count. Sum of `input_tokens` \+ `output_tokens`.

####  `` input_token_details `instance-attribute` ¶
    
    
    input_token_details: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[InputTokenDetails]
    

Breakdown of input token counts.

Does _not_ need to sum to full input token count. Does _not_ need to have all keys.

####  `` output_token_details `instance-attribute` ¶
    
    
    output_token_details: [NotRequired](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.NotRequired "<code>typing_extensions.NotRequired</code>")[OutputTokenDetails]
    

Breakdown of output token counts.

Does _not_ need to sum to full output token count. Does _not_ need to have all keys.

###  `` InputTokenDetails ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Breakdown of input token counts.

Does _not_ need to sum to full input token count. Does _not_ need to have all keys.

Example
    
    
    {
        "audio": 10,
        "cache_creation": 200,
        "cache_read": 100,
    }
    

May also hold extra provider-specific keys.

Added in `langchain-core` 0.3.9

ATTRIBUTE | DESCRIPTION  
---|---  
`audio` |  Audio input tokens. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)`  
`cache_creation` |  Input tokens that were cached and there was a cache miss. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)`  
`cache_read` |  Input tokens that were cached and there was a cache hit. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)`  
  
####  `` audio `instance-attribute` ¶
    
    
    audio: [int](https://docs.python.org/3/library/functions.html#int)
    

Audio input tokens.

####  `` cache_creation `instance-attribute` ¶
    
    
    cache_creation: [int](https://docs.python.org/3/library/functions.html#int)
    

Input tokens that were cached and there was a cache miss.

Since there was a cache miss, the cache was created from these tokens.

####  `` cache_read `instance-attribute` ¶
    
    
    cache_read: [int](https://docs.python.org/3/library/functions.html#int)
    

Input tokens that were cached and there was a cache hit.

Since there was a cache hit, the tokens were read from the cache. More precisely, the model state given these tokens was read from the cache.

###  `` OutputTokenDetails ¶

Bases: `[TypedDict](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypedDict "<code>typing_extensions.TypedDict</code>")`

Breakdown of output token counts.

Does _not_ need to sum to full output token count. Does _not_ need to have all keys.

Example
    
    
    {
        "audio": 10,
        "reasoning": 200,
    }
    

May also hold extra provider-specific keys.

Added in `langchain-core` 0.3.9

ATTRIBUTE | DESCRIPTION  
---|---  
`audio` |  Audio output tokens. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)`  
`reasoning` |  Reasoning output tokens. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)`  
  
####  `` audio `instance-attribute` ¶
    
    
    audio: [int](https://docs.python.org/3/library/functions.html#int)
    

Audio output tokens.

####  `` reasoning `instance-attribute` ¶
    
    
    reasoning: [int](https://docs.python.org/3/library/functions.html#int)
    

Reasoning output tokens.

Tokens generated by the model in a chain of thought process (i.e. by OpenAI's o1 models) that are not returned as part of model output.

Back to top

---
