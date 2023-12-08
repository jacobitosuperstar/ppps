import type { RouteObject } from "react-router-dom";
import { PATHS } from "../constants";
import { AuthenticationValidator } from "@/components";
import { MainLayout } from "@/layouts";
import EmployeesPage from "@/pages/Employees/Employees";

export const EmployeesRoute: RouteObject = {
  element: <AuthenticationValidator />,
  children: [
    {
      element: (
        <MainLayout>
          <EmployeesPage />
        </MainLayout>
      ),
      path: PATHS.EMPLOYEES,
    },
  ],
};
