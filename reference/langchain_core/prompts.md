# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:29.

## Converted Web Pages

### Prompts | LangChain Reference

**Source:** https://reference.langchain.com/python/langchain_core/prompts/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langchain_core/prompts.md "Edit this page")

# Prompts

##  `` langchain_core.prompts.chat.ChatPromptTemplate ¶

Bases: `BaseChatPromptTemplate`

Prompt template for chat models.

Use to create flexible templated prompts for chat models.
    
    
    from langchain_core.prompts import ChatPromptTemplate
    
    template = ChatPromptTemplate(
        [
            ("system", "You are a helpful AI bot. Your name is {name}."),
            ("human", "Hello, how are you doing?"),
            ("ai", "I'm doing well, thanks!"),
            ("human", "{user_input}"),
        ]
    )
    
    prompt_value = template.invoke(
        {
            "name": "Bob",
            "user_input": "What is your name?",
        }
    )
    # Output:
    # ChatPromptValue(
    #    messages=[
    #        SystemMessage(content='You are a helpful AI bot. Your name is Bob.'),
    #        HumanMessage(content='Hello, how are you doing?'),
    #        AIMessage(content="I'm doing well, thanks!"),
    #        HumanMessage(content='What is your name?')
    #    ]
    # )
    

Messages Placeholder
    
    
    # In addition to Human/AI/Tool/Function messages,
    # you can initialize the template with a MessagesPlaceholder
    # either using the class directly or with the shorthand tuple syntax:
    
    template = ChatPromptTemplate(
        [
            ("system", "You are a helpful AI bot."),
            # Means the template will receive an optional list of messages under
            # the "conversation" key
            ("placeholder", "{conversation}"),
            # Equivalently:
            # MessagesPlaceholder(variable_name="conversation", optional=True)
        ]
    )
    
    prompt_value = template.invoke(
        {
            "conversation": [
                ("human", "Hi!"),
                ("ai", "How can I assist you today?"),
                ("human", "Can you make me an ice cream sundae?"),
                ("ai", "No."),
            ]
        }
    )
    
    # Output:
    # ChatPromptValue(
    #    messages=[
    #        SystemMessage(content='You are a helpful AI bot.'),
    #        HumanMessage(content='Hi!'),
    #        AIMessage(content='How can I assist you today?'),
    #        HumanMessage(content='Can you make me an ice cream sundae?'),
    #        AIMessage(content='No.'),
    #    ]
    # )
    

Single-variable template

If your prompt has only a single input variable (i.e., 1 instance of "{variable_nams}"), and you invoke the template with a non-dict object, the prompt template will inject the provided argument into that variable location.
    
    
    from langchain_core.prompts import ChatPromptTemplate
    
    template = ChatPromptTemplate(
        [
            ("system", "You are a helpful AI bot. Your name is Carl."),
            ("human", "{user_input}"),
        ]
    )
    
    prompt_value = template.invoke("Hello, there!")
    # Equivalent to
    # prompt_value = template.invoke({"user_input": "Hello, there!"})
    
    # Output:
    #  ChatPromptValue(
    #     messages=[
    #         SystemMessage(content='You are a helpful AI bot. Your name is Carl.'),
    #         HumanMessage(content='Hello, there!'),
    #     ]
    # )
    

METHOD | DESCRIPTION  
---|---  
`__init__` |  Create a chat prompt template from a variety of message formats.  
`get_lc_namespace` |  Get the namespace of the LangChain object.  
`__add__` |  Combine two prompt templates.  
`validate_input_variables` |  Validate input variables.  
`from_template` |  Create a chat prompt template from a template string.  
`from_messages` |  Create a chat prompt template from a variety of message formats.  
`format_messages` |  Format the chat template into a list of finalized messages.  
`aformat_messages` |  Async format the chat template into a list of finalized messages.  
`partial` |  Get a new ChatPromptTemplate with some input variables already filled in.  
`append` |  Append a message to the end of the chat template.  
`extend` |  Extend the chat template with a sequence of messages.  
`__getitem__` |  Use to index into the chat template.  
`__len__` |  Return the length of the chat template.  
`save` |  Save prompt to file.  
`pretty_repr` |  Human-readable representation.  
`get_name` |  Get the name of the `Runnable`.  
`get_input_schema` |  Get the input schema for the prompt.  
`get_input_jsonschema` |  Get a JSON schema that represents the input to the `Runnable`.  
`get_output_schema` |  Get a Pydantic model that can be used to validate output to the `Runnable`.  
`get_output_jsonschema` |  Get a JSON schema that represents the output of the `Runnable`.  
`config_schema` |  The type of config this `Runnable` accepts specified as a Pydantic model.  
`get_config_jsonschema` |  Get a JSON schema that represents the config of the `Runnable`.  
`get_graph` |  Return a graph representation of this `Runnable`.  
`get_prompts` |  Return a list of prompts used by this `Runnable`.  
`__or__` |  Runnable "or" operator.  
`__ror__` |  Runnable "reverse-or" operator.  
`pipe` |  Pipe `Runnable` objects.  
`pick` |  Pick keys from the output `dict` of this `Runnable`.  
`assign` |  Assigns new fields to the `dict` output of this `Runnable`.  
`invoke` |  Invoke the prompt.  
`ainvoke` |  Async invoke the prompt.  
`batch` |  Default implementation runs invoke in parallel using a thread pool executor.  
`batch_as_completed` |  Run `invoke` in parallel on a list of inputs.  
`abatch` |  Default implementation runs `ainvoke` in parallel using `asyncio.gather`.  
`abatch_as_completed` |  Run `ainvoke` in parallel on a list of inputs.  
`stream` |  Default implementation of `stream`, which calls `invoke`.  
`astream` |  Default implementation of `astream`, which calls `ainvoke`.  
`astream_log` |  Stream all output from a `Runnable`, as reported to the callback system.  
`astream_events` |  Generate a stream of events.  
`transform` |  Transform inputs to outputs.  
`atransform` |  Transform inputs to outputs.  
`bind` |  Bind arguments to a `Runnable`, returning a new `Runnable`.  
`with_config` |  Bind config to a `Runnable`, returning a new `Runnable`.  
`with_listeners` |  Bind lifecycle listeners to a `Runnable`, returning a new `Runnable`.  
`with_alisteners` |  Bind async lifecycle listeners to a `Runnable`.  
`with_types` |  Bind input and output types to a `Runnable`, returning a new `Runnable`.  
`with_retry` |  Create a new `Runnable` that retries the original `Runnable` on exceptions.  
`map` |  Return a new `Runnable` that maps a list of inputs to a list of outputs.  
`with_fallbacks` |  Add fallbacks to a `Runnable`, returning a new `Runnable`.  
`as_tool` |  Create a `BaseTool` from a `Runnable`.  
`is_lc_serializable` |  Return `True` as this class is serializable.  
`lc_id` |  Return a unique identifier for this class for serialization purposes.  
`to_json` |  Serialize the `Runnable` to JSON.  
`to_json_not_implemented` |  Serialize a "not implemented" object.  
`configurable_fields` |  Configure particular `Runnable` fields at runtime.  
`configurable_alternatives` |  Configure alternatives for `Runnable` objects that can be set at runtime.  
`validate_variable_names` |  Validate variable names do not include restricted names.  
`format_prompt` |  Format prompt. Should return a ChatPromptValue.  
`aformat_prompt` |  Async format prompt. Should return a ChatPromptValue.  
`format` |  Format the chat template into a string.  
`aformat` |  Async format the chat template into a string.  
`dict` |  Return dictionary representation of prompt.  
`pretty_print` |  Print a human-readable representation.  
  
###  `` messages `instance-attribute` ¶
    
    
    messages: [Annotated](https://docs.python.org/3/library/typing.html#typing.Annotated "<code>typing.Annotated</code>")[[list](https://docs.python.org/3/library/stdtypes.html#list)[MessageLike], [SkipValidation](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.SkipValidation "<code>pydantic.SkipValidation</code>")()]
    

List of messages consisting of either message prompt templates or messages.

###  `` validate_template `class-attribute` `instance-attribute` ¶
    
    
    validate_template: [bool](https://docs.python.org/3/library/functions.html#bool) = False
    

Whether or not to try validating the template.

###  `` name `class-attribute` `instance-attribute` ¶
    
    
    name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None
    

The name of the `Runnable`. Used for debugging and tracing.

###  `` InputType `property` ¶
    
    
    InputType: [type](https://docs.python.org/3/library/functions.html#type)[Input]
    

Input type.

The type of input this `Runnable` accepts specified as a type annotation.

RAISES | DESCRIPTION  
---|---  
`[TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)` |  If the input type cannot be inferred.  
  
###  `` OutputType `property` ¶
    
    
    OutputType: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Return the output type of the prompt.

###  `` input_schema `property` ¶
    
    
    input_schema: [type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]
    

The type of input this `Runnable` accepts specified as a Pydantic model.

###  `` output_schema `property` ¶
    
    
    output_schema: [type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]
    

Output schema.

The type of output this `Runnable` produces specified as a Pydantic model.

###  `` config_specs `property` ¶
    
    
    config_specs: [list](https://docs.python.org/3/library/stdtypes.html#list)[ConfigurableFieldSpec]
    

List configurable fields for this `Runnable`.

###  `` lc_secrets `property` ¶
    
    
    lc_secrets: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

A map of constructor argument names to secret ids.

For example, `{"openai_api_key": "OPENAI_API_KEY"}`

###  `` lc_attributes `property` ¶
    
    
    lc_attributes: dict
    

List of attribute names that should be included in the serialized kwargs.

These attributes must be accepted by the constructor.

Default is an empty dictionary.

###  `` input_variables `instance-attribute` ¶
    
    
    input_variables: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

A list of the names of the variables whose values are required as inputs to the prompt.

###  `` optional_variables `class-attribute` `instance-attribute` ¶
    
    
    optional_variables: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=[])
    

A list of the names of the variables for placeholder or `MessagePlaceholder` that are optional.

These variables are auto inferred from the prompt and user need not provide them.

###  `` input_types `class-attribute` `instance-attribute` ¶
    
    
    input_types: dict[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default_factory=dict, exclude=True)
    

A dictionary of the types of the variables the prompt template expects.

If not provided, all variables are assumed to be strings.

###  `` output_parser `class-attribute` `instance-attribute` ¶
    
    
    output_parser: [BaseOutputParser](../output_parsers/#langchain_core.output_parsers.BaseOutputParser "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseOutputParser</span> \(<code>langchain_core.output_parsers.base.BaseOutputParser</code>\)") | None = None
    

How to parse the output of calling an LLM on this formatted prompt.

###  `` partial_variables `class-attribute` `instance-attribute` ¶
    
    
    partial_variables: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default_factory=dict)
    

A dictionary of the partial variables the prompt template carries.

Partial variables populate the template so that you don't need to pass them in every time you call the prompt.

###  `` metadata `class-attribute` `instance-attribute` ¶
    
    
    metadata: [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "<code>typing.Dict</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None
    

Metadata to be used for tracing.

###  `` tags `class-attribute` `instance-attribute` ¶
    
    
    tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None
    

Tags to be used for tracing.

###  `` __init__ ¶
    
    
    __init__(
        messages: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[MessageLikeRepresentation],
        *,
        template_format: PromptTemplateFormat = "f-string",
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> None
    

Create a chat prompt template from a variety of message formats.

PARAMETER | DESCRIPTION  
---|---  
`messages` |  Sequence of message representations. A message can be represented using the following formats:

  1. `BaseMessagePromptTemplate`
  2. `BaseMessage`
  3. 2-tuple of `(message type, template)`; e.g., `("human", "{user_input}")`
  4. 2-tuple of `(message class, template)`
  5. A string which is shorthand for `("human", template)`; e.g., `"{user_input}"`

**TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[MessageLikeRepresentation]`  
`template_format` |  Format of the template. **TYPE:** `PromptTemplateFormat` **DEFAULT:** `'f-string'`  
`input_variables` |  A list of the names of the variables whose values are required as inputs to the prompt.  
`optional_variables` |  A list of the names of the variables for placeholder or MessagePlaceholder that are optional. These variables are auto inferred from the prompt and user need not provide them.  
`partial_variables` |  A dictionary of the partial variables the prompt template carries. Partial variables populate the template so that you don't need to pass them in every time you call the prompt.  
`validate_template` |  Whether to validate the template.  
`input_types` |  A dictionary of the types of the variables the prompt template expects. If not provided, all variables are assumed to be strings.  
  
Examples:

Instantiation from a list of message templates:
    
    
    template = ChatPromptTemplate(
        [
            ("human", "Hello, how are you?"),
            ("ai", "I'm doing well, thanks!"),
            ("human", "That's good to hear."),
        ]
    )
    

Instantiation from mixed message formats:
    
    
    template = ChatPromptTemplate(
        [
            SystemMessage(content="hello"),
            ("human", "Hello, how are you?"),
        ]
    )
    

###  `` get_lc_namespace `classmethod` ¶
    
    
    get_lc_namespace() -> [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Get the namespace of the LangChain object.

RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]` |  `["langchain", "prompts", "chat"]`  
  
###  `` __add__ ¶
    
    
    __add__(other: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> ChatPromptTemplate
    

Combine two prompt templates.

PARAMETER | DESCRIPTION  
---|---  
`other` |  Another prompt template. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
RETURNS | DESCRIPTION  
---|---  
`ChatPromptTemplate` |  Combined prompt template.  
  
###  `` validate_input_variables `classmethod` ¶
    
    
    validate_input_variables(values: dict) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Validate input variables.

If input_variables is not set, it will be set to the union of all input variables in the messages.

PARAMETER | DESCRIPTION  
---|---  
`values` |  values to validate. **TYPE:** `dict`  
RETURNS | DESCRIPTION  
---|---  
`[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` |  Validated values.  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If input variables do not match.  
  
###  `` from_template `classmethod` ¶
    
    
    from_template(template: [str](https://docs.python.org/3/library/stdtypes.html#str), **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> ChatPromptTemplate
    

Create a chat prompt template from a template string.

Creates a chat template consisting of a single message assumed to be from the human.

PARAMETER | DESCRIPTION  
---|---  
`template` |  template string **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
`**kwargs` |  keyword arguments to pass to the constructor. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`ChatPromptTemplate` |  A new instance of this class.  
  
###  `` from_messages `classmethod` ¶
    
    
    from_messages(
        messages: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[MessageLikeRepresentation],
        template_format: PromptTemplateFormat = "f-string",
    ) -> ChatPromptTemplate
    

Create a chat prompt template from a variety of message formats.

Examples:

Instantiation from a list of message templates:
    
    
    template = ChatPromptTemplate.from_messages(
        [
            ("human", "Hello, how are you?"),
            ("ai", "I'm doing well, thanks!"),
            ("human", "That's good to hear."),
        ]
    )
    

Instantiation from mixed message formats:
    
    
    template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content="hello"),
            ("human", "Hello, how are you?"),
        ]
    )
    

Args: messages: Sequence of message representations.
    
    
        A message can be represented using the following formats:
    
        1. `BaseMessagePromptTemplate`
        2. `BaseMessage`
        3. 2-tuple of `(message type, template)`; e.g.,
            `("human", "{user_input}")`
        4. 2-tuple of `(message class, template)`
        5. A string which is shorthand for `("human", template)`; e.g.,
            `"{user_input}"`
    template_format: format of the template.
    

RETURNS | DESCRIPTION  
---|---  
`ChatPromptTemplate` |  a chat prompt template.  
  
###  `` format_messages ¶
    
    
    format_messages(**kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> [list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]
    

Format the chat template into a list of finalized messages.

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  keyword arguments to use for filling in template variables in all the template messages in this chat template. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  if messages are of unexpected types.  
RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]` |  list of formatted messages.  
  
###  `` aformat_messages `async` ¶
    
    
    aformat_messages(**kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> [list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]
    

Async format the chat template into a list of finalized messages.

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  keyword arguments to use for filling in template variables in all the template messages in this chat template. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]` |  list of formatted messages.  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If unexpected input.  
  
###  `` partial ¶
    
    
    partial(**kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> ChatPromptTemplate
    

Get a new ChatPromptTemplate with some input variables already filled in.

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  keyword arguments to use for filling in template variables. Ought to be a subset of the input variables. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`ChatPromptTemplate` |  A new ChatPromptTemplate.  
Example
    
    
    from langchain_core.prompts import ChatPromptTemplate
    
    template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an AI assistant named {name}."),
            ("human", "Hi I'm {user}"),
            ("ai", "Hi there, {user}, I'm {name}."),
            ("human", "{input}"),
        ]
    )
    template2 = template.partial(user="Lucy", name="R2D2")
    
    template2.format_messages(input="hello")
    

###  `` append ¶
    
    
    append(message: MessageLikeRepresentation) -> None
    

Append a message to the end of the chat template.

PARAMETER | DESCRIPTION  
---|---  
`message` |  representation of a message to append. **TYPE:** `MessageLikeRepresentation`  
  
###  `` extend ¶
    
    
    extend(messages: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[MessageLikeRepresentation]) -> None
    

Extend the chat template with a sequence of messages.

PARAMETER | DESCRIPTION  
---|---  
`messages` |  Sequence of message representations to append. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[MessageLikeRepresentation]`  
  
###  `` __getitem__ ¶
    
    
    __getitem__(index: [int](https://docs.python.org/3/library/functions.html#int) | [slice](https://docs.python.org/3/library/functions.html#slice)) -> MessageLike | ChatPromptTemplate
    

Use to index into the chat template.

RETURNS | DESCRIPTION  
---|---  
`MessageLike | ChatPromptTemplate` |  If index is an int, returns the message at that index.  
`MessageLike | ChatPromptTemplate` |  If index is a slice, returns a new `ChatPromptTemplate`  
`MessageLike | ChatPromptTemplate` |  containing the messages in that slice.  
  
###  `` __len__ ¶
    
    
    __len__() -> [int](https://docs.python.org/3/library/functions.html#int)
    

Return the length of the chat template.

###  `` save ¶
    
    
    save(file_path: [Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "<code>pathlib.Path</code>") | [str](https://docs.python.org/3/library/stdtypes.html#str)) -> None
    

Save prompt to file.

PARAMETER | DESCRIPTION  
---|---  
`file_path` |  path to file. **TYPE:** `[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path "<code>pathlib.Path</code>") | [str](https://docs.python.org/3/library/stdtypes.html#str)`  
  
###  `` pretty_repr ¶
    
    
    pretty_repr(html: [bool](https://docs.python.org/3/library/functions.html#bool) = False) -> [str](https://docs.python.org/3/library/stdtypes.html#str)
    

Human-readable representation.

PARAMETER | DESCRIPTION  
---|---  
`html` |  Whether to format as HTML. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
RETURNS | DESCRIPTION  
---|---  
`[str](https://docs.python.org/3/library/stdtypes.html#str)` |  Human-readable representation.  
  
###  `` get_name ¶
    
    
    get_name(suffix: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None, *, name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None) -> [str](https://docs.python.org/3/library/stdtypes.html#str)
    

Get the name of the `Runnable`.

PARAMETER | DESCRIPTION  
---|---  
`suffix` |  An optional suffix to append to the name. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`name` |  An optional name to use instead of the `Runnable`'s name. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[str](https://docs.python.org/3/library/stdtypes.html#str)` |  The name of the `Runnable`.  
  
###  `` get_input_schema ¶
    
    
    get_input_schema(config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None = None) -> [type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]
    

Get the input schema for the prompt.

PARAMETER | DESCRIPTION  
---|---  
`config` |  Configuration for the prompt. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]` |  The input schema for the prompt.  
  
###  `` get_input_jsonschema ¶
    
    
    get_input_jsonschema(config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Get a JSON schema that represents the input to the `Runnable`.

PARAMETER | DESCRIPTION  
---|---  
`config` |  A config to use when generating the schema. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]` |  A JSON schema that represents the input to the `Runnable`.  
Example
    
    
    from langchain_core.runnables import RunnableLambda
    
    
    def add_one(x: int) -> int:
        return x + 1
    
    
    runnable = RunnableLambda(add_one)
    
    print(runnable.get_input_jsonschema())
    

Added in `langchain-core` 0.3.0

###  `` get_output_schema ¶
    
    
    get_output_schema(config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None) -> [type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]
    

Get a Pydantic model that can be used to validate output to the `Runnable`.

`Runnable` objects that leverage the `configurable_fields` and `configurable_alternatives` methods will have a dynamic output schema that depends on which configuration the `Runnable` is invoked with.

This method allows to get an output schema for a specific configuration.

PARAMETER | DESCRIPTION  
---|---  
`config` |  A config to use when generating the schema. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]` |  A Pydantic model that can be used to validate output.  
  
###  `` get_output_jsonschema ¶
    
    
    get_output_jsonschema(config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Get a JSON schema that represents the output of the `Runnable`.

PARAMETER | DESCRIPTION  
---|---  
`config` |  A config to use when generating the schema. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]` |  A JSON schema that represents the output of the `Runnable`.  
Example
    
    
    from langchain_core.runnables import RunnableLambda
    
    
    def add_one(x: int) -> int:
        return x + 1
    
    
    runnable = RunnableLambda(add_one)
    
    print(runnable.get_output_jsonschema())
    

Added in `langchain-core` 0.3.0

###  `` config_schema ¶
    
    
    config_schema(*, include: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None) -> [type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]
    

The type of config this `Runnable` accepts specified as a Pydantic model.

To mark a field as configurable, see the `configurable_fields` and `configurable_alternatives` methods.

PARAMETER | DESCRIPTION  
---|---  
`include` |  A list of fields to include in the config schema. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]` |  A Pydantic model that can be used to validate config.  
  
###  `` get_config_jsonschema ¶
    
    
    get_config_jsonschema(*, include: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Get a JSON schema that represents the config of the `Runnable`.

PARAMETER | DESCRIPTION  
---|---  
`include` |  A list of fields to include in the config schema. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]` |  A JSON schema that represents the config of the `Runnable`.  
  
Added in `langchain-core` 0.3.0

###  `` get_graph ¶
    
    
    get_graph(config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None) -> Graph
    

Return a graph representation of this `Runnable`.

###  `` get_prompts ¶
    
    
    get_prompts(config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None) -> [list](https://docs.python.org/3/library/stdtypes.html#list)[BasePromptTemplate]
    

Return a list of prompts used by this `Runnable`.

###  `` __or__ ¶
    
    
    __or__(
        other: [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), Other]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Other]]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Other]]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], Other]
        | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), Other] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], Other] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
    ) -> [RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Other]
    

Runnable "or" operator.

Compose this `Runnable` with another object to create a `RunnableSequence`.

PARAMETER | DESCRIPTION  
---|---  
`other` |  Another `Runnable` or a `Runnable`-like object. **TYPE:** `[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), Other] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Other]] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Other]] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], Other] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), Other] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], Other] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Other]` |  A new `Runnable`.  
  
###  `` __ror__ ¶
    
    
    __ror__(
        other: [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Other, [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Other]], [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Other]], [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Other], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
        | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Other, [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Other], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
    ) -> [RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Other, Output]
    

Runnable "reverse-or" operator.

Compose this `Runnable` with another object to create a `RunnableSequence`.

PARAMETER | DESCRIPTION  
---|---  
`other` |  Another `Runnable` or a `Runnable`-like object. **TYPE:** `[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Other, [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Other]], [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Other]], [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Other], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Other, [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Other], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Other, Output]` |  A new `Runnable`.  
  
###  `` pipe ¶
    
    
    pipe(
        *others: [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), Other] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], Other], name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None
    ) -> [RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Other]
    

Pipe `Runnable` objects.

Compose this `Runnable` with `Runnable`-like objects to make a `RunnableSequence`.

Equivalent to `RunnableSequence(self, *others)` or `self | others[0] | ...`

Example
    
    
    from langchain_core.runnables import RunnableLambda
    
    
    def add_one(x: int) -> int:
        return x + 1
    
    
    def mul_two(x: int) -> int:
        return x * 2
    
    
    runnable_1 = RunnableLambda(add_one)
    runnable_2 = RunnableLambda(mul_two)
    sequence = runnable_1.pipe(runnable_2)
    # Or equivalently:
    # sequence = runnable_1 | runnable_2
    # sequence = RunnableSequence(first=runnable_1, last=runnable_2)
    sequence.invoke(1)
    await sequence.ainvoke(1)
    # -> 4
    
    sequence.batch([1, 2, 3])
    await sequence.abatch([1, 2, 3])
    # -> [4, 6, 8]
    

PARAMETER | DESCRIPTION  
---|---  
`*others` |  Other `Runnable` or `Runnable`-like objects to compose **TYPE:** `[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), Other] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], Other]` **DEFAULT:** `()`  
`name` |  An optional name for the resulting `RunnableSequence`. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Other]` |  A new `Runnable`.  
  
###  `` pick ¶
    
    
    pick(keys: [str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]) -> [RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Pick keys from the output `dict` of this `Runnable`.

Pick a single key:
    
    
    import json
    
    from langchain_core.runnables import RunnableLambda, RunnableMap
    
    as_str = RunnableLambda(str)
    as_json = RunnableLambda(json.loads)
    chain = RunnableMap(str=as_str, json=as_json)
    
    chain.invoke("[1, 2, 3]")
    # -> {"str": "[1, 2, 3]", "json": [1, 2, 3]}
    
    json_only_chain = chain.pick("json")
    json_only_chain.invoke("[1, 2, 3]")
    # -> [1, 2, 3]
    

Pick a list of keys:
    
    
    from typing import Any
    
    import json
    
    from langchain_core.runnables import RunnableLambda, RunnableMap
    
    as_str = RunnableLambda(str)
    as_json = RunnableLambda(json.loads)
    
    
    def as_bytes(x: Any) -> bytes:
        return bytes(x, "utf-8")
    
    
    chain = RunnableMap(str=as_str, json=as_json, bytes=RunnableLambda(as_bytes))
    
    chain.invoke("[1, 2, 3]")
    # -> {"str": "[1, 2, 3]", "json": [1, 2, 3], "bytes": b"[1, 2, 3]"}
    
    json_and_bytes_chain = chain.pick(["json", "bytes"])
    json_and_bytes_chain.invoke("[1, 2, 3]")
    # -> {"json": [1, 2, 3], "bytes": b"[1, 2, 3]"}
    

PARAMETER | DESCRIPTION  
---|---  
`keys` |  A key or list of keys to pick from the output dict. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]`  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]` |  a new `Runnable`.  
  
###  `` assign ¶
    
    
    assign(
        **kwargs: [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
        | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]],
    ) -> [RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Assigns new fields to the `dict` output of this `Runnable`.
    
    
    from langchain_core.language_models.fake import FakeStreamingListLLM
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import SystemMessagePromptTemplate
    from langchain_core.runnables import Runnable
    from operator import itemgetter
    
    prompt = (
        SystemMessagePromptTemplate.from_template("You are a nice assistant.")
        + "{question}"
    )
    model = FakeStreamingListLLM(responses=["foo-lish"])
    
    chain: Runnable = prompt | model | {"str": StrOutputParser()}
    
    chain_with_assign = chain.assign(hello=itemgetter("str") | model)
    
    print(chain_with_assign.input_schema.model_json_schema())
    # {'title': 'PromptInput', 'type': 'object', 'properties':
    {'question': {'title': 'Question', 'type': 'string'}}}
    print(chain_with_assign.output_schema.model_json_schema())
    # {'title': 'RunnableSequenceOutput', 'type': 'object', 'properties':
    {'str': {'title': 'Str',
    'type': 'string'}, 'hello': {'title': 'Hello', 'type': 'string'}}}
    

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  A mapping of keys to `Runnable` or `Runnable`-like objects that will be invoked with the entire output dict of this `Runnable`. **TYPE:** `[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]` |  A new `Runnable`.  
  
###  `` invoke ¶
    
    
    invoke(input: dict, config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> PromptValue
    

Invoke the prompt.

PARAMETER | DESCRIPTION  
---|---  
`input` |  Input to the prompt. **TYPE:** `dict`  
`config` |  Configuration for the prompt. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`PromptValue` |  The output of the prompt.  
  
###  `` ainvoke `async` ¶
    
    
    ainvoke(
        input: dict, config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    ) -> PromptValue
    

Async invoke the prompt.

PARAMETER | DESCRIPTION  
---|---  
`input` |  Input to the prompt. **TYPE:** `dict`  
`config` |  Configuration for the prompt. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`PromptValue` |  The output of the prompt.  
  
###  `` batch ¶
    
    
    batch(
        inputs: [list](https://docs.python.org/3/library/stdtypes.html#list)[Input],
        config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None = None,
        *,
        return_exceptions: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None,
    ) -> [list](https://docs.python.org/3/library/stdtypes.html#list)[Output]
    

Default implementation runs invoke in parallel using a thread pool executor.

The default implementation of batch works well for IO bound runnables.

Subclasses must override this method if they can batch more efficiently; e.g., if the underlying `Runnable` uses an API which supports a batch mode.

PARAMETER | DESCRIPTION  
---|---  
`inputs` |  A list of inputs to the `Runnable`. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[Input]`  
`config` |  A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None` **DEFAULT:** `None`  
`return_exceptions` |  Whether to return exceptions instead of raising them. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[Output]` |  A list of outputs from the `Runnable`.  
  
###  `` batch_as_completed ¶
    
    
    batch_as_completed(
        inputs: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Input],
        config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None = None,
        *,
        return_exceptions: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None,
    ) -> [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), Output | [Exception](https://docs.python.org/3/library/exceptions.html#Exception)]]
    

Run `invoke` in parallel on a list of inputs.

Yields results as they complete.

PARAMETER | DESCRIPTION  
---|---  
`inputs` |  A list of inputs to the `Runnable`. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Input]`  
`config` |  A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None` **DEFAULT:** `None`  
`return_exceptions` |  Whether to return exceptions instead of raising them. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), Output | [Exception](https://docs.python.org/3/library/exceptions.html#Exception)]` |  Tuples of the index of the input and the output from the `Runnable`.  
  
###  `` abatch `async` ¶
    
    
    abatch(
        inputs: [list](https://docs.python.org/3/library/stdtypes.html#list)[Input],
        config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None = None,
        *,
        return_exceptions: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None,
    ) -> [list](https://docs.python.org/3/library/stdtypes.html#list)[Output]
    

Default implementation runs `ainvoke` in parallel using `asyncio.gather`.

The default implementation of `batch` works well for IO bound runnables.

Subclasses must override this method if they can batch more efficiently; e.g., if the underlying `Runnable` uses an API which supports a batch mode.

PARAMETER | DESCRIPTION  
---|---  
`inputs` |  A list of inputs to the `Runnable`. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[Input]`  
`config` |  A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None` **DEFAULT:** `None`  
`return_exceptions` |  Whether to return exceptions instead of raising them. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[Output]` |  A list of outputs from the `Runnable`.  
  
###  `` abatch_as_completed `async` ¶
    
    
    abatch_as_completed(
        inputs: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Input],
        config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None = None,
        *,
        return_exceptions: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None,
    ) -> [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), Output | [Exception](https://docs.python.org/3/library/exceptions.html#Exception)]]
    

Run `ainvoke` in parallel on a list of inputs.

Yields results as they complete.

PARAMETER | DESCRIPTION  
---|---  
`inputs` |  A list of inputs to the `Runnable`. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Input]`  
`config` |  A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None` **DEFAULT:** `None`  
`return_exceptions` |  Whether to return exceptions instead of raising them. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), Output | [Exception](https://docs.python.org/3/library/exceptions.html#Exception)]]` |  A tuple of the index of the input and the output from the `Runnable`.  
  
###  `` stream ¶
    
    
    stream(
        input: Input, config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None
    ) -> [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Output]
    

Default implementation of `stream`, which calls `invoke`.

Subclasses must override this method if they support streaming output.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input to the `Runnable`. **TYPE:** `Input`  
`config` |  The config to use for the `Runnable`. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`Output` |  The output of the `Runnable`.  
  
###  `` astream `async` ¶
    
    
    astream(
        input: Input, config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None
    ) -> [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Output]
    

Default implementation of `astream`, which calls `ainvoke`.

Subclasses must override this method if they support streaming output.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input to the `Runnable`. **TYPE:** `Input`  
`config` |  The config to use for the `Runnable`. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Output]` |  The output of the `Runnable`.  
  
###  `` astream_log `async` ¶
    
    
    astream_log(
        input: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
        config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None,
        *,
        diff: [bool](https://docs.python.org/3/library/functions.html#bool) = True,
        with_streamed_output_list: [bool](https://docs.python.org/3/library/functions.html#bool) = True,
        include_names: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        include_types: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        include_tags: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        exclude_names: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        exclude_types: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        exclude_tags: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[RunLogPatch] | [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[RunLog]
    

Stream all output from a `Runnable`, as reported to the callback system.

This includes all inner runs of LLMs, Retrievers, Tools, etc.

Output is streamed as Log objects, which include a list of Jsonpatch ops that describe how the state of the run has changed in each step, and the final state of the run.

The Jsonpatch ops can be applied in order to construct state.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`config` |  The config to use for the `Runnable`. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`diff` |  Whether to yield diffs between each step or the current state. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
`with_streamed_output_list` |  Whether to yield the `streamed_output` list. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
`include_names` |  Only include logs with these names. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`include_types` |  Only include logs with these types. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`include_tags` |  Only include logs with these tags. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`exclude_names` |  Exclude logs with these names. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`exclude_types` |  Exclude logs with these types. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`exclude_tags` |  Exclude logs with these tags. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[RunLogPatch] | [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[RunLog]` |  A `RunLogPatch` or `RunLog` object.  
  
###  `` astream_events `async` ¶
    
    
    astream_events(
        input: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
        config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None,
        *,
        version: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")["v1", "v2"] = "v2",
        include_names: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        include_types: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        include_tags: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        exclude_names: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        exclude_types: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        exclude_tags: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[StreamEvent]
    

Generate a stream of events.

Use to create an iterator over `StreamEvent` that provide real-time information about the progress of the `Runnable`, including `StreamEvent` from intermediate results.

A `StreamEvent` is a dictionary with the following schema:

  * `event`: Event names are of the format: `on_[runnable_type]_(start|stream|end)`.
  * `name`: The name of the `Runnable` that generated the event.
  * `run_id`: Randomly generated ID associated with the given execution of the `Runnable` that emitted the event. A child `Runnable` that gets invoked as part of the execution of a parent `Runnable` is assigned its own unique ID.
  * `parent_ids`: The IDs of the parent runnables that generated the event. The root `Runnable` will have an empty list. The order of the parent IDs is from the root to the immediate parent. Only available for v2 version of the API. The v1 version of the API will return an empty list.
  * `tags`: The tags of the `Runnable` that generated the event.
  * `metadata`: The metadata of the `Runnable` that generated the event.
  * `data`: The data associated with the event. The contents of this field depend on the type of event. See the table below for more details.



Below is a table that illustrates some events that might be emitted by various chains. Metadata fields have been omitted from the table for brevity. Chain definitions have been included after the table.

Note

This reference table is for the v2 version of the schema.

event | name | chunk | input | output  
---|---|---|---|---  
`on_chat_model_start` | `'[model name]'` |  | `{"messages": [[SystemMessage, HumanMessage]]}` |   
`on_chat_model_stream` | `'[model name]'` | `AIMessageChunk(content="hello")` |  |   
`on_chat_model_end` | `'[model name]'` |  | `{"messages": [[SystemMessage, HumanMessage]]}` | `AIMessageChunk(content="hello world")`  
`on_llm_start` | `'[model name]'` |  | `{'input': 'hello'}` |   
`on_llm_stream` | `'[model name]'` | `'Hello'` |  |   
`on_llm_end` | `'[model name]'` |  | `'Hello human!'` |   
`on_chain_start` | `'format_docs'` |  |  |   
`on_chain_stream` | `'format_docs'` | `'hello world!, goodbye world!'` |  |   
`on_chain_end` | `'format_docs'` |  | `[Document(...)]` | `'hello world!, goodbye world!'`  
`on_tool_start` | `'some_tool'` |  | `{"x": 1, "y": "2"}` |   
`on_tool_end` | `'some_tool'` |  |  | `{"x": 1, "y": "2"}`  
`on_retriever_start` | `'[retriever name]'` |  | `{"query": "hello"}` |   
`on_retriever_end` | `'[retriever name]'` |  | `{"query": "hello"}` | `[Document(...), ..]`  
`on_prompt_start` | `'[template_name]'` |  | `{"question": "hello"}` |   
`on_prompt_end` | `'[template_name]'` |  | `{"question": "hello"}` | `ChatPromptValue(messages: [SystemMessage, ...])`  
  
In addition to the standard events, users can also dispatch custom events (see example below).

Custom events will be only be surfaced with in the v2 version of the API!

A custom event has following format:

Attribute | Type | Description  
---|---|---  
`name` | `str` | A user defined name for the event.  
`data` | `Any` | The data associated with the event. This can be anything, though we suggest making it JSON serializable.  
  
Here are declarations associated with the standard events shown above:

`format_docs`:
    
    
    def format_docs(docs: list[Document]) -> str:
        '''Format the docs.'''
        return ", ".join([doc.page_content for doc in docs])
    
    
    format_docs = RunnableLambda(format_docs)
    

`some_tool`:
    
    
    @tool
    def some_tool(x: int, y: str) -> dict:
        '''Some_tool.'''
        return {"x": x, "y": y}
    

`prompt`:
    
    
    template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are Cat Agent 007"),
            ("human", "{question}"),
        ]
    ).with_config({"run_name": "my_template", "tags": ["my_template"]})
    

For instance:
    
    
    from langchain_core.runnables import RunnableLambda
    
    
    async def reverse(s: str) -> str:
        return s[::-1]
    
    
    chain = RunnableLambda(func=reverse)
    
    events = [event async for event in chain.astream_events("hello", version="v2")]
    
    # Will produce the following events
    # (run_id, and parent_ids has been omitted for brevity):
    [
        {
            "data": {"input": "hello"},
            "event": "on_chain_start",
            "metadata": {},
            "name": "reverse",
            "tags": [],
        },
        {
            "data": {"chunk": "olleh"},
            "event": "on_chain_stream",
            "metadata": {},
            "name": "reverse",
            "tags": [],
        },
        {
            "data": {"output": "olleh"},
            "event": "on_chain_end",
            "metadata": {},
            "name": "reverse",
            "tags": [],
        },
    ]
    

Example: Dispatch Custom Event
    
    
    from langchain_core.callbacks.manager import (
        adispatch_custom_event,
    )
    from langchain_core.runnables import RunnableLambda, RunnableConfig
    import asyncio
    
    
    async def slow_thing(some_input: str, config: RunnableConfig) -> str:
        """Do something that takes a long time."""
        await asyncio.sleep(1) # Placeholder for some slow operation
        await adispatch_custom_event(
            "progress_event",
            {"message": "Finished step 1 of 3"},
            config=config # Must be included for python < 3.10
        )
        await asyncio.sleep(1) # Placeholder for some slow operation
        await adispatch_custom_event(
            "progress_event",
            {"message": "Finished step 2 of 3"},
            config=config # Must be included for python < 3.10
        )
        await asyncio.sleep(1) # Placeholder for some slow operation
        return "Done"
    
    slow_thing = RunnableLambda(slow_thing)
    
    async for event in slow_thing.astream_events("some_input", version="v2"):
        print(event)
    

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")`  
`config` |  The config to use for the `Runnable`. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`version` |  The version of the schema to use either `'v2'` or `'v1'`. Users should use `'v2'`. `'v1'` is for backwards compatibility and will be deprecated in `0.4.0`. No default will be assigned until the API is stabilized. custom events will only be surfaced in `'v2'`. **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['v1', 'v2']` **DEFAULT:** `'v2'`  
`include_names` |  Only include events from `Runnable` objects with matching names. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`include_types` |  Only include events from `Runnable` objects with matching types. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`include_tags` |  Only include events from `Runnable` objects with matching tags. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`exclude_names` |  Exclude events from `Runnable` objects with matching names. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`exclude_types` |  Exclude events from `Runnable` objects with matching types. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`exclude_tags` |  Exclude events from `Runnable` objects with matching tags. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. These will be passed to `astream_log` as this implementation of `astream_events` is built on top of `astream_log`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[StreamEvent]` |  An async stream of `StreamEvent`.  
RAISES | DESCRIPTION  
---|---  
`[NotImplementedError](https://docs.python.org/3/library/exceptions.html#NotImplementedError)` |  If the version is not `'v1'` or `'v2'`.  
  
###  `` transform ¶
    
    
    transform(
        input: [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Input], config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None
    ) -> [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Output]
    

Transform inputs to outputs.

Default implementation of transform, which buffers input and calls `astream`.

Subclasses must override this method if they can start producing output while input is still being generated.

PARAMETER | DESCRIPTION  
---|---  
`input` |  An iterator of inputs to the `Runnable`. **TYPE:** `[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Input]`  
`config` |  The config to use for the `Runnable`. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`Output` |  The output of the `Runnable`.  
  
###  `` atransform `async` ¶
    
    
    atransform(
        input: [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Input],
        config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None,
    ) -> [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Output]
    

Transform inputs to outputs.

Default implementation of atransform, which buffers input and calls `astream`.

Subclasses must override this method if they can start producing output while input is still being generated.

PARAMETER | DESCRIPTION  
---|---  
`input` |  An async iterator of inputs to the `Runnable`. **TYPE:** `[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Input]`  
`config` |  The config to use for the `Runnable`. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Output]` |  The output of the `Runnable`.  
  
###  `` bind ¶
    
    
    bind(**kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]
    

Bind arguments to a `Runnable`, returning a new `Runnable`.

Useful when a `Runnable` in a chain requires an argument that is not in the output of the previous `Runnable` or included in the user input.

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  The arguments to bind to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]` |  A new `Runnable` with the arguments bound.  
Example
    
    
    from langchain_ollama import ChatOllama
    from langchain_core.output_parsers import StrOutputParser
    
    model = ChatOllama(model="llama3.1")
    
    # Without bind
    chain = model | StrOutputParser()
    
    chain.invoke("Repeat quoted words exactly: 'One two three four five.'")
    # Output is 'One two three four five.'
    
    # With bind
    chain = model.bind(stop=["three"]) | StrOutputParser()
    
    chain.invoke("Repeat quoted words exactly: 'One two three four five.'")
    # Output is 'One two'
    

###  `` with_config ¶
    
    
    with_config(
        config: [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    ) -> [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]
    

Bind config to a `Runnable`, returning a new `Runnable`.

PARAMETER | DESCRIPTION  
---|---  
`config` |  The config to bind to the `Runnable`. **TYPE:** `[RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]` |  A new `Runnable` with the config bound.  
  
###  `` with_listeners ¶
    
    
    with_listeners(
        *,
        on_start: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run], None]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run, [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")], None]
        | None = None,
        on_end: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run], None] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run, [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")], None] | None = None,
        on_error: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run], None]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run, [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")], None]
        | None = None,
    ) -> [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]
    

Bind lifecycle listeners to a `Runnable`, returning a new `Runnable`.

The Run object contains information about the run, including its `id`, `type`, `input`, `output`, `error`, `start_time`, `end_time`, and any tags or metadata added to the run.

PARAMETER | DESCRIPTION  
---|---  
`on_start` |  Called before the `Runnable` starts running, with the `Run` object. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run], None] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run, [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")], None] | None` **DEFAULT:** `None`  
`on_end` |  Called after the `Runnable` finishes running, with the `Run` object. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run], None] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run, [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")], None] | None` **DEFAULT:** `None`  
`on_error` |  Called if the `Runnable` throws an error, with the `Run` object. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run], None] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run, [RunnableConfig](../runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")], None] | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]` |  A new `Runnable` with the listeners bound.  
Example
    
    
    from langchain_core.runnables import RunnableLambda
    from langchain_core.tracers.schemas import Run
    
    import time
    
    
    def test_runnable(time_to_sleep: int):
        time.sleep(time_to_sleep)
    
    
    def fn_start(run_obj: Run):
        print("start_time:", run_obj.start_time)
    
    
    def fn_end(run_obj: Run):
        print("end_time:", run_obj.end_time)
    
    
    chain = RunnableLambda(test_runnable).with_listeners(
        on_start=fn_start, on_end=fn_end
    )
    chain.invoke(2)
    

###  `` with_alisteners ¶
    
    
    with_alisteners(
        *,
        on_start: AsyncListener | None = None,
        on_end: AsyncListener | None = None,
        on_error: AsyncListener | None = None,
    ) -> [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]
    

Bind async lifecycle listeners to a `Runnable`.

Returns a new `Runnable`.

The Run object contains information about the run, including its `id`, `type`, `input`, `output`, `error`, `start_time`, `end_time`, and any tags or metadata added to the run.

PARAMETER | DESCRIPTION  
---|---  
`on_start` |  Called asynchronously before the `Runnable` starts running, with the `Run` object. **TYPE:** `AsyncListener | None` **DEFAULT:** `None`  
`on_end` |  Called asynchronously after the `Runnable` finishes running, with the `Run` object. **TYPE:** `AsyncListener | None` **DEFAULT:** `None`  
`on_error` |  Called asynchronously if the `Runnable` throws an error, with the `Run` object. **TYPE:** `AsyncListener | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]` |  A new `Runnable` with the listeners bound.  
Example
    
    
    from langchain_core.runnables import RunnableLambda, Runnable
    from datetime import datetime, timezone
    import time
    import asyncio
    
    
    def format_t(timestamp: float) -> str:
        return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()
    
    
    async def test_runnable(time_to_sleep: int):
        print(f"Runnable[{time_to_sleep}s]: starts at {format_t(time.time())}")
        await asyncio.sleep(time_to_sleep)
        print(f"Runnable[{time_to_sleep}s]: ends at {format_t(time.time())}")
    
    
    async def fn_start(run_obj: Runnable):
        print(f"on start callback starts at {format_t(time.time())}")
        await asyncio.sleep(3)
        print(f"on start callback ends at {format_t(time.time())}")
    
    
    async def fn_end(run_obj: Runnable):
        print(f"on end callback starts at {format_t(time.time())}")
        await asyncio.sleep(2)
        print(f"on end callback ends at {format_t(time.time())}")
    
    
    runnable = RunnableLambda(test_runnable).with_alisteners(
        on_start=fn_start, on_end=fn_end
    )
    
    
    async def concurrent_runs():
        await asyncio.gather(runnable.ainvoke(2), runnable.ainvoke(3))
    
    
    asyncio.run(concurrent_runs())
    # Result:
    # on start callback starts at 2025-03-01T07:05:22.875378+00:00
    # on start callback starts at 2025-03-01T07:05:22.875495+00:00
    # on start callback ends at 2025-03-01T07:05:25.878862+00:00
    # on start callback ends at 2025-03-01T07:05:25.878947+00:00
    # Runnable[2s]: starts at 2025-03-01T07:05:25.879392+00:00
    # Runnable[3s]: starts at 2025-03-01T07:05:25.879804+00:00
    # Runnable[2s]: ends at 2025-03-01T07:05:27.881998+00:00
    # on end callback starts at 2025-03-01T07:05:27.882360+00:00
    # Runnable[3s]: ends at 2025-03-01T07:05:28.881737+00:00
    # on end callback starts at 2025-03-01T07:05:28.882428+00:00
    # on end callback ends at 2025-03-01T07:05:29.883893+00:00
    # on end callback ends at 2025-03-01T07:05:30.884831+00:00
    

###  `` with_types ¶
    
    
    with_types(
        *, input_type: [type](https://docs.python.org/3/library/functions.html#type)[Input] | None = None, output_type: [type](https://docs.python.org/3/library/functions.html#type)[Output] | None = None
    ) -> [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]
    

Bind input and output types to a `Runnable`, returning a new `Runnable`.

PARAMETER | DESCRIPTION  
---|---  
`input_type` |  The input type to bind to the `Runnable`. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[Input] | None` **DEFAULT:** `None`  
`output_type` |  The output type to bind to the `Runnable`. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[Output] | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]` |  A new `Runnable` with the types bound.  
  
###  `` with_retry ¶
    
    
    with_retry(
        *,
        retry_if_exception_type: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type)[[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)], ...] = ([Exception](https://docs.python.org/3/library/exceptions.html#Exception),),
        wait_exponential_jitter: [bool](https://docs.python.org/3/library/functions.html#bool) = True,
        exponential_jitter_params: ExponentialJitterParams | None = None,
        stop_after_attempt: [int](https://docs.python.org/3/library/functions.html#int) = 3,
    ) -> [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]
    

Create a new `Runnable` that retries the original `Runnable` on exceptions.

PARAMETER | DESCRIPTION  
---|---  
`retry_if_exception_type` |  A tuple of exception types to retry on. **TYPE:** `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type)[[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)], ...]` **DEFAULT:** `([Exception](https://docs.python.org/3/library/exceptions.html#Exception),)`  
`wait_exponential_jitter` |  Whether to add jitter to the wait time between retries. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
`stop_after_attempt` |  The maximum number of attempts to make before giving up. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)` **DEFAULT:** `3`  
`exponential_jitter_params` |  Parameters for `tenacity.wait_exponential_jitter`. Namely: `initial`, `max`, `exp_base`, and `jitter` (all `float` values). **TYPE:** `ExponentialJitterParams | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]` |  A new `Runnable` that retries the original `Runnable` on exceptions.  
Example
    
    
    from langchain_core.runnables import RunnableLambda
    
    count = 0
    
    
    def _lambda(x: int) -> None:
        global count
        count = count + 1
        if x == 1:
            raise ValueError("x is 1")
        else:
            pass
    
    
    runnable = RunnableLambda(_lambda)
    try:
        runnable.with_retry(
            stop_after_attempt=2,
            retry_if_exception_type=(ValueError,),
        ).invoke(1)
    except ValueError:
        pass
    
    assert count == 2
    

###  `` map ¶
    
    
    map() -> [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[list](https://docs.python.org/3/library/stdtypes.html#list)[Input], [list](https://docs.python.org/3/library/stdtypes.html#list)[Output]]
    

Return a new `Runnable` that maps a list of inputs to a list of outputs.

Calls `invoke` with each input.

RETURNS | DESCRIPTION  
---|---  
`[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[list](https://docs.python.org/3/library/stdtypes.html#list)[Input], [list](https://docs.python.org/3/library/stdtypes.html#list)[Output]]` |  A new `Runnable` that maps a list of inputs to a list of outputs.  
Example
    
    
    from langchain_core.runnables import RunnableLambda
    
    
    def _lambda(x: int) -> int:
        return x + 1
    
    
    runnable = RunnableLambda(_lambda)
    print(runnable.map().invoke([1, 2, 3]))  # [2, 3, 4]
    

###  `` with_fallbacks ¶
    
    
    with_fallbacks(
        fallbacks: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]],
        *,
        exceptions_to_handle: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type)[[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)], ...] = ([Exception](https://docs.python.org/3/library/exceptions.html#Exception),),
        exception_key: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    ) -> RunnableWithFallbacks[Input, Output]
    

Add fallbacks to a `Runnable`, returning a new `Runnable`.

The new `Runnable` will try the original `Runnable`, and then each fallback in order, upon failures.

PARAMETER | DESCRIPTION  
---|---  
`fallbacks` |  A sequence of runnables to try if the original `Runnable` fails. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]]`  
`exceptions_to_handle` |  A tuple of exception types to handle. **TYPE:** `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type)[[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)], ...]` **DEFAULT:** `([Exception](https://docs.python.org/3/library/exceptions.html#Exception),)`  
`exception_key` |  If `string` is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key. If `None`, exceptions will not be passed to fallbacks. If used, the base `Runnable` and its fallbacks must accept a dictionary as input. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`RunnableWithFallbacks[Input, Output]` |  A new `Runnable` that will try the original `Runnable`, and then each Fallback in order, upon failures.  
Example
    
    
    from typing import Iterator
    
    from langchain_core.runnables import RunnableGenerator
    
    
    def _generate_immediate_error(input: Iterator) -> Iterator[str]:
        raise ValueError()
        yield ""
    
    
    def _generate(input: Iterator) -> Iterator[str]:
        yield from "foo bar"
    
    
    runnable = RunnableGenerator(_generate_immediate_error).with_fallbacks(
        [RunnableGenerator(_generate)]
    )
    print("".join(runnable.stream({})))  # foo bar
    

PARAMETER | DESCRIPTION  
---|---  
`fallbacks` |  A sequence of runnables to try if the original `Runnable` fails. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]]`  
`exceptions_to_handle` |  A tuple of exception types to handle. **TYPE:** `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type)[[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)], ...]` **DEFAULT:** `([Exception](https://docs.python.org/3/library/exceptions.html#Exception),)`  
`exception_key` |  If `string` is specified then handled exceptions will be passed to fallbacks as part of the input under the specified key. If `None`, exceptions will not be passed to fallbacks. If used, the base `Runnable` and its fallbacks must accept a dictionary as input. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`RunnableWithFallbacks[Input, Output]` |  A new `Runnable` that will try the original `Runnable`, and then each Fallback in order, upon failures.  
  
###  `` as_tool ¶
    
    
    as_tool(
        args_schema: [type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")] | None = None,
        *,
        name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        description: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        arg_types: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [type](https://docs.python.org/3/library/functions.html#type)] | None = None,
    ) -> [BaseTool](../../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span> \(<code>langchain_core.tools.BaseTool</code>\)")
    

Create a `BaseTool` from a `Runnable`.

`as_tool` will instantiate a `BaseTool` with a name, description, and `args_schema` from a `Runnable`. Where possible, schemas are inferred from `runnable.get_input_schema`.

Alternatively (e.g., if the `Runnable` takes a dict as input and the specific `dict` keys are not typed), the schema can be specified directly with `args_schema`.

You can also pass `arg_types` to just specify the required arguments and their types.

PARAMETER | DESCRIPTION  
---|---  
`args_schema` |  The schema for the tool. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")] | None` **DEFAULT:** `None`  
`name` |  The name of the tool. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`description` |  The description of the tool. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`arg_types` |  A dictionary of argument names to types. **TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [type](https://docs.python.org/3/library/functions.html#type)] | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[BaseTool](../../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span> \(<code>langchain_core.tools.BaseTool</code>\)")` |  A `BaseTool` instance.  
  
Typed dict input:
    
    
    from typing_extensions import TypedDict
    from langchain_core.runnables import RunnableLambda
    
    
    class Args(TypedDict):
        a: int
        b: list[int]
    
    
    def f(x: Args) -> str:
        return str(x["a"] * max(x["b"]))
    
    
    runnable = RunnableLambda(f)
    as_tool = runnable.as_tool()
    as_tool.invoke({"a": 3, "b": [1, 2]})
    

`dict` input, specifying schema via `args_schema`:
    
    
    from typing import Any
    from pydantic import BaseModel, Field
    from langchain_core.runnables import RunnableLambda
    
    def f(x: dict[str, Any]) -> str:
        return str(x["a"] * max(x["b"]))
    
    class FSchema(BaseModel):
        """Apply a function to an integer and list of integers."""
    
        a: int = Field(..., description="Integer")
        b: list[int] = Field(..., description="List of ints")
    
    runnable = RunnableLambda(f)
    as_tool = runnable.as_tool(FSchema)
    as_tool.invoke({"a": 3, "b": [1, 2]})
    

`dict` input, specifying schema via `arg_types`:
    
    
    from typing import Any
    from langchain_core.runnables import RunnableLambda
    
    
    def f(x: dict[str, Any]) -> str:
        return str(x["a"] * max(x["b"]))
    
    
    runnable = RunnableLambda(f)
    as_tool = runnable.as_tool(arg_types={"a": int, "b": list[int]})
    as_tool.invoke({"a": 3, "b": [1, 2]})
    

`str` input:
    
    
    from langchain_core.runnables import RunnableLambda
    
    
    def f(x: str) -> str:
        return x + "a"
    
    
    def g(x: str) -> str:
        return x + "z"
    
    
    runnable = RunnableLambda(f) | g
    as_tool = runnable.as_tool()
    as_tool.invoke("b")
    

###  `` is_lc_serializable `classmethod` ¶
    
    
    is_lc_serializable() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Return `True` as this class is serializable.

###  `` lc_id `classmethod` ¶
    
    
    lc_id() -> [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Return a unique identifier for this class for serialization purposes.

The unique identifier is a list of strings that describes the path to the object.

For example, for the class `langchain.llms.openai.OpenAI`, the id is `["langchain", "llms", "openai", "OpenAI"]`.

###  `` to_json ¶
    
    
    to_json() -> SerializedConstructor | SerializedNotImplemented
    

Serialize the `Runnable` to JSON.

RETURNS | DESCRIPTION  
---|---  
`SerializedConstructor | SerializedNotImplemented` |  A JSON-serializable representation of the `Runnable`.  
  
###  `` to_json_not_implemented ¶
    
    
    to_json_not_implemented() -> SerializedNotImplemented
    

Serialize a "not implemented" object.

RETURNS | DESCRIPTION  
---|---  
`SerializedNotImplemented` |  `SerializedNotImplemented`.  
  
###  `` configurable_fields ¶
    
    
    configurable_fields(
        **kwargs: AnyConfigurableField,
    ) -> [RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Output]
    

Configure particular `Runnable` fields at runtime.

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  A dictionary of `ConfigurableField` instances to configure. **TYPE:** `AnyConfigurableField` **DEFAULT:** `{}`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If a configuration key is not found in the `Runnable`.  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Output]` |  A new `Runnable` with the fields configured.  
      
    
    from langchain_core.runnables import ConfigurableField
    from langchain_openai import ChatOpenAI
    
    model = ChatOpenAI(max_tokens=20).configurable_fields(
        max_tokens=ConfigurableField(
            id="output_token_number",
            name="Max tokens in the output",
            description="The maximum number of tokens in the output",
        )
    )
    
    # max_tokens = 20
    print("max_tokens_20: ", model.invoke("tell me something about chess").content)
    
    # max_tokens = 200
    print(
        "max_tokens_200: ",
        model.with_config(configurable={"output_token_number": 200})
        .invoke("tell me something about chess")
        .content,
    )
    

###  `` configurable_alternatives ¶
    
    
    configurable_alternatives(
        which: ConfigurableField,
        *,
        default_key: [str](https://docs.python.org/3/library/stdtypes.html#str) = "default",
        prefix_keys: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        **kwargs: [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[], [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]],
    ) -> [RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Output]
    

Configure alternatives for `Runnable` objects that can be set at runtime.

PARAMETER | DESCRIPTION  
---|---  
`which` |  The `ConfigurableField` instance that will be used to select the alternative. **TYPE:** `ConfigurableField`  
`default_key` |  The default key to use if no alternative is selected. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)` **DEFAULT:** `'default'`  
`prefix_keys` |  Whether to prefix the keys with the `ConfigurableField` id. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`**kwargs` |  A dictionary of keys to `Runnable` instances or callables that return `Runnable` instances. **TYPE:** `[Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[], [Runnable](../runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]]` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Output]` |  A new `Runnable` with the alternatives configured.  
      
    
    from langchain_anthropic import ChatAnthropic
    from langchain_core.runnables.utils import ConfigurableField
    from langchain_openai import ChatOpenAI
    
    model = ChatAnthropic(
        model_name="claude-sonnet-4-5-20250929"
    ).configurable_alternatives(
        ConfigurableField(id="llm"),
        default_key="anthropic",
        openai=ChatOpenAI(),
    )
    
    # uses the default model ChatAnthropic
    print(model.invoke("which organization created you?").content)
    
    # uses ChatOpenAI
    print(
        model.with_config(configurable={"llm": "openai"})
        .invoke("which organization created you?")
        .content
    )
    

###  `` validate_variable_names ¶
    
    
    validate_variable_names() -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Validate variable names do not include restricted names.

###  `` format_prompt ¶
    
    
    format_prompt(**kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> ChatPromptValue
    

Format prompt. Should return a ChatPromptValue.

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  Keyword arguments to use for formatting. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`ChatPromptValue` |  ChatPromptValue.  
  
###  `` aformat_prompt `async` ¶
    
    
    aformat_prompt(**kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> ChatPromptValue
    

Async format prompt. Should return a ChatPromptValue.

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  Keyword arguments to use for formatting. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`ChatPromptValue` |  PromptValue.  
  
###  `` format ¶
    
    
    format(**kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> [str](https://docs.python.org/3/library/stdtypes.html#str)
    

Format the chat template into a string.

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  keyword arguments to use for filling in template variables in all the template messages in this chat template. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[str](https://docs.python.org/3/library/stdtypes.html#str)` |  formatted string.  
  
###  `` aformat `async` ¶
    
    
    aformat(**kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> [str](https://docs.python.org/3/library/stdtypes.html#str)
    

Async format the chat template into a string.

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  keyword arguments to use for filling in template variables in all the template messages in this chat template. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[str](https://docs.python.org/3/library/stdtypes.html#str)` |  formatted string.  
  
###  `` dict ¶
    
    
    dict(**kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> dict
    

Return dictionary representation of prompt.

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  Any additional arguments to pass to the dictionary. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`dict` |  Dictionary representation of the prompt.  
  
###  `` pretty_print ¶
    
    
    pretty_print() -> None
    

Print a human-readable representation.

Back to top

---
