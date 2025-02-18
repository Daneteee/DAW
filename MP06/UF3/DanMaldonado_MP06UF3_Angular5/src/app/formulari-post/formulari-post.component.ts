import { Component, OnInit } from '@angular/core';
import { NgClass, NgIf , LowerCasePipe} from '@angular/common';
import { ReactiveFormsModule, FormGroup, FormControl, FormBuilder, Validators } from '@angular/forms';
import { Post } from '../models/post';
import { ServeiPost } from '../services/post.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-formulari-post',
  standalone: true, 
  imports: [ReactiveFormsModule, NgClass, NgIf, HttpClientModule],
  templateUrl: './formulari-post.component.html',
  styleUrl: './formulari-post.component.css',
  providers: [LowerCasePipe, ServeiPost],
})

export class FormulariPostComponent implements OnInit {
  dades: Post | null = null; 
  missatge: string = ""; 
  myForm!: FormGroup;
  
  title = new FormControl('', [Validators.required]);
  body = new FormControl('', [Validators.required, Validators.minLength(5)]);
  id = new FormControl('', [Validators.required, Validators.min(1)]);
  userId = new FormControl('', [Validators.required, Validators.min(1)]);
  
  constructor(private fb: FormBuilder, private serveiPost: ServeiPost, private lowercasePipe: LowerCasePipe) {}
  
  ngOnInit(){
    this.myForm = this.fb.group({
      title: this.title,
      body: this.body,
      id: this.id,
      userId: this.userId
 
    });
  }

  postSearch() {
    const id = this.myForm.get('id')!.value;
    if (id){
      this.serveiPost.searchPost(id).subscribe({
        next: (post) => this.dades = post,
        error: () => this.missatge = "ERROR: No s'ha trobat cap post amb aquesta ID."
      });
    }
  }
  
  postAdd() {
    const post: Post = {
    userId: this.myForm.get('userId')!.value,
    id: this.myForm.get('id')!.value,
    title: this.lowercasePipe.transform(this.myForm.get('title')?.value),
    body: this.lowercasePipe.transform(this.myForm.get('body')?.value)

   };

   this.serveiPost.addPost(post).subscribe({
    next: () => {
      this.missatge = "Post afegit correctament";
      this.myForm.reset();
    },
    error: () => this.missatge = "ERROR: no s'ha pogut afegir el post."
   });
  }
}