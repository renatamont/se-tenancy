# STANDARD IMPORTS
from fastapi import APIRouter, Depends

# PROJECT IMPORTS
from src.domain.reports.models import CourseReportsModel
from src.services.courses.services import CourseReportService


class CourseReportRouter:

    __course_report_router = APIRouter()

    @staticmethod
    def get_course_report_router():
        return CourseReportRouter.__course_report_router

    @staticmethod
    @__course_report_router.get("/get_course_report", tags=["COURSE REPORT"])
    async def get_course_report_response(
            report: CourseReportsModel = Depends()
    ):
        response = await CourseReportService.get_course_to_report(
            tenant=report.tenant, class_id=report.class_id
        )
        return response
