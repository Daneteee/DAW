import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders  } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

import { Project } from '../models/project';
import { Global } from './global';

@Injectable()
export class ProjectService { 

    public url: string;
    constructor(
        private _http: HttpClient
    ) {
        this.url = Global.url;
    }

    // Afegim el mètode saveProject
    saveProject(project: Project): Observable<any> {
        const headers = new HttpHeaders().set('Content-Type', 'application/json');
        console.log(`${this.url}/save-project`);
        return this._http.post(`${this.url}/save-project`, project, { headers })
        .pipe(
            catchError(error => {
            console.error('Error occurred:', error);
            return throwError(error);
            })
        );
    }

    // Afegim el mètode getProjects
    getProjects(): Observable<any> {
        return this._http.get(this.url + 'projects');
    }

    // Afegim el mètode getProject
    getProject(id: string): Observable<any> {
        return this._http.get<any>(`${this.url}/project/${id}`);
    }

    // Afegim el mètode deleteProject
    deleteProject(id: string): Observable<any> {
        return this._http.delete(`${this.url}/project/${id}`);
    }
    
    // Afegim el mètode updateProject
    updateProject(id: string, project: Project): Observable<any> {
        return this._http.put(`${this.url}project/${id}`, project);
    }

    // Afegim el mètode saveImage
    saveImage(image: File, projectId : string): Observable<any> {
        const formData = new FormData();
        formData.append('image', image);
        return this._http.post(`${this.url}/upload-image/${projectId}`, formData);
      }

    // Afegim el mètode getImage
    getImage(image: string): Observable<any> {
        return this._http.get(`${this.url}/get-image/${image}`, { responseType: 'blob' });
    }

}