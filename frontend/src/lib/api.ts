const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000';

export async function fetchFromApi(endpoint: string, options: RequestInit = {}) {
  const response = await fetch(`${API_BASE}${endpoint}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  });

  if (!response.ok) {
    // In a real app, handle RFC7807 problem+json here
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || 'An API error occurred');
  }

  return response.json();
}
