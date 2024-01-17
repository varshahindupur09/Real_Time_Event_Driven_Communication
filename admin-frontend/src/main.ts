import { enableProdMode, importProvidersFrom } from '@angular/core';
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';
import { environment } from '../src/environements/environment'; // Update the path if needed

// Define the socket configuration
const socketConfig: SocketIoConfig = { url: 'http://localhost:8001', options: {} };

// Enable production mode if environment is set to production
if (environment.production) {
  enableProdMode();
}

// Bootstrap the main AppComponent with necessary providers
bootstrapApplication(AppComponent, {
  providers: [
    importProvidersFrom(SocketIoModule.forRoot(socketConfig))
  ]
}).catch(err => console.error(err));
