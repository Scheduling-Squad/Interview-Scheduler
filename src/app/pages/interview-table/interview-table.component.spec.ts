import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InterviewTableComponent } from './interview-table.component';

describe('InterviewTableComponent', () => {
  let component: InterviewTableComponent;
  let fixture: ComponentFixture<InterviewTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InterviewTableComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InterviewTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
