import axios from 'axios';
import { getQueue, removeFromQueue } from './idb';

const API_URL = 'http://localhost:8000'; // Default FastAPI URL

const api = axios.create({
  baseURL: API_URL,
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Offline Sync function
export async function syncOfflineQueue() {
  const queue = await getQueue();
  if (queue.length === 0) return 0;
  
  let synced = 0;
  for (const item of queue) {
    try {
      // POST the inspection (Idempotent endpoint will return 200 or 201)
      await api.post('/inspections', item);
      await removeFromQueue(item.temp_uuid);
      synced++;
    } catch (err) {
      console.error("Failed to sync item", item.temp_uuid, err);
      // If 422, there's a logic error, maybe we should still delete it or flag it.
      // For MVP, we'll keep it in queue to retry or add manual clear later.
    }
  }
  return synced;
}

export default api;
