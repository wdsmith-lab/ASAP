### 🧩 What is `:contentReference[oaicite:5]{index=5}`?

This is **internal citation markup** used by ChatGPT to reference a specific **source document** retrieved during a session — especially when using tools like the `web` or `file_search` plugin.

It has **two purposes**:

1. **Displays a footnote-style citation** (like `[5]`) in your response.
    
2. **Links that citation** to a specific source or reference you can view.
    

---

### 🔍 What the Parts Mean

|Component|Meaning|
|---|---|
|`:contentReference[...]`|Marks this as a citation-type content block|
|`oaicite:5`|Internally identifies the citation object with index `5`|
|`{index=5}`|Makes the citation render as `[5]` in your chat|

When rendered in the UI, this would look like:

> "... praised by community... [5]"

Clicking `[5]` opens the full content or document retrieved (e.g. the OverTake.gg page).

---

### 🤖 Why You See It Raw

Sometimes, when you're:

- Quoting from a response
    
- Reading the raw structure before rendering
    
- Using export tools or copy/paste
    

…the rendering doesn't happen and you just see the **raw citation tag** instead of the cleaned-up footnote.

---

### ✅ For ARCHIVIST

In prompt module templates or training messages for ARCHIVIST, you **should not** use this raw citation tag syntax. Instead, simply:

- Include links or markdown reference links
    
- Use footnote conventions manually if needed
    

> Example:  
> `"notes": "Fonts match historical imperfections[^1]"`  
> `[^1]: https://www.overtake.gg/downloads/...`