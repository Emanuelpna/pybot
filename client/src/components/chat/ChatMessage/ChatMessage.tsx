import { ChatMessageType } from "../../../domain/models/ChatMessageType";

import styles from "./styles.module.css";

type ChatMessageProps = {
  sender: string;
  content: string;
  type: ChatMessageType;
};

export function ChatMessage({ type, sender, content }: ChatMessageProps) {
  return (
    <article
      className={`${styles.chatMessage} ${
        type === ChatMessageType.USER ? styles.userQuestion : styles.botResponse
      }`}
    >
      <header>
        <strong>{sender}</strong>
      </header>

      {content}
    </article>
  );
}
