import { ChatMessageType } from "./ChatMessageType";

export class Message {
  private sender: string = "";
  private content: string = "";
  private type: ChatMessageType;
  private sentAt: Date = new Date();

  constructor(sender: string, content: string, type: ChatMessageType) {
    this.sender = sender;
    this.content = content;
    this.type = type;
  }

  public getSender() {
    return this.sender;
  }

  public getContent() {
    return this.content;
  }

  public getType() {
    return this.type;
  }

  public getSentAt() {
    return this.sentAt;
  }

  public toJsonObject() {
    return {
      sender: this.sender,
      content: this.content,
      type: this.type,
      sentAt: this.sentAt,
    };
  }
}
