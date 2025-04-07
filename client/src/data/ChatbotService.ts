import { ChatbotResponse } from "@/domain/models/ChatbotResponse";
import { HttpClient } from "./HttpClient";

export class ChatbotService {
  public static async askChatbot(userInput: string) {
    const response = await HttpClient.getJson<ChatbotResponse>(
      `/chat?user_message=${userInput}`
    );

    if (!response) return null;

    return response;
  }
}
