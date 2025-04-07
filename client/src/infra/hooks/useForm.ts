import { ChangeEvent, FormEvent, useState } from "react";

export type OnSubmitEventHandler = (formData: FormData) => Promise<void>;

export function useForm(onFormSubmitCallback: OnSubmitEventHandler) {
  const [formData, setFormData] = useState<Record<string, string>>({});

  function onFormSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    const formData = new FormData(event.currentTarget);

    onFormSubmitCallback?.(formData);
  }

  function setInputValue(name: string, value: string) {
    setFormData((formData) => ({
      ...formData,
      [name]: value,
    }));
  }

  function registerInput(name: string) {
    return {
      name,
      value: formData[name] ?? "",
      onChange: (event: ChangeEvent<HTMLInputElement>) =>
        setInputValue(name, event.target.value),
    };
  }

  return { formData, registerInput, onFormSubmit, setInputValue };
}
