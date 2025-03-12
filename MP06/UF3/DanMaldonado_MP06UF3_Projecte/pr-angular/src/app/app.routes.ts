import { Routes } from '@angular/router';
import { AboutComponent } from './components/about/about.component';
import { ProjectsComponent } from './components/projects/projects.component';
import { CreateComponent } from './components/create/create.component';
import { ErrorComponent } from './components/error/error.component';
import { ContactComponent } from './components/contact/contact.component';
import { DetailComponent } from './components/detail/detail.component';

export const routes: Routes = [
    { path: '', component: AboutComponent },
    { path: 'about', component: AboutComponent },
    { path: 'projects', component: ProjectsComponent },
    { path: 'create-project', component: CreateComponent },
    { path: 'contact', component: ContactComponent },
    { path: 'detail/:id', component: DetailComponent },
    { path: 'edit/:id', component: CreateComponent },
    { path: '**', component: ErrorComponent },
];