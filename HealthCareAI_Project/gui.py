# gui.py
import tkinter as tk
from tkinter import scrolledtext
import ai_client

def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return

    # Display user message (blue)
    chat_area.insert(tk.END, "You: " + user_input + "\n", "user")

    # Get bot response
    response = ai_client.chatbot_response(user_input)

    # Display bot response (green)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n", "bot")

    # Auto-scroll
    chat_area.yview(tk.END)

    # Clear input box
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("🌟 Health Care AI Assistant 🌟")
root.geometry("600x500")
root.configure(bg="#f0f8ff")

# Scrollable chat area
chat_area = scrolledtext.ScrolledText(root, bg="white", fg="black", wrap="word", font=("Arial", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Add colors/styles
chat_area.tag_config("user", foreground="blue", font=("Arial", 12, "bold"))
chat_area.tag_config("bot", foreground="green", font=("Arial", 12))

# Input box
entry = tk.Entry(root, bg="lightyellow", fg="black", font=("Arial", 12))
entry.pack(padx=10, pady=5, fill=tk.X)

# Send button
send_btn = tk.Button(root, text="Send", command=send_message, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
send_btn.pack(pady=5)

# Bind Enter key to send
entry.bind("<Return>", lambda event: send_message())

# Run GUI
if __name__ == "__main__":
    root.mainloop()
