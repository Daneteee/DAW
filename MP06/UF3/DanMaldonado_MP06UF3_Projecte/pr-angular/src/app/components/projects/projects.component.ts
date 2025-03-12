import { Component, OnInit } from '@angular/core';
import { ProjectService } from '../../services/project.service';
import { Project } from '../../models/project';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-projects',
  templateUrl: './projects.component.html',
  styleUrls: ['./projects.component.css'],
  standalone: true,
  imports: [RouterModule],
  providers: [ProjectService]
})
export class ProjectsComponent implements OnInit {

  // Afegim les propietats del component Projects
  public projects: Project[] = []; 

  constructor(private projectService: ProjectService) { }

  // Afegim el mètode ngOnInit
  ngOnInit(): void {

    // Crida al mètode getProjects
    this.getProjects();
  }

  // Afegim el mètode getProjects
  getProjects(): void {

    // Crida al mètode getProjects del servei projectService
    this.projectService.getProjects().subscribe({
      next: (response) => {
        console.log('Response:', response);

        // Guarda els projectes en la propietat projects
        this.projects = response.projects || [];
      },
      error: (err) => {
        console.error('Error fetching projects:', err);
        this.projects = []; 
      }
    });
  }
}