import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { EmployeeModel } from '../interfaces/employee';

@Injectable({
  providedIn: 'root',
})
export class EmployeeService {
  constructor(private http: HttpClient) {}
  configUrl: string = '/assets/employees.json';
  public getEmployees(): Observable<EmployeeModel[]> {
    return this.http.get<EmployeeModel[]>(this.configUrl);
  }
}
