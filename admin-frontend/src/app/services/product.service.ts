// src/app/services/product.service.ts
import { Injectable, Inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Socket } from 'ngx-socket-io';

export interface Product {
  id: number;
  title: string;
  image: string;
  likes: number;
}

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  products$: Observable<Product[]>;
  productLikes$: Observable<{ productId: number; likes: number }>;

  constructor(
    private http: HttpClient,
    private socket: Socket,
    @Inject('API_URL') private apiUrl: string // Injected API URL
  ) {
    // Initialize WebSocket events after socket is available
    this.products$ = this.socket.fromEvent<Product[]>('products'); // Listening for products update
    this.productLikes$ = this.socket.fromEvent<{ productId: number; likes: number }>('product_likes'); // Listening for like updates
  }

  // Fetches the initial list of products from the backend via HTTP
  getProducts(): Observable<Product[]> {
    return this.http.get<Product[]>(this.apiUrl);
  }

  // Sends a "like" action to the backend via HTTP
  likeProduct(id: number): Observable<any> {
    return this.http.post(`${this.apiUrl}/${id}/like`, {});
  }
}