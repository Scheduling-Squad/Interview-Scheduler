import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { InterviewTableComponent } from './pages/interview-table/interview-table.component';
import { UpdateScheduleComponent } from './pages/update-schedule/update-schedule.component';
import { NewInterviewComponent } from './pages/new-interview/new-interview.component';
import { HttpClientModule } from '@angular/common/http';
import { MaterialModule } from './environments/material.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    InterviewTableComponent,
    UpdateScheduleComponent,
    NewInterviewComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MaterialModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
