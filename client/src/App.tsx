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
  const [isAwaitingResponse, setIsAwaitingResponse] = useState<boolean>(false);
  const [messages, setMessages] = useState<Message[]>([]);

  async function onFormSubmit(formData: FormData) {
    setIsAwaitingResponse(true);

    try {
      const userInput = formData.get("user_input");

      if (!userInput) {
        setIsAwaitingResponse(false);
        return;
      }

      setMessages((messages) => [
        ...messages,
        new Message("José", userInput.toString(), ChatMessageType.USER),
      ]);

      const response = await ChatbotService.askChatbot(userInput.toString());

      if (!response) {
        setIsAwaitingResponse(false);
        return;
      }

      setMessages((messages) => [
        ...messages,
        new Message(
          "PyBot",
          response.message.join("\n\n"),
          ChatMessageType.CHATBOT
        ),
      ]);
    } finally {
      setIsAwaitingResponse(false);
    }
  }

  return (
    <>
      <div className="appContainer">
        <Logo />
      </div>

      <ChatContainer
        footer={
          <ChatInput
            isAwaitingResponse={isAwaitingResponse}
            onSubmitCallback={onFormSubmit}
          />
        }
      >
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
