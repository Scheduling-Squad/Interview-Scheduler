import { CandidateModel } from './candidate';
import { EmployeeModel } from './employee';
export class InterviewModal {
  date?: {
    year: number;
    month: number;
    day: number;
  };
  interview_id?: number;
  slot?: number;
  employees?: EmployeeModel[];
  candidate?: CandidateModel;
}
