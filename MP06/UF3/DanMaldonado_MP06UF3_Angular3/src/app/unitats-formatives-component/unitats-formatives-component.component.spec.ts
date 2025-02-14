import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UnitatsFormativesComponentComponent } from './unitats-formatives-component.component';

describe('UnitatsFormativesComponentComponent', () => {
  let component: UnitatsFormativesComponentComponent;
  let fixture: ComponentFixture<UnitatsFormativesComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [UnitatsFormativesComponentComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(UnitatsFormativesComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
