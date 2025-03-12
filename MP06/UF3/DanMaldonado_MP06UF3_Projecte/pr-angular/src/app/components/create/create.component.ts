import { Component } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ProjectService } from '../../services/project.service';
import { RouterModule } from '@angular/router';
import { ActivatedRoute, Router } from '@angular/router';
import { Project } from '../../models/project';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css'],
  standalone: true,
  imports: [ReactiveFormsModule, RouterModule],
  providers: [ProjectService]
})
export class CreateComponent {
  
  // Afegim les propietats del component Create
  public project: any;
  public title: string;
  public projectForm: FormGroup;
  public successMessage: string | null = null;
  public imagePreview: string | null = null;
  public projectId: string | null = null;
  public file: File | null = null;

  constructor(
    private fb: FormBuilder,
    private _projectService: ProjectService,
    private route: ActivatedRoute,
    private router: Router
  ) {
    // Afegim el constructor 
    this.title = 'Crear Projecte';
    this.projectForm = this.fb.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
      category: ['', Validators.required],
      langs: ['', Validators.required],
      year: ['', Validators.required],
      image: [null] 
    });
  
    // Comprovem si estem editant un projecte
    this.projectId = this.route.snapshot.paramMap.get('id');
    if (this.projectId) {
      this.title = 'Editar Projecte';
      this.getProject(this.projectId);
    } else {
      
      this.projectForm.get('image')?.setValidators(Validators.required);
    }
  }

  // Afegim el mètode getProject
  getProject(id: string): void {
    this._projectService.getProject(id).subscribe({
      next: (response: { project: any }) => {

        // Guarda el projecte en la propietat project
        this.project = response.project;
        this.projectForm.patchValue({
          name: this.project.name,
          description: this.project.description,
          category: this.project.category,
          langs: this.project.langs,
          year: this.project.year,
          image: this.project.image || null
        });
        
        // Mostra la imatge si existeix (preview)
        if (this.project.image && this.project.image !== 'null') {
          this._projectService.getImage(this.project.image).subscribe({
            next: (response) => {
              const reader = new FileReader();
              reader.onload = () => {
                this.imagePreview = reader.result as string;
              };
              reader.readAsDataURL(response);
            }
          });
        }

      },
      error: (err) => {
        console.error('Error carregant el projecte:', err);
      }
    });
  }
  
  // Afegim el mètode onSubmit
  onSubmit(): void {

    // Si el formulari és vàlid
    if (this.projectForm.valid) {

      // Crea un nou projecte amb les dades del formulari
      const project: Project = new Project(
        this.projectId || '',
        this.projectForm.value.name,
        this.projectForm.value.description,
        this.projectForm.value.category,
        this.projectForm.value.year,
        this.projectForm.value.langs,
        this.file ? this.file.name : this.projectForm.value.image 
      );

      // Si estem editant un projecte, envia'l amb el seu ID
      if (this.projectId) {
        this._projectService.updateProject(this.projectId, project).subscribe({
          next: (response) => {
            this.successMessage = 'Projecte actualitzat correctament! Pots veure\'l ';

            // Pujem la imatge si s'ha seleccionat
            if (this.file) {
              this._projectService.saveImage(this.file, this.projectId!).subscribe({
                next: (response) => {
                  console.log('Imatge guardada amb èxit:', response);
                },
                error: (error) => {
                  console.error('Error en guardar la imagen:', error);
                },
              });
            }
          },
          error: (error) => {
            console.error('Error actualitzant el projecte:', error);
            this.successMessage = null;
          },
        });
      } else {

        // Si no, creem un nou projecte
        this._projectService.saveProject(project).subscribe({
          next: (response) => {
            this.project = response.project;
            this.successMessage = 'Projecte creat correctament! ';
  
            // Pujem la imatge 
            if (this.file) {
              this._projectService.saveImage(this.file, response.project._id).subscribe({
                next: (response) => {
                  console.log('Imatge guardada amb èxit:', response);
                },
                error: (error) => {
                  console.error('Error en guardar la imatge:', error);
                }
              });
            }
          },
          error: (err) => {
            console.error('Error creant el projecte:', err);
          }
        });
      }
    }
  }
  
  // Afegim el mètode onFileSelected
  onFileSelected(event: any): void {

    const file = event.target.files[0];
    if (file) {
      
      // Mostra la imatge seleccionada (preview)
      const reader = new FileReader();
      reader.onload = () => {
        this.imagePreview = reader.result as string;
        this.projectForm.get('image')?.setValue(file.name);
        this.file = file; 
      };
      reader.readAsDataURL(file);
    } else {

      // Si no hi ha cap imatge seleccionada, fem un reset a la preview
      this.imagePreview = null;
      this.projectForm.get('image')?.setValue(null); 
      this.file = null;
    }
  }
}
