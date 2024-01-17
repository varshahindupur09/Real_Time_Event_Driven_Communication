// src/app/app.component.ts
import { Component } from '@angular/core';
import { ProductListComponent } from './components/product-list/product-list.component';
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ProductListComponent],
  templateUrl: './app.component.html',
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class AppComponent {
  title = 'admin-frontend';
}
