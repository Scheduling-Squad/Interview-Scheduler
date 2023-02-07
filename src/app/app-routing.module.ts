import { InterviewTableComponent } from './pages/interview-table/interview-table.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UpdateScheduleComponent } from './pages/update-schedule/update-schedule.component';
import { NewInterviewComponent } from './pages/new-interview/new-interview.component';

const routes: Routes = [
  { path: '', component: InterviewTableComponent },
  { path: 'updateschedule', component: UpdateScheduleComponent },
  { path: 'newinterview', component: NewInterviewComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
