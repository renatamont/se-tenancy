# PROJECT IMPORTS
from src.repositories.course.repositories import SqlAlchemyRepositories


class CourseReportService:

    @classmethod
    async def get_course_to_report(cls, tenant, class_id):
        query_result = await SqlAlchemyRepositories.get_courses_by_class_id(
            tenant, class_id
        )

        normalized_data = [{"course_id": course_id} for (course_id,) in query_result]

        return normalized_data
