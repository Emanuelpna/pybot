import { useState } from "react";

import { Message } from "@/domain/models/Message";
import { ChatMessageType } from "@/domain/models/ChatMessageType";

import { ChatbotService } from "@/data/ChatbotService";

import { Logo } from "@/components/commons/Logo/Logo";
import { ChatInput } from "@/components/chat/ChatInput/ChatInput";
import { ChatMessage } from "@/components/chat/ChatMessage/ChatMessage";
import { ChatContainer } from "@/components/chat/ChatContainer/ChatContainer";

import "./global.css";

function App() {
  const [messages, setMessages] = useState<Message[]>([]);

  async function onFormSubmit(formData: FormData) {
    const userInput = formData.get("user_input");

    if (!userInput) return;

    setMessages((messages) => [
      ...messages,
      new Message("José", userInput.toString(), ChatMessageType.USER),
    ]);

    const response = await ChatbotService.askChatbot(userInput.toString());

    if (!response) return;

    setMessages((messages) => [
      ...messages,
      new Message("PyBot", response.message, ChatMessageType.CHATBOT),
    ]);
  }

  return (
    <>
      <div className="appContainer">
        <Logo />
      </div>

      <ChatContainer footer={<ChatInput onSubmitCallback={onFormSubmit} />}>
        {messages.map((message) => (
          <ChatMessage
            key={message.getSentAt().toISOString()}
            content={message.getContent()}
            sender={message.getSender()}
            type={message.getType()}
          />
        ))}
      </ChatContainer>
    </>
  );
}

export default App;
