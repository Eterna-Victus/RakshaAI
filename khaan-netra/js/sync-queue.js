/* Offline queue shared by Khaan Netra scan and incident adapters. */
const KHAAN_SYNC_KEY = 'khaan-netra-sync-queue';

function getSyncQueue() {
  try { return JSON.parse(localStorage.getItem(KHAAN_SYNC_KEY) || '[]'); } catch { return []; }
}

function enqueueSync(item) {
  const queue = getSyncQueue().filter(entry => entry.temp_uuid !== item.temp_uuid);
  queue.push({ ...item, sync_state: 'pending', retry_count: item.retry_count || 0 });
  localStorage.setItem(KHAAN_SYNC_KEY, JSON.stringify(queue));
  return queue.length;
}

function removeSynced(tempUuid) {
  localStorage.setItem(KHAAN_SYNC_KEY, JSON.stringify(getSyncQueue().filter(item => item.temp_uuid !== tempUuid)));
}

async function replaySyncQueue(apiUrl = 'http://localhost:8000') {
  const queue = getSyncQueue();
  if (!queue.length) return 0;
  try {
    const response = await fetch(`${apiUrl}/api/sync/batch`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ items: queue }) });
    const data = await response.json();
    data.results.forEach((result, index) => { if (result.ok) removeSynced(queue[index].temp_uuid); });
    return data.results.filter(result => result.ok).length;
  } catch { return 0; }
}

window.KhaanSyncQueue = { getSyncQueue, enqueueSync, replaySyncQueue };