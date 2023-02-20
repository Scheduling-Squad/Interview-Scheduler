import { CandidateService } from './../../services/candidate-service.service';
import { Component, OnInit } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatTable } from '@angular/material/table';
import { MatMenu } from '@angular/material/menu';
import { Router } from '@angular/router';
import { InterviewModal } from 'src/app/interfaces/interview';
import { TimeMap } from 'src/app/constants/TimeMap';
// const ELEMENT_DATA: InterviewTable[] = [
//   { id: 1, candidateName: 'shankar', interviewTime: Date.now().toString() },
//   { id: 3, candidateName: 'selva', interviewTime: Date.now().toString() },
//   { id: 4, candidateName: 'peter', interviewTime: Date.now().toString() },
// ];

@Component({
  selector: 'app-interview-table',
  templateUrl: './interview-table.component.html',
  styleUrls: ['./interview-table.component.css'],
})
export class InterviewTableComponent implements OnInit {
  constructor(
    private candidateService: CandidateService,
    private router: Router
  ) {}
  interviews: InterviewModal[] = [];
  displayedColumns: string[] = [
    'id',
    'panel',
    'date',
    'slot',
    'candidateName',
    'actions',
  ];

  //dataSource = ELEMENT_DATA;
  getTiming(slot: number) {
    switch (slot) {
      case 1: {
        return '8:00AM-9:00AM';
      }
      case 2: {
        return '9:00AM-10:00AM';
      }
      case 3: {
        return '10:00AM-11:00AM';
      }
      case 4: {
        return '11:00AM-12:00AM';
      }
      case 5: {
        return '2:00PM-3:00PM';
      }
      case 6: {
        return '3:00PM-4:00PM';
      }
      default: {
        return 'Rejected';
      }
    }
  }
  OnDelete() {
    if (confirm('Are you sure to delete ')) {
    }
  }
  OnUpdate() {
    this.router.navigate(['/updateschedule']);
  }
  getInterviews() {
    this.candidateService.getInterviewTableData().subscribe({
      next: (data) => {
        console.log(data);
        console.log(data[0].candidate?.name);
        this.interviews = data;
      },
    });
  }
  ngOnInit() {
    this.getInterviews();
  }
}
