export class HttpClient {
  private static BASE_URL = "http://127.0.0.1:8000";

  public static async getJson<TResponse>(
    path: string
  ): Promise<TResponse | null> {
    const result = await fetch(`${this.BASE_URL}${path}`);

    const response = await result.json();

    if (!response) return null;

    return response as TResponse;
  }
}
