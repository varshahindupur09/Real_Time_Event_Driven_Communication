import { ApplicationConfig, Provider } from '@angular/core';
import { provideHttpClient } from '@angular/common/http';
import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';

// WebSocket configuration
const socketConfig: SocketIoConfig = { url: 'http://localhost:8001', options: {} };

export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(),
    { provide: 'API_URL', useValue: 'http://localhost:8001/api/products' },
    { provide: SocketIoModule, useValue: socketConfig }
  ]
};
