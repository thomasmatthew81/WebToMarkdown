# Web Content Collection

> A collection of 1 web pages converted to Markdown format. Generated on 2025-11-15 15:03:33.

## Converted Web Pages

### Runtime | LangChain Reference

**Source:** https://reference.langchain.com/python/langgraph/runtime/

Skip to content 

[ ](https://github.com/langchain-ai/docs/tree/main/reference/python/docs/langgraph/runtime.md "Edit this page")

# Runtime

##  `` langgraph.runtime.Runtime `dataclass` ¶

Bases: `[Generic](https://docs.python.org/3/library/typing.html#typing.Generic "<code>typing.Generic</code>")[ContextT]`

Convenience class that bundles run-scoped context and other runtime utilities.

Added in version v0.6.0

Example:
    
    
    from typing import TypedDict
    from langgraph.graph import StateGraph
    from dataclasses import dataclass
    from langgraph.runtime import Runtime
    from langgraph.store.memory import InMemoryStore
    
    
    @dataclass
    class Context:  # (1)!
        user_id: str
    
    
    class State(TypedDict, total=False):
        response: str
    
    
    store = InMemoryStore()  # (2)!
    store.put(("users",), "user_123", {"name": "Alice"})
    
    
    def personalized_greeting(state: State, runtime: Runtime[Context]) -> State:
        '''Generate personalized greeting using runtime context and store.'''
        user_id = runtime.context.user_id  # (3)!
        name = "unknown_user"
        if runtime.store:
            if memory := runtime.store.get(("users",), user_id):
                name = memory.value["name"]
    
        response = f"Hello {name}! Nice to see you again."
        return {"response": response}
    
    
    graph = (
        StateGraph(state_schema=State, context_schema=Context)
        .add_node("personalized_greeting", personalized_greeting)
        .set_entry_point("personalized_greeting")
        .set_finish_point("personalized_greeting")
        .compile(store=store)
    )
    
    result = graph.invoke({}, context=Context(user_id="user_123"))
    print(result)
    # > {'response': 'Hello Alice! Nice to see you again.'}
    

  1. Define a schema for the runtime context.
  2. Create a store to persist memories and other information.
  3. Use the runtime context to access the `user_id`.



###  `` context `class-attribute` `instance-attribute` ¶
    
    
    context: ContextT = [field](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "<code>dataclasses.field</code>")(default=None)
    

Static context for the graph run, like `user_id`, `db_conn`, etc.

Can also be thought of as 'run dependencies'.

###  `` store `class-attribute` `instance-attribute` ¶
    
    
    store: [BaseStore](../store/#langgraph.store.base.BaseStore "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">BaseStore</span> \(<code>langgraph.store.base.BaseStore</code>\)") | None = [field](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "<code>dataclasses.field</code>")(default=None)
    

Store for the graph run, enabling persistence and memory.

###  `` stream_writer `class-attribute` `instance-attribute` ¶
    
    
    stream_writer: [StreamWriter](../types/#langgraph.types.StreamWriter "<code class="doc-symbol doc-symbol-heading doc-symbol-attribute"></code>            <span class="doc doc-object-name doc-attribute-name">StreamWriter</span>
    
    
      <span class="doc doc-labels">
          <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
      </span> \(<code>langgraph.types.StreamWriter</code>\)") = [field](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "<code>dataclasses.field</code>")(default=_no_op_stream_writer)
    

Function that writes to the custom stream.

###  `` previous `class-attribute` `instance-attribute` ¶
    
    
    previous: [Any](https://docs.python.org/3/library/typing.html#typing.Any "<code>typing.Any</code>") = [field](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "<code>dataclasses.field</code>")(default=None)
    

The previous return value for the given thread.

Only available with the functional API when a checkpointer is provided.

##  `` langgraph.runtime ¶

FUNCTION | DESCRIPTION  
---|---  
`get_runtime` |  Get the runtime for the current graph run.  
  
###  `` get_runtime ¶
    
    
    get_runtime(context_schema: [type](https://docs.python.org/3/library/functions.html#type)[ContextT] | None = None) -> Runtime[ContextT]
    

Get the runtime for the current graph run.

PARAMETER | DESCRIPTION  
---|---  
`context_schema` |  Optional schema used for type hinting the return type of the runtime. **TYPE:** `[type](https://docs.python.org/3/library/functions.html#type)[ContextT] | None` **DEFAULT:** `None`  
RETURNS | DESCRIPTION  
---|---  
`Runtime[ContextT]` |  The runtime for the current graph run.  
  
Back to top

---
