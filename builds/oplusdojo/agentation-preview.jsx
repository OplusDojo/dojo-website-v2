// Bundled and injected only by dev.py. Never included in generated site HTML.
import React from 'react';
import { createRoot } from 'react-dom/client';
import { Agentation } from 'agentation';

if (!document.getElementById('agentation-preview')) {
  const host = document.createElement('div');
  host.id = 'agentation-preview';
  document.body.appendChild(host);
  createRoot(host).render(
    <Agentation appName="O+Dojo local preview" endpoint="http://localhost:4747" />,
  );
}
