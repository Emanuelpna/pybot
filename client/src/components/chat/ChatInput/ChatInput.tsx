import { SentIcon } from "@/components/icons/SentIcon";

import { OnSubmitEventHandler, useForm } from "@/infra/hooks/useForm";

import styles from "./styles.module.css";

type ChatInputProps = {
  onSubmitCallback: OnSubmitEventHandler;
};

export function ChatInput({ onSubmitCallback }: ChatInputProps) {
  const { onFormSubmit, registerInput, setInputValue } = useForm(
    async (formData) => {
      await onSubmitCallback(formData);

      setInputValue("user_input", "");
    }
  );

  return (
    <footer className={styles.chatInputWrapper}>
      <form onSubmit={onFormSubmit}>
        <label className={styles.inputLabel}>
          <input
            type="text"
            autoFocus
            className={styles.input}
            placeholder="Pergunte ao Chatbot"
            {...registerInput("user_input")}
          />

          <button type="submit" className={styles.button}>
            <SentIcon />
          </button>
        </label>
      </form>
    </footer>
  );
}
