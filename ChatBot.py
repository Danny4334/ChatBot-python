import tkinter as tk

class ChatbotGUI:

    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        # Create a frame to hold the chat log
        self.chat_frame = tk.Frame(master)
        self.chat_frame.grid(row=0, column=0, padx=5, pady=5)

        # Create a scrollbar for the chat log
        self.chat_scrollbar = tk.Scrollbar(self.chat_frame)
        self.chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a text widget for the chat log
        self.chatlog = tk.Text(self.chat_frame, state=tk.DISABLED, yscrollcommand=self.chat_scrollbar.set, height=20, width=50)
        self.chatlog.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.chat_scrollbar.config(command=self.chatlog.yview)

        # Create a frame to hold the user input
        self.input_frame = tk.Frame(master)
        self.input_frame.grid(row=1, column=0, padx=5, pady=5)

        # Create an entry widget for the user input
        self.entry = tk.Entry(self.input_frame, width=50)
        self.entry.pack(side=tk.LEFT, padx=5, pady=5)
        self.entry.bind("<Return>", self.send_message)

        # Create a send button for the user input
        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message, bg="#25D366", fg="white", activebackground="#128C7E", activeforeground="white")
        self.send_button.pack(side=tk.LEFT, padx=5, pady=5)

    def send_message(self, event=None):
        message = self.entry.get()
        self.entry.delete(0, tk.END)

        response = respond_to_user_input(message)

        # Add user's message to chat log in a green bubble
        self.chatlog.configure(state=tk.NORMAL)
        self.chatlog.insert(tk.END, "You: " + message + "\n", "greenbubble")
        self.chatlog.tag_configure("greenbubble", background="#25D366", foreground="white", justify="right")

        # Add chatbot's response to chat log in a gray bubble
        self.chatlog.insert(tk.END, "Chatbot: " + response + "\n", "graybubble")
        self.chatlog.tag_configure("graybubble", background="gray", foreground="white", justify="left")

        self.chatlog.configure(state=tk.DISABLED)

def respond_to_user_input(user_input):
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return "Hello there! How can I assist you today?"

    elif "good" in user_input.lower() or "great" in user_input.lower():
        return "That's great to hear! Is there anything I can help you with?"

    elif "bad" in user_input.lower() or "not good" in user_input.lower():
        return "I'm sorry to hear that. Can you tell me more about what's bothering you?"

    elif "thank" in user_input.lower() or "thanks" in user_input.lower():
        return "You're welcome! Is there anything else I can help you with?"

    elif "how are you" in user_input.lower():
        return "I'm a computer program, so I don't have feelings, but I'm here to help you!"

    elif "what can you do" in user_input.lower():
        return "I can help you with anything you need, from answering questions to providing recommendations."

    elif "recommend" in user_input.lower() or "suggest" in user_input.lower():
        return "Sure, what kind of recommendation are you looking for? Books, movies, restaurants?"

    elif "book" in user_input.lower() or "reading" in user_input.lower():
        return "There are so many great books out there! What genre do you like to read?"

    elif "movie" in user_input.lower() or "watching" in user_input.lower():
        return "There are so many great movies out there! What genre do you like to watch?"


    elif "restaurant" in user_input.lower() or "eating" in user_input.lower():
        return "There are so many great restaurants out there! What type of cuisine do you like?"

    elif "coding" in user_input.lower() or "python" in user_input.lower():
        return "I'm a computer program, so I don't have feelings, but I'm here to help you!"

    elif "good bye" in user_input.lower() or "bye" in user_input.lower():
        return "Goodbye!"

    elif "music" in user_input.lower() or "hiphop" in user_input.lower() or "grime" in user_input.lower():
        return "Who is your favorite artist?"

    else:
        return "I'm sorry, I didn't quite understand what you said. Can you please try rephrasing your question or statement?"


root = tk.Tk()
chatbot_gui = ChatbotGUI(root)
root.mainloop()





