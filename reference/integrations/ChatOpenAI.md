# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:22.

## Converted Web Pages

### ChatOpenAI | LangChain Reference

**Source:** https://reference.langchain.com/python/integrations/langchain_openai/ChatOpenAI/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/integrations/langchain_openai/ChatOpenAI.md "Edit this page")

#  `ChatOpenAI`¶

Reference docs

This page contains **reference documentation** for `ChatOpenAI`. See [the docs](https://docs.langchain.com/oss/python/integrations/chat/openai) for conceptual guides, tutorials, and examples on using `ChatOpenAI`.

##  `` langchain_openai.chat_models.ChatOpenAI ¶

Bases: `[BaseChatOpenAI](../BaseChatOpenAI/#langchain_openai.chat_models.base.BaseChatOpenAI "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseChatOpenAI</span> \(<code>langchain_openai.chat_models.base.BaseChatOpenAI</code>\)")`

Interface to OpenAI chat model APIs.

Setup

Install `langchain-openai` and set environment variable `OPENAI_API_KEY`.
    
    
    pip install -U langchain-openai
    
    # or using uv
    uv add langchain-openai
    
    
    
    export OPENAI_API_KEY="your-api-key"
    

Key init args — completion params Param | Type | Description  
---|---|---  
`model` | `str` | Name of OpenAI model to use.  
`temperature` | `float` | Sampling temperature.  
`max_tokens` | `int | None` | Max number of tokens to generate.  
`logprobs` | `bool | None` | Whether to return logprobs.  
`stream_options` | `dict` | Configure streaming outputs, like whether to return token usage when streaming (`{"include_usage": True}`).  
`use_responses_api` | `bool | None` | Whether to use the responses API.  
  
See full list of supported init args and their descriptions below.

Key init args — client params Param | Type | Description  
---|---|---  
`timeout` | `float | Tuple[float, float] | Any | None` | Timeout for requests.  
`max_retries` | `int | None` | Max number of retries.  
`api_key` | `str | None` | OpenAI API key. If not passed in will be read from env var `OPENAI_API_KEY`.  
`base_url` | `str | None` | Base URL for API requests. Only specify if using a proxy or service emulator.  
`organization` | `str | None` | OpenAI organization ID. If not passed in will be read from env var `OPENAI_ORG_ID`.  
  
See full list of supported init args and their descriptions below.

Instantiate

Create a model instance with desired params. For example:
    
    
    from langchain_openai import ChatOpenAI
    
    model = ChatOpenAI(
        model="...",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # api_key="...",
        # base_url="...",
        # organization="...",
        # other params...
    )
    

See all available params below.

Preserved params

Any param which is not explicitly supported will be passed directly to [`openai.OpenAI.chat.completions.create(...)`](https://platform.openai.com/docs/api-reference/chat/create) every time to the model is invoked. For example:
    
    
    from langchain_openai import ChatOpenAI
    import openai
    
    ChatOpenAI(..., frequency_penalty=0.2).invoke(...)
    
    # Results in underlying API call of:
    
    openai.OpenAI(..).chat.completions.create(..., frequency_penalty=0.2)
    
    # Which is also equivalent to:
    
    ChatOpenAI(...).invoke(..., frequency_penalty=0.2)
    

Invoke

Generate a response from the model:
    
    
    messages = [
        (
            "system",
            "You are a helpful translator. Translate the user sentence to French.",
        ),
        ("human", "I love programming."),
    ]
    model.invoke(messages)
    

Results in an `AIMessage` response:
    
    
    AIMessage(
        content="J'adore la programmation.",
        response_metadata={
            "token_usage": {
                "completion_tokens": 5,
                "prompt_tokens": 31,
                "total_tokens": 36,
            },
            "model_name": "gpt-4o",
            "system_fingerprint": "fp_43dfabdef1",
            "finish_reason": "stop",
            "logprobs": None,
        },
        id="run-012cffe2-5d3d-424d-83b5-51c6d4a593d1-0",
        usage_metadata={"input_tokens": 31, "output_tokens": 5, "total_tokens": 36},
    )
    

Stream

Stream a response from the model:
    
    
    for chunk in model.stream(messages):
        print(chunk.text, end="")
    

Results in a sequence of `AIMessageChunk` objects with partial content:
    
    
    AIMessageChunk(content="", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")
    AIMessageChunk(content="J", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")
    AIMessageChunk(content="'adore", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")
    AIMessageChunk(content=" la", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")
    AIMessageChunk(
        content=" programmation", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0"
    )
    AIMessageChunk(content=".", id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0")
    AIMessageChunk(
        content="",
        response_metadata={"finish_reason": "stop"},
        id="run-9e1517e3-12bf-48f2-bb1b-2e824f7cd7b0",
    )
    

To collect the full message, you can concatenate the chunks:
    
    
    stream = model.stream(messages)
    full = next(stream)
    for chunk in stream:
        full += chunk
    
    
    
    full = AIMessageChunk(
        content="J'adore la programmation.",
        response_metadata={"finish_reason": "stop"},
        id="run-bf917526-7f58-4683-84f7-36a6b671d140",
    )
    

Async

Asynchronous equivalents of `invoke`, `stream`, and `batch` are also available:
    
    
    # Invoke
    await model.ainvoke(messages)
    
    # Stream
    async for chunk in (await model.astream(messages))
    
    # Batch
    await model.abatch([messages])
    

Results in an `AIMessage` response:
    
    
    AIMessage(
        content="J'adore la programmation.",
        response_metadata={
            "token_usage": {
                "completion_tokens": 5,
                "prompt_tokens": 31,
                "total_tokens": 36,
            },
            "model_name": "gpt-4o",
            "system_fingerprint": "fp_43dfabdef1",
            "finish_reason": "stop",
            "logprobs": None,
        },
        id="run-012cffe2-5d3d-424d-83b5-51c6d4a593d1-0",
        usage_metadata={
            "input_tokens": 31,
            "output_tokens": 5,
            "total_tokens": 36,
        },
    )
    

For batched calls, results in a `list[AIMessage]`.

Tool calling
    
    
    from pydantic import BaseModel, Field
    
    
    class GetWeather(BaseModel):
        '''Get the current weather in a given location'''
    
        location: str = Field(
            ..., description="The city and state, e.g. San Francisco, CA"
        )
    
    
    class GetPopulation(BaseModel):
        '''Get the current population in a given location'''
    
        location: str = Field(
            ..., description="The city and state, e.g. San Francisco, CA"
        )
    
    
    model_with_tools = model.bind_tools(
        [GetWeather, GetPopulation]
        # strict = True  # Enforce tool args schema is respected
    )
    ai_msg = model_with_tools.invoke(
        "Which city is hotter today and which is bigger: LA or NY?"
    )
    ai_msg.tool_calls
    
    
    
    [
        {
            "name": "GetWeather",
            "args": {"location": "Los Angeles, CA"},
            "id": "call_6XswGD5Pqk8Tt5atYr7tfenU",
        },
        {
            "name": "GetWeather",
            "args": {"location": "New York, NY"},
            "id": "call_ZVL15vA8Y7kXqOy3dtmQgeCi",
        },
        {
            "name": "GetPopulation",
            "args": {"location": "Los Angeles, CA"},
            "id": "call_49CFW8zqC9W7mh7hbMLSIrXw",
        },
        {
            "name": "GetPopulation",
            "args": {"location": "New York, NY"},
            "id": "call_6ghfKxV264jEfe1mRIkS3PE7",
        },
    ]
    

Parallel tool calls

[`openai >= 1.32`](https://pypi.org/project/openai/) supports a `parallel_tool_calls` parameter that defaults to `True`. This parameter can be set to `False` to disable parallel tool calls:
    
    
    ai_msg = model_with_tools.invoke(
        "What is the weather in LA and NY?", parallel_tool_calls=False
    )
    ai_msg.tool_calls
    
    
    
    [
        {
            "name": "GetWeather",
            "args": {"location": "Los Angeles, CA"},
            "id": "call_4OoY0ZR99iEvC7fevsH8Uhtz",
        }
    ]
    

Like other runtime parameters, `parallel_tool_calls` can be bound to a model using `model.bind(parallel_tool_calls=False)` or during instantiation by setting `model_kwargs`.

See `bind_tools` for more.

Built-in (server-side) tools

You can access [built-in tools](https://platform.openai.com/docs/guides/tools?api-mode=responses) supported by the OpenAI Responses API. See [LangChain docs](https://docs.langchain.com/oss/python/integrations/chat/openai#responses-api) for more detail.
    
    
    from langchain_openai import ChatOpenAI
    
    model = ChatOpenAI(model="...", output_version="responses/v1")
    
    tool = {"type": "web_search"}
    model_with_tools = model.bind_tools([tool])
    
    response = model_with_tools.invoke("What was a positive news story from today?")
    response.content
    
    
    
    [
        {
            "type": "text",
            "text": "Today, a heartwarming story emerged from ...",
            "annotations": [
                {
                    "end_index": 778,
                    "start_index": 682,
                    "title": "Title of story",
                    "type": "url_citation",
                    "url": "<url of story>",
                }
            ],
        }
    ]
    

Added in `langchain-openai` 0.3.9

Added in `langchain-openai` 0.3.26: Updated `AIMessage` format

[`langchain-openai >= 0.3.26`](https://pypi.org/project/langchain-openai/#history) allows users to opt-in to an updated `AIMessage` format when using the Responses API. Setting `ChatOpenAI(..., output_version="responses/v1")` will format output from reasoning summaries, built-in tool invocations, and other response items into the message's `content` field, rather than `additional_kwargs`. We recommend this format for new applications.

Managing conversation state

OpenAI's Responses API supports management of [conversation state](https://platform.openai.com/docs/guides/conversation-state?api-mode=responses). Passing in response IDs from previous messages will continue a conversational thread.
    
    
    from langchain_openai import ChatOpenAI
    
    model = ChatOpenAI(
        model="...",
        use_responses_api=True,
        output_version="responses/v1",
    )
    response = model.invoke("Hi, I'm Bob.")
    response.text
    
    
    
    "Hi Bob! How can I assist you today?"
    
    
    
    second_response = model.invoke(
        "What is my name?",
        previous_response_id=response.response_metadata["id"],
    )
    second_response.text
    
    
    
    "Your name is Bob. How can I help you today, Bob?"
    

Added in `langchain-openai` 0.3.9

Added in `langchain-openai` 0.3.26

You can also initialize `ChatOpenAI` with `use_previous_response_id`. Input messages up to the most recent response will then be dropped from request payloads, and `previous_response_id` will be set using the ID of the most recent response.
    
    
    model = ChatOpenAI(model="...", use_previous_response_id=True)
    

Reasoning output

OpenAI's Responses API supports [reasoning models](https://platform.openai.com/docs/guides/reasoning?api-mode=responses) that expose a summary of internal reasoning processes.
    
    
    from langchain_openai import ChatOpenAI
    
    reasoning = {
        "effort": "medium",  # 'low', 'medium', or 'high'
        "summary": "auto",  # 'detailed', 'auto', or None
    }
    
    model = ChatOpenAI(
        model="...", reasoning=reasoning, output_version="responses/v1"
    )
    response = model.invoke("What is 3^3?")
    
    # Response text
    print(f"Output: {response.text}")
    
    # Reasoning summaries
    for block in response.content:
        if block["type"] == "reasoning":
            for summary in block["summary"]:
                print(summary["text"])
    
    
    
    Output: 3³ = 27
    Reasoning: The user wants to know...
    

Added in `langchain-openai` 0.3.26: Updated `AIMessage` format

[`langchain-openai >= 0.3.26`](https://pypi.org/project/langchain-openai/#history) allows users to opt-in to an updated `AIMessage` format when using the Responses API. Setting `ChatOpenAI(..., output_version="responses/v1")` will format output from reasoning summaries, built-in tool invocations, and other response items into the message's `content` field, rather than `additional_kwargs`. We recommend this format for new applications.

Structured output
    
    
    from pydantic import BaseModel, Field
    
    
    class Joke(BaseModel):
        '''Joke to tell user.'''
    
        setup: str = Field(description="The setup of the joke")
        punchline: str = Field(description="The punchline to the joke")
        rating: int | None = Field(
            description="How funny the joke is, from 1 to 10"
        )
    
    
    structured_model = model.with_structured_output(Joke)
    structured_model.invoke("Tell me a joke about cats")
    
    
    
    Joke(
        setup="Why was the cat sitting on the computer?",
        punchline="To keep an eye on the mouse!",
        rating=None,
    )
    

See `with_structured_output` for more info.

JSON mode
    
    
    json_model = model.bind(response_format={"type": "json_object"})
    ai_msg = json_model.invoke(
        "Return a JSON object with key 'random_ints' and a value of 10 random ints in [0-99]"
    )
    ai_msg.content
    
    
    
    '\\n{\\n  "random_ints": [23, 87, 45, 12, 78, 34, 56, 90, 11, 67]\\n}'
    

Image input
    
    
    import base64
    import httpx
    from langchain.messages import HumanMessage
    
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
    image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")
    message = HumanMessage(
        content=[
            {"type": "text", "text": "describe the weather in this image"},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_data}"},
            },
        ]
    )
    
    ai_msg = model.invoke([message])
    ai_msg.content
    
    
    
    "The weather in the image appears to be clear and pleasant. The sky is mostly blue with scattered, light clouds, suggesting a sunny day with minimal cloud cover. There is no indication of rain or strong winds, and the overall scene looks bright and calm. The lush green grass and clear visibility further indicate good weather conditions."
    

Token usage
    
    
    ai_msg = model.invoke(messages)
    ai_msg.usage_metadata
    
    ```txt
    {"input_tokens": 28, "output_tokens": 5, "total_tokens": 33}
    

When streaming, set the `stream_usage` kwarg:
    
    
    stream = model.stream(messages, stream_usage=True)
    full = next(stream)
    for chunk in stream:
        full += chunk
    full.usage_metadata
    
    
    
    {"input_tokens": 28, "output_tokens": 5, "total_tokens": 33}
    

Logprobs
    
    
    logprobs_model = model.bind(logprobs=True)
    ai_msg = logprobs_model.invoke(messages)
    ai_msg.response_metadata["logprobs"]
    
    
    
    {
        "content": [
            {
                "token": "J",
                "bytes": [74],
                "logprob": -4.9617593e-06,
                "top_logprobs": [],
            },
            {
                "token": "'adore",
                "bytes": [39, 97, 100, 111, 114, 101],
                "logprob": -0.25202933,
                "top_logprobs": [],
            },
            {
                "token": " la",
                "bytes": [32, 108, 97],
                "logprob": -0.20141791,
                "top_logprobs": [],
            },
            {
                "token": " programmation",
                "bytes": [
                    32,
                    112,
                    114,
                    111,
                    103,
                    114,
                    97,
                    109,
                    109,
                    97,
                    116,
                    105,
                    111,
                    110,
                ],
                "logprob": -1.9361265e-07,
                "top_logprobs": [],
            },
            {
                "token": ".",
                "bytes": [46],
                "logprob": -1.2233183e-05,
                "top_logprobs": [],
            },
        ]
    }
    

Response metadata
    
    
    ai_msg = model.invoke(messages)
    ai_msg.response_metadata
    
    
    
    {
        "token_usage": {
            "completion_tokens": 5,
            "prompt_tokens": 28,
            "total_tokens": 33,
        },
        "model_name": "gpt-4o",
        "system_fingerprint": "fp_319be4768e",
        "finish_reason": "stop",
        "logprobs": None,
    }
    

Flex processing

OpenAI offers a variety of [service tiers](https://platform.openai.com/docs/guides/flex-processing?api-mode=responses). The "flex" tier offers cheaper pricing for requests, with the trade-off that responses may take longer and resources might not always be available. This approach is best suited for non-critical tasks, including model testing, data enhancement, or jobs that can be run asynchronously.

To use it, initialize the model with `service_tier="flex"`:
    
    
    from langchain_openai import ChatOpenAI
    
    model = ChatOpenAI(model="...", service_tier="flex")
    

Note that this is a beta feature that is only available for a subset of models. See OpenAI [flex processing docs](https://platform.openai.com/docs/guides/flex-processing?api-mode=responses) for more detail.

OpenAI-compatible APIs

`ChatOpenAI` can be used with OpenAI-compatible APIs like [LM Studio](https://lmstudio.ai/), [vLLM](https://github.com/vllm-project/vllm), [Ollama](https://ollama.com/), and others.

To use custom parameters specific to these providers, use the `extra_body` parameter.

LM Studio example with TTL (auto-eviction)
    
    
    from langchain_openai import ChatOpenAI
    
    model = ChatOpenAI(
        base_url="http://localhost:1234/v1",
        api_key="lm-studio",  # Can be any string
        model="mlx-community/QwQ-32B-4bit",
        temperature=0,
        extra_body={"ttl": 300},  # Auto-evict model after 5 minutes of inactivity
    )
    

vLLM example with custom parameters
    
    
    model = ChatOpenAI(
        base_url="http://localhost:8000/v1",
        api_key="EMPTY",
        model="meta-llama/Llama-2-7b-chat-hf",
        extra_body={"use_beam_search": True, "best_of": 4},
    )
    

`model_kwargs` vs `extra_body`

Use the correct parameter for different types of API arguments:

**Use`model_kwargs` for:**

  * Standard OpenAI API parameters not explicitly defined as class parameters
  * Parameters that should be flattened into the top-level request payload
  * Examples: `max_completion_tokens`, `stream_options`, `modalities`, `audio`


    
    
    # Standard OpenAI parameters
    model = ChatOpenAI(
        model="...",
        model_kwargs={
            "stream_options": {"include_usage": True},
            "max_completion_tokens": 300,
            "modalities": ["text", "audio"],
            "audio": {"voice": "alloy", "format": "wav"},
        },
    )
    

**Use`extra_body` for:**

  * Custom parameters specific to OpenAI-compatible providers (vLLM, LM Studio, OpenRouter, etc.)
  * Parameters that need to be nested under `extra_body` in the request
  * Any non-standard OpenAI API parameters


    
    
    # Custom provider parameters
    model = ChatOpenAI(
        base_url="http://localhost:8000/v1",
        model="custom-model",
        extra_body={
            "use_beam_search": True,  # vLLM parameter
            "best_of": 4,  # vLLM parameter
            "ttl": 300,  # LM Studio parameter
        },
    )
    

**Key Differences:**

  * `model_kwargs`: Parameters are **merged into top-level** request payload
  * `extra_body`: Parameters are **nested under`extra_body`** key in request



Warning

Always use `extra_body` for custom parameters, **not** `model_kwargs`. Using `model_kwargs` for non-OpenAI parameters will cause API errors.

Prompt caching optimization

For high-volume applications with repetitive prompts, use `prompt_cache_key` per-invocation to improve cache hit rates and reduce costs:
    
    
    model = ChatOpenAI(model="...")
    
    response = model.invoke(
        messages,
        prompt_cache_key="example-key-a",  # Routes to same machine for cache hits
    )
    
    customer_response = model.invoke(messages, prompt_cache_key="example-key-b")
    support_response = model.invoke(messages, prompt_cache_key="example-key-c")
    
    # Dynamic cache keys based on context
    cache_key = f"example-key-{dynamic_suffix}"
    response = model.invoke(messages, prompt_cache_key=cache_key)
    

Cache keys help ensure requests with the same prompt prefix are routed to machines with existing cache, providing cost reduction and latency improvement on cached tokens.

METHOD | DESCRIPTION  
---|---  
`get_name` |  Get the name of the `Runnable`.  
`get_input_schema` |  Get a Pydantic model that can be used to validate input to the `Runnable`.  
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
`invoke` |  Transform a single input into an output.  
`ainvoke` |  Transform a single input into an output.  
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
`__init__` |   
`lc_id` |  Return a unique identifier for this class for serialization purposes.  
`to_json` |  Serialize the `Runnable` to JSON.  
`to_json_not_implemented` |  Serialize a "not implemented" object.  
`configurable_fields` |  Configure particular `Runnable` fields at runtime.  
`configurable_alternatives` |  Configure alternatives for `Runnable` objects that can be set at runtime.  
`set_verbose` |  If verbose is `None`, set it.  
`generate_prompt` |  Pass a sequence of prompts to the model and return model generations.  
`agenerate_prompt` |  Asynchronously pass a sequence of prompts and return model generations.  
`get_token_ids` |  Get the tokens present in the text with tiktoken package.  
`get_num_tokens` |  Get the number of tokens present in the text.  
`get_num_tokens_from_messages` |  Calculate num tokens for `gpt-3.5-turbo` and `gpt-4` with `tiktoken` package.  
`generate` |  Pass a sequence of prompts to the model and return model generations.  
`agenerate` |  Asynchronously pass a sequence of prompts to a model and return generations.  
`dict` |  Return a dictionary of the LLM.  
`bind_tools` |  Bind tool-like objects to this chat model.  
`build_extra` |  Build extra kwargs from additional params that were passed in.  
`validate_temperature` |  Validate temperature parameter for different models.  
`validate_environment` |  Validate that api key and python package exists in environment.  
`get_lc_namespace` |  Get the namespace of the LangChain object.  
`is_lc_serializable` |  Return whether this model can be serialized by LangChain.  
`with_structured_output` |  Model wrapper that returns outputs formatted to match the given schema.  
  
###  `` name `class-attribute` `instance-attribute` ¶
    
    
    name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None
    

The name of the `Runnable`. Used for debugging and tracing.

###  `` InputType `property` ¶
    
    
    InputType: [TypeAlias](https://docs.python.org/3/library/typing.html#typing.TypeAlias "<code>typing.TypeAlias</code>")
    

Get the input type for this `Runnable`.

###  `` OutputType `property` ¶
    
    
    OutputType: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Get the output type for this `Runnable`.

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

###  `` cache `class-attribute` `instance-attribute` ¶
    
    
    cache: [BaseCache](../../../langchain_core/caches/#langchain_core.caches.BaseCache "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseCache</span> \(<code>langchain_core.caches.BaseCache</code>\)") | [bool](https://docs.python.org/3/library/functions.html#bool) | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=None, exclude=True)
    

Whether to cache the response.

  * If `True`, will use the global cache.
  * If `False`, will not use a cache
  * If `None`, will use the global cache if it's set, otherwise no cache.
  * If instance of `BaseCache`, will use the provided cache.



Caching is not currently supported for streaming methods of models.

###  `` verbose `class-attribute` `instance-attribute` ¶
    
    
    verbose: [bool](https://docs.python.org/3/library/functions.html#bool) = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default_factory=_get_verbosity, exclude=True, repr=False)
    

Whether to print out response text.

###  `` callbacks `class-attribute` `instance-attribute` ¶
    
    
    callbacks: Callbacks = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=None, exclude=True)
    

Callbacks to add to the run trace.

###  `` tags `class-attribute` `instance-attribute` ¶
    
    
    tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=None, exclude=True)
    

Tags to add to the run trace.

###  `` metadata `class-attribute` `instance-attribute` ¶
    
    
    metadata: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=None, exclude=True)
    

Metadata to add to the run trace.

###  `` custom_get_token_ids `class-attribute` `instance-attribute` ¶
    
    
    custom_get_token_ids: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[str](https://docs.python.org/3/library/stdtypes.html#str)], [list](https://docs.python.org/3/library/stdtypes.html#list)[[int](https://docs.python.org/3/library/functions.html#int)]] | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(
        default=None, exclude=True
    )
    

Optional encoder to use for counting tokens.

###  `` rate_limiter `class-attribute` `instance-attribute` ¶
    
    
    rate_limiter: [BaseRateLimiter](../../../langchain_core/rate_limiters/#langchain_core.rate_limiters.BaseRateLimiter "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.rate_limiters.BaseRateLimiter</span>") | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=None, exclude=True)
    

An optional rate limiter to use for limiting the number of requests.

###  `` disable_streaming `class-attribute` `instance-attribute` ¶
    
    
    disable_streaming: [bool](https://docs.python.org/3/library/functions.html#bool) | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['tool_calling'] = False
    

Whether to disable streaming for this model.

If streaming is bypassed, then `stream`/`astream`/`astream_events` will defer to `invoke`/`ainvoke`.

  * If `True`, will always bypass streaming case.
  * If `'tool_calling'`, will bypass streaming case only when the model is called with a `tools` keyword argument. In other words, LangChain will automatically switch to non-streaming behavior (`invoke`) only when the tools argument is provided. This offers the best of both worlds.
  * If `False` (Default), will always use streaming case if available.



The main reason for this flag is that code might be written using `stream` and a user may want to swap out a given model for another model whose the implementation does not properly support streaming.

###  `` output_version `class-attribute` `instance-attribute` ¶
    
    
    output_version: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(
        default_factory=from_env("LC_OUTPUT_VERSION", default=None)
    )
    

Version of `AIMessage` output format to use.

This field is used to roll-out new output formats for chat model `AIMessage` responses in a backwards-compatible way.

Supported values:

  * `'v0'`: `AIMessage` format as of `langchain-openai 0.3.x`.
  * `'responses/v1'`: Formats Responses API output items into AIMessage content blocks (Responses API only)
  * `'v1'`: v1 of LangChain cross-provider standard.



Behavior changed in `langchain-openai` 1.0.0

Default updated to `"responses/v1"`.

###  `` profile `property` ¶
    
    
    profile: [ModelProfile](../../../langchain_model_profiles/#langchain_model_profiles.ModelProfile "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ModelProfile</span> \(<code>langchain_model_profiles.ModelProfile</code>\)")
    

Return profiling information for the model.

This property relies on the `langchain-model-profiles` package to retrieve chat model capabilities, such as context window sizes and supported features.

RAISES | DESCRIPTION  
---|---  
`[ImportError](https://docs.python.org/3/library/exceptions.html#ImportError)` |  If `langchain-model-profiles` is not installed.  
RETURNS | DESCRIPTION  
---|---  
`[ModelProfile](../../../langchain_model_profiles/#langchain_model_profiles.ModelProfile "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">ModelProfile</span> \(<code>langchain_model_profiles.ModelProfile</code>\)")` |  A `ModelProfile` object containing profiling information for the model.  
  
###  `` model_name `class-attribute` `instance-attribute` ¶
    
    
    model_name: [str](https://docs.python.org/3/library/stdtypes.html#str) = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default='gpt-3.5-turbo', alias='model')
    

Model name to use.

###  `` temperature `class-attribute` `instance-attribute` ¶
    
    
    temperature: [float](https://docs.python.org/3/library/functions.html#float) | None = None
    

What sampling temperature to use.

###  `` model_kwargs `class-attribute` `instance-attribute` ¶
    
    
    model_kwargs: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default_factory=[dict](https://docs.python.org/3/library/stdtypes.html#dict))
    

Holds any model parameters valid for `create` call not explicitly specified.

###  `` openai_api_key `class-attribute` `instance-attribute` ¶
    
    
    openai_api_key: [SecretStr](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretStr "<code>pydantic.SecretStr</code>") | None | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[], [str](https://docs.python.org/3/library/stdtypes.html#str)] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[], [Awaitable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "<code>collections.abc.Awaitable</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str)]] = (
        [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(
            alias="api_key", default_factory=secret_from_env("OPENAI_API_KEY", default=None)
        )
    )
    

API key to use.

Can be inferred from the `OPENAI_API_KEY` environment variable, or specified as a string, or sync or async callable that returns a string.

Specify with environment variable
    
    
    export OPENAI_API_KEY=...
    
    
    
    from langchain_openai import ChatOpenAI
    
    model = ChatOpenAI(model="gpt-5-nano")
    

Specify with a string
    
    
    from langchain_openai import ChatOpenAI
    
    model = ChatOpenAI(model="gpt-5-nano", api_key="...")
    

Specify with a sync callable
    
    
    from langchain_openai import ChatOpenAI
    
    def get_api_key() -> str:
        # Custom logic to retrieve API key
        return "..."
    
    model = ChatOpenAI(model="gpt-5-nano", api_key=get_api_key)
    

Specify with an async callable
    
    
    from langchain_openai import ChatOpenAI
    
    async def get_api_key() -> str:
        # Custom async logic to retrieve API key
        return "..."
    
    model = ChatOpenAI(model="gpt-5-nano", api_key=get_api_key)
    

###  `` openai_api_base `class-attribute` `instance-attribute` ¶
    
    
    openai_api_base: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=None, alias='base_url')
    

Base URL path for API requests, leave blank if not using a proxy or service emulator.

###  `` openai_organization `class-attribute` `instance-attribute` ¶
    
    
    openai_organization: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=None, alias='organization')
    

Automatically inferred from env var `OPENAI_ORG_ID` if not provided.

###  `` request_timeout `class-attribute` `instance-attribute` ¶
    
    
    request_timeout: [float](https://docs.python.org/3/library/functions.html#float) | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[float](https://docs.python.org/3/library/functions.html#float), [float](https://docs.python.org/3/library/functions.html#float)] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(
        default=None, alias="timeout"
    )
    

Timeout for requests to OpenAI completion API. Can be float, `httpx.Timeout` or `None`.

###  `` stream_usage `class-attribute` `instance-attribute` ¶
    
    
    stream_usage: [bool](https://docs.python.org/3/library/functions.html#bool) | None = None
    

Whether to include usage metadata in streaming output. If enabled, an additional message chunk will be generated during the stream including usage metadata.

This parameter is enabled unless `openai_api_base` is set or the model is initialized with a custom client, as many chat completions APIs do not support streaming token usage.

Added in `langchain-openai` 0.3.9

Behavior changed in `langchain-openai` 0.3.35

Enabled for default base URL and client.

###  `` max_retries `class-attribute` `instance-attribute` ¶
    
    
    max_retries: [int](https://docs.python.org/3/library/functions.html#int) | None = None
    

Maximum number of retries to make when generating.

###  `` presence_penalty `class-attribute` `instance-attribute` ¶
    
    
    presence_penalty: [float](https://docs.python.org/3/library/functions.html#float) | None = None
    

Penalizes repeated tokens.

###  `` frequency_penalty `class-attribute` `instance-attribute` ¶
    
    
    frequency_penalty: [float](https://docs.python.org/3/library/functions.html#float) | None = None
    

Penalizes repeated tokens according to frequency.

###  `` seed `class-attribute` `instance-attribute` ¶
    
    
    seed: [int](https://docs.python.org/3/library/functions.html#int) | None = None
    

Seed for generation

###  `` logprobs `class-attribute` `instance-attribute` ¶
    
    
    logprobs: [bool](https://docs.python.org/3/library/functions.html#bool) | None = None
    

Whether to return logprobs.

###  `` top_logprobs `class-attribute` `instance-attribute` ¶
    
    
    top_logprobs: [int](https://docs.python.org/3/library/functions.html#int) | None = None
    

Number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to true if this parameter is used.

###  `` logit_bias `class-attribute` `instance-attribute` ¶
    
    
    logit_bias: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int)] | None = None
    

Modify the likelihood of specified tokens appearing in the completion.

###  `` streaming `class-attribute` `instance-attribute` ¶
    
    
    streaming: [bool](https://docs.python.org/3/library/functions.html#bool) = False
    

Whether to stream the results or not.

###  `` n `class-attribute` `instance-attribute` ¶
    
    
    n: [int](https://docs.python.org/3/library/functions.html#int) | None = None
    

Number of chat completions to generate for each prompt.

###  `` top_p `class-attribute` `instance-attribute` ¶
    
    
    top_p: [float](https://docs.python.org/3/library/functions.html#float) | None = None
    

Total probability mass of tokens to consider at each step.

###  `` reasoning_effort `class-attribute` `instance-attribute` ¶
    
    
    reasoning_effort: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None
    

Constrains effort on reasoning for reasoning models. For use with the Chat Completions API.

Reasoning models only.

Currently supported values are `'minimal'`, `'low'`, `'medium'`, and `'high'`. Reducing reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.

###  `` reasoning `class-attribute` `instance-attribute` ¶
    
    
    reasoning: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None
    

Reasoning parameters for reasoning models. For use with the Responses API.
    
    
    reasoning={
        "effort": "medium",  # Can be "low", "medium", or "high"
        "summary": "auto",  # Can be "auto", "concise", or "detailed"
    }
    

Added in `langchain-openai` 0.3.24

###  `` verbosity `class-attribute` `instance-attribute` ¶
    
    
    verbosity: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None
    

Controls the verbosity level of responses for reasoning models. For use with the Responses API.

Currently supported values are `'low'`, `'medium'`, and `'high'`.

Added in `langchain-openai` 0.3.28

###  `` tiktoken_model_name `class-attribute` `instance-attribute` ¶
    
    
    tiktoken_model_name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None
    

The model name to pass to tiktoken when using this class. Tiktoken is used to count the number of tokens in documents to constrain them to be under a certain limit. By default, when set to None, this will be the same as the embedding model name. However, there are some cases where you may want to use this Embedding class with a model name not supported by tiktoken. This can include when using Azure embeddings or when using one of the many model providers that expose an OpenAI-like API but with different models. In those cases, in order to avoid erroring when tiktoken is called, you can specify a model name to use here.

###  `` http_client `class-attribute` `instance-attribute` ¶
    
    
    http_client: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=None, exclude=True)
    

Optional `httpx.Client`. Only used for sync invocations. Must specify `http_async_client` as well if you'd like a custom client for async invocations.

###  `` http_async_client `class-attribute` `instance-attribute` ¶
    
    
    http_async_client: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=None, exclude=True)
    

Optional `httpx.AsyncClient`. Only used for async invocations. Must specify `http_client` as well if you'd like a custom client for sync invocations.

###  `` stop `class-attribute` `instance-attribute` ¶
    
    
    stop: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [str](https://docs.python.org/3/library/stdtypes.html#str) | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=None, alias='stop_sequences')
    

Default stop sequences.

###  `` extra_body `class-attribute` `instance-attribute` ¶
    
    
    extra_body: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None
    

Optional additional JSON properties to include in the request parameters when making requests to OpenAI compatible APIs, such as vLLM, LM Studio, or other providers.

This is the recommended way to pass custom parameters that are specific to your OpenAI-compatible API provider but not part of the standard OpenAI API.

Examples:

  * [LM Studio](https://lmstudio.ai/) TTL parameter: `extra_body={"ttl": 300}`
  * [vLLM](https://github.com/vllm-project/vllm) custom parameters: `extra_body={"use_beam_search": True}`
  * Any other provider-specific parameters



Warning

Do not use `model_kwargs` for custom parameters that are not part of the standard OpenAI API, as this will cause errors when making API calls. Use `extra_body` instead.

###  `` include_response_headers `class-attribute` `instance-attribute` ¶
    
    
    include_response_headers: [bool](https://docs.python.org/3/library/functions.html#bool) = False
    

Whether to include response headers in the output message `response_metadata`.

###  `` disabled_params `class-attribute` `instance-attribute` ¶
    
    
    disabled_params: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=None)
    

Parameters of the OpenAI client or `chat.completions` endpoint that should be disabled for the given model.

Should be specified as `{"param": None | ['val1', 'val2']}` where the key is the parameter and the value is either None, meaning that parameter should never be used, or it's a list of disabled values for the parameter.

For example, older models may not support the `'parallel_tool_calls'` parameter at all, in which case `disabled_params={"parallel_tool_calls": None}` can be passed in.

If a parameter is disabled then it will not be used by default in any methods, e.g. in `with_structured_output`. However this does not prevent a user from directly passed in the parameter during invocation.

###  `` include `class-attribute` `instance-attribute` ¶
    
    
    include: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None
    

Additional fields to include in generations from Responses API.

Supported values:

  * `'file_search_call.results'`
  * `'message.input_image.image_url'`
  * `'computer_call_output.output.image_url'`
  * `'reasoning.encrypted_content'`
  * `'code_interpreter_call.outputs'`



Added in `langchain-openai` 0.3.24

###  `` service_tier `class-attribute` `instance-attribute` ¶
    
    
    service_tier: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None
    

Latency tier for request. Options are `'auto'`, `'default'`, or `'flex'`. Relevant for users of OpenAI's scale tier service.

###  `` store `class-attribute` `instance-attribute` ¶
    
    
    store: [bool](https://docs.python.org/3/library/functions.html#bool) | None = None
    

If `True`, OpenAI may store response data for future use.

Defaults to `True` for the Responses API and `False` for the Chat Completions API.

Added in `langchain-openai` 0.3.24

###  `` truncation `class-attribute` `instance-attribute` ¶
    
    
    truncation: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None
    

Truncation strategy (Responses API). Can be `'auto'` or `'disabled'` (default). If `'auto'`, model may drop input items from the middle of the message sequence to fit the context window.

Added in `langchain-openai` 0.3.24

###  `` use_previous_response_id `class-attribute` `instance-attribute` ¶
    
    
    use_previous_response_id: [bool](https://docs.python.org/3/library/functions.html#bool) = False
    

If `True`, always pass `previous_response_id` using the ID of the most recent response. Responses API only.

Input messages up to the most recent response will be dropped from request payloads.

For example, the following two are equivalent:
    
    
    model = ChatOpenAI(
        model="...",
        use_previous_response_id=True,
    )
    model.invoke(
        [
            HumanMessage("Hello"),
            AIMessage("Hi there!", response_metadata={"id": "resp_123"}),
            HumanMessage("How are you?"),
        ]
    )
    
    
    
    model = ChatOpenAI(model="...", use_responses_api=True)
    model.invoke([HumanMessage("How are you?")], previous_response_id="resp_123")
    

Added in `langchain-openai` 0.3.26

###  `` use_responses_api `class-attribute` `instance-attribute` ¶
    
    
    use_responses_api: [bool](https://docs.python.org/3/library/functions.html#bool) | None = None
    

Whether to use the Responses API instead of the Chat API.

If not specified then will be inferred based on invocation params.

Added in `langchain-openai` 0.3.9

###  `` max_tokens `class-attribute` `instance-attribute` ¶
    
    
    max_tokens: [int](https://docs.python.org/3/library/functions.html#int) | None = [Field](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field "<code>pydantic.Field</code>")(default=None, alias='max_completion_tokens')
    

Maximum number of tokens to generate.

###  `` lc_secrets `property` ¶
    
    
    lc_secrets: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Mapping of secret environment variables.

###  `` lc_attributes `property` ¶
    
    
    lc_attributes: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Get the attributes of the langchain object.

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
    
    
    get_input_schema(config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None) -> [type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]
    

Get a Pydantic model that can be used to validate input to the `Runnable`.

`Runnable` objects that leverage the `configurable_fields` and `configurable_alternatives` methods will have a dynamic input schema that depends on which configuration the `Runnable` is invoked with.

This method allows to get an input schema for a specific configuration.

PARAMETER | DESCRIPTION  
---|---  
`config` |  A config to use when generating the schema. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]` |  A Pydantic model that can be used to validate input.  
  
###  `` get_input_jsonschema ¶
    
    
    get_input_jsonschema(config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Get a JSON schema that represents the input to the `Runnable`.

PARAMETER | DESCRIPTION  
---|---  
`config` |  A config to use when generating the schema. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
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
    
    
    get_output_schema(config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None) -> [type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]
    

Get a Pydantic model that can be used to validate output to the `Runnable`.

`Runnable` objects that leverage the `configurable_fields` and `configurable_alternatives` methods will have a dynamic output schema that depends on which configuration the `Runnable` is invoked with.

This method allows to get an output schema for a specific configuration.

PARAMETER | DESCRIPTION  
---|---  
`config` |  A config to use when generating the schema. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[type](https://docs.python.org/3/library/functions.html#type)[[BaseModel](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel "<code>pydantic.BaseModel</code>")]` |  A Pydantic model that can be used to validate output.  
  
###  `` get_output_jsonschema ¶
    
    
    get_output_jsonschema(config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None) -> [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

Get a JSON schema that represents the output of the `Runnable`.

PARAMETER | DESCRIPTION  
---|---  
`config` |  A config to use when generating the schema. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
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
    
    
    get_graph(config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None) -> Graph
    

Return a graph representation of this `Runnable`.

###  `` get_prompts ¶
    
    
    get_prompts(config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None) -> [list](https://docs.python.org/3/library/stdtypes.html#list)[BasePromptTemplate]
    

Return a list of prompts used by this `Runnable`.

###  `` __or__ ¶
    
    
    __or__(
        other: [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), Other]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Other]]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Other]]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], Other]
        | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), Other] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], Other] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
    ) -> [RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Other]
    

Runnable "or" operator.

Compose this `Runnable` with another object to create a `RunnableSequence`.

PARAMETER | DESCRIPTION  
---|---  
`other` |  Another `Runnable` or a `Runnable`-like object. **TYPE:** `[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), Other] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Other]] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Other]] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], Other] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), Other] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], Other] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Other]` |  A new `Runnable`.  
  
###  `` __ror__ ¶
    
    
    __ror__(
        other: [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Other, [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Other]], [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Other]], [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Other], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
        | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Other, [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Other], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")],
    ) -> [RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Other, Output]
    

Runnable "reverse-or" operator.

Compose this `Runnable` with another object to create a `RunnableSequence`.

PARAMETER | DESCRIPTION  
---|---  
`other` |  Another `Runnable` or a `Runnable`-like object. **TYPE:** `[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Other, [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Other]], [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Other]], [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Other], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Other, [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Other], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]`  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Other, Output]` |  A new `Runnable`.  
  
###  `` pipe ¶
    
    
    pipe(
        *others: [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), Other] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], Other], name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None
    ) -> [RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Other]
    

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
`*others` |  Other `Runnable` or `Runnable`-like objects to compose **TYPE:** `[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), Other] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], Other]` **DEFAULT:** `()`  
`name` |  An optional name for the resulting `RunnableSequence`. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Other]` |  A new `Runnable`.  
  
###  `` pick ¶
    
    
    pick(keys: [str](https://docs.python.org/3/library/stdtypes.html#str) | [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]) -> [RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

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
`[RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]` |  a new `Runnable`.  
  
###  `` assign ¶
    
    
    assign(
        **kwargs: [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
        | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]],
    ) -> [RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]
    

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
`**kwargs` |  A mapping of keys to `Runnable` or `Runnable`-like objects that will be invoked with the entire output dict of this `Runnable`. **TYPE:** `[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "<code>collections.abc.Mapping</code>")[[str](https://docs.python.org/3/library/stdtypes.html#str), [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]], [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]]` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]` |  A new `Runnable`.  
  
###  `` invoke ¶
    
    
    invoke(
        input: [LanguageModelInput](../../../langchain_core/language_models/#langchain_core.language_models.base.LanguageModelInput "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">LanguageModelInput</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langchain_core.language_models.base.LanguageModelInput</code>\)"),
        config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None = None,
        *,
        stop: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [AIMessage](../../../langchain/messages/#langchain.messages.AIMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">AIMessage</span> \(<code>langchain_core.messages.AIMessage</code>\)")
    

Transform a single input into an output.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input to the `Runnable`. **TYPE:** `Input`  
`config` |  A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`Output` |  The output of the `Runnable`.  
  
###  `` ainvoke `async` ¶
    
    
    ainvoke(
        input: [LanguageModelInput](../../../langchain_core/language_models/#langchain_core.language_models.base.LanguageModelInput "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">LanguageModelInput</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langchain_core.language_models.base.LanguageModelInput</code>\)"),
        config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None = None,
        *,
        stop: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [AIMessage](../../../langchain/messages/#langchain.messages.AIMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">AIMessage</span> \(<code>langchain_core.messages.AIMessage</code>\)")
    

Transform a single input into an output.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input to the `Runnable`. **TYPE:** `Input`  
`config` |  A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`Output` |  The output of the `Runnable`.  
  
###  `` batch ¶
    
    
    batch(
        inputs: [list](https://docs.python.org/3/library/stdtypes.html#list)[Input],
        config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None = None,
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
`config` |  A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None` **DEFAULT:** `None`  
`return_exceptions` |  Whether to return exceptions instead of raising them. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[Output]` |  A list of outputs from the `Runnable`.  
  
###  `` batch_as_completed ¶
    
    
    batch_as_completed(
        inputs: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Input],
        config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None = None,
        *,
        return_exceptions: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None,
    ) -> [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), Output | [Exception](https://docs.python.org/3/library/exceptions.html#Exception)]]
    

Run `invoke` in parallel on a list of inputs.

Yields results as they complete.

PARAMETER | DESCRIPTION  
---|---  
`inputs` |  A list of inputs to the `Runnable`. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Input]`  
`config` |  A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None` **DEFAULT:** `None`  
`return_exceptions` |  Whether to return exceptions instead of raising them. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), Output | [Exception](https://docs.python.org/3/library/exceptions.html#Exception)]` |  Tuples of the index of the input and the output from the `Runnable`.  
  
###  `` abatch `async` ¶
    
    
    abatch(
        inputs: [list](https://docs.python.org/3/library/stdtypes.html#list)[Input],
        config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None = None,
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
`config` |  A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [list](https://docs.python.org/3/library/stdtypes.html#list)[[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None` **DEFAULT:** `None`  
`return_exceptions` |  Whether to return exceptions instead of raising them. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[Output]` |  A list of outputs from the `Runnable`.  
  
###  `` abatch_as_completed `async` ¶
    
    
    abatch_as_completed(
        inputs: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Input],
        config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None = None,
        *,
        return_exceptions: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None,
    ) -> [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), Output | [Exception](https://docs.python.org/3/library/exceptions.html#Exception)]]
    

Run `ainvoke` in parallel on a list of inputs.

Yields results as they complete.

PARAMETER | DESCRIPTION  
---|---  
`inputs` |  A list of inputs to the `Runnable`. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[Input]`  
`config` |  A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys. Please refer to `RunnableConfig` for more details. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")] | None` **DEFAULT:** `None`  
`return_exceptions` |  Whether to return exceptions instead of raising them. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[int](https://docs.python.org/3/library/functions.html#int), Output | [Exception](https://docs.python.org/3/library/exceptions.html#Exception)]]` |  A tuple of the index of the input and the output from the `Runnable`.  
  
###  `` stream ¶
    
    
    stream(
        input: [LanguageModelInput](../../../langchain_core/language_models/#langchain_core.language_models.base.LanguageModelInput "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">LanguageModelInput</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langchain_core.language_models.base.LanguageModelInput</code>\)"),
        config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None = None,
        *,
        stop: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[[AIMessageChunk](../../../langchain/messages/#langchain.messages.AIMessageChunk "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">AIMessageChunk</span> \(<code>langchain_core.messages.AIMessageChunk</code>\)")]
    

Default implementation of `stream`, which calls `invoke`.

Subclasses must override this method if they support streaming output.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input to the `Runnable`. **TYPE:** `Input`  
`config` |  The config to use for the `Runnable`. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`Output` |  The output of the `Runnable`.  
  
###  `` astream `async` ¶
    
    
    astream(
        input: [LanguageModelInput](../../../langchain_core/language_models/#langchain_core.language_models.base.LanguageModelInput "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">LanguageModelInput</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langchain_core.language_models.base.LanguageModelInput</code>\)"),
        config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span>") | None = None,
        *,
        stop: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[[AIMessageChunk](../../../langchain/messages/#langchain.messages.AIMessageChunk "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">AIMessageChunk</span> \(<code>langchain_core.messages.AIMessageChunk</code>\)")]
    

Default implementation of `astream`, which calls `ainvoke`.

Subclasses must override this method if they support streaming output.

PARAMETER | DESCRIPTION  
---|---  
`input` |  The input to the `Runnable`. **TYPE:** `Input`  
`config` |  The config to use for the `Runnable`. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Output]` |  The output of the `Runnable`.  
  
###  `` astream_log `async` ¶
    
    
    astream_log(
        input: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
        config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None,
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
`config` |  The config to use for the `Runnable`. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
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
        config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None,
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
`config` |  The config to use for the `Runnable`. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
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
        input: [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Input], config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None
    ) -> [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Output]
    

Transform inputs to outputs.

Default implementation of transform, which buffers input and calls `astream`.

Subclasses must override this method if they can start producing output while input is still being generated.

PARAMETER | DESCRIPTION  
---|---  
`input` |  An iterator of inputs to the `Runnable`. **TYPE:** `[Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "<code>collections.abc.Iterator</code>")[Input]`  
`config` |  The config to use for the `Runnable`. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`Output` |  The output of the `Runnable`.  
  
###  `` atransform `async` ¶
    
    
    atransform(
        input: [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Input],
        config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None,
    ) -> [AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Output]
    

Transform inputs to outputs.

Default implementation of atransform, which buffers input and calls `astream`.

Subclasses must override this method if they can start producing output while input is still being generated.

PARAMETER | DESCRIPTION  
---|---  
`input` |  An async iterator of inputs to the `Runnable`. **TYPE:** `[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Input]`  
`config` |  The config to use for the `Runnable`. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") | None` **DEFAULT:** `{}`  
YIELDS | DESCRIPTION  
---|---  
`[AsyncIterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "<code>collections.abc.AsyncIterator</code>")[Output]` |  The output of the `Runnable`.  
  
###  `` bind ¶
    
    
    bind(**kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]
    

Bind arguments to a `Runnable`, returning a new `Runnable`.

Useful when a `Runnable` in a chain requires an argument that is not in the output of the previous `Runnable` or included in the user input.

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  The arguments to bind to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]` |  A new `Runnable` with the arguments bound.  
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
        config: [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None = None, **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    ) -> [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]
    

Bind config to a `Runnable`, returning a new `Runnable`.

PARAMETER | DESCRIPTION  
---|---  
`config` |  The config to bind to the `Runnable`. **TYPE:** `[RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)") | None` **DEFAULT:** `None`  
`**kwargs` |  Additional keyword arguments to pass to the `Runnable`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]` |  A new `Runnable` with the config bound.  
  
###  `` with_listeners ¶
    
    
    with_listeners(
        *,
        on_start: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run], None]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run, [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")], None]
        | None = None,
        on_end: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run], None] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run, [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")], None] | None = None,
        on_error: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run], None]
        | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run, [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")], None]
        | None = None,
    ) -> [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]
    

Bind lifecycle listeners to a `Runnable`, returning a new `Runnable`.

The Run object contains information about the run, including its `id`, `type`, `input`, `output`, `error`, `start_time`, `end_time`, and any tags or metadata added to the run.

PARAMETER | DESCRIPTION  
---|---  
`on_start` |  Called before the `Runnable` starts running, with the `Run` object. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run], None] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run, [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")], None] | None` **DEFAULT:** `None`  
`on_end` |  Called after the `Runnable` finishes running, with the `Run` object. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run], None] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run, [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")], None] | None` **DEFAULT:** `None`  
`on_error` |  Called if the `Runnable` throws an error, with the `Run` object. **TYPE:** `[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run], None] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[Run, [RunnableConfig](../../../langchain_core/runnables/#langchain_core.runnables.RunnableConfig "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.RunnableConfig</span> \(<code>langchain_core.runnables.config.RunnableConfig</code>\)")], None] | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]` |  A new `Runnable` with the listeners bound.  
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
    ) -> [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]
    

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
`[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]` |  A new `Runnable` with the listeners bound.  
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
    ) -> [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]
    

Bind input and output types to a `Runnable`, returning a new `Runnable`.

PARAMETER | DESCRIPTION  
---|---  
`input_type` |  The input type to bind to the `Runnable`. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[Input] | None` **DEFAULT:** `None`  
`output_type` |  The output type to bind to the `Runnable`. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[Output] | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]` |  A new `Runnable` with the types bound.  
  
###  `` with_retry ¶
    
    
    with_retry(
        *,
        retry_if_exception_type: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type)[[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)], ...] = ([Exception](https://docs.python.org/3/library/exceptions.html#Exception),),
        wait_exponential_jitter: [bool](https://docs.python.org/3/library/functions.html#bool) = True,
        exponential_jitter_params: ExponentialJitterParams | None = None,
        stop_after_attempt: [int](https://docs.python.org/3/library/functions.html#int) = 3,
    ) -> [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]
    

Create a new `Runnable` that retries the original `Runnable` on exceptions.

PARAMETER | DESCRIPTION  
---|---  
`retry_if_exception_type` |  A tuple of exception types to retry on. **TYPE:** `[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type)[[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)], ...]` **DEFAULT:** `([Exception](https://docs.python.org/3/library/exceptions.html#Exception),)`  
`wait_exponential_jitter` |  Whether to add jitter to the wait time between retries. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `True`  
`stop_after_attempt` |  The maximum number of attempts to make before giving up. **TYPE:** `[int](https://docs.python.org/3/library/functions.html#int)` **DEFAULT:** `3`  
`exponential_jitter_params` |  Parameters for `tenacity.wait_exponential_jitter`. Namely: `initial`, `max`, `exp_base`, and `jitter` (all `float` values). **TYPE:** `ExponentialJitterParams | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]` |  A new `Runnable` that retries the original `Runnable` on exceptions.  
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
    
    
    map() -> [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[list](https://docs.python.org/3/library/stdtypes.html#list)[Input], [list](https://docs.python.org/3/library/stdtypes.html#list)[Output]]
    

Return a new `Runnable` that maps a list of inputs to a list of outputs.

Calls `invoke` with each input.

RETURNS | DESCRIPTION  
---|---  
`[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[[list](https://docs.python.org/3/library/stdtypes.html#list)[Input], [list](https://docs.python.org/3/library/stdtypes.html#list)[Output]]` |  A new `Runnable` that maps a list of inputs to a list of outputs.  
Example
    
    
    from langchain_core.runnables import RunnableLambda
    
    
    def _lambda(x: int) -> int:
        return x + 1
    
    
    runnable = RunnableLambda(_lambda)
    print(runnable.map().invoke([1, 2, 3]))  # [2, 3, 4]
    

###  `` with_fallbacks ¶
    
    
    with_fallbacks(
        fallbacks: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]],
        *,
        exceptions_to_handle: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[type](https://docs.python.org/3/library/functions.html#type)[[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)], ...] = ([Exception](https://docs.python.org/3/library/exceptions.html#Exception),),
        exception_key: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
    ) -> RunnableWithFallbacks[Input, Output]
    

Add fallbacks to a `Runnable`, returning a new `Runnable`.

The new `Runnable` will try the original `Runnable`, and then each fallback in order, upon failures.

PARAMETER | DESCRIPTION  
---|---  
`fallbacks` |  A sequence of runnables to try if the original `Runnable` fails. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]]`  
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
`fallbacks` |  A sequence of runnables to try if the original `Runnable` fails. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]]`  
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
    ) -> [BaseTool](../../../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span> \(<code>langchain_core.tools.BaseTool</code>\)")
    

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
`[BaseTool](../../../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span> \(<code>langchain_core.tools.BaseTool</code>\)")` |  A `BaseTool` instance.  
  
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
    

###  `` __init__ ¶
    
    
    __init__(*args: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"), **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> None
    

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
    ) -> [RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Output]
    

Configure particular `Runnable` fields at runtime.

PARAMETER | DESCRIPTION  
---|---  
`**kwargs` |  A dictionary of `ConfigurableField` instances to configure. **TYPE:** `AnyConfigurableField` **DEFAULT:** `{}`  
RAISES | DESCRIPTION  
---|---  
`[ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If a configuration key is not found in the `Runnable`.  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Output]` |  A new `Runnable` with the fields configured.  
      
    
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
        **kwargs: [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[], [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]],
    ) -> [RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Output]
    

Configure alternatives for `Runnable` objects that can be set at runtime.

PARAMETER | DESCRIPTION  
---|---  
`which` |  The `ConfigurableField` instance that will be used to select the alternative. **TYPE:** `ConfigurableField`  
`default_key` |  The default key to use if no alternative is selected. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)` **DEFAULT:** `'default'`  
`prefix_keys` |  Whether to prefix the keys with the `ConfigurableField` id. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`**kwargs` |  A dictionary of keys to `Runnable` instances or callables that return `Runnable` instances. **TYPE:** `[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>")[[], [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span>")[Input, Output]]` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[RunnableSerializable](../../../langchain_core/runnables/#langchain_core.runnables.base.RunnableSerializable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.RunnableSerializable</span>")[Input, Output]` |  A new `Runnable` with the alternatives configured.  
      
    
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
    

###  `` set_verbose ¶
    
    
    set_verbose(verbose: [bool](https://docs.python.org/3/library/functions.html#bool) | None) -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

If verbose is `None`, set it.

This allows users to pass in `None` as verbose to access the global setting.

PARAMETER | DESCRIPTION  
---|---  
`verbose` |  The verbosity setting to use. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool) | None`  
RETURNS | DESCRIPTION  
---|---  
`[bool](https://docs.python.org/3/library/functions.html#bool)` |  The verbosity setting to use.  
  
###  `` generate_prompt ¶
    
    
    generate_prompt(
        prompts: [list](https://docs.python.org/3/library/stdtypes.html#list)[PromptValue],
        stop: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        callbacks: Callbacks = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> LLMResult
    

Pass a sequence of prompts to the model and return model generations.

This method should make use of batched calls for models that expose a batched API.

Use this method when you want to:

  1. Take advantage of batched calls,
  2. Need more output from the model than just the top generated value,
  3. Are building chains that are agnostic to the underlying language model type (e.g., pure text completion models vs chat models).

PARAMETER | DESCRIPTION  
---|---  
`prompts` |  List of `PromptValue` objects. A `PromptValue` is an object that can be converted to match the format of any language model (string for pure text generation models and `BaseMessage` objects for chat models). **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[PromptValue]`  
`stop` |  Stop words to use when generating. Model output is cut off at the first occurrence of any of these substrings. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`callbacks` |  `Callbacks` to pass through. Used for executing additional functionality, such as logging or streaming, throughout generation. **TYPE:** `Callbacks` **DEFAULT:** `None`  
`**kwargs` |  Arbitrary additional keyword arguments. These are usually passed to the model provider API call. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`LLMResult` |  An `LLMResult`, which contains a list of candidate `Generation` objects for each input prompt and additional model provider-specific output.  
  
###  `` agenerate_prompt `async` ¶
    
    
    agenerate_prompt(
        prompts: [list](https://docs.python.org/3/library/stdtypes.html#list)[PromptValue],
        stop: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        callbacks: Callbacks = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> LLMResult
    

Asynchronously pass a sequence of prompts and return model generations.

This method should make use of batched calls for models that expose a batched API.

Use this method when you want to:

  1. Take advantage of batched calls,
  2. Need more output from the model than just the top generated value,
  3. Are building chains that are agnostic to the underlying language model type (e.g., pure text completion models vs chat models).

PARAMETER | DESCRIPTION  
---|---  
`prompts` |  List of `PromptValue` objects. A `PromptValue` is an object that can be converted to match the format of any language model (string for pure text generation models and `BaseMessage` objects for chat models). **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[PromptValue]`  
`stop` |  Stop words to use when generating. Model output is cut off at the first occurrence of any of these substrings. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`callbacks` |  `Callbacks` to pass through. Used for executing additional functionality, such as logging or streaming, throughout generation. **TYPE:** `Callbacks` **DEFAULT:** `None`  
`**kwargs` |  Arbitrary additional keyword arguments. These are usually passed to the model provider API call. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`LLMResult` |  An `LLMResult`, which contains a list of candidate `Generation` objects for each input prompt and additional model provider-specific output.  
  
###  `` get_token_ids ¶
    
    
    get_token_ids(text: [str](https://docs.python.org/3/library/stdtypes.html#str)) -> [list](https://docs.python.org/3/library/stdtypes.html#list)[[int](https://docs.python.org/3/library/functions.html#int)]
    

Get the tokens present in the text with tiktoken package.

###  `` get_num_tokens ¶
    
    
    get_num_tokens(text: [str](https://docs.python.org/3/library/stdtypes.html#str)) -> [int](https://docs.python.org/3/library/functions.html#int)
    

Get the number of tokens present in the text.

Useful for checking if an input fits in a model's context window.

This should be overridden by model-specific implementations to provide accurate token counts via model-specific tokenizers.

PARAMETER | DESCRIPTION  
---|---  
`text` |  The string input to tokenize. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str)`  
RETURNS | DESCRIPTION  
---|---  
`[int](https://docs.python.org/3/library/functions.html#int)` |  The integer number of tokens in the text.  
  
###  `` get_num_tokens_from_messages ¶
    
    
    get_num_tokens_from_messages(
        messages: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[BaseMessage](../../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")],
        tools: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [type](https://docs.python.org/3/library/functions.html#type) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [BaseTool](../../../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span> \(<code>langchain_core.tools.BaseTool</code>\)")] | None = None,
    ) -> [int](https://docs.python.org/3/library/functions.html#int)
    

Calculate num tokens for `gpt-3.5-turbo` and `gpt-4` with `tiktoken` package.

Warning

You must have the `pillow` installed if you want to count image tokens if you are specifying the image as a base64 string, and you must have both `pillow` and `httpx` installed if you are specifying the image as a URL. If these aren't installed image inputs will be ignored in token counting.

[OpenAI reference](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb).

PARAMETER | DESCRIPTION  
---|---  
`messages` |  The message inputs to tokenize. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[BaseMessage](../../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]`  
`tools` |  If provided, sequence of `dict`, `BaseModel`, function, or `BaseTool` to be converted to tool schemas. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [type](https://docs.python.org/3/library/functions.html#type) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [BaseTool](../../../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span> \(<code>langchain_core.tools.BaseTool</code>\)")] | None` **DEFAULT:** `None`  
  
###  `` generate ¶
    
    
    generate(
        messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]],
        stop: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        callbacks: Callbacks = None,
        *,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: dict[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        run_name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> LLMResult
    

Pass a sequence of prompts to the model and return model generations.

This method should make use of batched calls for models that expose a batched API.

Use this method when you want to:

  1. Take advantage of batched calls,
  2. Need more output from the model than just the top generated value,
  3. Are building chains that are agnostic to the underlying language model type (e.g., pure text completion models vs chat models).

PARAMETER | DESCRIPTION  
---|---  
`messages` |  List of list of messages. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]]`  
`stop` |  Stop words to use when generating. Model output is cut off at the first occurrence of any of these substrings. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`callbacks` |  `Callbacks` to pass through. Used for executing additional functionality, such as logging or streaming, throughout generation. **TYPE:** `Callbacks` **DEFAULT:** `None`  
`tags` |  The tags to apply. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata to apply. **TYPE:** `dict[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`run_name` |  The name of the run. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Arbitrary additional keyword arguments. These are usually passed to the model provider API call. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`LLMResult` |  An `LLMResult`, which contains a list of candidate `Generations` for each input prompt and additional model provider-specific output.  
  
###  `` agenerate `async` ¶
    
    
    agenerate(
        messages: [list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]],
        stop: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        callbacks: Callbacks = None,
        *,
        tags: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None = None,
        metadata: dict[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None = None,
        run_name: [str](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
        run_id: [UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> LLMResult
    

Asynchronously pass a sequence of prompts to a model and return generations.

This method should make use of batched calls for models that expose a batched API.

Use this method when you want to:

  1. Take advantage of batched calls,
  2. Need more output from the model than just the top generated value,
  3. Are building chains that are agnostic to the underlying language model type (e.g., pure text completion models vs chat models).

PARAMETER | DESCRIPTION  
---|---  
`messages` |  List of list of messages. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[BaseMessage](../../../langchain_core/language_models/#langchain_core.messages.BaseMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseMessage</span> \(<code>langchain_core.messages.BaseMessage</code>\)")]]`  
`stop` |  Stop words to use when generating. Model output is cut off at the first occurrence of any of these substrings. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`callbacks` |  `Callbacks` to pass through. Used for executing additional functionality, such as logging or streaming, throughout generation. **TYPE:** `Callbacks` **DEFAULT:** `None`  
`tags` |  The tags to apply. **TYPE:** `[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | None` **DEFAULT:** `None`  
`metadata` |  The metadata to apply. **TYPE:** `dict[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | None` **DEFAULT:** `None`  
`run_name` |  The name of the run. **TYPE:** `[str](https://docs.python.org/3/library/stdtypes.html#str) | None` **DEFAULT:** `None`  
`run_id` |  The ID of the run. **TYPE:** `[UUID](https://docs.python.org/3/library/uuid.html#uuid.UUID "<code>uuid.UUID</code>") | None` **DEFAULT:** `None`  
`**kwargs` |  Arbitrary additional keyword arguments. These are usually passed to the model provider API call. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`LLMResult` |  An `LLMResult`, which contains a list of candidate `Generations` for each input prompt and additional model provider-specific output.  
  
###  `` dict ¶
    
    
    dict(**kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")) -> dict
    

Return a dictionary of the LLM.

###  `` bind_tools ¶
    
    
    bind_tools(
        tools: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [type](https://docs.python.org/3/library/functions.html#type) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [BaseTool](../../../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span> \(<code>langchain_core.tools.BaseTool</code>\)")],
        *,
        tool_choice: [dict](https://docs.python.org/3/library/stdtypes.html#dict) | [str](https://docs.python.org/3/library/stdtypes.html#str) | [bool](https://docs.python.org/3/library/functions.html#bool) | None = None,
        strict: [bool](https://docs.python.org/3/library/functions.html#bool) | None = None,
        parallel_tool_calls: [bool](https://docs.python.org/3/library/functions.html#bool) | None = None,
        response_format: _DictOrPydanticClass | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span> \(<code>langchain_core.runnables.Runnable</code>\)")[[LanguageModelInput](../../../langchain_core/language_models/#langchain_core.language_models.base.LanguageModelInput "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">LanguageModelInput</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langchain_core.language_models.LanguageModelInput</code>\)"), [AIMessage](../../../langchain/messages/#langchain.messages.AIMessage "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">AIMessage</span> \(<code>langchain_core.messages.AIMessage</code>\)")]
    

Bind tool-like objects to this chat model.

Assumes model is compatible with OpenAI tool-calling API.

PARAMETER | DESCRIPTION  
---|---  
`tools` |  A list of tool definitions to bind to this chat model. Supports any tool definition handled by `langchain_core.utils.function_calling.convert_to_openai_tool`. **TYPE:** `[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "<code>collections.abc.Sequence</code>")[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")] | [type](https://docs.python.org/3/library/functions.html#type) | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "<code>collections.abc.Callable</code>") | [BaseTool](../../../langchain/tools/#langchain.tools.BaseTool "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain.tools.BaseTool</span> \(<code>langchain_core.tools.BaseTool</code>\)")]`  
`tool_choice` |  Which tool to require the model to call. Options are:

  * `str` of the form `'<<tool_name>>'`: calls `<<tool_name>>` tool.
  * `'auto'`: automatically selects a tool (including no tool).
  * `'none'`: does not call a tool.
  * `'any'` or `'required'` or `True`: force at least one tool to be called.
  * `dict` of the form `{"type": "function", "function": {"name": <<tool_name>>}}`: calls `<<tool_name>>` tool.
  * `False` or `None`: no effect, default OpenAI behavior.

**TYPE:** `[dict](https://docs.python.org/3/library/stdtypes.html#dict) | [str](https://docs.python.org/3/library/stdtypes.html#str) | [bool](https://docs.python.org/3/library/functions.html#bool) | None` **DEFAULT:** `None`  
`strict` |  If `True`, model output is guaranteed to exactly match the JSON Schema provided in the tool definition. The input schema will also be validated according to the [supported schemas](https://platform.openai.com/docs/guides/structured-outputs/supported-schemas?api-mode=responses#supported-schemas). If `False`, input schema will not be validated and model output will not be validated. If `None`, `strict` argument will not be passed to the model. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool) | None` **DEFAULT:** `None`  
`parallel_tool_calls` |  Set to `False` to disable parallel tool use. Defaults to `None` (no specification, which allows parallel tool use). **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool) | None` **DEFAULT:** `None`  
`response_format` |  Optional schema to format model response. If provided and the model does not call a tool, the model will generate a [structured response](https://platform.openai.com/docs/guides/structured-outputs). **TYPE:** `_DictOrPydanticClass | None` **DEFAULT:** `None`  
`kwargs` |  Any additional parameters are passed directly to `bind`. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
  
###  `` build_extra `classmethod` ¶
    
    
    build_extra(values: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Build extra kwargs from additional params that were passed in.

###  `` validate_temperature `classmethod` ¶
    
    
    validate_temperature(values: [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")]) -> [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")
    

Validate temperature parameter for different models.

  * gpt-5 models (excluding gpt-5-chat) only allow `temperature=1` or unset (Defaults to 1)



###  `` validate_environment ¶
    
    
    validate_environment() -> [Self](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Self "<code>typing_extensions.Self</code>")
    

Validate that api key and python package exists in environment.

###  `` get_lc_namespace `classmethod` ¶
    
    
    get_lc_namespace() -> [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]
    

Get the namespace of the LangChain object.

RETURNS | DESCRIPTION  
---|---  
`[list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)]` |  `["langchain", "chat_models", "openai"]`  
  
###  `` is_lc_serializable `classmethod` ¶
    
    
    is_lc_serializable() -> [bool](https://docs.python.org/3/library/functions.html#bool)
    

Return whether this model can be serialized by LangChain.

###  `` with_structured_output ¶
    
    
    with_structured_output(
        schema: _DictOrPydanticClass | None = None,
        *,
        method: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")["function_calling", "json_mode", "json_schema"] = "json_schema",
        include_raw: [bool](https://docs.python.org/3/library/functions.html#bool) = False,
        strict: [bool](https://docs.python.org/3/library/functions.html#bool) | None = None,
        **kwargs: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>"),
    ) -> [Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span> \(<code>langchain_core.runnables.Runnable</code>\)")[[LanguageModelInput](../../../langchain_core/language_models/#langchain_core.language_models.base.LanguageModelInput "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">LanguageModelInput</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langchain_core.language_models.LanguageModelInput</code>\)"), _DictOrPydantic]
    

Model wrapper that returns outputs formatted to match the given schema.

PARAMETER | DESCRIPTION  
---|---  
`schema` |  The output schema. Can be passed in as:

  * an OpenAI function/tool schema,
  * a JSON Schema,
  * a `TypedDict` class,
  * or a Pydantic class.

If `schema` is a Pydantic class then the model output will be a Pydantic instance of that class, and the model-generated fields will be validated by the Pydantic class. Otherwise the model output will be a dict and will not be validated. See `langchain_core.utils.function_calling.convert_to_openai_tool` for more on how to properly specify types and descriptions of schema fields when specifying a Pydantic or `TypedDict` class. **TYPE:** `_DictOrPydanticClass | None` **DEFAULT:** `None`  
`method` |  The method for steering model generation, one of:

  * `'json_schema'`: Uses OpenAI's [Structured Output API](https://platform.openai.com/docs/guides/structured-outputs). See the docs for a list of supported models.
  * `'function_calling'`: Uses OpenAI's [tool-calling API](https://platform.openai.com/docs/guides/function-calling) (formerly called function calling).
  * `'json_mode'`: Uses OpenAI's [JSON mode](https://platform.openai.com/docs/guides/structured-outputs/json-mode). Note that if using JSON mode then you must include instructions for formatting the output into the desired schema into the model call.

Learn more about the [differences between methods](https://platform.openai.com/docs/guides/structured-outputs/function-calling-vs-response-format). **TYPE:** `[Literal](https://docs.python.org/3/library/typing.html#typing.Literal "<code>typing.Literal</code>")['function_calling', 'json_mode', 'json_schema']` **DEFAULT:** `'json_schema'`  
`include_raw` |  If `False` then only the parsed structured output is returned. If an error occurs during model output parsing it will be raised. If `True` then both the raw model response (a `BaseMessage`) and the parsed model response will be returned. If an error occurs during output parsing it will be caught and returned as well. The final output is always a `dict` with keys `'raw'`, `'parsed'`, and `'parsing_error'`. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool)` **DEFAULT:** `False`  
`strict` | 

  * `True`: Model output is guaranteed to exactly match the schema. The input schema will also be validated according to the [supported schemas](https://platform.openai.com/docs/guides/structured-outputs/supported-schemas?api-mode=responses#supported-schemas).
  * `False`: Input schema will not be validated and model output will not be validated.
  * `None`: `strict` argument will not be passed to the model.

If schema is specified via `TypedDict` or JSON schema, `strict` is not enabled by default. Pass `strict=True` to enable it. Note `strict` can only be non-null if `method` is `'json_schema'` or `'function_calling'`. **TYPE:** `[bool](https://docs.python.org/3/library/functions.html#bool) | None` **DEFAULT:** `None`  
`tools` |  A list of tool-like objects to bind to the chat model. Requires that:

  * `method` is `'json_schema'` (default).
  * `strict=True`
  * `include_raw=True`

If a model elects to call a tool, the resulting `AIMessage` in `'raw'` will include tool calls. Example
    
    
    from langchain.chat_models import init_chat_model
    from pydantic import BaseModel
    
    
    class ResponseSchema(BaseModel):
        response: str
    
    
    def get_weather(location: str) -> str:
        \"\"\"Get weather at a location.\"\"\"
        pass
    
    model = init_chat_model("openai:gpt-4o-mini")
    
    structured_model = model.with_structured_output(
        ResponseSchema,
        tools=[get_weather],
        strict=True,
        include_raw=True,
    )
    
    structured_model.invoke("What's the weather in Boston?")
    
    
    
    {
        "raw": AIMessage(content="", tool_calls=[...], ...),
        "parsing_error": None,
        "parsed": None,
    }
      
  
`kwargs` |  Additional keyword args are passed through to the model. **TYPE:** `[Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>")` **DEFAULT:** `{}`  
RETURNS | DESCRIPTION  
---|---  
`[Runnable](../../../langchain_core/runnables/#langchain_core.runnables.base.Runnable "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">langchain_core.runnables.base.Runnable</span> \(<code>langchain_core.runnables.Runnable</code>\)")[[LanguageModelInput](../../../langchain_core/language_models/#langchain_core.language_models.base.LanguageModelInput "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">LanguageModelInput</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span> \(<code>langchain_core.language_models.LanguageModelInput</code>\)"), _DictOrPydantic]` |  A `Runnable` that takes same inputs as a `langchain_core.language_models.chat.BaseChatModel`. If `include_raw` is `False` and `schema` is a Pydantic class, `Runnable` outputs an instance of `schema` (i.e., a Pydantic object). Otherwise, if `include_raw` is `False` then `Runnable` outputs a `dict`. If `include_raw` is `True`, then `Runnable` outputs a `dict` with keys:

  * `'raw'`: `BaseMessage`
  * `'parsed'`: `None` if there was a parsing error, otherwise the type depends on the `schema` as described above.
  * `'parsing_error'`: `BaseException | None`

  
  
Behavior changed in `langchain-openai` 0.3.0

`method` default changed from `"function_calling"` to `"json_schema"`.

Behavior changed in `langchain-openai` 0.3.12

Support for `tools` added.

Behavior changed in `langchain-openai` 0.3.21

Pass `kwargs` through to the model.

Example: `schema=Pydantic` class, `method='json_schema'`, `include_raw=False`, `strict=True`

Note, OpenAI has a number of restrictions on what types of schemas can be provided if `strict = True`. When using Pydantic, our model cannot specify any Field metadata (like min/max constraints) and fields cannot have default values.

See [all constraints](https://platform.openai.com/docs/guides/structured-outputs/supported-schemas).
    
    
    from langchain_openai import ChatOpenAI
    from pydantic import BaseModel, Field
    
    
    class AnswerWithJustification(BaseModel):
        '''An answer to the user question along with justification for the answer.'''
    
        answer: str
        justification: str | None = Field(
            default=..., description="A justification for the answer."
        )
    
    
    model = ChatOpenAI(model="...", temperature=0)
    structured_model = model.with_structured_output(AnswerWithJustification)
    
    structured_model.invoke(
        "What weighs more a pound of bricks or a pound of feathers"
    )
    
    
    
    AnswerWithJustification(
        answer="They weigh the same",
        justification="Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.",
    )
    

Example: `schema=Pydantic` class, `method='function_calling'`, `include_raw=False`, `strict=False`
    
    
    from langchain_openai import ChatOpenAI
    from pydantic import BaseModel, Field
    
    
    class AnswerWithJustification(BaseModel):
        '''An answer to the user question along with justification for the answer.'''
    
        answer: str
        justification: str | None = Field(
            default=..., description="A justification for the answer."
        )
    
    
    model = ChatOpenAI(model="...", temperature=0)
    structured_model = model.with_structured_output(
        AnswerWithJustification, method="function_calling"
    )
    
    structured_model.invoke(
        "What weighs more a pound of bricks or a pound of feathers"
    )
    
    
    
    AnswerWithJustification(
        answer="They weigh the same",
        justification="Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.",
    )
    

Example: `schema=Pydantic` class, `method='json_schema'`, `include_raw=True`
    
    
    from langchain_openai import ChatOpenAI
    from pydantic import BaseModel
    
    
    class AnswerWithJustification(BaseModel):
        '''An answer to the user question along with justification for the answer.'''
    
        answer: str
        justification: str
    
    
    model = ChatOpenAI(model="...", temperature=0)
    structured_model = model.with_structured_output(
        AnswerWithJustification, include_raw=True
    )
    
    structured_model.invoke(
        "What weighs more a pound of bricks or a pound of feathers"
    )
    
    
    
    {
        "raw": AIMessage(
            content="",
            additional_kwargs={
                "tool_calls": [
                    {
                        "id": "call_Ao02pnFYXD6GN1yzc0uXPsvF",
                        "function": {
                            "arguments": '{"answer":"They weigh the same.","justification":"Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ."}',
                            "name": "AnswerWithJustification",
                        },
                        "type": "function",
                    }
                ]
            },
        ),
        "parsed": AnswerWithJustification(
            answer="They weigh the same.",
            justification="Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume or density of the objects may differ.",
        ),
        "parsing_error": None,
    }
    

Example: `schema=TypedDict` class, `method='json_schema'`, `include_raw=False`, `strict=False`
    
    
    from typing_extensions import Annotated, TypedDict
    
    from langchain_openai import ChatOpenAI
    
    
    class AnswerWithJustification(TypedDict):
        '''An answer to the user question along with justification for the answer.'''
    
        answer: str
        justification: Annotated[
            str | None, None, "A justification for the answer."
        ]
    
    
    model = ChatOpenAI(model="...", temperature=0)
    structured_model = model.with_structured_output(AnswerWithJustification)
    
    structured_model.invoke(
        "What weighs more a pound of bricks or a pound of feathers"
    )
    
    
    
    {
        "answer": "They weigh the same",
        "justification": "Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume and density of the two substances differ.",
    }
    

Example: `schema=OpenAI` function schema, `method='json_schema'`, `include_raw=False`
    
    
    from langchain_openai import ChatOpenAI
    
    oai_schema = {
        "name": "AnswerWithJustification",
        "description": "An answer to the user question along with justification for the answer.",
        "parameters": {
            "type": "object",
            "properties": {
                "answer": {"type": "string"},
                "justification": {
                    "description": "A justification for the answer.",
                    "type": "string",
                },
            },
            "required": ["answer"],
        },
    }
    
    model = ChatOpenAI(model="...", temperature=0)
    structured_model = model.with_structured_output(oai_schema)
    
    structured_model.invoke(
        "What weighs more a pound of bricks or a pound of feathers"
    )
    
    
    
    {
        "answer": "They weigh the same",
        "justification": "Both a pound of bricks and a pound of feathers weigh one pound. The weight is the same, but the volume and density of the two substances differ.",
    }
    

Example: `schema=Pydantic` class, `method='json_mode'`, `include_raw=True`
    
    
    from langchain_openai import ChatOpenAI
    from pydantic import BaseModel
    
    
    class AnswerWithJustification(BaseModel):
        answer: str
        justification: str
    
    
    model = ChatOpenAI(model="...", temperature=0)
    structured_model = model.with_structured_output(
        AnswerWithJustification, method="json_mode", include_raw=True
    )
    
    structured_model.invoke(
        "Answer the following question. "
        "Make sure to return a JSON blob with keys 'answer' and 'justification'.\\n\\n"
        "What's heavier a pound of bricks or a pound of feathers?"
    )
    
    
    
    {
        "raw": AIMessage(
            content='{\\n    "answer": "They are both the same weight.",\\n    "justification": "Both a pound of bricks and a pound of feathers weigh one pound. The difference lies in the volume and density of the materials, not the weight." \\n}'
        ),
        "parsed": AnswerWithJustification(
            answer="They are both the same weight.",
            justification="Both a pound of bricks and a pound of feathers weigh one pound. The difference lies in the volume and density of the materials, not the weight.",
        ),
        "parsing_error": None,
    }
    

Example: `schema=None`, `method='json_mode'`, `include_raw=True`
    
    
    structured_model = model.with_structured_output(
        method="json_mode", include_raw=True
    )
    
    structured_model.invoke(
        "Answer the following question. "
        "Make sure to return a JSON blob with keys 'answer' and 'justification'.\\n\\n"
        "What's heavier a pound of bricks or a pound of feathers?"
    )
    
    
    
    {
        "raw": AIMessage(
            content='{\\n    "answer": "They are both the same weight.",\\n    "justification": "Both a pound of bricks and a pound of feathers weigh one pound. The difference lies in the volume and density of the materials, not the weight." \\n}'
        ),
        "parsed": {
            "answer": "They are both the same weight.",
            "justification": "Both a pound of bricks and a pound of feathers weigh one pound. The difference lies in the volume and density of the materials, not the weight.",
        },
        "parsing_error": None,
    }
    

Back to top

---
