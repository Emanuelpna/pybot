import { ReactNode } from "react";

import styles from "./styles.module.css";

type ChatContainerProps = {
  children: ReactNode;
  footer: ReactNode;
};

export function ChatContainer({ children, footer }: ChatContainerProps) {
  return (
    <main className={styles.chatContainer}>
      <div className={styles.chatMessagesContainer}>
        <div className={styles.chatMessagesWrapper}>{children}</div>
      </div>

      {footer}
    </main>
  );
}
