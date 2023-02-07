import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { InterviewModal } from '../interfaces/interview';
@Injectable({
  providedIn: 'root',
})
export class CandidateService {
  constructor(private http: HttpClient) {}
  configUrl: string = '/assets/interview.json';
  public getInterviewTableData(): Observable<InterviewModal[]> {
    // let data = [
    //   { id: 1, candidateName: 'shankar', interviewTime: Date.now().toString() },
    //   { id: 3, candidateName: 'selva', interviewTime: Date.now().toString() },
    //   { id: 4, candidateName: 'peter', interviewTime: Date.now().toString() },
    // ];
    return this.http.get<InterviewModal[]>(this.configUrl);
    //return data;
  }
  getConfig() {
    return this.http.get(this.configUrl);
  }
}
