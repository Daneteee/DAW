import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ProjectService } from '../../services/project.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css'],
  providers: [ProjectService]
})
export class DetailComponent implements OnInit {

  showModal: boolean =false;
  project: any;
  loading = true;
  error: string | null = null;

  constructor(
    private route: ActivatedRoute,
    private projectService: ProjectService,
    private router: Router
  ) {}

  ngOnInit(): void {
    // Get the project ID from the route
    const id = this.route.snapshot.paramMap.get('id');
    
    if (id) {
      this.getProject(id);
    } else {
      this.error = 'No project ID provided';
      this.loading = false;
    }
  }

  getProject(id: string): void {
    this.projectService.getProject(id).subscribe({
      next: (response) => {
        this.project = response.project; 
        this.loading = false;
        console.log('Projecte rebut:', this.project);
      },
      error: (err) => {
        this.error = 'Error carregant el projecte';
        this.loading = false;
        console.error('Error carregant el projecte:', err);
      }
    });
  }
  
  deleteProject(id: string): void {
    const confirm = window.confirm('Estàs segur que vols eliminar aquest projecte?');
  
    if (confirm) {
      this.projectService.deleteProject(id).subscribe({
        next: () => {
          alert('Projecte eliminat correctament');
          console.log('Projecte eliminat correctament');
          window.location.href = '/projects';
        },
        error: (err) => {
          alert('Error al eliminar el projecte');
          console.error('Error al eliminar el projecte:', err);
        }
      });
    }
  }
  

  editProject(id: string): void {
    this.router.navigate(['/edit', id]);
  }
}