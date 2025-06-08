import { SentIcon } from "@/components/icons/SentIcon";

import { OnSubmitEventHandler, useForm } from "@/infra/hooks/useForm";

import styles from "./styles.module.css";
import { LoadingIcon } from "@/components/icons/LoadingIcon/LoadingIcon";

type ChatInputProps = {
  isAwaitingResponse: boolean;
  onSubmitCallback: OnSubmitEventHandler;
};

export function ChatInput({
  isAwaitingResponse,
  onSubmitCallback,
}: ChatInputProps) {
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

          <button
            type="submit"
            className={styles.button}
            disabled={isAwaitingResponse}
          >
            {isAwaitingResponse ? <LoadingIcon /> : <SentIcon />}
          </button>
        </label>
      </form>
    </footer>
  );
}
