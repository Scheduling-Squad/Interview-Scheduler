import { EmployeeModel } from './../../interfaces/employee';
import { COMMA, ENTER } from '@angular/cdk/keycodes';
import { Component, ElementRef, ViewChild, Input, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';
import { MatChipInputEvent } from '@angular/material/chips';
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
import { EmployeeService } from 'src/app/services/employee.service';

@Component({
  selector: 'app-new-interview',
  templateUrl: './new-interview.component.html',
  styleUrls: ['./new-interview.component.css'],
})
export class NewInterviewComponent implements OnInit {
  separatorKeysCodes: number[] = [ENTER, COMMA];
  fruitCtrl = new FormControl('');
  filteredFruits: Observable<string[]>;
  selectedDate?: Date;
  fruits: string[] = ['Lemon'];
  allFruits: string[] = ['Apple', 'Lemon', 'Lime', 'Orange', 'Strawberry'];
  allEmployees: EmployeeModel[] = [];
  @ViewChild('fruitInput')
  fruitInput!: ElementRef<HTMLInputElement>;

  constructor(private employeeService: EmployeeService) {
    this.filteredFruits = this.fruitCtrl.valueChanges.pipe(
      startWith(null),
      map((fruit: string | null) =>
        fruit ? this._filter(fruit) : this.allFruits.slice()
      )
    );
  }
  ngOnInit(): void {
    this.getEmployees();
  }

  add(event: MatChipInputEvent): void {
    const value = (event.value || '').trim();
    // Add our fruit
    if (value) {
      if (this.fruits.length < 4) {
        console.log(this.fruits.length);
        this.fruits.push(value);
      }
    }

    // Clear the input value
    event.chipInput!.clear();

    this.fruitCtrl.setValue(null);
  }

  remove(fruit: string): void {
    const index = this.fruits.indexOf(fruit);

    if (index >= 0) {
      this.fruits.splice(index, 1);
    }
  }

  selected(event: MatAutocompleteSelectedEvent): void {
    if (this.fruits.length < 3) {
      if (!this.fruits.includes(event.option.viewValue)) {
        this.fruits.push(event.option.viewValue);
      }
    }
    this.fruitInput.nativeElement.value = '';
    this.fruitCtrl.setValue(null);
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();

    return this.allFruits.filter((fruit) =>
      fruit.toLowerCase().includes(filterValue)
    );
  }
  private getEmployees() {
    this.employeeService.getEmployees().subscribe({
      next: (data) => {
        console.log(data);
        this.allEmployees = data;
      },
    });
  }
  public isMaxEmployee() {
    console.log(this.fruits.length);
    return this.fruits.length == 3;
  }
  public onDateSelect() {
    console.log(1);
  }
}
