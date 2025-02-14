import { TestBed } from '@angular/core/testing';

import { CotxesService } from './cotxes.service';

describe('CotxesService', () => {
  let service: CotxesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CotxesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
