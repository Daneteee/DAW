import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SuccesfulComponentComponent } from './succesful-component.component';

describe('SuccesfulComponentComponent', () => {
  let component: SuccesfulComponentComponent;
  let fixture: ComponentFixture<SuccesfulComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SuccesfulComponentComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SuccesfulComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
