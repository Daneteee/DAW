import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CotxesComponent } from './cotxes.component';

describe('CotxesComponent', () => {
  let component: CotxesComponent;
  let fixture: ComponentFixture<CotxesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CotxesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CotxesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
