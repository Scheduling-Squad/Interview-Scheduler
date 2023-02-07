import { Injectable } from '@angular/core';
import { InterviewTable } from '../interfaces/interviewTable';

@Injectable({
  providedIn: 'root',
})
export class CandidateService {
  constructor() {}

  public getInterviewTableData(): InterviewTable[] {
    let data = [
      { id: 1, candidateName: 'shankar', interviewTime: Date.now().toString() },
      { id: 3, candidateName: 'selva', interviewTime: Date.now().toString() },
      { id: 4, candidateName: 'peter', interviewTime: Date.now().toString() },
    ];

    return data;
  }
}
