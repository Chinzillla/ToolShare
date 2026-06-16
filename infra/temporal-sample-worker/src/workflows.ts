export async function bookingConnectionWorkflow(bookingId: string): Promise<string> {
  return `Temporal worker connected for booking ${bookingId}`;
}
