import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { Post } from "../models/post";

@Injectable(
    
)
export class ServeiPost {
    constructor(private http: HttpClient) { }
    url = 'https://jsonplaceholder.typicode.com/posts';

    searchPost(id: number): Observable<Post> {
        return this.http.get<Post>(`${this.url}/${id}`);
    }

    addPost(post: Post): Observable<Post> {
        return this.http.post<Post>(this.url, post);
    }
}